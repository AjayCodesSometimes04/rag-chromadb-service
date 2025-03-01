from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from openai._types import NotGiven

NOT_GIVEN = NotGiven()

class SourceFileModel(BaseModel):
    source_filepath: str
    max_chars: int = 1000

class OpenAIVectorizerRequestModel(BaseModel):
    api_key: str
    api_version: str
    api_type: str
    model_name: str
    api_base: str

class ChromaDBRequestModel(BaseModel):
    host: str
    port: int
    collection_name: str

#Request Model for adding documents in ChromaDB
class AddDocumentRequestModel(BaseModel):
    sourcefile_details: SourceFileModel
    embedding_details: OpenAIVectorizerRequestModel
    chromadb_details: ChromaDBRequestModel

#Response Model for adding documents in ChromaDB
class AddDocumentResponseModel(BaseModel):
    message: str