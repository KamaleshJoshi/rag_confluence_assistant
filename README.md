Steps to Run:

Step 1: 
    Open command terminal 1: Start LLM Backend
        cd backend
        python -m venv llm-env
        llm-env\Scripts\activate
        pip install -r requirements-llm.txt


    Open command terminal 2: Start UI
        cd frontend
        python -m venv ui-env
        ui-env\Scripts\activate
        pip install -r requirements-ui.txt


Step 2:
    One time setup:
        Download Mistral GGUF model => In the terminal 1 run "python download_model.py"

        Extract data from confluence => In the terminal 2 run "python extract_confluence.py"


Step 3:
    In terminal 1: python serve_llama_cpp.py
    In terminal 2:  streamlit run app.py