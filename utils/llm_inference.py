from utils.config import LLM_MODEL_NAME, USE_LOCAL_LLM, HF_API_TOKEN
from transformers import pipeline
from huggingface_hub import InferenceClient
from utils.nemotron import nemotron_generate

# Load model
if USE_LOCAL_LLM:
    generator = pipeline("text-generation", model=LLM_MODEL_NAME, device=0, torch_dtype="auto")
else:
    client = InferenceClient(model=LLM_MODEL_NAME, token=HF_API_TOKEN)

def generate_answer(context, question):
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    return nemotron_generate(prompt)

def ask_llm(query, retriever):
    """
    Given a user query and a retriever, retrieve relevant context and generate an answer.
    """
    context_chunks = retriever(query, top_k=5)
    context = "\n".join(context_chunks)
    return generate_answer(context, query)
