# Backend Phase 1 🚀  
* FastAPI Training Project*

This repository contains backend development work done during a structured FastAPI training.  
 The goal is to build a production-ready FastAPI app with database integration and proper API design.

---

## 📋 Table of Contents

 
  - [Day 1 – FastAPI Fundamentals](#day-1-fastapi-fundamentals)  
  - [Day 2 – Pydantic & Validation](#day-2-pydantic-&-validation)  
  - [Day 3 – Database & CRUD](#day-3-database-&-crud)  
  
---

### 🗓 Day 3 – Database + CRUD + Async

**Concepts Covered:**

- What is ORM?
ORM (Object–Relational Mapping) is a technique that allows you to interact with a relational database using programming language objects (like Python classes) instead of writing raw SQL queries.


- DB connection with FastAPI

Two main things:
-sqlalchemy → ORM
ORM (like SQLAlchemy) is a tool that converts your Python objects into SQL queries.
-psycopg2-binary → PostgreSQL driver (connector)
A database driver is like a translator/connector between Python and the actual database (PostgreSQL, MySQL, etc.).
    • Examples for PostgreSQL: psycopg2, asyncpg.
    • Examples for MySQL: mysqlclient, pymysql.

 Install Required Packages 
pip install fastapi uvicorn sqlalchemy psycopg2-binary


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "postgresql://username:password@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Explanation
    • create_engine() → Connects SQLAlchemy to PostgreSQL
    • SessionLocal → Creates database sessions
    • Base → Parent class for all ORM models
Think of Base as foundation of all tables.


**Mini Project – Task API with Database**

Tasks to implement:

- Connect PostgreSQL
- Create `Task` table
- CRUD endpoints using DB and dependency injection


