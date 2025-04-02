from huggingface_hub import snapshot_download
from pathlib import Path

# Define the local path inside your current directory
mistral_models_path = Path.cwd().joinpath('models', 'Mistral-7B-Instruct-v0.2-GGUF')
mistral_models_path.mkdir(parents=True, exist_ok=True)

# Download only the required GGUF model file
snapshot_download(
    repo_id="TheBloke/Mistral-7B-Instruct-v0.2-GGUF",
    allow_patterns=["mistral-7b-instruct-v0.2.Q4_K_M.gguf"],
    local_dir=mistral_models_path
)

print(f"✅ Mistral GGUF model downloaded at: {mistral_models_path}")

# from huggingface_hub import snapshot_download
# from pathlib import Path

# model_path = Path.cwd().joinpath("models/TinyLlama")
# model_path.mkdir(parents=True, exist_ok=True)

# snapshot_download(
#     repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
#     allow_patterns=["TinyLlama-1.1B-Chat-v1.0.Q4_K_M.gguf"],
#     local_dir=model_path
# )