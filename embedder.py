import requests

def embed(text):
    url = "http://localhost:11434/api/embeddings"

    payload = {
        "model": "nomic-embed-text",
        "prompt": text
    }

    r = requests.post(url, json=payload)
    data = r.json()

    # Ollama returns: {"embedding": [...]}
    return data["embedding"]
