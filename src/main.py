from dotenv import load_dotenv
from summarize import summarize_document
from qa import ask_question

load_dotenv()

if __name__ == "__main__":
    summary = summarize_document("data/sample.txt")
    print("Title:", summary.title)
    print("Summary:", summary.summary)
    print("Keywords:", summary.keywords)

    answer = ask_question("data/sample.txt", "What is the main topic?")
    print("Answer:", answer)