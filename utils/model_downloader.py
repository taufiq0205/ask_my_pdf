# utils/model_downloader.py

import os
import logging
import shutil
from tqdm import tqdm

from sentence_transformers import SentenceTransformer
from utils.config import EMBEDDING_MODEL_NAME, EMBEDDING_MODEL_LOCAL_PATH, HF_API_TOKEN

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def download_embedding_model():
    if os.path.exists(EMBEDDING_MODEL_LOCAL_PATH):
        logger.info(f"Embedding model already exists at {EMBEDDING_MODEL_LOCAL_PATH}")
        return

    logger.info(f"Downloading embedding model {EMBEDDING_MODEL_NAME} to {EMBEDDING_MODEL_LOCAL_PATH}")
    
    # tqdm progress display
    with tqdm(total=100, desc="Downloading Model", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}%", ncols=70) as pbar:
        model = SentenceTransformer(EMBEDDING_MODEL_NAME, use_auth_token=HF_API_TOKEN)
        for _ in range(10):
            pbar.update(10)  # Fake update progress (because sentence-transformers downloads all at once)

    # Save model to your project folder
    if not os.path.exists(EMBEDDING_MODEL_LOCAL_PATH):
        os.makedirs(EMBEDDING_MODEL_LOCAL_PATH)

    model.save(EMBEDDING_MODEL_LOCAL_PATH)
    logger.info(f"Model saved locally at {EMBEDDING_MODEL_LOCAL_PATH}")
