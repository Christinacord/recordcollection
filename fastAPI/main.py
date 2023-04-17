from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import albums
import os

app = FastAPI()
app.include_router(albums.router, tags=["albums"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get("CORS_HOST", "http://localhost:3000")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)