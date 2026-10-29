# Advanced FastAPI: CORS, Headers, Validation & Best Practices

As your FastAPI application grows, you need to handle cross-origin requests, validate incoming data, manage HTTP headers, and follow architectural best practices. This guide covers these essential advanced topics.

## 1. CORS (Cross-Origin Resource Sharing)

By default, web browsers enforce the **Same-Origin Policy**, which blocks frontend web applications from making API requests to a different domain, port, or protocol than the one they were served from.

To allow your frontend (e.g., Vue or React on port 5173) to communicate with your backend (FastAPI on port 8000), you must enable CORS using FastAPI's built-in middleware.

**Implementation:**

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow specific origins (Best practice for production)
origins = [
    "https://myfrontend.com",
    "http://localhost:5173",
]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Use ["*"] to allow all origins (good for dev, bad for prod)
    allow_credentials=True, # Allow cookies to be sent with requests
    allow_methods=["GET", "POST", "PUT", "DELETE"], # Or ["*"] for all methods
    allow_headers=["*"], # Allow all headers
)

```

## 2. HTTP Headers

Headers pass additional information back and forth between the client and server.

### Setting Response Headers

In FastAPI, you can set custom headers on your responses by declaring a `Response` parameter in your path operation function and modifying its `headers` dictionary.

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/api/data")
def get_data(response: Response):
    # Set a single header
    response.headers["Cache-Control"] = "no-store"
    
    # Set multiple custom headers
    response.headers["X-Custom-Header"] = "MySuperSecretValue"
    
    # Content-Type is automatically set to application/json when returning a dict
    return {"data": "Secure data"}

```

## 3. Data Validation with Pydantic

Never trust client input. Always validate data before processing it or saving it to a database. While other frameworks require third-party libraries for this, FastAPI relies completely on **Pydantic**, a powerful data validation library native to Python.

By defining a Pydantic `BaseModel`, you get automatic validation, type conversion, and error handling out of the box.

**Installation (if using specific types like EmailStr):**

```bash
pip install "pydantic[email]"

```

**Implementation:**

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

app = FastAPI()

# Define a Pydantic schema for validation
class UserSchema(BaseModel):
    # Field(...) makes it required, with a minimum length of 3
    username: str = Field(..., min_length=3, description="Username must be at least 3 characters")
    # EmailStr automatically validates the string as a proper email format
    email: EmailStr 
    # ge=18 means greater than or equal to 18. Optional makes the field not strictly required.
    age: Optional[int] = Field(None, ge=18, description="Must be at least 18")

@app.post("/api/users")
def create_user(user: UserSchema):
    # If the code reaches this point, the data is already 100% validated by Pydantic.
    # If validation fails, FastAPI automatically returns a 422 Unprocessable Entity error 
    # with detailed JSON explaining exactly which fields failed and why.
    
    return {"message": "User valid!", "data": user.model_dump()}

```

## 4. Various Types of Responses

FastAPI provides multiple response classes to send different types of data to the client depending on what you are trying to achieve:

```python
from fastapi import FastAPI, Response, status
from fastapi.responses import (
    JSONResponse, 
    HTMLResponse, 
    FileResponse, 
    RedirectResponse
)
import os

app = FastAPI()

@app.get("/responses")
def different_responses():
    
    # 1. JSON Data (Standard for APIs)
    # return {"name": "Alice", "role": "Admin"} # FastAPI converts dicts automatically
    # OR explicitly: return JSONResponse(content={"name": "Alice"})

    # 2. HTML or Plain Text
    # return HTMLResponse(content="<h1>Welcome to my App</h1>")

    # 3. Send a File (e.g., an image or PDF to display in browser)
    # file_path = os.path.join(os.getcwd(), "public", "image.png")
    # return FileResponse(path=file_path)

    # 4. Trigger a File Download (Forces browser to save the file)
    # return FileResponse(path="/path/to/report.pdf", filename="Q1-Report.pdf")

    # 5. Redirect the Client to another URL
    # return RedirectResponse(url="https://new-website.com", status_code=301)

    # 6. Render an HTML Template (Requires Jinja2 installed: pip install jinja2)
    # (Setup involves defining a Jinja2Templates instance, omitted here for brevity)
    # return templates.TemplateResponse("index.html", {"request": request, "title": "Home Page"})
    
    # 7. End response without data (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

```

## 5. FastAPI Best Practices

1. **Use Pydantic BaseSettings for Environment Variables:** Instead of just using `python-dotenv`, use Pydantic's `BaseSettings` to validate your environment variables on startup.
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()

```


2. **Centralized Error Handling:** Use FastAPI's `@app.exception_handler()` to catch and format specific exceptions globally.
```python
from fastapi import Request
from fastapi.responses import JSONResponse

class CustomException(Exception):
    pass

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=500,
        content={"error": "Something broke!"},
    )

```


3. **Separation of Concerns:** Don't put all your code in `main.py`.
* Use **APIRouter** to group related routes (e.g., `/users`, `/products`) into separate files, just like Express Routers.
* Example: `router = APIRouter(prefix="/users")`, then `app.include_router(user_router)`.


4. **Use Gzip Compression:** Decrease the size of the response body for large payloads.
```python
from fastapi.middleware.gzip import GZipMiddleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

```


5. **Implement Rate Limiting:** Protect your API from brute-force attacks and DDoS. In the FastAPI ecosystem, the **SlowApi** library (which integrates easily with FastAPI) is commonly used to limit how often a single IP can make requests.