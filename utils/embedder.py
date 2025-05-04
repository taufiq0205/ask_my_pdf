from sentence_transformers import SentenceTransformer
from utils.config import EMBEDDING_MODEL_LOCAL_PATH
from utils.model_downloader import download_embedding_model

def get_embedder():
    download_embedding_model()
    embedder = SentenceTransformer(EMBEDDING_MODEL_LOCAL_PATH)
    return embedder

def embed_texts(texts, embedder):
    return embedder.encode(texts, show_progress_bar=True)
