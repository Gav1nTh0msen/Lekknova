# Lekknova

> A full-stack, cross-platform food and nutrition tracking application designed to log, standardize, and analyze daily dietary intake.

> **Note on Branch Strategy:** Active development occurs on feature and development branches. The `main` branch contains verified production releases. Please switch to the `dev` branch to view current progress and active codebase updates.

---

## Overview

Lekknova is a full-stack mobile application built to streamline daily nutrition management. It features asynchronous REST API endpoints, automatic unit conversions, and real-time macronutrient processing. Currently in development, and I hope to push it early-mid 2027.

---

## Tech Stack

| Domain | Technologies | Status |
| :--- | :--- | :--- |
| **Languages** | Python, TypeScript, SQL | Active |
| **Backend** | FastAPI, Uvicorn, Asynchronous REST APIs | In Progress |
| **Database & ORM** | PostgreSQL, SQLAlchemy, Alembic | In Progress |
| **Frontend** | React Native (Expo), TypeScript | In Progress |
| **Tooling & Version Control** | Git, GitHub, Virtualenv | Active |

---
## System Architecture & Data Flow

* **React Native / Expo Client (TypeScript)** *(In Progress)*
  * └─ *HTTP / JSON (Asynchronous REST API)* ─► **FastAPI Backend** *(In Progress)*
    * └─ *SQLAlchemy ORM* ─► **PostgreSQL Database** *(In Progress)*



## Environment (In Progress)
#### Configuration
> Note that these are temporary, put no stock into these actually working. Please see the dev branch read me for further details.

Copy .env.example to .env in the backend directory and configure the environment parameters:

BashDATABASE_URL=postgresql://user:password@localhost:5432/lekknova_db

SECRET_KEY=your_jwt_secret_key_here

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

## Local Setup & Installation (In Progress)
>Note that these are temporary for now. Put no stock into these commands.
### Prerequisites
Python 3.10+Node.js (v18+)PostgreSQL1. 
#### Backend Setup
Clone the repository

git clone https://github.com/Gav1nTh0msen/Lekknova.git

cd Lekknova/backend

### Set up virtual environment

python3 -m venv venv

source venv/bin/activate  
##### On Windows: venv\Scripts\activate

## Install dependencies (In Progress)

pip install -r requirements.txt

## Run database migrations (In Progress)

alembic upgrade head

## Start local FastAPI server (In Progress)

uvicorn main:app --reload

2\. Frontend SetupBashcd ../frontend

## Install dependencies (In Progress)

npm install

## Start Expo dev server (In Progress)

npx expo start

Testing & Quality AssuranceStatus: Planned --- Test suites will be integrated alongside API route implementation.Bash# Run backend test suite

pytest

## Run type check (In Progress)
mypy .

# License
> Currently not lisensed

This project **will eventually** licensed under the MIT License.
