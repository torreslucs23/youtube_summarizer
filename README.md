# My firts Steps
Create a venv ambience:
```sh
uv venv
source .venv/bin/activate
```

install the necessary packages
```sh
uv pip install transformers youtube-transcript-api openai python-dotenv
```
Save the dependencies
```sh
uv pip freeze > requirements.txt
```

## Docker
We can build using: 
```
docker build -t youtube-summary .
```
