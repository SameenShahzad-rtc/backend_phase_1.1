
# Backend Phase 1.1 🚀  
* FastAPI Training Project*

This repository contains backend development work done during a structured FastAPI training.  
 The goal is to build a production-ready FastAPI app with database integration and proper API design.

---

## 📋 Table of Contents
 
  - [Day 2 – Pydantic & Validation](#day-2-pydantic-&-validation)  

---

### 🗓 Day 2 – Pydantic + Validation + Structure

**Concepts Covered:**

- # Pydantic models
Purpose: Define data structure + validation for requests and responses.
Pydantic ensures the data matches the expected type and automatically raises errors for invalid input.

- # Request validation

FastAPI automatically validates incoming request data using Pydantic models. 
Wrong type → automatic error
Missing required field → automatic error

- # Response models
what you api returns
sometime we donot want to return all data like 

- # Status codes
FastAPI allows you to set correct HTTP status codes. 
200 → OK
201 → Created
404 → Not Found
400 → Bad Request

from fastapi import status

- # HTTPException: used to raise errors manually.
- # Modular structure
    • Keeps code organized
    • Makes it scalable and maintainable
    • Each file has a single responsibility

- # APIRouter
Used to separate routes into modules. 
from fastapi import APIRouter

- # Environment variables:
Purpose: create a separate file to store secrets/configuration safely (DB URLs, API keys, secret keys). 


**Mini Project – Refactor Task API**

Include:

- Pydantic models: `TaskCreate`, `TaskResponse`
- Validation: title must be 3+ characters
- Proper status codes
- Routes in APIRouter

---
