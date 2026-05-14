"""
Polyreasoner - Main Entry Point
Multi-perspective reasoning system with dynamic agent selection
"""

import json
import re
import sys
from pathlib import Path

from llama_cpp import Llama

from config import MODEL_PATHS, MODEL_SETTINGS, DEFAULT_AGENTS, AVAILABLE_AGENTS, MAX_AGENTS
from prompts import ROUTER_PROMPT, SYNTHESIS_PROMPT
from agents import run_agents_sequential, format_agent_outputs


class Polyreasoner:
    """
    Multi-perspective reasoning system.
    Uses LLM to dynamically decide when to activate multi-agent analysis.
    """
    
    def __init__(self):
        self.router_llm = None
        self.agent_llm = None
        self.conversation_history = []
    
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
        """
        llm = self.reload_router()
        
        formatted_outputs = format_agent_outputs(agent_outputs)
        
        prompt = SYNTHESIS_PROMPT.format(
            agent_outputs=formatted_outputs,
            original_query=original_query
        )
        
        response = llm(
            prompt,
            max_tokens=1024,  # Enough for full structured synthesis
            temperature=0.7,
            stop=["</response>"]
        )
        
        return response["choices"][0]["text"].strip()
    
    def process(self, user_input: str) -> str:
        """
        Main processing function.
        Handles both normal conversation and multi-agent reasoning.
        """
        # Build prompt with conversation history
        history_text = ""
        for msg in self.conversation_history[-5:]:  # Last 5 exchanges
            history_text += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n"
        
        full_prompt = f"{ROUTER_PROMPT}\n\n{history_text}User: {user_input}\nAssistant:"
        
        # Get router response
        llm = self.load_router()
        response = llm(
            full_prompt,
            max_tokens=512,  # Faster routing
            temperature=0.7,
            stop=["User:", "</response>"]
        )
        
        router_output = response["choices"][0]["text"].strip()
        
        # Check for polymode activation
        polymode_config = self.detect_polymode(router_output)
        
        if polymode_config:
            # Multi-agent mode activated
            print("\n🔍 poly-reasoning...")
            print(f"   Agents: {', '.join(polymode_config['agents'])}")
            print(f"   Reason: {polymode_config.get('reasoning', 'N/A')}\n")
            
            # Run agents sequentially (same model can't be accessed in parallel)
            agent_llm = self.load_agents()
            agent_results = run_agents_sequential(
                agent_names=polymode_config["agents"],
                idea=user_input,
                context=polymode_config.get("context", ""),
                llm=agent_llm
            )
            
            # Synthesize results
            print("\n📊 Synthesizing perspectives...\n")
            final_response = self.synthesize(agent_results, user_input)
            
        else:
            # Normal conversation mode
            final_response = router_output
        
        # Store in conversation history
        self.conversation_history.append({
            "user": user_input,
            "assistant": final_response
        })
        
        return final_response


def main():
    """CLI entry point"""
    print("=" * 60)
    print("  POLYREASONER")
    print("  Multi-Perspective Reasoning System")
    print("=" * 60)
    print()
    print("Type your questions or ideas. For complex decisions,")
    print("I'll automatically activate multi-perspective analysis.")
    print()
    print("Commands: 'quit' to exit, 'clear' to reset conversation")
    print("-" * 60)
    print()
    
    reasoner = Polyreasoner()
    
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
