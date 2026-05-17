# 🧠 Artificial General Intelligence (AGI)

AGI research aims to build systems that can **reason, learn, plan, generalize, and act across domains** — not just perform a single narrow task.

This part of the Academy explains:
- What AGI actually means  
- The skills required to work toward AGI  
- Core AGI subfields  
- Research directions  
- Links to ML → DL → GenAI → Agents → AGI  
- Projects, tools & resources  
- Learning roadmap  

AGI is built on everything before it — **Machine Learning → Deep Learning → Transformers → GenAI → Agents → AGI**.

---

# 🧱 Prerequisites

Before learning AGI, you must have a strong understanding of:

### 🔹 Required
- **Deep Learning** → `../DeepLearning/README.md`
- **Transformers & LLMs** → `../GenerativeAI/README.md`
- **Reinforcement Learning basics**
- **Math (linear algebra, probability, calculus)** → `../Fundamentals/README.md`

### 🔹 Highly Recommended
- **Agents & tool use**
- **Multimodal DL (vision + text)**
- **Basic robotics knowledge (optional but helpful)** → `../Robotics/README.md`

AGI sits at the **top of the intelligence hierarchy**.

---

# 🌐 1. What is AGI?

AGI = Systems capable of:
- Autonomous decision-making  
- Long-horizon planning  
- Multi-step reasoning  
- Learning new skills  
- Operating across tasks & domains  
- Using tools  
- Building models of the world  
- Improving themselves over time  

AGI is **not** one algorithm.  
It is a **stack** of multiple AI capabilities connected together.

---

# 🧩 2. Core AGI Subfields

### 🔹 **1. Multimodal Deep Learning**
Models that understand:
- Vision  
- Text  
- Audio  
- Video  
- Actions  

Examples:  
CLIP, GPT-4o, Flamingo, LLaVA, Kosmos-2  

---

### 🔹 **2. Large Language Models & Reasoning**
- Transformers  
- Long-context models  
- Chain-of-Thought reasoning  
- Program synthesis  
- Tool use  
- Planning  

LLMs form the **reasoning core** of modern proto-AGI systems.

---

### 🔹 **3. Reinforcement Learning (CRITICAL)**
- RLHF  
- PPO / A2C / SAC  
- Hierarchical RL  
- World models (MuZero-style)  
- Agency & reward modeling  

RL is essential for **autonomous behavior**, not just text generation.

---

### 🔹 **4. Agents & Tool Use**
Agents are LLMs that:
- Use tools  
- Plan steps  
- Query memory  
- Execute functions  
- Adapt based on feedback  

Frameworks:  
LangGraph, SmolAgents, OpenDevin, AutoGPT, Voyager

---

### 🔹 **5. Cognitive Architectures**
Inspired by:
- Human memory  
- Reasoning  
- Working memory  
- Planning & symbolic logic  

Hybrid neural-symbolic systems belong here.

---

### 🔹 **6. Continual & Lifelong Learning**
- Avoiding catastrophic forgetting  
- Curriculum learning  
- Adaptive memory  
- Meta-learning  

An AGI must learn **continuously**, not freeze after training.

---

### 🔹 **7. World Models**
Systems that build internal models of:
- The environment  
- Cause & effect  
- Spatial and temporal structure  
- Future prediction  

Examples:  
Dreamer, MuZero, VideoGPT, latent-
