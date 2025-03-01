from fastapi import APIRouter
from modules.monitoring import get_healthcheck
from modules.add_document import vectorize_documents
from modules.search_document import search_documents_from_chromadb
from schemas.add_document import AddDocumentRequestModel, AddDocumentResponseModel
from schemas.search_document import SearchDocumentRequestModel, SearchDocumentResponseModel

router = APIRouter()

@router.get("/healthcheck", tags=["monitoring"])
async def healthcheck():
    response = get_healthcheck()
    return response

@router.post("/add_documents", response_model = AddDocumentResponseModel, tags=["add documents"])
async def add_documents(request: AddDocumentRequestModel):
    response = vectorize_documents(request)
    return response

@router.post("/search_documents", response_model =  SearchDocumentResponseModel, tags=["search documents"])
async def search_documents(request: SearchDocumentRequestModel):
    response = search_documents_from_chromadb(request)
    return response