import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_text(file_path: str) -> str:
    """Load text from a file."""
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
        sys.exit(1)

def ask_question(document: str, question: str) -> str:
    """Ask a question about the document using GPT."""
    prompt = f"""
        You are a document-based question answering assistant.
        Answer the question using ONLY the information provided in the document.
        If the answer cannot be found in the document, say "The document does not contain this information."

        Document:
        {document}

        Question:
        {question}
        """
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You answer questions stricktly based on the provided documents."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python qa.py <path_to_text_file> <question>")
        sys.exit(1)

    file_path = sys.argv[1]
    question = sys.argv[2]

    document_text = load_text(file_path)
    answer = ask_question(document_text, question)

    print("ANSWER:")
    print(answer)