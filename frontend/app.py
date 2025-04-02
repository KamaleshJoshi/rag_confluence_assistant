import streamlit as st
import requests
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

@st.cache_resource
def load_db():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local("confluence.index", embeddings, allow_dangerous_deserialization=True)

db = load_db()

def get_answer(query):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([doc.page_content[:1000] for doc in docs])
    prompt = f"""[INST] Use the context below to answer the question.

Context:
{context}

Question: {query}

Answer: [/INST]"""

    try:
        response = requests.post("http://localhost:8000/generate", json={"prompt": prompt, "max_tokens": 512})
        return response.json()["text"]
    except Exception as e:
        return f"❌ Error: {e}"

st.title("🔍 Confluence AI Search")
query = st.text_input("Ask a question")

if st.button("Search") and query:
    st.write("🔎 Searching...")
    answer = get_answer(query)
    st.markdown(f"### Answer:\n{answer}")
