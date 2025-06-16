from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser


def build_summary_prompt():
    """
    Build a summary prompt template for summarizing text.
    """
    prompt = PromptTemplate.from_template(
        [
            ("system", "You are a helpful assistant that summarizes text."),
            (
                "user",
                "Summarize the following text:\n{input}\n\n"
                "Please provide a concise summary in one paragraph.",
            ),
        ],
        output_parser=StrOutputParser(),
    )