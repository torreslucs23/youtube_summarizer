from langchain_groq import ChatGroq
import os
from config.keys import GROQ_API_KEY


api_key = GROQ_API_KEY

async def create_llm():
    """
    Create a ChatGroq instance with the specified model and parameters.
    """
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    
    # Initialize the ChatGroq instance with the specified model and parameters
    return ChatGroq(
        model="llama3-70b-8192",
        temperature=0.7,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=api_key
    )
