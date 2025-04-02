from flask import Flask, request, jsonify
from llama_cpp import Llama
import multiprocessing

app = Flask(__name__)

llm = Llama(
    model_path="./models/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    #model_path="./models/TinyLlama/TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=multiprocessing.cpu_count(),  # use all cores
    n_batch=128,  # Use higher batch size
    verbose=False
)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    output = llm(prompt, max_tokens=512, temperature=0.1)
    return jsonify({"text": output["choices"][0]["text"].strip()})

if __name__ == "__main__":
    app.run(port=8000)

