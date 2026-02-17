# AI-Document-Q-A-Summarization-Assistant

A production-style AI document assistant that:
- Summarizes long documents into concise bullet points
- Answers questions strictly grounded in sourse text
- Detects insuffucuent information to prevent hallucination

Built with GPT models and transformer-based NLP approaches.

## Project Structure
```
AI-Document-Q-A-Summarization-Assistant/
├── data/ 
│ └── sample.txt 
├── src/ 
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
Large Language Models have transformed how we interact with text. However, deploying them responsibly requires:
- Grounding responses in source data
- Controlling hallucinations
- Designing modular, maintainable systems

This application allows users to:
- Summarize documents using GPT-based LLMs
- Ask questions about a document 
- Explicitly detect when information is missing

## Features
- **Document Summarization**
  - Generates concise bullet-point summaries from text files
  - Uses prompt constraints to control hallucinations
- **Document-Based Question Answering**
  - Answers questions using *only* the provided document
  - Refuses to fabricate information when insufficient context exists
- **Prompt Grounding**
  - Clear separation between document context and model instructions
  - Explicit system contraints to prevent external knowledge leakage
- **Modular Python Architecture**
  - Extensible design for adding new models
  - Clean separation of concerns
  - Centralized LLM abstraction layer

## Model Comparison
| Model | Type | Use Case | Notes |
|------|------|----------|-------|
| GPT | Generative | Summarization, open-ended Q&A | Flexible, prompt-driven |
| BERT | Extractive | Document-grounded Q&A | Deterministic, factual |
| XLNet | Classification | Text classification | Permutation language modeling, outputs label + confidence score |

This project demonstrates when to use **generative** vs **extractive** NLP approaches depending on task requirements.

## Tech Stack
- **Python 3.10**
- **OpenAI GPT Models**
- **Hugginf Face Transformers** (experimental)
- **python-dotenv** for environment management
- **VS Code** 
- **Git & GitHub** 

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
- Design modular AI systems
- Comparing generative vs extractive NLP approaches
- Transition from traditional NLP concepts to LLM workflows
- Production-style environment configuration 

## Future Improvements
- Expand BERT-based extractive QA with evaluation metrics
- Implement document chunking + embeddings (RAG pipeline)
- Add a Streamlit UI for interactive usage
- Support PDF and multi-document inputs
- Add automated answer evaluation metrics

## Author
Drew Andersen
Aspiring AI / Machine Learning Engineer