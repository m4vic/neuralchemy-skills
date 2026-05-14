# Neuralchemy Skills (Core)

This is the single-page skills map for Neuralchemy: what to learn, in what order, with high-signal links.

Website: www.neuralchemy.in

## Roadmap (recommended order)
1) Fundamentals (Python + math + data)
2) Machine Learning (metrics, leakage, generalization)
3) Deep Learning (PyTorch training + debugging)
4) Transformers / LLMs (RAG, tool use, evaluation)
5) AI Security basics (prompt injection, jailbreak mindset)
6) Tools + System Design (ship, observe, secure boundaries)

---

## 1) Fundamentals

### Python
- Python tutorial: https://docs.python.org/3/tutorial/
- Automate the Boring Stuff (book): https://automatetheboringstuff.com/

### Math (enough for ML/DL)
- 3Blue1Brown - Linear Algebra: https://www.3blue1brown.com/topics/linear-algebra
- 3Blue1Brown - Calculus: https://www.3blue1brown.com/topics/calculus
- Khan Academy - Statistics & Probability: https://www.khanacademy.org/math/statistics-probability

### Data basics
- Pandas docs: https://pandas.pydata.org/docs/
- NumPy docs: https://numpy.org/doc/

---

## 2) Machine Learning
- StatQuest (clear intuition): https://www.youtube.com/@statquest
- scikit-learn User Guide: https://scikit-learn.org/stable/user_guide.html

Minimum projects:
- Tabular classification with leakage checks + proper metrics
- Imbalanced classification (precision/recall, PR-AUC)

---

## 3) Deep Learning (PyTorch)
- PyTorch tutorials: https://docs.pytorch.org/tutorials/
- fast.ai (practical DL): https://course.fast.ai/

Minimum projects:
- Train an image classifier (baseline + error analysis)
- Build a reusable training template (configs, logging, checkpoints)

---

## 4) Transformers / LLMs

### Core understanding
- The Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/
- Attention Is All You Need (paper): https://arxiv.org/abs/1706.03762
- Hugging Face NLP/LLM course: https://huggingface.co/learn/nlp-course/chapter1/1

### LLM applications (RAG + tool use)
- Learn RAG basics: chunking, retrieval, reranking, eval sets
- Treat tool output + retrieved text as untrusted input (security boundary)

Minimum projects:
- RAG baseline + small evaluation set
- Tool-using agent demo with allowlists + audit logs

---

## 5) AI Security Basics (Prompt Injection / Jailbreaks)

Start with the risk model:
- Direct prompt injection (user tries to override instructions)
- Indirect prompt injection (retrieved docs / webpages / tool outputs inject instructions)

Security reading (papers/refs):
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Not what you've signed up for (Indirect Prompt Injection): https://arxiv.org/abs/2302.12173
- Prompt Injection attack against LLM-integrated Applications: https://arxiv.org/abs/2306.05499

More papers: `../papers/README.md` (or open `papers/README.md` from the repo root)

---

## 6) Tools (Codex / Claude Code / Workflows)

### Codex (CLI)
- Getting started: https://help.openai.com/en/articles/11096431
- GitHub repo: https://github.com/openai/codex

### Claude Code
- Overview: https://docs.anthropic.com/en/docs/claude-code/overview

### Prompt/eval workflow ("AntiGravity")
- Version prompts like code
- Keep an eval set and track regressions
- Log safely (no secrets in logs)

---

## 7) System Design (for AI systems)
- MIT 6.824 (distributed systems): https://pdos.csail.mit.edu/6.824/
- NIST AI RMF 1.0: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

Design habits:
- Least privilege for tools
- Explicit trust boundaries
- Timeouts, retries, graceful degradation
- Observability + redaction

---

## Apply / Join Neuralchemy

Email: neuralchemyai@gmail.com

Send:
- Resume (PDF)
- GitHub link
- Hugging Face profile link
- Role you want (AI Security Researcher / ML Researcher / Curriculum / Maintainer)

Direct apply link:
- [Apply](mailto:neuralchemyai@gmail.com?subject=Neuralchemy%20Application%20-%20ROLE&body=Hi%20Neuralchemy%20Team%2C%0A%0AName%3A%0ARole%3A%0AGitHub%3A%0AHuggingFace%3A%0ALinkedIn%3A%0A%0AAttach%20your%20resume%20(PDF)%20and%20optionally%20a%20short%20writeup%20of%20your%20work.%0A)
