# Understanding HTTP Methods & API Testing

When building APIs with FastAPI, you use HTTP methods (also known as HTTP verbs) to define the action the client wants to perform. This guide explains the core methods (GET, POST, PUT, PATCH, DELETE), how to route them in FastAPI using decorators, and how to test them.

## 1. HTTP Methods & FastAPI Syntax

Here are the five primary HTTP methods used in RESTful APIs. In FastAPI, request bodies are automatically parsed and validated using Pydantic models.

### GET (Retrieve)

Used to fetch data from the server. It should *only* retrieve data and have no other effect (it is "safe").

```python
from fastapi import FastAPI

app = FastAPI()

# Fetch all items
@app.get("/api/users")
def get_users():
    return {"message": "Fetching all users"}

# Fetch a single item by ID
@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return {"message": f"Fetching user with ID: {user_id}"}

```

### POST (Create)

Used to send data to the server to create a new resource. The data is automatically extracted from the request body and validated against a Pydantic model.

```python
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.post("/api/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {
        "message": "User created successfully", 
        "user": user
    }

```

### PUT (Replace)

Used to update an *existing* resource. A PUT request replaces the entire resource with the provided data.

```python
@app.put("/api/users/{user_id}")
def replace_user(user_id: int, completely_updated_user: User):
    return {
        "message": f"Completely replaced user {user_id}", 
        "data": completely_updated_user
    }

```

### PATCH (Partial Update)

Used to apply partial modifications to a resource. Unlike PUT, you only send the fields you want to change. In FastAPI, you typically handle this by making the Pydantic model fields optional.

```python
from typing import Optional

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

@app.patch("/api/users/{user_id}")
def update_user(user_id: int, updates: UserUpdate):
    # .model_dump(exclude_unset=True) ensures we only process fields the client actually sent
    applied_updates = updates.model_dump(exclude_unset=True)
    return {
        "message": f"Partially updated user {user_id}", 
        "updatesApplied": applied_updates
    }

```

### DELETE (Remove)

Used to delete a specified resource.

```python
@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"Deleted user {user_id}"}

```

---

## 2. API Testing Tools

When building your application, you need a way to send these requests to your server. While standard tools work perfectly, FastAPI provides an incredible built-in advantage out of the box.

### FastAPI Interactive Docs (Swagger UI)

Unlike most frameworks, FastAPI automatically generates interactive documentation for your API based on your Python type hints.

* **How it works:** Simply run your server and navigate to `http://localhost:8000/docs` in your browser. You will see a graphical interface where you can click "Try it out", fill in parameters or JSON bodies, and hit "Execute" to test your API directly.
* **Great for:** Immediate testing without installing any third-party tools, and providing living documentation to frontend developers.

### Postman

Postman is one of the most popular graphical GUI tools for API testing.

* **How it works:** You create a "Workspace", set the URL (e.g., `http://localhost:8000/api/users`), select the HTTP Method from a dropdown, add any necessary JSON to the "Body" tab, and click "Send".
* **Great for:** Saving collections of requests, sharing with teams, and writing automated test scripts.

### Bruno

Bruno is a newer, open-source alternative to Postman.

* **How it works:** Similar GUI to Postman, but it stores all your API collections locally on your computer as plain text files (using a custom markup language).
* **Great for:** Privacy, version control (you can commit your API tests to Git alongside your code), and lightweight usage.

### cURL

cURL is a command-line tool used to transfer data using various network protocols. It comes pre-installed on most Mac and Linux systems, and modern Windows operating systems.

* **How it works:** You type commands directly into your terminal.
* **Great for:** Quick tests, automated bash scripts, and environments where you don't have a graphical interface.

**cURL Examples (Assuming Uvicorn running on port 8000):**

* **GET request:**

```bash
curl http://localhost:8000/api/users

```

* **POST request:**

```bash
curl -X POST http://localhost:8000/api/users \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john@example.com"}'

```

* **PATCH request:**

```bash
curl -X PATCH http://localhost:8000/api/users/1 \
-H "Content-Type: application/json" \
-d '{"name": "John Updated"}'

```

---

## 3. Official Documentation Links

To dive deeper into these topics, refer to the official documentation:

* **FastAPI Tutorial - First Steps:** [https://fastapi.tiangolo.com/tutorial/first-steps/](https://fastapi.tiangolo.com/tutorial/first-steps/)
* **FastAPI Path Parameters:** [https://fastapi.tiangolo.com/tutorial/path-params/](https://fastapi.tiangolo.com/tutorial/path-params/)
* **FastAPI Body (Pydantic Models):** [https://fastapi.tiangolo.com/tutorial/body/](https://fastapi.tiangolo.com/tutorial/body/)
* **Postman Learning Center:** [https://learning.postman.com/docs/getting-started/introduction/](https://learning.postman.com/docs/getting-started/introduction/)
* **Bruno Documentation:** [https://docs.usebruno.com/](https://docs.usebruno.com/)