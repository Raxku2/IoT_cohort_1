# Getting Started with FastAPI

FastAPI is a modern, fast (high-performance), and minimalist web framework for building APIs with Python based on standard Python type hints. This guide will walk you through setting up a FastAPI project, running it, and understanding the core concepts like routing, requests, and responses.

## 1. Project Initialization

Before installing FastAPI, create a new directory for your project and initialize a Python virtual environment to isolate your dependencies.

```bash
mkdir my-fastapi-app
cd my-fastapi-app

# Initialize a virtual environment
python -m venv venv

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate

# OR Activate the virtual environment (Windows)
venv\Scripts\activate

```

## 2. Installation

You can install FastAPI and an ASGI server (Uvicorn) using your preferred package manager:

**Using pip:**

```bash
pip install fastapi "uvicorn[standard]"

```

**Using poetry:**

```bash
poetry add fastapi uvicorn

```

**Using uv:**

```bash
uv pip install fastapi uvicorn

```

## 3. Basic Configuration & Running the App

Create a file named `main.py` in your project root and add the following code to set up a basic server:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

# A simple route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

```

**To run the application:**

```bash
uvicorn main:app

```

*Note: `main` refers to the file `main.py`, and `app` refers to the `FastAPI` instance created inside it.*

## 4. What is Uvicorn's `--reload`?

Similar to Nodemon in the Node.js ecosystem, **Uvicorn's `--reload` flag** is a utility feature that monitors for any changes in your source code and automatically restarts your server. It is incredibly helpful during development because you don't have to manually stop and restart the server every time you make a change to your code.

**Running with Auto-Reload:**
Start your server in development mode using:

```bash
uvicorn main:app --reload

```

---

## 5. Routing Configuration

Routing refers to determining how an application responds to a client request to a particular endpoint (URI) and a specific HTTP request method (GET, POST, PUT, DELETE). In FastAPI, this is handled using Python decorators.

```python
from fastapi import FastAPI

app = FastAPI()

# GET request
@app.get("/users")
def get_users():
    return "Get all users"

# POST request
@app.post("/users")
def create_user():
    return "Create a new user"

# PUT request (Update)
@app.put("/users/{id}")
def update_user(id: int):
    return f"Update user with ID: {id}"

# DELETE request
@app.delete("/users/{id}")
def delete_user(id: int):
    return f"Delete user with ID: {id}"

```

---

## 6. Handling the Request

In FastAPI, you don't typically extract data from a single `req` object. Instead, FastAPI leverages standard Python type hints to automatically extract, validate, and document the request parameters.

### Middleware for Body Parsing

**CRITICAL:** Unlike Express.js, you do *not* need to configure middleware to parse JSON payloads. FastAPI automatically reads, parses, and validates JSON bodies out of the box using Pydantic models.

### Extracting Data

Here is how you read different parts of the incoming request:

```python
from fastapi import FastAPI, Header, Path, Query, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model for the request body
class UserPayload(BaseModel):
    name: str
    age: int

@app.post("/api/data/{user_id}")
def receive_data(
    # 2. Reading URL Parameters (Dynamic routing parts)
    # e.g., /api/data/123 -> user_id will be 123 (and strictly cast as an int)
    user_id: int = Path(...),

    # 3. Reading Query Strings
    # e.g., /api/data/123?search=apple -> search will be 'apple'
    search: Optional[str] = Query(None),

    # 1. Reading Headers
    # Headers are automatically converted from hyphens to underscores (e.g., user-agent -> user_agent)
    authorization: Optional[str] = Header(None),
    user_agent: Optional[str] = Header(None),

    # 4. Reading the Body
    # Requires no middleware. Automatically parsed and validated against the UserPayload model.
    request_body: UserPayload = Body(...)
):
    print("Body:", request_body)

    return {"message": "Data received!"}

```

---

## 7. Making a Response

In FastAPI, you simply return a Python `dict`, `list`, or Pydantic model, and it is automatically converted into a JSON response. For custom responses (HTML, specific status codes, redirects), FastAPI provides specialized response classes.

```python
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse, Response

app = FastAPI()

# Note: You can set a default status code in the route decorator
@app.get("/response-examples", status_code=status.HTTP_201_CREATED)
def response_examples():
    
    # 1. Send HTML
    # return HTMLResponse(content="<h1>Hello World</h1>")

    # 2. Send JSON (Most common for APIs)
    # By simply returning a dictionary, FastAPI automatically converts it to JSON
    # return {"message": "Success", "data": [1, 2, 3]}

    # 3. Set a specific Status Code dynamically and send JSON
    # return JSONResponse(status_code=404, content={"error": "User not found"})
    
    # 4. Send a Status Code without a body
    # return Response(status_code=status.HTTP_200_OK)
    
    # 5. Redirect the user
    # return RedirectResponse(url="https://google.com")

    # Example of a complete response (status code 201 is handled by the decorator above):
    return {
        "status": "success",
        "message": "Resource created successfully"
    }

```