# Tool Skills (Neuralchemy)

Practical skills we care about (to move fast building + testing ML/LLM systems).

## Python + PyTorch (core)
- Write clean experiments (config, seeds, logging, metrics)
- Debug training issues (nan/inf, exploding gradients, dataloader bugs)
- Implement and read models (forward pass, attention blocks, loss functions)

## LLM Dev Workflows
### Codex
- Use it to refactor, add tests, build small prototypes, and audit changes.
- Keep PRs small; write minimal reproducible issues.

### Claude Code
- Use it for quick repo navigation, summarizing modules, and drafting docs.
- Validate important changes locally (don't trust auto-edits blindly).

### AntiGravity (if you mean the prompt/tooling workflow)
- Define repeatable prompts + evaluation harnesses.
- Track prompts and outputs like code (versioned).

## Systems / Design Basics (LLM apps)
- RAG architecture basics (chunking, retrieval, reranking, eval)
- Agent/tool calling risks (tool access control, allowlists, provenance)
- Observability (what to log, redaction, incident response)

## Security basics (LLM apps)
- Prompt injection: direct + indirect (RAG content injection)
- Data exfiltration scenarios (secrets in context, tool outputs, logs)
- Guardrails that actually help: input/output filtering, sandboxing, least privilege
