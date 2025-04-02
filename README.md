# 🧠 AI-Powered Confluence Search Assistant (Local RAG Pipeline)

This is a prototype project to demonstrate how to build a **local AI-based search assistant** for Confluence pages using a Retrieval-Augmented Generation (RAG) approach. It uses `llama-cpp-python` to run a quantized LLM locally, semantic search via FAISS, and a Streamlit UI to ask questions in plain English.

---

## ✅ Steps to Run the AI-Powered Confluence Assistant

This project uses **LLM + semantic search** to enable natural language search over Confluence pages — fully locally, without internet or cloud services.

---

### 🧰 Step 1: Setup Environment and Dependencies

#### Terminal 1 — Start the LLM Backend

```bash
cd backend
python -m venv llm-env
llm-env\Scripts\activate
pip install -r requirements-llm.txt
```

- Sets up the backend to serve a local language model via Flask.
- Uses `llama-cpp-python` to run Mistral or TinyLlama locally.

#### Terminal 2 — Start the UI

```bash
cd frontend
python -m venv ui-env
ui-env\Scripts\activate
pip install -r requirements-ui.txt
```

- Prepares your Streamlit frontend and tools to embed/search documentation locally.

---

### 📦 Step 2: One-Time Setup

#### 🧠 Download the LLM model

In **Terminal 1**, run:

```bash
python download_model.py
```

- Downloads a quantized `.gguf` model (TinyLlama or Mistral) for CPU inference.

#### 📥 Extract Confluence Content

In **Terminal 2**, run:

```bash
python extract_confluence.py
```

- Uses your Atlassian API token to fetch Confluence pages.
- Cleans them into plain text and saves them in `confluence_pages.csv`.

---

### 🚀 Step 3: Launch the Full Stack

#### Terminal 1 — Start the LLM backend

```bash
python serve_llama_cpp.py
```

- Serves the model through a local Flask API.

#### Terminal 2 — Run the Streamlit UI

```bash
streamlit run app.py
```

- Launches a browser where you can ask questions.
- Answers are generated using retrieved context and the local LLM.

---

## 🔍 How It Works

This is a **RAG pipeline** with the following steps:

1. Pull Confluence data using API (`extract_confluence.py`)
2. Generate embeddings with HuggingFace (`generate_embeddings.py`)
3. Serve a quantized local LLM (`serve_llama_cpp.py`)
4. Search and chat via Streamlit (`app.py`)

---

📂 **GitHub Repo**: https://github.com/KamaleshJoshi/rag_confluence_assistant

🧠 Built to explore RAG, LLMs, semantic search, and local-first AI applications.