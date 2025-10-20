# 🧩 PostFlow – Secure Online Posting Backend

A backend API for managing user posts with **authentication, authorization**, and complete **CRUD operations**, built using **FastAPI**, **SQLAlchemy ORM**, **PostgreSQL**, and **Alembic**.  
This project demonstrates how to design scalable, secure, and production-ready backend systems.

---

## 🚀 Features

- 🔐 **User Authentication & Authorization** – Secure login and registration using JWT tokens.  
- 📝 **Post Management** – Create, read, update, and delete posts via RESTful APIs.  
- 🧱 **Database Integration** – PostgreSQL handled through SQLAlchemy ORM.  
- 🔄 **Migrations** – Smooth database schema updates using Alembic.  
- ⚙️ **Environment-based Configuration** – Supports .env for database and secret management.  
- 🧪 **Modular Code Structure** – Organized routers, models, and schemas for easy scalability.

---

## 🧰 Tech Stack

| Category | Technologies |
|-----------|---------------|
| Language | Python |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Authentication | JWT |
| Tools | VS Code, Postman |

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Deekshi082/PostFlow.git
   cd PostFlow


Create a virtual environment

python -m venv venv
source venv/bin/activate    # for macOS/Linux
venv\Scripts\activate       # for Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables
Create a .env file (refer .env.example) and add:

DATABASE_URL=postgresql://username:password@localhost:5432/postflow_db
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


Run migrations

alembic upgrade head


Start the FastAPI server

uvicorn app.main:app --reload


Access API Docs

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


🧪 Example .env.example
DATABASE_URL=postgresql://postgres:password@localhost:5432/postflow
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30


👨‍💻 Author

Deekshith S
