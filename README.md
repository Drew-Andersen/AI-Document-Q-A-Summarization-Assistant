# AI-Document-Q-A-Summarization-Assistant
An AI-powered document assistant that uses Large Language Models (LLMs) to summarize documents and answer questions **strictly based on provided text**.  
This project demonstrates practical usage of GPT models, prompt engineering, and modern NLP workflows in a production-style Python codebase.

## Project Structure
AI-Document-Q-A-Summarization-Assistant/
├── data/ 
│ └── sample.txt 
├── src/ 
│ ├── summarize.py 
│ ├── qa.py 
│ └── bert_qa.py 
├── .gitignore 
├── requirements.txt 
└── README.md 

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
- **python-dotenv** for environment management
- **VS Code** 
- **Git & GitHub** 

*(Currently expanding with Hugging Face Transformers and BERT-based models)*

## Setup and Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/Drew-Andersen/AI-Document-Q-A-Summarization-Assistant.git
cd AI-Document-Q-A-Summarization-Assistant
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables
Create a <code>.env</code> file in the root directory:
```.env
OPENAI_API_KEY=your_api_key_here
```

## Usage
> All scripts are designed to be run from the project root using the provided CLI interface.

Document Summarization
```bash
python src/summarize.py data/sample.txt
```

Document Question Answering (GPT)
```bash
python src/qa.py data/sample.txt "What are large language models?"
```
If the document does not contain the answer, the assistant will explicitly state that.

BERT-based Question Answering (Hugging Face)
```bash
python src/bert_qa.py
```

## Model Comparison
| Model | Type | Use Case | Notes |
|------|------|----------|-------|
| GPT | Generative | Summarization, open-ended Q&A | Flexible, prompt-driven |
| BERT | Extractive | Document-grounded Q&A | Deterministic, factual |

This project demonstrates when to use **generative** vs **extractive** NLP approaches depending on task requirements.

## What This Project Demonstrates
- Practical LLM integration using modern OpenAI APIs
- Prompt engineering for grounding and hallucination control
- Clean separation of data loading, inference, and CLI logic
- Transition from traditional NLP concepts to LLM-based workflows
- Real-world AI engineering best practices

## Future Improvements
- Expand BERT-based extractive question answering
- Add XLNet-based text classification
- Implement LangChain pipeline for document chunking and embeddings
- Add a Streamlit UI for interactive usage
- Support PDF and multi-document inputs
- Add evaluation metrics for answer quality

## Author
Drew Andersen
Aspiring AI / Machine Learning Engineer