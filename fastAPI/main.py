from fastapi import FastAPI
from authenticator import authenticator
from fastapi.middleware.cors import CORSMiddleware
from routers import accounts, albums
import os


app = FastAPI()
app.include_router(authenticator.router, tags=["accounts"])
app.include_router(accounts.router, tags=["accounts"])
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
