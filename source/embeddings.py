import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List

embedder = SentenceTransformer("all-MiniLM-L6-v2") #Pre-trained embedding model

embedding_vector_dimension: int = 384
index = faiss.IndexFlatL2(embedding_vector_dimension)
documents: List[str] = []

def add_document(text: str) -> None:
    """Converts text to embedding vector and adds it to index."""

    vector = embedder.encode([text])
    vector = np.array(vector, dtype=np.float32)
    index.add(vector)
    documents.append(text)

def search(query: str, top_k: int = 3) -> List[str]:
    """Searches for the most similar document chunks."""
    vector = embedder.encode([query])
    vector = np.array(vector, dtype=np.float32)
    _, indices = index.search(vector, top_k)
    
    return [documents[i] for i in indices[0]]

def test_embedder():
    sentences = [
        "The weather is lovely today.",
        "It's so sunny outside!",
        "He drove to the stadium.",
    ]

    embeddings = embedder.encode(sentences)
    print(embeddings.shape)

    similarities = embedder.similarity(embeddings, embeddings)
    print(similarities)
