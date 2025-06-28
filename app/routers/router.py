from fastapi import APIRouter, HTTPException
from app.services.youtube_loader import load_youtube_transcript
import logging
from pydantic import BaseModel
from app.services.modelService.summary_service import summarize

router = APIRouter()

class Req(BaseModel):
    url: str

@router.get("/")
def read_root():
    return {"message": "Hello, World!"}

@router.post("/summary/")
async def get_summary(body: Req):
    """""send a youtube url to a Llama model and get the summary of the video transcript"""""
    url = body.url
    if not url:
        return {"error": "URL is required"}
    try:
        response = await summarize(url)
    except Exception:
        logging.error(f"No transcript found for URL: {url}")
        raise
    logging.info(f"Transcript loaded successfully for URL: {url}")

    return {"summary": response}