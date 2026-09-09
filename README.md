# 🚀 FastAPI React Chat: Full-Stack AI Assistant

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

![App Screenshot](docs/screenshot.png)

A powerful, full-stack AI Chat application built to master modern web development technologies. This project seamlessly integrates a high-performance **FastAPI** backend with a dynamic **React** frontend, utilizing **PostgreSQL** for robust data persistence and **OpenAI** for intelligent responses.

Designed with **N-Layer Architecture**, this project serves as a comprehensive example of building scalable, maintainable, and production-ready software systems.

---

## ✨ Features

- **🤖 Intelligent Chat:** Powered by OpenAI's GPT models for natural, context-aware conversations.
- **🧠 Conversation Memory:** Remembers past messages within a session for coherent dialogue.
- **💾 Persistent History:** All chats are saved in a PostgreSQL database using SQLAlchemy ORM.
- **🎨 Modern UI:** A responsive, dark-mode enabled interface built with React, Vite, and custom CSS (Glassmorphism).
- **📱 Mobile Responsive:** Fully optimized for mobile devices with a collapsible sidebar and touch-friendly controls.
- **⚡ High Performance:** Async capabilities of FastAPI ensure lightning-fast responses.
- **🔒 Secure:** JWT-based structure (ready for expansion) and environment variable management.
- **🏗️ N-Layer Architecture:**
    - **API Layer:** Handles HTTP requests and routing.
    - **Service Layer:** Contains business logic.
    - **Data Layer:** Manages database interactions (DAO pattern).
    - **Domain Layer:** Defines core entities and models.

---

## 🛠️ Technology Stack

| Component       | Technology                          |
| :-------------- | :---------------------------------- |
| **Backend**     | Python, FastAPI, Uvicorn, SQLAlchemy |
| **Frontend**    | React, Vite, JavaScript, CSS3       |
| **Database**    | PostgreSQL                          |
| **AI Engine**   | OpenAI API                          |
| **Tools**       | Git, Docker (Optional), ngrok       |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js & npm (for frontend development)
- PostgreSQL installed and running

### One-Click Launch (Recommended)
This project includes a smart startup script `baslat.bat` that handles everything for you:
1.  Sets up the environment.
2.  Starts the generic Uvicorn server.
3.  Launches the application in your browser (`http://localhost:8000`).
4.  (Optional) Starts **ngrok** tunneling if available.

Just double-click **`baslat.bat`** in the root directory!

### Manual Setup
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/azizdeniz890/fastapi-react-chat.git
    cd fastapi-react-chat
    ```

2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Base Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment:**
    Create a `.env` file (or set variables in `baslat.bat`) with:
    ```env
    DATABASE_URL=postgresql://user:password@localhost/dbname
    OPENAI_API_KEY=sk-...
    ```

5.  **Run Application:**
    ```bash
    uvicorn app.main:app --reload
    ```

---

## 📂 Project Structure

```
fastapi-react-chat/
├── app/                  # Backend Application (N-Layer Architecture)
│   ├── api/              # API Layer (Endpoints & Schemas)
│   ├── auth/             # Authentication (JWT & Rate Limiting)
│   ├── config/           # Configuration Settings
│   ├── data/             # Data Access Layer (DAO & Database Connection)
│   ├── domain/           # Domain Entities & Models
│   ├── infra/            # Infrastructure (OpenAI Client)
│   ├── service/          # Business Logic Layer
│   └── main.py           # Application Entry Point
├── frontend/             # React Frontend
│   ├── src/              # Components, Hooks, & Styles
│   └── index.html        # Entry HTML
├── static/               # Compiled Frontend Assets
├── docs/                 # Documentation Images
├── requirements.txt      # Python Dependencies
├── baslat.bat            # One-Click Startup Script
└── README.md             # Project Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> **Note:** This project was built for educational purposes to demonstrate full-stack development skills.
