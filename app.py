import streamlit as st
import os

from src.ingestion import extract_text
from src.chunking import create_chunks
from src.embeddings import create_embeddings
st.set_page_config(
    page_title="Advanced RAG Research Assistant",
    layout="wide"
)

st.title("📚 Advanced RAG Research Assistant")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "docx"]
)

if uploaded_file:

    # Create directory if not exists
    os.makedirs("data/raw", exist_ok=True)

    save_path = os.path.join(
        "data/raw",
        uploaded_file.name
    )

    # Save uploaded file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    # Extract text
    text = extract_text(save_path)

    st.subheader("Extracted Text")

    st.text_area(
        "Preview",
        text[:3000],
        height=300
    )
    # chunks = create_chunks(text)
    # for chunk in chunks:
    #     st.write(chunk.page_content)

    

    st.write(
        f"Total Characters Extracted: {len(text)}"
    )
    #creating chunks from the extracted text!!
    chunks=create_chunks(text)
    st.subheader("Text chunks")
    st.write(f"Total chunks created:{len(chunks)}")

    # Generating embeddings form the extracted text 
    embeddings=create_embeddings(chunks)
    st.subheader("Embeddings")
    st.write(f"Embeddings shape: {embeddings.shape}")



