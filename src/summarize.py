import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def load_text(file_path: str) -> str:
    """Load text from a file."""
    try: 
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Error: File not found at {file_path}')
        sys.exit(1)

def summariz_text(text: str) -> str:
    """Generate a summary using GPT"""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = (
        "Summarize the following document in 5 concise bullet points."
        "Focus ont he key ideas and main conclusions.\n\n"
        f"{text}"
    )

    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful AI assistant.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python summarize.py <path_to_text_file>')
        sys.exit(1)
    
    file_path = sys.argv[1]
    document_text = load_text(file_path)
    summary = summariz_text(document_text)

    print("SUMMARY:\n")
    print(summary)