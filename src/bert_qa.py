"""
BERT-based Question Andwering using Hugging Face Transformers.
This module answers questions strickly based on the provided documents.
"""

from transformers import pipeline
from pathlib import Path

def load_document(path: str) -> str:
    return Path(path).read_text(encoding='utf-8')

def answer_question(document: str, question: str) -> str:
    qa_pipeline = pipeline(
        'question-answering',
        model='distilbert-base-cased-distilled-squad'
    )
    return qa_pipeline(question=question, context = document)

if __name__ == "__main__":
    doc_path = 'data.sample.txt'
    document = load_document(doc_path)

    question = input('Ask a question about the document: ')
    result = answer_question(document, question)

    print('\nAnswer:', result['answer'])
    print('Confidence:', round(result['score'], 4))