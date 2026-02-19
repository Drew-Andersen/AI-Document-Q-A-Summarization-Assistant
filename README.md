# AI-Document-Q-A-Summarization-Assistant

A Retrieval-Augmented Generation (RAG) system built with LangChain that:
- Summarizes long documents into concise bullet points
- Answers grounded questions using vector retrieval
- Streams responses in real-time using LangChain LCEL
- Uses Chroma for semantic search

Built with OpenAI GPT models, LangChain LCEL pipelines, RAG, and transformer-based NLP architectures.

## Project Architecture
This project demonstrates a modular AI system built using LangChain Expression Language (LCEL).

Key architectural concepts:
- invoke() - single input execution
- batch() - parallel multi-input execution
- stream() - token-level streaming output
- LCEL piping (|) for composable AI pipelines

## Project Structure
```
AI-Document-Q-A-Summarization-Assistant/
├── data 
│ └── sample.txt 
├── src 
│ ├── llm 
│ │   └── model.py 
│ ├── rag 
│ │   ├── retriever.py
│ │   └── vectorstore.py
│ ├── practice 
│ │   ├── bert_qa.py 
│ │   ├── langchain_openai_test.py
│ │   └── xlnet_text_classifier.py
│ ├── main.py
│ ├── qa.py
│ ├── summarize.py 
│ └── utils.py 
├── .gitignore 
├── README.md 
└── requirements.txt  
```

## Overview
Large Language Models (LLMs) have transformed how we interact with text. 
Responsible deployment requires:
- Grounding responses in source data
- Controlling hallucinations
- Designing modular, maintainable systems

This application demonstrates:
- Generative LLM summarization
- Document-grounded question answering 
- Streaming outputs using LCEL
- Clean separation of concerns between CLI, pipelines, and utilities

## Features
### Document Summarization
  - Uses structured Pydantic schema
  - Extracts:
    - Title
    - Summary
    - Keywords
  - Enforces format using `PydanticOutputParser`

### Retrieval-Augmented Generation (RAG)
- Splits documents into semantic chunks
- Embeds chunks using OpenAI embeddings
- Stores embeddings in Chroma vector database
- Uses MMR retrieval for diverse context
- Grounds answers strictly in retrieved context

### Streaming Responses
- Streams LLM output token-by-token using LCEL `.stream()`

### LCEL Pipeline
Built using LangChain Expression Language:
  - `RunnablePassthrough`
  - `RunnableLambda`
  - Prompt templates
  - Output parsers
  - Streaming execution

## Model Comparison
| Model | Type | Use Case | Notes |
|------|------|----------|-------|
| GPT | Generative | Summarization, open-ended Q&A | Flexible, prompt-driven |
| BERT | Extractive | Document-grounded Q&A | Deterministic, factual |
| XLNet | Classification | Text classification | Permutation language modeling, outputs label + confidence score |

This project demonstrates when to use **generative** vs **extractive** NLP approaches depending on task requirements.

## Tech Stack
- **Python 3.10+**
- **OpenAI GPT Models**
- **LangChain (LCEL)** 
- **python-dotenv** 
- **Hugging Face Transformers (practice modules)** 

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
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage
> All scripts are designed to be run from the project root using the provided CLI interface.

Document Summarization and Question Answering
```bash
python src/main.py
```
You will see:
1. Structured document summary
2. Prompt for a question
3. Streamed grounded answer

### Experimental Implementations (Practice Folder)
BERT-based Question Answering (Hugging Face)
```bash
python src/practice/bert_qa.py
```

XLNet Classification
```bash
python src/practice/xlnet_text_classifier.py
```

## What This Project Demonstrates
- Retrieval-Augmented Generation (RAG)
- Vector similarity search
- MMR retrieval strategy
- Document chunking strategies
- Structured LLM outputs
- Prompt engineering
- Streaming inference
- Modular AI system design

## Future Improvements
- Source citation display
- Persistent vector database loading
- Evaluation pipeline for QA
- Web UI interface (FastAPI, Flask, or Streamlit)

## Author
Drew Andersen
Aspiring AI / Machine Learning Engineer