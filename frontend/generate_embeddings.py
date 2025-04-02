from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import pandas as pd

df = pd.read_csv("confluence_pages.csv")
texts = df["content"].tolist()

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_texts(texts, embedding)
db.save_local("confluence.index")

print("Embeddings saved to confluence.index/")
