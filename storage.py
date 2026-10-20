import faiss
import numpy as np
import json
import os

EMBED_DIM = 768  # match your Ollama embedding dimension

class FaissStore:
    def __init__(self, index_path="vectorstore/index.faiss", meta_path="vectorstore/metadata.json"):
        self.index_path = index_path
        self.meta_path = meta_path

        os.makedirs("vectorstore", exist_ok=True)

        self.index = faiss.IndexFlatL2(EMBED_DIM)
        self.metadata = []

    def add(self, vector, metadata):
        vector = np.array(vector).astype("float32").reshape(1, -1)
        self.index.add(vector)
        self.metadata.append(metadata)

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.meta_path, "w") as f:
            json.dump(self.metadata, f, indent=2)

    def load(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
        if os.path.exists(self.meta_path):
            with open(self.meta_path, "r") as f:
                self.metadata = json.load(f)

    def count(self):
        return self.index.ntotal


# Alias so both imports work
VectorStore = FaissStore
