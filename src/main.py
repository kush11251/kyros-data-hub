from fastapi import FastAPI
from src.routers import data_router

app = FastAPI()

app.include_router(data_router, prefix='/data')
