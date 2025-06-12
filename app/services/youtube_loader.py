import time
import asyncio
from langchain_community.document_loaders import YoutubeLoader
from typing import List, Optional

async def load_youtube_transcript(video_url: str, language: List[str] = ["en"], translation: Optional[str] = None):
    for attempt in range(3):
        try:
            loader = YoutubeLoader.from_youtube_url(video_url, language=language, translation=translation)
            docs = loader.load()
            return docs
        except Exception as e:
            print(f"[Attempt {attempt+1}] Error loading YouTube transcript: {e}")
            await asyncio.sleep(3)
    return []
