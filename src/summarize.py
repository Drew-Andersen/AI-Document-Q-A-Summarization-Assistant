from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from llm.model import get_llm
from utils import load_text

class SummarySchema(BaseModel):
    title: str
    summary: str
    keywords: list[str]

def build_summarization_chain():
    output_parser = PydanticOutputParser(pydantic_object=SummarySchema)

    prompt = ChatPromptTemplate.from_template(
        """
        You are a document summarization assistant.
        Return structured output.

        {format_instructions}

        Summarize the following document:
        {document}
        """
    )

    llm = get_llm()

    chain = prompt | llm | output_parser

    return chain

def summarize_document(file_path: str):
    document = load_text(file_path)

    chain = build_summarization_chain()

    return chain.invoke({
        "document": document,
        "format_instructions": PydanticOutputParser(
            pydantic_object=SummarySchema
        ).get_format_instructions()
    })