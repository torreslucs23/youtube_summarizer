import os
import io
import getpass
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.llms import HuggingFaceHub
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def load_youtube_transcript(video_url, language = 'en', translation = None):
    loader = YoutubeLoader.from_youtube_url(video_url, language=language, translation=translation)
    if not loader:
        raise ValueError("Failed to load YouTube transcript. Please check the video URL or language settings.")
    print(f"Loading transcript for video: {video_url}")
    return loader.load()[0]

loaded_docs = load_youtube_transcript("https://www.youtube.com/watch?v=7QU1nvuxaMA", ["en"])
print(loaded_docs)