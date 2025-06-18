import time
from langchain_community.document_loaders import YoutubeLoader
from typing import List, Optional
import logging
logger = logging.getLogger(__name__)


#load_youtube_transcript function to load YouTube transcripts with retries
async def load_youtube_transcript(video_url: str, language: List[str] = ["pt", "pt-BR", "en"]):
    for attempt in range(3):
        try:
            loader = YoutubeLoader.from_youtube_url(video_url, language=language)
            docs = loader.load()
            return docs
        except Exception as e:
            print(f"[Attempt {attempt+1}] Error loading YouTube transcript: {e}")
            time.sleep(2)
    return []
