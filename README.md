# GenAI Knowledge Assistant (RAG-Based)
### Production-Ready Generative AI Application for Enterprise Knowledge Retrieval

---

## 📌 Overview
The **GenAI Knowledge Assistant** is a **production-ready Retrieval-Augmented Generation (RAG) system** designed to help enterprises quickly extract accurate answers from internal documents such as policies, manuals, FAQs, and reports.

Unlike traditional keyword-based search, this system enables **natural language querying** over organizational knowledge while keeping responses **grounded in source documents**, significantly reducing time spent searching and interpreting information.

---

## 🎯 Business Problem
In most organizations, critical knowledge is scattered across:
- PDF policy documents
- Internal manuals
- Knowledge base articles
- FAQs and text files

Employees often spend **10–15 minutes per query** manually:
- Searching documents
- Scanning multiple files
- Interpreting relevant sections

This results in:
- Productivity loss
- Inconsistent answers
- High dependency on subject-matter experts

---

## ✅ Solution
This project implements a **GenAI-powered Knowledge Assistant** that:

- Accepts **natural language questions**
- Retrieves **relevant document context** using vector search
- Generates **accurate, grounded answers** using an LLM
- Exposes functionality via a **REST API**
- Provides an easy-to-use **Streamlit UI**

---

## 📈 Measurable Impact
- ⏱ **~60% reduction in document search time**
- 📉 Reduced dependency on manual document review
- 🧠 Improved accuracy and consistency of responses
- 🔁 Reusable architecture for multiple departments

---

## 🧠 Key Concepts Demonstrated
- Retrieval-Augmented Generation (RAG)
- Embedding-based semantic search
- Vector databases (FAISS)
- Prompt engineering for grounded responses
- Separation of backend (AI logic) and frontend (UI)
- Production-style API deployment

---

## 🏗️ System Architecture
User (UI / API Client)
↓
Streamlit UI
↓
FastAPI Backend
↓
Retriever (FAISS Vector DB)
↓
Relevant Document Chunks
↓
Prompt Template + Context
↓
LLM (OpenAI API)
↓
Final Grounded Answer

---

## 🧰 Technology Stack

### Programming & Data
- Python
- Pandas
- SQL (conceptual integration)
- DuckDB (optional analytics)

### Generative AI
- OpenAI API (LLMs)
- Prompt Engineering
- Embeddings
- Retrieval-Augmented Generation (RAG)

### Vector Database
- FAISS (local, scalable)

### Backend & APIs
- FastAPI
- REST architecture
- Environment-based configuration

### Frontend
- Streamlit (lightweight UI)

### Dev & Ops
- Virtual environments
- Modular code structure
- Deployment-ready design

---

## 📁 Project Structure
genai-knowledge-assistant/
│
├── api/
│ └── main.py # FastAPI backend entry point
│
├── ui/
│ └── app.py # Streamlit user interface
│
├── src/
│ ├── config.py # Environment & configuration
│ ├── loader.py # Document loading (PDF/TXT)
│ ├── vector_store.py # FAISS vector database logic
│ └── rag_chain.py # RAG pipeline orchestration
│
├── scripts/
│ └── ingest_documents.py # One-time document ingestion
│
├── data/
│ └── documents/ # Input documents
│
├── embeddings/ # Persisted FAISS index
│
├── requirements.txt
├── .env.example
└── README.md

---

## ▶️ How It Works (Step-by-Step)

1. **Document Ingestion**
   - PDF and text documents are loaded
   - Documents are split into chunks
   - Embeddings are generated
   - Vectors are stored in FAISS

2. **Query Handling**
   - User submits a natural language question
   - Relevant chunks are retrieved via vector similarity
   - Retrieved context is injected into the LLM prompt

3. **Answer Generation**
   - LLM generates a response grounded in retrieved content
   - Answer is returned via API and displayed in UI

---

## 🚀 How to Run Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Configure environment

Create .env file:
OPENAI_API_KEY=your_api_key_here
3️⃣ Add documents

Place PDFs or text files in:
data/documents/ 
```

## 🧪 Example Use Cases

“What does the leave policy say about carry-forward?”

“Summarize the employee handbook.”

“What are the escalation steps in the operations manual?”

“List key compliance requirements from policy documents.”

## 🔐 Why RAG (Instead of Fine-Tuning)?

Faster to update documents

Lower operational cost

Reduced hallucination risk

Better compliance and traceability

## 🔮 Future Enhancements

Source citation display

Role-based access control

Agentic AI for multi-step workflows

Docker + cloud deployment

Monitoring and evaluation metrics

## 👤 Author

Swapnil Iwarkar
Applied AI & Data Scientist
LinkedIn: https://linkedin.com/in/swapnil-iwarkar66
