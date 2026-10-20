# RAG Ingestion Pipeline with AI Guardrails

This project implements a secure, production‑ready ingestion pipeline for Retrieval‑Augmented Generation (RAG).  
It processes PDF documents, chunks them, scans each chunk using AI Guardrails, embeds the text using Ollama, and stores vectors in a FAISS vector store.

The pipeline enforces **Zero‑Trust principles** by validating every chunk before embedding and storage.

---

## 🚀 Features

### 🔹 1. PDF Loading & Chunking
- Uses `PyPDFLoader` to extract text.
- Splits documents using `RecursiveCharacterTextSplitter`.
- Configurable chunk size and overlap.

### 🔹 2. AI Guardrails (LLM Guard)
Each chunk is scanned for:
- **Prompt Injection**
- **Secrets / PII**
- **Toxicity**

Only safe chunks are embedded and stored.

### 🔹 3. Embedding via Ollama
- Uses `nomic-embed-text` model.
- Local inference via `http://localhost:11434/api/embeddings`.

### 🔹 4. FAISS Vector Store
- Stores embeddings using `IndexFlatL2`.
- Metadata stored in JSON.
- Supports loading, saving, and counting vectors.

### 🔹 5. Zero‑Trust Architecture
- Every input is scanned before processing.
- Guardrails applied at ingestion and retrieval.
- No chunk enters the vector store without passing security checks.

---

## 📂 Project Structure

ingestion/
│
├── chunker.py          # PDF loading + chunking
├── guardrails.py       # AI Guardrail scanners
├── embedder.py         # Embedding via Ollama
├── storage.py          # FAISS vector store
├── pipeline.py         # Main ingestion pipeline
├── ingest.py           # CLI entrypoint
│
vectorstore/
├── index.faiss         # FAISS index
└── metadata.json       # Chunk metadata

Code


---

## 🧠 Architecture Overview

The ingestion pipeline follows a secure, multi‑stage flow:

1. **Load PDF** → extract raw text  
2. **Chunk text** → manageable segments  
3. **Scan chunk** → guardrails (PII, toxicity, prompt injection)  
4. **Embed chunk** → vector representation  
5. **Store vector** → FAISS + metadata  
6. **Persist store** → disk save

See architecture diagram below.


---

# 🏗️ **Architecture Diagram (ASCII + description)**  
You can later convert this into a PNG using draw.io or Mermaid.

```markdown
                ┌──────────────────────────┐
                │        PDF File          │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   PyPDFLoader (Extract)  │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │ RecursiveCharacterSplitter│
                │   (Chunking)              │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     AI Guardrails        │
                │ PromptInjection / PII /  │
                │ Toxicity Scanners        │
                └─────────────┬────────────┘
                     Reject ❌ │   │ Accept ✔️
                              ▼
                ┌──────────────────────────┐
                │   Ollama Embeddings      │
                │  nomic-embed-text model  │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │      FAISS Vector Store  │
                │  + Metadata JSON         │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Persist to Disk        │
                └──────────────────────────┘

---

## 🔧 Installation

```bash
pip install langchain-community langchain-text-splitters llm-guard faiss-cpu requests

ollama pull nomic-embed-text

## Running the Ingestion pipeline
python ingest.py <path_to_pdf>

Example:
python ingest.py docs/whitepaper.pdf

Inspecting the Vector Store -
python inspect_store.py
