from pydantic import BaseModel
from typing import Optional
from schemas.add_document import ChromaDBRequestModel, OpenAIVectorizerRequestModel

class ChromaDBSearchRequestModel(ChromaDBRequestModel):
    query_texts: str
    n_results: int = 3

class SearchDocumentRequestModel(BaseModel):
    chromadb_details: ChromaDBSearchRequestModel
    embedding_details: OpenAIVectorizerRequestModel
    

class SearchDocumentResponseModel(BaseModel):
    ids: list
    distances: list | None=None
    metadatas: list | None=None
    embeddings: list | None=None
    documents: list | None=None
    uris: list | None=None
    data: list | None=None
    included: list | None=None