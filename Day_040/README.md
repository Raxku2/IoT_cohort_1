# Understanding HTTP Methods & API Testing

When building APIs with Express.js, you use HTTP methods (also known as HTTP verbs) to define the action the client wants to perform. This guide explains the core methods (GET, POST, PUT, PATCH, DELETE), how to route them in Express, and how to test them.

## 1. HTTP Methods & Express Syntax

Here are the five primary HTTP methods used in RESTful APIs:

### GET (Retrieve)
Used to fetch data from the server. It should *only* retrieve data and have no other effect (it is "safe").

```javascript
// Fetch all items
app.get('/api/users', (req, res) => {
  res.json({ message: 'Fetching all users' });
});

// Fetch a single item by ID
app.get('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `Fetching user with ID: ${userId}` });
});
```

### POST (Create)
Used to send data to the server to create a new resource. The data is included in the body of the request.

```javascript
app.post('/api/users', (req, res) => {
  const newUser = req.body; // Requires app.use(express.json())
  res.status(201).json({ 
    message: 'User created successfully', 
    user: newUser 
  });
});
```

### PUT (Replace)
Used to update an *existing* resource. A PUT request replaces the entire resource with the provided data. If a field is missing in the request, it is typically set to null or removed.

```javascript
app.put('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  const completelyUpdatedUser = req.body;
  res.json({ 
    message: `Completely replaced user ${userId}`, 
    data: completelyUpdatedUser 
  });
});
```

### PATCH (Partial Update)
Used to apply partial modifications to a resource. Unlike PUT, you only send the fields you want to change, leaving the rest intact.

```javascript
app.patch('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  const updates = req.body; // e.g., just sending { "email": "new@email.com" }
  res.json({ 
    message: `Partially updated user ${userId}`, 
    updatesApplied: updates 
  });
});
```

### DELETE (Remove)
Used to delete a specified resource.

```javascript
app.delete('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  res.json({ message: `Deleted user ${userId}` });
});
```

---

## 2. API Testing Tools

When building your Express application, you need a way to send these requests (especially POST, PUT, PATCH, DELETE) to your server without building a frontend UI first. This is where API testing tools come in.

### Postman
Postman is one of the most popular graphical GUI tools for API testing. 
* **How it works:** You create a "Workspace", set the URL (e.g., `http://localhost:3000/api/users`), select the HTTP Method from a dropdown, add any necessary JSON to the "Body" tab, and click "Send".
* **Great for:** Saving collections of requests, sharing with teams, and writing automated test scripts.

### Bruno
Bruno is a newer, open-source alternative to Postman. 
* **How it works:** Similar GUI to Postman, but it stores all your API collections locally on your computer as plain text files (using a custom markup language).
* **Great for:** Privacy, version control (you can commit your API tests to Git alongside your code), and lightweight usage.

### cURL
cURL is a command-line tool used to transfer data using various network protocols. It comes pre-installed on most Mac and Linux systems, and modern Windows operating systems.
* **How it works:** You type commands directly into your terminal.
* **Great for:** Quick tests, automated bash scripts, and environments where you don't have a graphical interface.

**cURL Examples:**

*   **GET request:**
    ```bash
    curl http://localhost:3000/api/users
    ```
*   **POST request:**
    ```bash
    curl -X POST http://localhost:3000/api/users \
    -H "Content-Type: application/json" \
    -d '{"name": "John Doe", "email": "john@example.com"}'
    ```
*   **PATCH request:**
    ```bash
    curl -X PATCH http://localhost:3000/api/users/1 \
    -H "Content-Type: application/json" \
    -d '{"name": "John Updated"}'
    ```

---

## 3. Official Documentation Links

To dive deeper into these topics, refer to the official documentation:

*   **Express.js Routing:** [https://expressjs.com/en/guide/routing.html](https://expressjs.com/en/guide/routing.html)
*   **Express.js API Reference:** [https://expressjs.com/en/4x/api.html](https://expressjs.com/en/4x/api.html)
*   **Postman Learning Center:** [https://learning.postman.com/docs/getting-started/introduction/](https://learning.postman.com/docs/getting-started/introduction/)
*   **Bruno Documentation:** [https://docs.usebruno.com/](https://docs.usebruno.com/)
