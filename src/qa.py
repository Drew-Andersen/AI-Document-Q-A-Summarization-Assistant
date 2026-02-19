from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core. output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from rag.retriever import get_retriever

def build_qa_chain(file_path: str):
    retriever = get_retriever(file_path)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    prompt = ChatPromptTemplate.from_template(
        """
        Answer the question using ONLY the context below.
        If the answer is not in the context, say:
        "The document does not contain the information."

        Context: 
        {context}

        Question:
        {question}
        If the question refers to an acronym, use the expanded form found in the context.
        """)
    
    llm = ChatOpenAI()
    output_parser = StrOutputParser()

    chain = (
        {
        "context": retriever | RunnableLambda(format_docs), 
        "question": RunnablePassthrough()
        } 
        | prompt 
        | llm 
        | output_parser
    )

    return chain

