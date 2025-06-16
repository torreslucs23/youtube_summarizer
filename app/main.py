import asyncio
from services.youtube_loader import load_youtube_transcript
import logging
from services.modelService.create_model import create_llm
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


async def main():
    url = "https://www.youtube.com/watch?v=1FOJpHdSgVk"
    docs =  await load_youtube_transcript(url)
    llm = await create_llm()
    response = llm.invoke("me faça um resumo com algumas palavras do vídeo: " + docs[0].page_content)
    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
