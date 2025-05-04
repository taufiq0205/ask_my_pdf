import faiss
import numpy as np
import pickle
from utils.config import FAISS_INDEX_PATH, CHUNK_DATA_PATH

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index

def save_index(index, chunks):
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(CHUNK_DATA_PATH, 'wb') as f:
        pickle.dump(chunks, f)

def load_index_and_chunks():
    index = faiss.read_index(FAISS_INDEX_PATH)
    with open(CHUNK_DATA_PATH, 'rb') as f:
        chunks = pickle.load(f)
    return index, chunks

def retrieve(query, embedder, index, chunks, top_k=5):
    q_emb = embedder.encode([query])
    distances, indices = index.search(np.array(q_emb), top_k)
    return [chunks[i] for i in indices[0]]

def get_retriever(docs, embedder):
    """
    Given a list of document chunks and an embedder, create a FAISS index and return a retrieval function.
    """
    embeddings = embedder.encode(docs, show_progress_bar=True)
    index = create_faiss_index(embeddings)

    def retriever(query, top_k=5):
        return retrieve(query, embedder, index, docs, top_k=top_k)

    return retriever
