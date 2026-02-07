import os
from llama_cpp import Llama

MODEL_PATH = os.getenv("MODEL_PATH", "../model/Phi-3-mini-4k-instruct-q4.gguf")
llm = Llama(model_path=MODEL_PATH, n_ctx=4096)

def generate(prompt: str) -> str:
    """Generate response from the LLM."""

    output = llm(prompt, max_tokens=512, stop=["</s>"], echo=False)

    return output["choices"][0]["text"].strip()
