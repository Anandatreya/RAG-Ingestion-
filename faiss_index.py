import faiss, pickle
idx = faiss.read_index("faiss.index")
print("index.ntotal =", idx.ntotal)
with open("faiss_meta.pkl","rb") as f:
    meta = pickle.load(f)
print("len(metadata) =", len(meta))
print("first meta keys:", list(meta[0].keys()) if meta else None)
