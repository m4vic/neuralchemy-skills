# Agentic AI (Tool-Using LLM Systems)

Agents are LLM systems that plan and take actions using tools (APIs, search, code execution, databases).

## Why this matters for Neuralchemy
Tool use expands the attack surface:
- Indirect prompt injection via retrieved content or tool output
- Tool abuse (calling privileged tools, data exfiltration)
- Unsafe autonomy (actions without hard gates/confirmation)

## Core Concepts
- Tool calling: schemas, tool selection, input validation
- ReAct-style loops: think -> act -> observe -> repeat
- Memory: what to store, what never to store (secrets)
- Guardrails: least privilege, allowlists, policy checks at the tool boundary

## What to Build
- A minimal agent with 2-3 tools (search, calculator, file read) and explicit permissions
- An injection test suite where tool outputs contain hostile instructions
- An audit log that records decisions + tool calls (with redaction)

## Related
- AI Security basics: `../Ai-security/README.md`
- Reading list: `../../papers/README.md`
