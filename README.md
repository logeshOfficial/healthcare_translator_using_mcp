## 🏥 Healthcare Translator using MCP (Model Context Protocol)

A healthcare-focused language translation system built using Model Context Protocol (MCP), designed to safely translate patient–doctor conversations while preserving medical accuracy and context.

This project demonstrates how MCP can be used to build context-aware, modular AI services suitable for real-world healthcare applications.

### 🚀 Project Overview

In healthcare, simple word-by-word translation is dangerous — medical context matters.

This project uses MCP (Model Context Protocol) to:

* Maintain structured medical context

* Translate healthcare conversations accurately

* Enable modular AI communication between services

* Support both stdio-based MCP and HTTP-based MCP servers

### 🧠 What is MCP (Model Context Protocol)?

MCP is a protocol that allows AI models and tools to:

* Share structured context

* Communicate through defined interfaces

* Remain modular, reusable, and scalable

Why MCP for Healthcare?

* Medical data needs context preservation

* Clear separation of responsibilities (translation, extraction, response)

* Easy integration with multiple clients (CLI, HTTP, agents)

### 📁 Project Structure
healthcare_translator_using_MCP/
│── app.py                 # Client application
│── mcp_server.py          # MCP server (stdio-based)
│── mcp_server_http.py     # MCP server (HTTP-based)
│── ai_utils.py            # AI helper & prompt utilities
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
│── .gitignore             # Ignored files
│── .env.example           # Environment variable template
│── venv/                  # Virtual environment (ignored)
│── .env                   # Secrets (ignored)


### 🔧 Features
✅ Context-aware medical translation
✅ MCP-compliant server architecture
✅ Supports multiple languages
✅ HTTP-ready for production usage
✅ Secure handling of environment variables
✅ Clean, modular, interview-friendly design

# ⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/healthcare_translator_using_MCP.git
cd healthcare_translator_using_MCP

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Environment Variables
OPENAI_API_KEY=your_api_key_here
TARGET_LANGUAGE=ta

▶️ Running the Project
Option 1: MCP (stdio-based)
python mcp_server.py

Option 2: MCP (HTTP-based)
python mcp_server_http.py

Run Client
python app.py

# 🩺 Example Use Case
Input (English): "I have severe pain on the left side of my head and dizziness."
Output (Tamil): "எனக்கு இடது பக்கத் தலையில் கடுமையான வலி மற்றும் தலைசுற்றல் உள்ளது."

✔ Medical meaning preserved
✔ Context maintained
✔ Safe for healthcare communication

# 🔐 Security Best Practices

1. .env files are excluded using .gitignore

2. API keys are never hardcoded

3. .env.example provided for reference

4. Virtual environments are ignored

# 🛠️ Tech Stack

1. Python
2. Model Context Protocol (MCP)
3. OpenAI / LLMs
4. HTTP APIs
5. dotenv
6. Virtual Environments