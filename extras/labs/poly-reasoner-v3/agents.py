"""
Polyreasoner Agents
Individual perspective execution logic
"""

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from prompts import AGENT_PROMPTS


def run_agent(agent_name: str, idea: str, context: str, llm) -> dict:
    """
    Run a single agent and return its analysis.
    Each agent is isolated - sees only the idea and its own prompt.
    """
    if agent_name not in AGENT_PROMPTS:
        return {
            "agent": agent_name,
            "error": f"Unknown agent: {agent_name}"
        }
    
    # Build prompt with idea
    prompt = AGENT_PROMPTS[agent_name] + f"\n\n{idea}"
    if context:
        prompt += f"\n\nAdditional context: {context}"
    
    try:
        # Generate response
        response = llm(
            prompt,
            max_tokens=200,  # Shorter for speed
            temperature=0.7,
            stop=["</response>", "\n\n\n"]
        )
        
        output_text = response["choices"][0]["text"].strip()
        
        # Parse JSON from response
        result = parse_agent_output(output_text)
        result["agent"] = agent_name
        
        return result
        
    except Exception as e:
        return {
            "agent": agent_name,
            "error": str(e),
            "raw_output": output_text if 'output_text' in dir() else None
        }


def parse_agent_output(text: str) -> dict:
    """
    Extract JSON from agent response.
    Handles cases where model outputs extra text around JSON.
    """
    # Try direct JSON parse
    try:
        return json.loads(text)
    except:
        pass
    
    # Try to find JSON in response
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        try:
            return json.loads(json_match.group())
        except:
            pass
    
    # Fallback: return raw text as result
    return {
        "verdict": "unknown",
        "confidence": 0.5,
        "raw_output": text,
        "parse_failed": True
    }


def run_agents_sequential(agent_names: list, idea: str, context: str, llm) -> list:
    """
    Run agents sequentially (llama-cpp doesn't support parallel access to same model).
    Each agent runs in isolation - no shared state.
    """
    results = []
    
    for name in agent_names:
        try:
            result = run_agent(name, idea, context, llm)
            results.append(result)
            print(f"  ✓ {name} complete")
        except Exception as e:
            results.append({
                "agent": name,
                "error": str(e)
            })
            print(f"  ✗ {name} failed: {e}")
    
    return results


def format_agent_outputs(results: list) -> str:
    """
    Format agent outputs for synthesis prompt.
    """
    formatted = []
    
    for result in results:
        agent = result.get("agent", "unknown")
        
        if "error" in result:
            formatted.append(f"**{agent.upper()}**: Error - {result['error']}")
        else:
            # Pretty format the result
            formatted.append(f"**{agent.upper()}**:\n```json\n{json.dumps(result, indent=2)}\n```")
    
    return "\n\n".join(formatted)
