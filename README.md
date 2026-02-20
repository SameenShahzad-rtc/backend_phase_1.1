# Backend Phase 1 🚀  
* FastAPI Training Project*

This repository contains backend development work done during a structured FastAPI training.  
 The goal is to build a production-ready FastAPI app with database integration and proper API design.

---

## 📋 Table of Contents

 
  - [Day 1 – FastAPI Fundamentals](#day-1-fastapi-fundamentals)  
  
### 🗓 Day 1 – FastAPI Fundamentals

**Concepts Covered:**

- **What is FastAPI?**

Fast api is a  modern and fast web framework for building APIs with Python. 
API = Application Programming Interface → It allows two applications to communicate with each other. 
It is based on Python type hints, which makes your code cleaner and reduces bugs. 
----Python is a dynamically typed language → normally, you don’t have to declare the type of a variable.Type hints let you optionally specify the type of variables, function parameters, and return values.They help humans and tools (like editors, linters, and FastAPI) understand your code better, but Python itself does not enforce types at runtime 
Example
age: int = 25

# String type
name: str = "Mubeen"
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 10)
print(result)

-> int means this function returns an integer.

-**ASGI vs WSGI (high-level)**

# WSGI = Web Server Gateway Interface
It’s a standard “bridge” between Python web apps and web servers.Basically: WSGI tells Python how to talk to the web server and vice versa.
WSGI is synchronous:
-Handles one request at a time per thread/process.
-Good for normal web pages where users just request HTML or JSON.
-Not ideal for real-time apps like chat, WebSockets, or live updates.
How it works:

Browser -> Web Server -> WSGI Interface -> Python App -> WSGI -> Web Server -> Browser
 The WSGI interface defines how the server passes requests to Python and how Python sends back responses.

- Installing FastAPI + Uvicorn
- Basic app structure
- HTTP methods (GET, POST, PUT, DELETE)
- Path parameters
- Query parameters
- Request body
- Automatic docs (Swagger)
# What is ASGI?
ASGI = Asynchronous Server Gateway Interface
It’s the modern version of WSGI, designed for both synchronous and asynchronous apps.Supports real-time features like:
-WebSockets (chat apps, live updates)
-Background tasks
Key points about ASGI
-ASGI is asynchronous:
-Can handle many requests at the same time.
-Works with modern web frameworks like FastAPI, Starlette, Django Channels.
How it works:

Browser -> ASGI Server -> ASGI Interface -> Python App -> ASGI -> Server -> Browser

**Mini Project – Simple Task API**

Build endpoints:

- `GET /` → Welcome message  
- `GET /tasks` → Return list of tasks  
- `POST /tasks` → Add a task  
- `GET /tasks/{task_id}` → Get a single task  
- `DELETE /tasks/{task_id}` → Delete a task



---
