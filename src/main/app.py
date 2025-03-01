from fastapi import FastAPI, Request, status, Depends
from routers import router

app = FastAPI()
api_root_path = "/api/v1"

app.include_router(prefix=api_root_path, router=router.router)