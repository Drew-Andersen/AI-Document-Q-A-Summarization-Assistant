from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core. output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from utils import load_text

def build_qa_question():
    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using ONLY the context below.
        If the answer is not in the context, say:
        "The document does not contain the information."

        Context: 
        {context}

        Question:
        {question}
        """)
    
    chat_prompt = ChatOpenAI()
    otput_parser = StrOutputParser()

    chain = prompt | chat_prompt | otput_parser

    return chain

