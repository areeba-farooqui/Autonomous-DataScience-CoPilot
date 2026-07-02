from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from knowledge_base import knowledge_base

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts):

    embeddings = model.encode(texts)

    return np.array(embeddings).astype("float32")


def build_faiss_index(texts):

    embeddings = create_embeddings(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, embeddings

def retrieve_documents(query, texts, index, top_k=3):

    query_embedding = create_embeddings([query])

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        results.append(texts[i])

    return results

index, embeddings = build_faiss_index(knowledge_base)