import os
import json
import requests
import ollama
from sentence_transformers import SentenceTransformer

OLLAMA_MODEL="mistral"

embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(chunk):
    """
    Generates embeddings using a SentenceTransformer model.
    """
    embedding = embedding_model.encode(chunk).tolist()  # Convert to list for compatibility
    return embedding


def get_llm_answer(prompt):
    """
    Generates a response using the Ollama model.
    """
    messages = [{"role": "user", "content": prompt}]
    
    response = ollama.chat(model=OLLAMA_MODEL, messages=messages)
    
    # Extract response content
    return response.get("message", {}).get("content", "No response received.")

