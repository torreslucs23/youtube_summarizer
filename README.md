# YouTube Video Summarizer

This app automatically generates **summaries of YouTube videos** using large language models (LLMs) through the Groq API.

---

##  How to Use

### 1. Create a virtual environment using `uv`:
```bash
uv venv
source .venv/bin/activate
```

### 2. Install the required packages:
```bash
uv pip install transformers youtube-transcript-api openai python-dotenv
```

### 3. Save the installed packages to `requirements.txt`:
```bash
uv pip freeze > requirements.txt
```

### 4. Set up your API key:
Create a `.env` file in the root directory of the project and add your Groq API key:

```
GROQ_API_KEY=your-api-key-here
```

### 5. Run the application:
```bash
uvicorn app.main:app --reload
```

---

##  Notes

- Make sure the YouTube video has **captions available**, as the app relies on transcripts to generate summaries.
- The Groq API key is **required** for the app to function properly.

---

## Techs Used

- [YouTube Loader API](https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.youtube.YoutubeLoader.html)
- [Llama3-70B](https://huggingface.co/Groq/Llama-3-Groq-70B-Tool-Use)
- [Uvicorn](https://www.uvicorn.org/)
- [Groq API](https://console.groq.com/)

---

Made with  by Lucas Torres