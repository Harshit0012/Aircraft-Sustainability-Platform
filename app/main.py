from fastapi import FastAPI
from .router import auth, visualapi
from pydantic import BaseSettings
from fastapi.middleware.cors import CORSMiddleware

setting = BaseSettings()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(visualapi.router)

