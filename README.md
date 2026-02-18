# AI-Document-Q-A-Summarization-Assistant

A production-style AI document assistant that:
- Summarizes long documents into concise bullet points
- Answers questions strictly grounded in source text
- Streams responses in real-time using LangChain LCEL
- Detects insufficient information to prevent hallucination

Built with OpenAI GPT models, LangChain LCEL pipelines, and transformer-based NLP architectures.

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
Large Language Models (LLMs) have transformed how we interact with text. However, deploying them responsibly requires:
- Grounding responses in source data
- Controlling hallucinations
- Designing modular, maintainable systems

This application demonstrates:
- Generative LLM summarization
- Document-grounded question answering 
- Streaming outputs using LCEL
- Clean separation of concerns between CLI, pipelines, and utilities

## Features
- **Document Summarization**
  - Bullet-point summaries
  - Keyword extraction
  - Structured output
- **LCEL-Based Question Answering**
  - Answers questions using *only* the provided document
  - Explicitly states when information is missing
  - Real-time token streaming in the CLI
- **Modular Architecture**
  - Reusable QA chain
  - Clear separation of runtime logic and LLM logic
  - Easily extensible to RAG pipelines

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
```.env
OPENAI_API_KEY=your_api_key_here
```

## Usage
> All scripts are designed to be run from the project root using the provided CLI interface.

Document Summarization and Question Answering
```bash
python src/main.py
```
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
- Practical LLM integration using modern OpenAI APIs
- Prompt engineering for grounding and hallucination control
- Designing modular AI systems
- Comparing generative vs extractive NLP approaches
- Transitioning from traditional NLP concepts to LLM workflows
- Production-style environment configuration 

## Future Improvements
- Convert summarization to LCEL
- Add RAG pipeline with embeddings
- Integrate vector database
- Add Streamlit UI
- Add evaluation benchmarking with batch()

## Author
Drew Andersen
Aspiring AI / Machine Learning Engineer