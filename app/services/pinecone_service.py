import pinecone
from app.services.ollama_service import get_embedding
import os
from pinecone import Pinecone, ServerlessSpec


# PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# pinecone.init(api_key=PINECONE_API_KEY, environment='gcp-starter') 

pc = Pinecone(
        api_key=os.environ.get("PINECONE_API_KEY")
    )

EMBEDDING_DIMENSION = 384

def embed_chunks_to_pinecone(chunks, index_name):
    if index_name in pc.list_indexes().names():
        pc.delete_index(name = index_name)
    
    pc.create_index(name = index_name, dimension = EMBEDDING_DIMENSION,metric = 'cosine',spec=ServerlessSpec(cloud="aws",region="us-east-1"))
    index = pc.Index(name = index_name)
    embeddings_with_ids = []
    for i,chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        embeddings_with_ids.append((str(i),embedding,chunk))
    upserts = [(id,vec,{"chunk_text":text}) for id,vec,text in embeddings_with_ids]
    index.upsert(vectors = upserts)

def get_similar_context_chunks(query, index_name):
    question_embedding = get_embedding(query)
    index = pc.Index(name = index_name)
    query_results = index.query(vector=question_embedding, top_k=3, include_metadata=True)
    context_chunks = [x['metadata']['chunk_text'] for x in query_results['matches']]
    return context_chunks

