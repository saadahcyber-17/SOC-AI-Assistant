# 🛡️ SOC AI Assistant

> An AI-powered Cybersecurity Assistant built using **Retrieval-Augmented Generation (RAG)**, **Llama 3**, **FastAPI**, and **ChromaDB** to provide intelligent, context-aware cybersecurity assistance.


![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Llama3](https://img.shields.io/badge/Llama-3-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Powered-success?style=for-the-badge)

</p>

---

# 📖 Overview

SOC AI Assistant is a **Retrieval-Augmented Generation (RAG)** application developed to assist SOC analysts, cybersecurity students, and security enthusiasts by providing accurate, context-aware responses to cybersecurity questions.

Unlike traditional AI chatbots, the assistant retrieves relevant information from a cybersecurity knowledge base before generating responses, improving answer accuracy while reducing hallucinations.

The application combines semantic search with Large Language Models to answer questions related to:

- Windows Event Logs
- MITRE ATT&CK
- Splunk
- Threat Hunting
- Incident Response
- Authentication Attacks
- Cybersecurity Fundamentals

This project was built while learning **AI Security** to better understand the architecture and attack surface of modern LLM applications, including Prompt Injection, Knowledge Base Poisoning, Secure Retrieval, and Vector Databases.

---

# ✨ Features

- 🤖 AI-powered cybersecurity assistant
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using ChromaDB
- ⚡ FastAPI backend
- 🦙 Llama 3 integration
- 💬 Interactive chat interface
- 🛡 Cybersecurity knowledge base
- 🎯 Context-aware responses
- 📖 MITRE ATT&CK support
- 📊 Windows Event Log explanations
- 🔐 AI Security focused architecture

---

# 🏗 Architecture

```
                User
                  │
                  ▼
         Frontend (HTML/CSS/JS)
                  │
                  ▼
             FastAPI Backend
                  │
        ┌─────────┴──────────┐
        ▼                    ▼
 Embedding Model        Llama 3
        │
        ▼
     ChromaDB
(Vector Database)
        │
        ▼
Relevant Cybersecurity Documents
        │
        ▼
Context-Aware Response

```

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Backend | FastAPI |
| LLM | Llama 3 |
| Vector Database | ChromaDB |
| Frontend | HTML, CSS, JavaScript |
| AI | Retrieval-Augmented Generation (RAG) |
| Embeddings | Ollama Embeddings |

---

# 💡 Example Questions

- What is Event ID 4625?
- Explain Kerberoasting.
- What is MITRE ATT&CK?
- Explain Pass-the-Hash.
- Generate a Splunk SPL query for failed logins.
- How do I investigate brute-force attacks?
- Explain Windows Authentication Logs.

---

# 🎯 Learning Objectives

This project was developed to gain practical experience with:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embeddings
- FastAPI
- LLM Integration
- Prompt Engineering
- Semantic Search
- AI Security
- Prompt Injection
- Secure AI Application Development

---

# 🔒 AI Security Perspective

Building this project provided hands-on exposure to several AI security concepts, including:

- Prompt Injection
- Knowledge Base Poisoning
- Data Leakage
- Secure Retrieval
- Context Injection
- Vector Database Security
- LLM Attack Surface
- Retrieval Validation

---

# 🚀 Future Improvements

- User Authentication
- Role-Based Access Control
- Prompt Injection Detection
- Conversation Memory
- Multi-Document Retrieval
- SIEM Integration
- PDF Upload Support
- AI Threat Detection
- SOC Alert Analysis
- REST API Documentation

---

# 👨‍💻 Author

**Saad Ahmed**

Cybersecurity Student | SOC Analyst | AI Security Enthusiast

---

# ⭐ Support

If you found this project interesting, consider giving it a **Star ⭐** to support future development.
