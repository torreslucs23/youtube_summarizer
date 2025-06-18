import logging
from fastapi import FastAPI
from app.api.api import api_router


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI(title="AI summary youtube service")

app.include_router(api_router)

