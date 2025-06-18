from langchain_core.prompts import  ChatPromptTemplate


def build_summary_prompt(transcription: str) -> ChatPromptTemplate:
    """
    Cria um prompt para o modelo LLaMA com o objetivo de resumir um vídeo do YouTube em português.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente útil e fluente em português, especializado em resumir transcrições de"
        " vídeos do YouTube de maneira bem detalhada, explicando ao usuário toda a mensagem."),
        ("user", (
            "Aqui está a transcrição de um vídeo:\n\n"
            "{transcription}\n\n"
            "Por favor, faça um resumo claro e conciso desse vídeo em **português**, com apenas um parágrafo."
        )),
    ])
    
    return prompt.partial(transcription=transcription)