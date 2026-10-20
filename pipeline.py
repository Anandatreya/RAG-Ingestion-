from ingestion.chunker import load_and_chunk
from ingestion.guardrails import scan_chunk
from ingestion.embedder import embed
from ingestion.storage import FaissStore

def ingest(pdf_path):
    print(f"Loading {pdf_path}")
    chunks = load_and_chunk(pdf_path)

    store = FaissStore()

    for chunk in chunks:
        ok, risks = scan_chunk(chunk)

        if not ok:
            print(f"Rejected chunk due to risks: {risks}")
            continue

        vector = embed(chunk.page_content)
        store.add(vector, {"source": pdf_path, "text": chunk.page_content})

    store.save()
    print("Ingestion complete.")
