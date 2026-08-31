# FastAPI CI/CD Starter 🚀

This repository serves as a starting point for understanding and implementing Continuous Integration and Continuous Deployment (CI/CD) with GitHub Actions for a FastAPI application. The application is pre-dockerized and includes PostgreSQL database integration.

---

## Features
- 🐍 **FastAPI**: A modern Python web framework for building APIs.
- 🐳 **Dockerized Application**: Containerized setup for easy development and deployment.
- 🗃️ **PostgreSQL Integration**: Example database configuration.
- 📦 **CI/CD Ready**: Includes a GitHub Actions workflow for building, testing, and deploying.

---

## Tutorial

This project is part of a detailed [**CI/CD with GitHub Actions and FastAPI**](https://agathabahati.hashnode.dev/preview/65a98cf90f58063884316aad#heading-objectives) tutorial. Check out the article to follow along and understand how to set up your CI/CD pipeline from scratch.

---

## Prerequisites
Before you begin, ensure you have the following installed:
1. **Docker and Docker Compose**
2. **Python 3.10+**
3. **Git**

---

## Getting Started

### 1. Clone the Repository
with https:
```bash
git clone https://github.com/MoigeMatino/fastapi-ci-cd-starter.git
cd fastapi-ci-cd-starter
```
with ssh:
```bash
git clone git@github.com:MoigeMatino/fastapi-ci-cd-starter.git
cd fastapi-ci-cd-starter
```
### 2. Set Up the .env File
Create a `.env` file in the root directory and provide your database credentials. Example:
```plaintext
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_database
DB_HOST=db
DB_PORT=5432
```

### 3. Start the Application

Run the following command to start the FastAPI application and the PostgreSQL database:
```bash
docker-compose up --build
```

### 4. Access the Application

Open your browser and navigate to: http://localhost:8000. Explore the auto-generated API docs at:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure
```plaintext
fastapi-ci-cd-starter/
├── app/
│   ├── __init__.py         # Entry point for the FastAPI app
│   ├── models.py           # SQLModel definitions
│   ├── database.py         # Database connection
│   ├── routes/
|   |   |--- __init__.py  
│   │   └── items.py        # Example API routes
├── tests/
|   |   |--- __init__.py
│   |   └── test_items.py   # Example test for the API
├── Dockerfile              # Dockerfile for the FastAPI app
├── .gitignore              # gitignore file
├── .dockerignore           # Dockerignore file
├── compose.yaml            # Docker Compose configuration
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment file
└── README.md               # Project documentation

```
## Running Tests
To run the test suite:
```bash
docker-compose exec app pytest tests
```
# fastapi-ci-cd
