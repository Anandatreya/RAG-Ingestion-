from ingestion.storage import VectorStore

store = VectorStore()
store.load()   # <-- THIS WAS MISSING

print("Total vectors:", store.index.ntotal)

for i, m in enumerate(store.metadata):
    print(f"\nChunk {i}:")
    print(m["text"])
    print("----")
