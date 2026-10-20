import sys
from ingestion.pipeline import ingest

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    ingest(pdf_path)
