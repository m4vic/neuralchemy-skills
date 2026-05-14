# Transformers / LLMs (Core)

This track focuses on transformer fundamentals, LLM application patterns (RAG, tool use), and evaluation basics.

## Prerequisites
- Deep Learning (PyTorch): `../DeepLearning/README.md`
- Tools/MLOps (recommended): `../Tools/README.md`

## What you should be able to do
- Explain attention/transformers at a high level
- Implement a small transformer block (or read one confidently)
- Build a basic RAG pipeline and evaluate it
- Understand how tool use expands the security surface

## Core Topics
- Attention + transformer architecture
- Tokenization basics (why it matters)
- Fine-tuning vs prompting vs RAG (tradeoffs)
- RAG: chunking, retrieval, reranking, evaluation sets
- Agents/tool calling: tool boundaries, least privilege, logging

## High-signal Resources
- The Illustrated Transformer: https://jalammar.github.io/illustrated-transformer/
- Attention Is All You Need (paper): https://arxiv.org/abs/1706.03762

## Projects (proof of skill)
- RAG baseline + evaluation set (precision/recall style + qualitative review)
- Compare: prompting vs RAG vs finetuning (small-scale experiment)
- Tool-using agent demo with explicit allowlists + audit logs

## Optional
- Agentic AI notes: `AgenticAI.md`

## Security Link
- AI Security basics (prompt injection): `../Ai-security/README.md`
- Reading list: `../../papers/README.md`
