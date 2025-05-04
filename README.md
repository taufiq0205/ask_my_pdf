# 📚 LLM RAG App

A modern, user-friendly AI-powered document chat application built with Streamlit and Hugging Face models. This project enables you to upload PDFs, ask questions in natural language, and receive intelligent answers generated from your own documents.

---

## 🚀 Features

- **PDF Upload & Chat**: Upload one or more PDF files and interact with them using a conversational interface.
- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval with advanced language models for accurate, context-aware answers.
- **Custom Embeddings**: Uses state-of-the-art sentence embeddings (MiniLM) for semantic search.
- **Modern UI**: Clean, responsive chat interface inspired by ChatGPT and Claude.
- **Local or Cloud LLM**: Easily switch between local and cloud-based large language models.

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/) (Python), Custom CSS
- **PDF Processing:** [PyMuPDF (pymupdf)](https://pymupdf.readthedocs.io/)
- **Embeddings:** [Sentence Transformers](https://www.sbert.net/) (MiniLM model)
- **Vector Search:** [FAISS](https://github.com/facebookresearch/faiss)
- **Large Language Models:** [Hugging Face Transformers](https://huggingface.co/transformers/), [Torch](https://pytorch.org/)
- **Model Hub:** [Hugging Face Hub](https://huggingface.co/)
- **Utilities:** [tqdm](https://tqdm.github.io/) (progress bars), Python logging, pickle, numpy
- **Environment/Secrets:** `.env` file (dotenv pattern)

---

## 🛠️ How It Works

1. **Upload PDFs**: Drag and drop your PDF files into the sidebar.
2. **Ask Questions**: Type your question in the chat box at the bottom.
3. **Get Answers**: The app retrieves relevant document chunks and generates an answer using an LLM.

---

## 🏗️ Project Structure


rag-llm/
├── app.py                # Main Streamlit app
├── utils/                # Utility modules (embedding, retrieval, LLM inference, etc.)
├── models/               # Downloaded embedding models (ignored by git)
├── data/                 # Indexes and chunked data
├── style/                # CSS for UI
├── .env                  # API keys and secrets (ignored by git)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

