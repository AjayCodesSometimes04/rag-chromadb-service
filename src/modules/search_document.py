from fastapi import HTTPException
from schemas.search_document import SearchDocumentResponseModel
from modules.add_document import get_or_create_collection
from chromadb.utils.embedding_functions.openai_embedding_function import OpenAIEmbeddingFunction

def search_documents_from_chromadb(request):
    try:
        host = request.chromadb_details.host
        port = request.chromadb_details.port
        collection_name = request.chromadb_details.collection_name
        query_texts = request.chromadb_details.query_texts
        n_results = request.chromadb_details.n_results
    except UnicodeDecodeError as e:
        raise HTTPException(e)
    
    try:
        embedding_function = OpenAIEmbeddingFunction(api_key = request.embedding_details.api_key,                                                
                                                    api_version = request.embedding_details.api_version,
                                                    model_name = request.embedding_details.model_name,
                                                    api_type = request.embedding_details.api_type,
                                                    api_base = request.embedding_details.api_base
                                                        )
        collection = get_or_create_collection(collection_name=collection_name, host=host, port=port, 
                                                embedding_function=embedding_function)
        result = collection.query(query_texts=query_texts, n_results=n_results)
        return SearchDocumentResponseModel(ids=result['ids'], distances=result['distances'],
                                           metadatas=result['metadatas'], query_embeddings=result['embeddings'],
                                           documents=result['documents'], uris=result['uris'],
                                           data=result['data'], included=result['included']
                                           )
    except Exception as e:
        raise HTTPException(e)