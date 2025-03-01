from fastapi import HTTPException
import chromadb, string, random, os
from modules.splitter import split_file
from schemas.add_document import AddDocumentResponseModel
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

def vectorize_documents(request):
    try:
        ids = []
        host = request.chromadb_details.host
        port = request.chromadb_details.port
        collection_name = request.chromadb_details.collection_name
        documents = split_file(request)

    except UnicodeDecodeError as e:
        raise HTTPException(e)
    
    for _ in range(len(documents)):
        ids.append(generate_random_number())

    try:
        embedding_function = OpenAIEmbeddingFunction(api_key = request.embedding_details.api_key, 
                                                     api_version = request.embedding_details.api_version,
                                                     model_name = request.embedding_details.model_name,
                                                     api_type = request.embedding_details.api_type,
                                                     api_base = request.embedding_details.api_base
                                                     )
        collection = get_or_create_collection(collection_name=collection_name, host=host, port=port, 
                                              embedding_function=embedding_function)
        result = collection.add(documents = documents, ids=ids)
        return AddDocumentResponseModel(message=f"Documents successfully added to the {collection_name} collection !")
    except Exception as e:
        raise HTTPException(e)
    
def generate_random_number(length=20):
    data = string.digits
    return ''.join(random.choice(data) for _ in range(length))

def get_chroma_client():
    client = chromadb.PersistentClient()
    return client

def get_chroma_httpClient(host, port):
    client = chromadb.HttpClient(host=host, port=port)
    return client

def get_or_create_collection(collection_name, embedding_function = None, host = None, port = None):
    if host and port:
        client = get_chroma_httpClient(host=host, port=port)
    else:
        client = get_chroma_client()

    collection = client.get_or_create_collection(name = collection_name, metadata={"hnsw:space":"cosine"}, embedding_function=embedding_function)
    return collection