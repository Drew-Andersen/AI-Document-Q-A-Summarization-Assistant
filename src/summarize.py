from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import PydanticOutputParser

from llm.model import get_llm
from utils import load_text

class SummarySchema(BaseModel):
    title: str
    summary: str
    keywords: list[str]

def summarize_document(file_path: str):
    document = load_text(file_path)

    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=SummarySchema)

    format_instructions = parser.get_format_instructions()

    messages = [
        SystemMessage(
            content="You are a document summarization assistant. Return structured output."
        ),
        HumanMessage(
            content=f"""Summarize the following document.
            
            {format_instructions}

            Document: 
            {document}
            """
        )
    ]

    response = llm.invoke(messages)
    return parser.parse(response.content)