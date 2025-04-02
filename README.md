# AI-Powered Confluence Search Assistant (Local RAG Pipeline)

This is a prototype project to demonstrate how to build a local AI-based search assistant for Confluence pages using a Retrieval-Augmented Generation (RAG) approach. It uses `llama-cpp-python` to run a quantized LLM locally, semantic search via FAISS, and a Streamlit UI to ask questions in plain English.

---

## Steps to Run the AI-Powered Confluence Assistant

This project uses LLM + semantic search to enable natural language search over Confluence pages — fully locally, without internet or cloud services.

---

### Step 1: Setup Environment and Dependencies

#### Terminal 1 — Start the LLM Backend

```bash
cd backend
python -m venv llm-env
llm-env\Scripts\activate
pip install -r requirements-llm.txt
```

#### Terminal 2 — Start the UI

```bash
cd frontend
python -m venv ui-env
ui-env\Scripts\activate
pip install -r requirements-ui.txt
```

---

### Step 2: One-Time Setup

#### Configure `.env` File

Create a `.env` file in the `frontend/` folder with the following content:

```
CONFLUENCE_EMAIL=your_email@example.com
CONFLUENCE_API_TOKEN=your_confluence_api_token_here
CONFLUENCE_DOMAIN=https://yourdomain.atlassian.net
CONFLUENCE_SPACE_KEY=your_space_key
HF_TOKEN=your_huggingface_token_here
```

#### Download the LLM model

In Terminal 1, run:

```bash
python download_model.py
```

#### Extract Confluence Content

In Terminal 2, run:

```bash
python extract_confluence.py
```

#### Generate Embeddings

In Terminal 2, after extracting content, run:

```bash
python generate_embeddings.py
```

---

### Step 3: Launch the Full Stack

#### Terminal 1 — Start the LLM backend

```bash
python serve_llama_cpp.py
```

#### Terminal 2 — Run the Streamlit UI

```bash
streamlit run app.py
```

---

## How It Works

1. Pull Confluence data using API (`extract_confluence.py`)
2. Generate embeddings with HuggingFace (`generate_embeddings.py`)
3. Serve a quantized local LLM (`serve_llama_cpp.py`)
4. Search and chat via Streamlit (`app.py`)

---

Built to explore RAG, LLMs, semantic search, and local-first AI applications.