# AI-Document-Q-A-Summarization-Assistant
An AI-powered document assistant that uses Large Language Models (LLMs) to summarize documents and answer questions **strictly based on provided text**.  
This project demonstrates practical usage of GPT models, prompt engineering, and modern NLP workflows in a production-style Python codebase.

## Overview
Large Language Models have transformed how we interact with text, but deploying them responsibly requires grounding responses in source data and controlling hallucinations.

This application allows users to:
- Summarize documents using GPT-based LLMs
- Ask questions about a document and receive grounded answers
- Detect when a document does *not* contain sufficient information

## Features
- **Document Summarization**
  - Generates concise bullet-point summaries from text files
- **Document-Based Question Answering**
  - Answers questions using *only* the provided document
  - Explicitly avoids hallucinations when information is missing
- **Prompt Grounding**
  - Clear separation between document context and model knowledge
- **Modular Python Architecture**
  - Clean, extensible structure suitable for future expansion

## Tech Stack
- **Python 3.10**
- **OpenAI GPT Models**
- **python-dotenv** for enviornment management
- **VS Code** for development
- **Git & GitHub** for version control

*(Planned additions: Hugging Face Transformers, BERT, XLNet, LangChain)*

## Setup and Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Drew-Andersen/AI-Document-Q-A-Summarization-Assistant.git
cd AI-Document-Q-A-Summarization-Assistant
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
source .env/bin/activate
```

### 3️⃣ Install dependancies
```bash
pip install requirements.txt
```

### 4️⃣ Set environment variables
Create a <code>.env</code> file in the root directory:
```.env
OPENAI_APY_KEY = your_api_key_here
```

## Usage
Document Summarization
```bash
python src/summarize.py data/sample.txt
```

Document Question Answering
```bash
python src/qa.py data/sample.txt "What are large language models?"
```
If the document does not contain the answer, the assistant will explicitly state that.

## What This Project Demonstrates
- Practical LLM integration using modern OpenAI APIs
- Prompt engineering for grounding and hallucination control
- Clean separation of data loading, inference, and CLI logic
- Transition from traditional NLP concepts to LLM-based workflows
- Real-world AI engineering best practices

## Future Improvements
- Add Hugging Face BERT-based Question Answering
- Add XLNet-based text classification
- Implement LangChain pipeline for document chunking and embeddings
- Add a Streamlit UI for interactive usage
- Support PDF and multi-document imputs
- Add evaluation metrics for answer quality

## Author
Drew Andersen
Aspiring AI / Machine Learning Engineer