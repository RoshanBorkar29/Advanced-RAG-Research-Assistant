from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def create_embeddings(chunks):

    chunk_texts = [
        chunk.page_content
        for chunk in chunks
    ]

    embeddings = model.encode(
        chunk_texts,
        show_progress_bar=True
    )

    return embeddings