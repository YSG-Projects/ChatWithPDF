# 📄 ChatWithPDF Clone using GenAI

A Streamlit-based web app that lets you upload and chat with your PDF files using OpenAI’s LLMs. Inspired by [chatpdf.com](https://www.chatpdf.com), this project leverages LangChain, FAISS, and OpenAI to create a semantic question-answering chatbot from your PDF documents.

---

## 🚀 Features

- Upload and process any PDF
- Semantic chunking and vector storage using FAISS
- Conversational querying powered by GPT-3.5 via LangChain
- Chat history with contextual memory
- Simple Streamlit UI

---

## 🛠️ Tech Stack

| Layer           | Tools Used                      |
|----------------|----------------------------------|
| PDF Handling    | PyPDF2                          |
| Embeddings      | OpenAI Embeddings (via LangChain) |
| Vector Store    | FAISS (in-memory)               |
| LLM Chat Engine | LangChain + OpenAI Chat Models  |
| Frontend        | Streamlit                       |
| Secrets         | python-dotenv                   |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/chatpdf-clone.git
cd chatpdf-clone
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
