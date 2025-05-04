# CONFIGURATION SETTINGS

EMBEDDING_MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
EMBEDDING_MODEL_LOCAL_PATH = './models/all-MiniLM-L6-v2'
LLM_MODEL_NAME = 'mistralai/Mistral-7B-Instruct-v0.3'
USE_LOCAL_LLM = False
HF_API_TOKEN = None

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

FAISS_INDEX_PATH = 'data/index.faiss'
CHUNK_DATA_PATH = 'data/chunks.pkl'