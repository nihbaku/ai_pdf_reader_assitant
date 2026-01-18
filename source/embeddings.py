import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List

embedder = SentenceTransformer("all-MiniLM-L6-v2")

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
