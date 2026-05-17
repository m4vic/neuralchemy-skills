# AI Security (LLM + Agent Security) - Basics

This track is intentionally lightweight: enough to understand prompt injection and common failure modes in LLM apps.

## 1) Prompt Injection (what it is)
Prompt injection is when untrusted text causes the model to ignore intended instructions or reveal/exfiltrate data.

Types:
- Direct injection: user message tries to override system/developer instructions
- Indirect injection: retrieved documents / webpages / tool outputs contain malicious instructions (RAG risk)

## 2) Common Risk Scenarios
- RAG: attacker poisons a document so retrieved context contains malicious instructions
- Tool use: model is tricked into calling tools in unsafe ways (data access, browsing, code execution)
- Secret leakage: API keys, internal prompts, or private data appear in context/logs

## 3) Basic Defenses (practical)
- Treat retrieved content as untrusted: quote it, separate it, and never "obey" it
- Least privilege tools: allowlist tools + restrict scopes + require confirmations for sensitive actions
- Input/output filtering (helpful but not sufficient)
- Sandboxing for code/tools + strict network/file permissions
- Logging + redaction: log for incident response, but never log secrets

## 4) What to Build (Projects)
See `../Projects/README.md` for suggested AI security projects:
- Prompt-injection test suite for a toy RAG app
- Data exfiltration demo + mitigation checklist
- Tool-abuse scenarios + guardrails evaluation

## 5) Papers to Read
See `../../papers/README.md`
