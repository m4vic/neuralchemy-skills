"""
Polyreasoner v3 - With PromptShield Integration
Multi-perspective reasoning system with LLM security protection
"""

import json
import re
import sys
from pathlib import Path

from llama_cpp import Llama

# Add parent directory to path for PromptShield import
sys.path.insert(0, str(Path(__file__).parent.parent))
from promptshield import Shield
from promptshield.methods import load_attack_patterns

from config import MODEL_PATHS, MODEL_SETTINGS, DEFAULT_AGENTS, AVAILABLE_AGENTS, MAX_AGENTS
from prompts import ROUTER_PROMPT, SYNTHESIS_PROMPT
from agents import run_agents_sequential, format_agent_outputs


class SecurePolyreasoner:
    """
    Multi-perspective reasoning system with PromptShield protection.
    Protects against prompt injection and ensures safe multi-agent reasoning.
    """
    
    def __init__(self, shield_level=5):
        self.router_llm = None
        self.agent_llm = None
        self.conversation_history = []
        
        # Initialize PromptShield
        print("🛡️  Initializing PromptShield...")
        load_attack_patterns(str(Path(__file__).parent.parent / 'promptshield' / 'attack_db'))
        self.shield = Shield(level=shield_level)
        print(f"✓ PromptShield L{shield_level} active\n")
    
    def load_router(self):
        """Load the router/synthesizer model (Qwen 14B)"""
        if self.router_llm is None:
            print("Loading router model...")
            self.router_llm = Llama(
                model_path=MODEL_PATHS["router"],
                **MODEL_SETTINGS["router"]
            )
            print("Router model loaded.")
        return self.router_llm
    
    def load_agents(self):
        """Load the agent model (Mistral 7B)"""
        # Check if same model as router
        if MODEL_PATHS["agents"] == MODEL_PATHS["router"]:
            return self.load_router()
        
        if self.agent_llm is None:
            print("Loading agent model...")
            # Unload router to free VRAM if different model
            if self.router_llm is not None:
                del self.router_llm
                self.router_llm = None
            
            self.agent_llm = Llama(
                model_path=MODEL_PATHS["agents"],
                **MODEL_SETTINGS["agents"]
            )
            print("Agent model loaded.")
        return self.agent_llm
    
    def reload_router(self):
        """Reload router after using agent model"""
        if MODEL_PATHS["agents"] != MODEL_PATHS["router"]:
            if self.agent_llm is not None:
                del self.agent_llm
                self.agent_llm = None
            self.router_llm = None
            return self.load_router()
        return self.router_llm
    
    def detect_polymode(self, response: str) -> dict | None:
        """
        Check if response contains <polymode> tag.
        Returns parsed JSON config or None.
        """
        match = re.search(r'<polymode>([\s\S]*?)</polymode>', response)
        if not match:
            return None
        
        try:
            config = json.loads(match.group(1))
            
            # Validate agents
            valid_agents = [a for a in config.get("agents", []) if a in AVAILABLE_AGENTS]
            if not valid_agents:
                valid_agents = DEFAULT_AGENTS
            
            # Limit to MAX_AGENTS for speed
            config["agents"] = valid_agents[:MAX_AGENTS]
            return config
            
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "agents": DEFAULT_AGENTS[:MAX_AGENTS],
                "context": "",
                "reasoning": "JSON parse failed, using defaults"
            }
    
    def synthesize(self, agent_outputs: list, original_query: str) -> str:
        """
        Combine agent perspectives into final response.
        Uses router model for synthesis.
        Protected by output shield.
        """
        llm = self.reload_router()
        
        formatted_outputs = format_agent_outputs(agent_outputs)
        
        prompt = SYNTHESIS_PROMPT.format(
            agent_outputs=formatted_outputs,
            original_query=original_query
        )
        
        response = llm(
            prompt,
            max_tokens=512,
            temperature=0.7,
            stop=["</response>"]
        )
        
        synthesis = response["choices"][0]["text"].strip()
        
        # OUTPUT PROTECTION: Check synthesis for leaks
        output_check = self.shield.protect_output(
            response=synthesis,
            metadata={"canary": "synthesis"}  # Minimal metadata for synthesis
        )
        
        if output_check["blocked"]:
            print(f"⚠️  Synthesis blocked: {output_check['reason']}")
            return "I've completed the analysis, but detected a potential security issue. Please rephrase your question."
        
        return output_check["safe_response"]
    
    def process(self, user_input: str) -> str:
        """
        Main processing function with PromptShield protection.
        Handles both normal conversation and multi-agent reasoning.
        """
        
        # INPUT PROTECTION: Check user input for attacks
        input_check = self.shield.protect_input(
            user_input=user_input,
            system_context="You are Polyreasoner, a multi-perspective reasoning system.",
            session_id="polyreasoner-session"
        )
        
        if input_check["blocked"]:
            print(f"\n🚫 Security Alert: {input_check['reason']}")
            print(f"   Threat Level: {input_check['threat_level']:.2f}\n")
            return "I've detected a potential security issue with your input. Please rephrase your question."
        
        # Build prompt with conversation history
        history_text = ""
        for msg in self.conversation_history[-5:]:  # Last 5 exchanges
            history_text += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n"
        
        # Use secured system context from shield
        full_prompt = f"{ROUTER_PROMPT}\n\n{history_text}User: {user_input}\nAssistant:"
        
        # Get router response
        llm = self.load_router()
        response = llm(
            full_prompt,
            max_tokens=256,
            temperature=0.7,
            stop=["User:", "</response>"]
        )
        
        router_output = response["choices"][0]["text"].strip()
        
        # OUTPUT PROTECTION: Check router response
        router_check = self.shield.protect_output(
            response=router_output,
            metadata=input_check["metadata"]
        )
        
        if router_check["blocked"]:
            print(f"\n⚠️  Router output blocked: {router_check['reason']}\n")
            return "I apologize, but I need to reformulate my response for security reasons."
        
        # Use safe response from shield
        safe_router_output = router_check["safe_response"]
        
        # Check for polymode activation
        polymode_config = self.detect_polymode(safe_router_output)
        
        if polymode_config:
            # Multi-agent mode activated
            print("\n🔍 poly-reasoning...")
            print(f"   Agents: {', '.join(polymode_config['agents'])}")
            print(f"   Reason: {polymode_config.get('reasoning', 'N/A')}")
            print(f"   🛡️  Protected: PromptShield active\n")
            
            # Run agents sequentially
            agent_llm = self.load_agents()
            agent_results = run_agents_sequential(
                agent_names=polymode_config["agents"],
                idea=user_input,
                context=polymode_config.get("context", ""),
                llm=agent_llm
            )
            
            # Protect each agent output
            protected_results = []
            for agent_result in agent_results:
                output_check = self.shield.protect_output(
                    response=agent_result["analysis"],
                    metadata={"canary": f"agent_{agent_result['agent']}"}
                )
                
                if not output_check["blocked"]:
                    protected_results.append({
                        **agent_result,
                        "analysis": output_check["safe_response"]
                    })
                else:
                    print(f"   ⚠️  {agent_result['agent']} output filtered")
            
            # Synthesize results (also protected)
            print("\n📊 Synthesizing perspectives (protected)...\n")
            final_response = self.synthesize(protected_results, user_input)
            
        else:
            # Normal conversation mode (already protected)
            final_response = safe_router_output
        
        # Store in conversation history
        self.conversation_history.append({
            "user": user_input,
            "assistant": final_response
        })
        
        return final_response


def main():
    """CLI entry point"""
    print("=" * 60)
    print("  POLYREASONER v3 + PROMPTSHIELD")
    print("  Secure Multi-Perspective Reasoning")
    print("=" * 60)
    print()
    print("Type your questions or ideas. For complex decisions,")
    print("I'll automatically activate multi-perspective analysis.")
    print()
    print("Security: PromptShield L5 protection active")
    print()
    print("Commands: 'quit' to exit, 'clear' to reset conversation")
    print("-" * 60)
    print()
    
    reasoner = SecurePolyreasoner(shield_level=5)
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            if user_input.lower() == 'clear':
                reasoner.conversation_history = []
                print("Conversation cleared.\n")
                continue
            
            print()
            response = reasoner.process(user_input)
            print(f"Polyreasoner: {response}")
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}\n")


if __name__ == "__main__":
    main()
