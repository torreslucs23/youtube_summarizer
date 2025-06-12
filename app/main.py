import asyncio
from services.youtube_loader import load_youtube_transcript

async def main():
    url = "https://www.youtube.com/watch?v=AmsaaNFJ_Sk"
    docs = await load_youtube_transcript(url)
    print(docs)

if __name__ == "__main__":
    asyncio.run(main())
