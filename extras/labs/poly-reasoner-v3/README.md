# Polyreasoner

Multi-perspective reasoning system for idea evaluation and decision support.

## What It Does

Polyreasoner is a conversational AI that **automatically activates multi-perspective analysis** when you ask complex questions or need to evaluate decisions.

- **Simple queries** → Direct response (like ChatGPT)
- **Complex decisions** → Spawns multiple specialized agents → Synthesizes insights

## Quick Start

### 1. Install Dependencies

```bash
# With GPU support (recommended)
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

# Or CPU only
pip install llama-cpp-python
```

### 2. Download Models

Place models in the `models/` folder:

```bash
# Router model (Qwen 14B) - you may already have this
huggingface-cli download Qwen/Qwen2.5-14B-Instruct-GGUF qwen2.5-14b-instruct-q4_k_m.gguf --local-dir ./models

# Agent model (Mistral 7B) - optional, can use same model for both
huggingface-cli download TheBloke/Mistral-7B-Instruct-v0.2-GGUF mistral-7b-instruct-v0.2.Q4_K_M.gguf --local-dir ./models
```

### 3. Configure (Optional)

Edit `config.py` to set model paths:

```python
MODEL_PATHS = {
    "router": "models/Qwen2.5-14B-Instruct-Q4_K_M.gguf",
    "agents": "models/Qwen2.5-14B-Instruct-Q4_K_M.gguf"  # Can use same model
}
```

### 4. Run

```bash
python main.py
```

## Web Interface (Alternative)

For a cleaner UI experience, use the Gradio web interface:

```bash
# Install Gradio if not already installed
pip install gradio

# Launch web interface
python webapp.py
```

Then open **http://127.0.0.1:7860** in your browser.

## Usage Examples

### Normal Conversation
```
You: Hello, how are you?
Polyreasoner: I'm doing well! How can I help you today?
```

### Multi-Perspective Analysis (Automatic)
```
You: Should I open source my ML project?

🔍 poly-reasoning...
   Agents: business, risk, security, contrarian
   Reason: Decision about public visibility with IP implications

  ✓ business complete
  ✓ risk complete
  ✓ security complete
  ✓ contrarian complete

📊 Synthesizing perspectives...

Polyreasoner: ## Overall Assessment
Based on multi-perspective analysis, open sourcing has strong benefits but requires careful preparation...

### Business Perspective
- Community building opportunity
- Can attract talent pipeline
- May enable competitors

### Risk Perspective
- IP exposure risk (moderate)
- Maintenance burden (ongoing)
...
```

## Architecture

```
User Query
    ↓
Router (Qwen 14B) - Decides if multi-agent needed
    ├─ Simple → Direct response
    └─ Complex → Spawns agents
              ↓
Agents (Mistral 7B or Qwen) - Run in parallel
    ├─ Business
    ├─ Risk
    ├─ Security
    ├─ Feasibility
    ├─ Impact
    ├─ Ethical
    └─ Contrarian
              ↓
Synthesizer (Qwen 14B) - Combines perspectives
              ↓
Final Response
```

## Available Agents

| Agent | Focus |
|-------|-------|
| `business` | Market fit, revenue, competitive advantage |
| `risk` | Threats, failure modes, what could go wrong |
| `security` | Vulnerabilities, privacy, attack vectors |
| `feasibility` | Technical complexity, resources, timeline |
| `impact` | Long-term consequences, scalability |
| `ethical` | Moral implications, fairness |
| `contrarian` | Devil's advocate, argues against |

## Customization

### Add New Agent

1. Add agent name to `config.py`:
```python
AVAILABLE_AGENTS = [..., "new_agent"]
```

2. Add prompt in `prompts.py`:
```python
AGENT_PROMPTS["new_agent"] = """Your prompt here..."""
```

### Change Models

Edit `config.py`:
```python
MODEL_PATHS = {
    "router": "path/to/your/router/model.gguf",
    "agents": "path/to/your/agent/model.gguf"
}
```

## Security Testing

Polyreasoner is designed for testing with:
- **Rapture** - Prompt injection testing
- **PromptShield** - LLM security analysis

Each agent runs in isolation, making it suitable for studying:
- Cross-agent contamination
- Prompt injection propagation
- Agent manipulation techniques

## Commands

- `quit` - Exit the program
- `clear` - Reset conversation history

## File Structure

```
polyreasoner/
├── main.py          # Entry point + orchestration
├── config.py        # Model paths + settings
├── prompts.py       # All system prompts
├── agents.py        # Agent execution logic
├── requirements.txt # Dependencies
└── models/          # Your GGUF models
```

## Requirements

- Python 3.10+
- 12GB+ VRAM (for GPU inference)
- Or 16GB+ RAM (for CPU inference)

## License

MIT
