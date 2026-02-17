import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

def test_langchain_openai():
    llm = ChatOpenAI(
        model = 'gpt-4',
        temperature = 0
    )

    messages = [
        SystemMessage(content="You are a helpful AI assistant."),
        HumanMessage(content="Explain Large Language Models in simple terms.")
    ]

    response = llm.invoke(messages)
    print(response.content)

if __name__ == "__main__":
    test_langchain_openai()