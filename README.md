# Lekknova

> A full-stack, cross-platform food and nutrition tracking application designed to log, standardize, and analyze daily dietary intake.

> **Note on Branch Strategy:** Active development occurs on feature and development branches. The `main` branch contains verified production releases. Please switch to the `dev` branch to view current progress and active codebase updates.

---

## Overview

>Lekknova is designed to streamline daily nutrition tracking with high performance and low friction. It features async REST API endpoints, automatic unit conversions, and real-time macronutrient calculations. 
>
>The project is actively under development, targeting a initial release in early-to-mid 2027.

---

## Tech Stack

| Domain | Technologies | Status |
| :--- | :--- | :--- |
| **Languages** | Python 3.10+, TypeScript, SQL | Active |
| **Backend Framework** | FastAPI, Uvicorn, Pydantic v2 | In Progress |
| **Database & ORM** | PostgreSQL, AsyncPG, SQLAlchemy 2.0 (Async), Alembic | In Progress |
| **Security & Auth** | Argon2id (`pwdlib`), PyJWT, OAuth2 Bearer Tokens | In Progress |
| **Frontend** | React Native (Expo), TypeScript | Planned |
| **DevOps & Tooling** | Git, GitHub, Python Virtualenv | Active |

---
## System Architecture
```
┌──────────────────────────────┐
│  React Native / Expo Client  │
│         (TypeScript)         │
└──────────────┬───────────────┘
               │ HTTP / JSON (OAuth2 + JWT)
               ▼
┌──────────────────────────────┐
│       FastAPI Backend        │
│       (Async REST API)       │
└──────────────┬───────────────┘
               │ SQLAlchemy 2.0 (AsyncPG)
               ▼
┌──────────────────────────────┐
│     PostgreSQL Database      │
│     (Persistent Storage)     │
└──────────────────────────────┘
```

---
## Getting Started

### Prerequisites
> Python 3.10+
>
> PostgreSQL instance
>
> Node.js (v18+) 

### Backend Setup
#### 1. Clone This Repository
```
git clone [https://github.com/Gav1nTh0msen/Lekknova.git](https://github.com/Gav1nTh0msen/Lekknova.git)
cd Lekknova
```

#### 2. Configure Environment Variables:
```
# Copy the example environment file and update credentials
cp .env.example .env
```

#### 3. Set up Virtual Environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 4. Install Dependencies:
```
# Remember to install the proper requirements in the back and front end!
pip install -r requirements.txt
```

#### 5. Run Database Migrations:
```
alembic upgrade head
```

#### 6. Start Local Development Server:
```
uvicorn app.main:app --reload
```

---
## Testing
> Status: Planned — Test suites will be integrated alongside API implementation.
```
# Run backend test suite
pytest

# Run static type checking
mypy .
```

---
# License

This project is currently unlicensed. It will eventually be released under the MIT License.
