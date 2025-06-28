from langchain_groq import ChatGroq
import os
from app.config.keys import GROQ_API_KEY


api_key = GROQ_API_KEY

# class Groq_LLM(ChatGroq):
#     def __init__(self):
#         if not api_key:
#             raise ValueError("GROQ_API_KEY environment variable is not set.")
#         super().__init__(
#             model="llama3-70b-8192",
#             temperature=0.7,
#             max_tokens=1024,
#             timeout=None,
#             max_retries=2,
#             api_key = GROQ_API_KEY
#         )


def create_llm():
    """
    Create a ChatGroq instance with the specified model and parameters.
    """
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    
    # Initialize the ChatGroq instance with the specified model and parameters
    return ChatGroq(
        model="llama3-70b-8192",
        temperature=0.7,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
        api_key=api_key
    )
