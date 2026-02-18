from dotenv import load_dotenv
from summarize import summarize_document
from qa import build_qa_question
from utils import load_text

load_dotenv()

# The app will summarize the document and show the title, summary, and keywords
if __name__ == "__main__":
    file_path = "data/sample.txt"

    summary = summarize_document(file_path)
    print("Title:", summary.title)
    print("Summary:", summary.summary)
    print("Keywords:", summary.keywords)

    # Load the document
    document = load_text(file_path)

    # Build QA chain
    qa_chain = build_qa_question()
    question = input("\nEnter your question about the document: ").strip()
    print("Answer:\n")

    for chunk in qa_chain.stream({
        "context": document,
        "question": question
    }):
        print(chunk, end="", flush=True)