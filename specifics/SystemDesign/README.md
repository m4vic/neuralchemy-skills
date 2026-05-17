# System Design (for AI Systems)

Goal: build judgment for designing reliable ML/LLM systems (performance, failure modes, security boundaries).

## Core Ideas
- Think in invariants: what must always be true
- Model trust boundaries: what is untrusted input (users, retrieved docs, tool output)
- Design for failure: timeouts, retries, partial failure, degradation
- Make systems observable: logs/metrics/traces (with redaction)

## 6-Month Track (optional, but high leverage)

### Months 1-2: Systems foundations
- Concurrency basics (threads vs async, deadlocks, backpressure)
- Debugging fundamentals (profiling, bottlenecks)

Suggested resources:
- Rob Pike: Concurrency is not Parallelism (talk)
- Brendan Gregg: Linux performance tooling (talk + site)

### Months 3-4: Distributed reality
- Timeouts and retries
- Consistency and state
- Graceful degradation

Suggested resources:
- MIT 6.824 (distributed systems)

### Month 5: Security thinking
- Threat modeling (trust boundaries, abuse cases)
- Least privilege (especially for tool-using agents)

Suggested resources:
- OWASP threat modeling overview

### Month 6: Testing + regression
- Scenario testing
- Property-based testing
- Safety regression + drift tracking

Suggested resources:
- Hypothesis (property-based testing)

## Loop to Build Skill
Build -> break -> observe -> refine -> document.

