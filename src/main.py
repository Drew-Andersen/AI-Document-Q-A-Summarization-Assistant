from dotenv import load_dotenv
from summarize import summarize_document
from qa import ask_question

load_dotenv()

# The app will summarize the document and show the title, summary, and keywords
if __name__ == "__main__":
    summary = summarize_document("data/sample.txt")
    print("Title:", summary.title)
    print("Summary:", summary.summary)
    print("Keywords:", summary.keywords)

    # User can ask their own question about the document
    question = input("\nEnter your question about the document: ").strip()
    answer = ask_question("data/sample.txt", question)
    print("Answer:", answer)