import streamlit as st
from utils.model_downloader import download_embedding_model
from utils.embedder import get_embedder
from utils.document_loader import load_documents
from utils.retriever import get_retriever
from utils.llm_inference import ask_llm

st.set_page_config(page_title="LLM RAG App", page_icon="📄", layout="wide")

# --- Load external CSS ---
with open("style/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# --- Sidebar: PDF Upload ---
with st.sidebar:
    st.title("📄 PDF Chat")
    st.markdown("Upload your PDFs here to start chatting with your documents.")
    uploaded_files = st.file_uploader("Upload PDFs", type=['pdf'], accept_multiple_files=True)
    if st.button("Clear Chat"):
        st.session_state.pop("chat_history", None)
        st.session_state.pop("retriever", None)
        st.session_state.pop("docs", None)
        st.rerun()

# --- Download and Load Embedding Model (once) ---
@st.cache_resource
def get_cached_embedder():
    download_embedding_model()
    return get_embedder()

embedder = get_cached_embedder()

# --- Document Processing and Retriever Setup ---
if uploaded_files:
    if "docs" not in st.session_state or st.session_state.get("uploaded_files") != uploaded_files:
        with st.spinner('🔄 Processing documents...'):
            docs = load_documents(uploaded_files)
            retriever = get_retriever(docs, embedder)
            st.session_state["docs"] = docs
            st.session_state["retriever"] = retriever
            st.session_state["uploaded_files"] = uploaded_files
            st.session_state["chat_history"] = []
    else:
        docs = st.session_state["docs"]
        retriever = st.session_state["retriever"]
else:
    docs = None
    retriever = None

# --- Main Chat UI ---
# REMOVE the entire st.markdown("""<style>...</style>""", unsafe_allow_html=True) block here
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# --- Chat History Display ---
chat_history = st.session_state.get("chat_history", [])
for entry in chat_history:
    if entry["role"] == "user":
        st.markdown(f'<div class="user-msg">{entry["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-msg">{entry["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Chat Input (fixed at bottom, Apple style) ---
if retriever:
    st.markdown('<div class="input-container"><div class="input-inner">', unsafe_allow_html=True)
    user_query = st.text_input(
        "Ask anything...",
        key="user_input",
        label_visibility="collapsed",
        placeholder="Ask anything about your PDFs..."
    )
    send = st.button("Send", key="send_btn")
    st.markdown('</div></div>', unsafe_allow_html=True)

    if send and user_query.strip():
        # Append user message
        chat_history.append({"role": "user", "content": user_query})
        st.session_state["chat_history"] = chat_history

        with st.spinner('🔄 Generating Answer...'):
            response = ask_llm(user_query, retriever)
        # Append AI response
        chat_history.append({"role": "assistant", "content": response})
        st.session_state["chat_history"] = chat_history

        st.rerun()
else:
    st.info("Please upload PDFs to start chatting.")
