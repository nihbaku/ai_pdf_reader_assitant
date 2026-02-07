from embeddings import search
from llm import generate

def rag_answer(query: str) -> str:
    """Retrieves relevant context and returns generated prompt."""

    context_chunks = search(query)
    context_text = "\n".join(context_chunks)

    prompt = f"""
You are a helpful assistant. Use the provided context to answer the question.

Context:
{context_text}

Question: {query}
Answer:
"""

    return generate(prompt)
