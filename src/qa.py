from langchain_core.messages import SystemMessage, HumanMessage
from llm.model import get_llm
from utils import load_text

def ask_question(file_path: str, question: str):
    document = load_text(file_path)
    llm = get_llm()

    messages = [
        SystemMessage(
            content = "You are a document question-answering assistant. Return only the answer to the question. Do not restate the question."
        ),
        HumanMessage(
            content=f"""
            Answer the question based only on the document below.

            Document:
            {document}
            """
        )
    ]

    response = llm.invoke(messages)
    return response.content