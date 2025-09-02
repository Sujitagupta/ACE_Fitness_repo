# ACEest Fitness & Gym - DevOps Assignment

This repository contains the implementation for **Assignment 1** of the course *Introduction to DevOps (CSIZG514/SEZG514)*.  
The project demonstrates **Flask app development, unit testing with Pytest, containerization with Docker, and CI/CD automation using GitHub Actions**.

---

## Project Overview
ACEest Fitness & Gym is a lightweight Flask web application that allows:
- Logging workouts against a **Gym ID**
- Viewing workouts by entering a **Gym ID**

The app showcases the **DevOps workflow**:
1. Application Development
2. Version Control with Git & GitHub
3. Unit Testing (Pytest)
4. Automated Testing (via GitHub Actions)
5. Containerization (Docker)
6. CI/CD Pipeline with GitHub Actions

---

## Repository Structure
```
.
├── app.py                    # Flask application
├── test_app.py               # Unit tests with pytest
├── requirements.txt          # Python dependencies
├── Dockerfile                # Dockerfile for containerization
├── templates/
│   ├── index.html            # Home page
│   └── view_workouts.html    # Workouts page
└── .github/
    └── workflows/
        └── ci.yml            # GitHub Actions CI/CD workflow
```

---

## Setup & Run Locally

### Clone the Repository
```bash
git clone https://github.com/Sujitagupta/ACE_Fitness_repo.git
cd ACE_Fitness_repo
```

### Create Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

### Run the Flask App
```bash
python3 app.py
```

App will be available at: **http://127.0.0.1:5000**

---

## Running Tests

### Run all tests with pytest
```bash
pytest
```

---

## Docker Support

### Build Docker Image
```bash
docker build -t aceest_fitness .
```

### Run Docker Container
```bash
docker run -p 5000:5000 aceest_fitness
```

App will be available at: **http://localhost:5000**

---

## CI/CD with GitHub Actions

The workflow file **`.github/workflows/ci.yml`** ensures:
- Automatic build on every `git push`
- Installation of dependencies
- Execution of **pytest** unit tests
- Validation of Docker build

You can view the CI/CD runs under the **Actions** tab of this repository.

---
