import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.config import CHUNK_SIZE, CHUNK_OVERLAP
from utils.logger import setup_logger

logger = setup_logger()

def load_pdf(file_path):
    logger.info(f"Loading PDF: {file_path}")
    try:
        doc = fitz.open(file_path)
        return " ".join(page.get_text() for page in doc)
    except Exception as e:
        logger.error(f"Error loading PDF: {str(e)}")
        raise

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_text(text)

def load_documents(uploaded_files):
    """
    Accepts a list of uploaded PDF files (from Streamlit), extracts text, and chunks them.
    Returns a list of text chunks.
    """
    all_chunks = []
    for uploaded_file in uploaded_files:
        # Streamlit's uploaded_file is a file-like object, so we need to read it into PyMuPDF
        try:
            doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            text = " ".join(page.get_text() for page in doc)
            chunks = chunk_text(text)
            all_chunks.extend(chunks)
        except Exception as e:
            logger.error(f"Error processing uploaded file {uploaded_file.name}: {str(e)}")
            continue
    return all_chunks
