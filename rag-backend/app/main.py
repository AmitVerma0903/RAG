import logging
import os

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware

from app.logging_config import setup_logging
from app.routes import rag

load_dotenv()
setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI()
frontend_url = (os.getenv("FRONTEND_PRODUCTION_URL") or "https://your-default.com").rstrip("/")
logger.info("CORS allowed frontend URL: %s", frontend_url)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
        frontend_url,
        f"{frontend_url}/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(rag.router, prefix="/rag")