from ingestion.embedder import embed
v = embed("test query")
print("len(embed)=", len(v))
