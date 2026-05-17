"""
Polyreasoner Configuration
Edit paths to match your model locations
"""

# Model paths (edit these to match your setup)
MODEL_PATHS = {
    "router": "models\mistral-7b-instruct-v0.2.Q4_K_M.gguf",  # Routing + Synthesis
    "agents": "models\mistral-7b-instruct-v0.2.Q4_K_M.gguf"   # Same model = no swapping = fast
}

# Model settings - balanced for quality and speed
MODEL_SETTINGS = {
    "router": {
        "n_ctx": 6144,       # Enough for conversation + routing
        "n_gpu_layers": -1,  # Use all GPU layers
        "verbose": False
    },
    "agents": {
        "n_ctx": 4096,       # Agents need moderate context
        "n_gpu_layers": -1,
        "verbose": False
    }
}

# Available perspectives
AVAILABLE_AGENTS = [
    "business",     # Market fit, revenue, competitive advantage
    "risk",         # Threats, downsides, failure modes
    "security",     # Vulnerabilities, privacy, attack vectors
    "feasibility",  # Technical complexity, resources, timeline
    "impact",       # Long-term consequences, scalability
    "ethical",      # Moral implications, fairness
    "contrarian"    # Devil's advocate, argues against
]

# Default agents when routing fails (keep minimal for speed)
DEFAULT_AGENTS = ["business", "risk", "contrarian"]

# Max agents to run (limits LLM calls)
MAX_AGENTS = 3
