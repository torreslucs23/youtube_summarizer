from fastapi import HTTPException
from app.services.modelService.create_model import create_llm
from app.services.youtube_loader import load_youtube_transcript
from app.services.modelService.prompt_pipeline import build_summary_prompt
from langchain_core.output_parsers import StrOutputParser

async def summarize(url: str) -> str | dict:
    if not url:
        return {"error": "URL is required"}

    docs = await load_youtube_transcript(url)
    transcription = docs[0].page_content if docs else None
    if transcription:
        # llm = Groq_LLM()
        llm = create_llm()
        prompt = build_summary_prompt(transcription)
        chain = prompt | llm | StrOutputParser()
        response = chain.invoke({})
        return response.strip()
    else:
        raise HTTPException(status_code=400, detail="Transcript not found for the provided URL")