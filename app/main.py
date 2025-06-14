import asyncio
from services.youtube_loader import load_youtube_transcript
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


async def main():
    url = "https://www.youtube.com/watch?v=68O8ez0eEGE"
    docs =  await load_youtube_transcript(url)
    logger.info(docs[0].page_content)

if __name__ == "__main__":
    asyncio.run(main())
