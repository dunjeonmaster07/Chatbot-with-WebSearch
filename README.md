# 🤖 End-to-End Agentic AI Project

This project demonstrates how to build an **Agentic AI system** combining the power of **LLMs**, **LangGraph**, and a **Streamlit frontend**, with modular components for flexibility and scalability.

---

## 🧠 Concept Overview

### 🔁 Agentic AI = Chatbot + Workflow Engine

We use **LangGraph** to structure a multi-step agent workflow as a **graph** with:
- **Nodes**: Logic + LLMs (tools, functions)
- **Edges**: Data/state transitions between nodes

---

## 🧱 Project Architecture

### 📦 Frontend
- **Streamlit-based UI**
- Interactive user interface to send queries and display AI responses
- Frontend communicates with the backend graph pipeline

### 🕸 Workflow Engine (LangGraph)
- **Directed graph of nodes and edges**
- Each node can be:
  - A function
  - A tool
  - A call to an LLM (e.g., OpenAI, Groq, Azure)
- **Edges** define the control flow (state-based routing)

---

## 🔌 Independent Components
- Fully modular design
- Add or remove tools/LLMs independently
- Current examples:
  - `function + LLMs`: For classification, hallucination detection
  - `function2 + LLMs`: For grading, retrieval, or rewriting
  - More plug-and-play tools can be added

---

## 🔄 Pipeline
- Built using **LangGraph state management**
- Maintains conversation state and tool outputs across turns
- Capable of building **complex conditional workflows**

---

## 🚀 Features
- ✅ Modular nodes and LLM functions
- ✅ State-based routing with memory
- ✅ UI built with Streamlit
- ✅ Flexible graph design for experimentation

---

## 📌 Stack
- **Frontend**: `Streamlit`
- **Graph Orchestrator**: `LangGraph`
- **LLMs**: Groq, Azure OpenAI, OpenRouter, etc.
- **Tools**: Wikipedia, Arxiv, Web Search (Tavily), Custom Tools

---

## 📷 Visual Overview

![Architecture](./b36707de-a995-43b4-96dd-95dfdebcd7de.png)

---

## 🛠️ Setup

```bash
git clone https://github.com/your-username/langgraph-agentic-ai
cd langgraph-agentic-ai

# Optional: Create virtual env
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
# simple_ChatBot
### Chatbot with Web Search
