# 🚀 Convo Pro

Convo Pro is a ChatGPT-style Generative AI chat application built using Streamlit and Ollama, with persistent conversation storage via MongoDB.
The application is deployed on AWS EC2 using Docker-based services.

# ✨ Features

1. Chat with a locally hosted LLM (ChatGPT-like experience)

2. Persistent chat history stored in MongoDB

3. Clean and interactive Streamlit UI

4. Deployed on AWS EC2

5. Dockerized LLM and database services


# 🛠 Tech Stack

1. UI: Streamlit

2. LLM Provider: Ollama

3. LLM Orchestration: LlamaIndex

4. Database: MongoDB

5. Containerization: Docker (Ollama & MongoDB)

6. Cloud: AWS EC2

7. Language: Python

# 📦 Dependencies

streamlit==1.49.1

ollama==0.5.3

llama-index==0.14.0

llama-index-llms-ollama==0.7.2
pymongo==4.14.1

pydantic==2.11.7

pydantic-settings==2.10.1

python-dotenv==1.1.1

# 🐳 Docker Usage (Minimal & Honest)

This project uses official Docker images for core services:

- ollama/ollama → LLM service

- mongo → Chat history storage

Docker is used on AWS EC2 to:

- Run Ollama as a containerized LLM service

- Run MongoDB as a containerized database

- Keep services isolated and portable

⚠️ The Python Streamlit application runs directly on EC2 (not containerized).

# ⚙️ Environment Variables

MONGO_DB_URL="mongodb://localhost:27017/"  

MONGO_DB_NAME="chat_app"

OLLAMA_URL="http://localhost:11434"

OLLAMA_MODELS="gemma2:2b,tinyllama:1.1b"

# 🚀 Running Locally

pip install -r requirements.txt

Run MongoDB locally on port 27017

ollama run gemma2:2b

ollama run tinyllama:1.1b

streamlit run app.py

# ☁️ Deployment

- Hosted on AWS EC2

- Ollama and MongoDB running via Docker containers

- Streamlit app served on port 8501

# 📹 Demo Video:

[https://youtu.be/ZWDa6QvRVPo](https://www.youtube.com/watch?v=ZWDa6QvRVPo)

# 🎯 Why This Project

This project demonstrates:

1.Practical use of Generative AI & LLMs

2.Chat memory persistence

3.Real deployment experience using Docker + AWS EC2

4.End-to-end AI application development

# 👨‍💻 Author

Ashish Mittal
Generative AI Developer

# ⭐ If you like this project, give it a star!
