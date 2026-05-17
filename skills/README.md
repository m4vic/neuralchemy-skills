# Neuralchemy Skills and Hiring Roadmap

Website: www.neuralchemy.in

This roadmap is for candidates who want to join Neuralchemy as:
- AI Security Engineer
- AI Security Researcher
- AI Engineer (LLM/Agent systems)
- ML Researcher
- Startup generalist (curriculum, maintainer, builder)

It is built from the full `specifics/` archive and converted into one actionable startup prep plan.

---

## What Neuralchemy Actually Hires For

We hire people who can:
1) Learn fast and ship small, reliable systems
2) Think clearly about trust boundaries and abuse cases
3) Turn ideas into reproducible experiments and writeups
4) Communicate tradeoffs, not just model outputs

If you can do this with evidence, titles matter less.

---

## 12-Week Core Plan (Everyone)

Use this first, regardless of role.

### Phase 0 (Week 0): Setup + Operating Habits
- Read: `../README.md`, `../specifics/README.md`
- Set up: Git, Python envs, reproducible project template
- Habit target: one clean README per project, one command to run, one command to test

### Phase 1 (Weeks 1-2): Fundamentals
- Track: `../specifics/Fundamentals/README.md`
- Learn: Python, math for ML, data basics, reproducibility
- Minimum proof:
  - One cleaned dataset notebook/script
  - One short note explaining leakage and metric choice
- Resources:
  - Python tutorial: https://docs.python.org/3/tutorial/
  - NumPy docs: https://numpy.org/doc/
  - Pandas docs: https://pandas.pydata.org/docs/
  - 3Blue1Brown linear algebra/calculus: https://www.3blue1brown.com/topics/linear-algebra / https://www.3blue1brown.com/topics/calculus
  - Khan Academy statistics: https://www.khanacademy.org/math/statistics-probability

### Phase 2 (Weeks 3-4): Machine Learning Evaluation Instincts
- Track: `../specifics/MachineLearning/README.md`
- Learn: splits, leakage prevention, precision/recall, ROC-AUC, calibration
- Minimum proof:
  - Tabular classification project with leakage checks
  - Imbalanced classification project with proper metrics
- Resources:
  - StatQuest: https://www.youtube.com/@statquest
  - Scikit-learn guide: https://scikit-learn.org/stable/user_guide.html

### Phase 3 (Weeks 5-6): Deep Learning Execution (PyTorch)
- Track: `../specifics/DeepLearning/README.md`
- Learn: clean training loops, autograd debugging, regularization, checkpoints
- Minimum proof:
  - Image or text classifier with error analysis
  - Reusable training harness (configs, logging, checkpoints)
- Resources:
  - PyTorch tutorials: https://pytorch.org/tutorials/
  - fast.ai: https://course.fast.ai/

### Phase 4 (Weeks 7-8): LLM Systems and Agentic Foundations
- Track: `../specifics/GenerativeAI/README.md`
- Optional deep dive: `../specifics/GenerativeAI/AgenticAI.md`
- Learn: transformer basics, RAG pipeline, tool-calling boundaries, eval sets
- Minimum proof:
  - RAG baseline with retrieval evaluation set
  - Tool-using agent with allowlists and audit logs
- Resources:
  - Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/
  - Attention paper: https://arxiv.org/abs/1706.03762

### Phase 5 (Weeks 9-10): AI Security Core
- Track: `../specifics/Ai-security/README.md`
- Learn: direct and indirect prompt injection, data exfiltration, tool abuse
- Minimum proof:
  - Prompt injection test suite for a toy RAG app
  - Mitigation checklist mapped to concrete threats
- Reading priority:
  - OWASP Top 10 for LLM Apps: https://owasp.org/www-project-top-10-for-large-language-model-applications/
  - Indirect prompt injection: https://arxiv.org/abs/2302.12173
  - HouYi prompt injection: https://arxiv.org/abs/2306.05499
  - Full list: `../papers/README.md`

### Phase 6 (Weeks 11-12): Startup Shipping Layer
- Tracks:
  - `../specifics/Tools/README.md`
  - `../specifics/SystemDesign/README.md`
- Learn: FastAPI, Docker, CI basics, observability, failure design, least privilege
- Minimum proof:
  - One deployable AI microservice with tests and logs
  - One architecture note with trust boundaries and fallback paths

---

## Role Lanes (Pick 1 Primary + 1 Secondary)

### Lane A: AI Security Engineer
Focus:
- Build guardrails and secure defaults for LLM systems
- Add practical controls at input, tool, and output boundaries

Must show:
- Threat model + abuse cases for one LLM app
- Injection/data exfiltration test harness
- Security regression checklist

Best repo anchors:
- `../specifics/Ai-security/README.md`
- `../specifics/Projects/README.md`
- `../specifics/labs/poly-reasoner-v3/PROMPTSHIELD_INTEGRATION.md`

### Lane B: AI Security Researcher
Focus:
- Study jailbreak/injection behavior and defense reliability
- Produce reproducible experiments and concise findings

Must show:
- A small benchmark of 20-50 adversarial prompts
- Attack taxonomy + defense failure analysis
- Paper-style writeup (method, results, limitations)

Best repo anchors:
- `../papers/README.md`
- `../specifics/legacy-docs/PAPERS.md`
- `../specifics/labs/poly-reasoner-v3/README.md`

### Lane C: AI Engineer (LLM Product Builder)
Focus:
- Build useful LLM/agent features safely under startup constraints
- Optimize speed, reliability, and developer ergonomics

Must show:
- End-to-end RAG or tool-using workflow
- Eval harness with pass/fail criteria
- API service + CI + logging redaction

Best repo anchors:
- `../specifics/GenerativeAI/README.md`
- `../specifics/Tools/README.md`
- `../specifics/SystemDesign/README.md`

### Lane D: ML Researcher (Applied Systems)
Focus:
- Experiments, ablations, metrics, and model behavior analysis
- Practical training/evaluation pipelines

Must show:
- One reproducible ML/DL experiment suite
- Clear baseline vs improved model comparison
- Error analysis and calibration commentary

Best repo anchors:
- `../specifics/MachineLearning/README.md`
- `../specifics/DeepLearning/README.md`
- `../specifics/Projects/README.md`

### Lane E: Startup Generalist (Curriculum / Maintainer / Builder)
Focus:
- Keep systems, docs, and contributors moving
- Turn scattered links into actionable learning and execution paths

Must show:
- One strong documentation restructure PR
- One project rubric with acceptance criteria
- One maintenance sweep (broken links, consistency, triage)

Best repo anchors:
- `../specifics/legacy-docs/JOIN_US.md`
- `../specifics/legacy-docs/CONTRIBUTING.md`
- `../specifics/legacy-docs/TOOLS_SKILLS.md`

---

## Optional Extended Tracks (After Core)

Take these only after the 12-week core + one role lane:

- AGI direction and research context: `../specifics/AGI/README.md`
- Robotics systems path: `../specifics/Robotics/README.md`
- Quant finance specialization: `../specifics/QuantFinance/README.md`
- Computer vision module notes: `../specifics/notes/ComputerVision.md`
- Experimental lab workflows: `../specifics/labs/README.md`

Rule: depth is useful only if you keep shipping proofs in your primary lane.

---

## Project Portfolio Requirements Before Applying

Build at least 3 artifacts:

1) **Security artifact**
- Prompt-injection or tool-abuse evaluation with mitigations

2) **Engineering artifact**
- Deployed AI/LLM service with logs, tests, and clear run instructions

3) **Research artifact**
- Structured experiment writeup with metrics and failure analysis

Strong bonus:
- Harden `poly-reasoner-v3` style agent workflows and document tradeoffs

Project ideas: `../specifics/Projects/README.md`

---

## Startup Readiness Checklist (Self-Score)

Score each item 0 (no), 1 (partial), 2 (confident):

- I can explain trust boundaries for an LLM app.
- I can design eval sets for model and security behavior.
- I can detect leakage and metric misuse in ML pipelines.
- I can ship a small service with Docker and CI.
- I can log safely (redaction, no secrets).
- I can write a threat model with concrete mitigations.
- I can communicate tradeoffs and next actions clearly.

Target score before applying: **10+/14** (minimum), **12+/14** (strong).

---

## Application Package (Neuralchemy)

Email: neuralchemyai@gmail.com

Send:
- Resume (PDF)
- GitHub profile + 1-3 relevant repos
- Hugging Face profile (if available)
- Role preference (primary + secondary lane)
- One short writeup: what you built, what failed, what you improved

Direct apply link:
- [Apply](mailto:neuralchemyai@gmail.com?subject=Neuralchemy%20Application%20-%20ROLE&body=Hi%20Neuralchemy%20Team%2C%0A%0AName%3A%0APrimary%20Role%3A%0ASecondary%20Role%3A%0AGitHub%3A%0AHuggingFace%3A%0ALinkedIn%3A%0A%0AProjects%20(1-3)%3A%0AWhat%20I%20built%20and%20learned%3A%0A%0AAttach%20resume%20(PDF).%0A)

---

## One-Line Execution Rule

Learn -> build -> break -> secure -> measure -> document -> ship.
