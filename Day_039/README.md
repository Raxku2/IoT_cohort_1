# Getting Started with Express.js

Express.js is a fast, unopinionated, and minimalist web framework for Node.js. This guide will walk you through setting up an Express project, running it, and understanding the core concepts like routing, requests, and responses.

## 1. Project Initialization

Before installing Express, create a new directory for your project and initialize it.

```bash
mkdir my-express-app
cd my-express-app

# Initialize with npm
npm init -y

# OR Initialize with yarn
yarn init -y

# OR Initialize with bun
bun init -y
```

## 2. Installation

You can install Express using your preferred package manager:

**Using npm:**
```bash
npm install express
```

**Using yarn:**
```bash
yarn add express
```

**Using bun:**
```bash
bun add express
```

## 3. Basic Configuration & Running the App

Create a file named `index.js` (or `app.js`) in your project root and add the following code to set up a basic server:

```javascript
// index.js
const express = require('express');
const app = express();
const PORT = 3000;

// A simple route
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

**To run the application:**
```bash
node index.js
```
*Note: If you are using Bun, you can run it using `bun run index.js`.*

## 4. What is Nodemon?

**Nodemon** is a utility tool that monitors for any changes in your source and automatically restarts your server. It is incredibly helpful during development because you don't have to manually stop and restart the server every time you make a change to your code.

**Installation:**
Install it as a development dependency:
```bash
npm install -D nodemon
# or: yarn add -D nodemon
# or: bun add -d nodemon
```

**Configuration:**
Add a script to your `package.json` file:
```json
"scripts": {
  "start": "node index.js",
  "dev": "nodemon index.js"
}
```

**Running with Nodemon:**
Now, start your server in development mode using:
```bash
npm run dev
# or: yarn dev
# or: bun run dev
```

---

## 5. Routing Configuration

Routing refers to determining how an application responds to a client request to a particular endpoint (URI) and a specific HTTP request method (GET, POST, PUT, DELETE).

```javascript
// GET request
app.get('/users', (req, res) => {
  res.send('Get all users');
});

// POST request
app.post('/users', (req, res) => {
  res.send('Create a new user');
});

// PUT request (Update)
app.put('/users/:id', (req, res) => {
  res.send(`Update user with ID: ${req.params.id}`);
});

// DELETE request
app.delete('/users/:id', (req, res) => {
  res.send(`Delete user with ID: ${req.params.id}`);
});
```

---

## 6. Handling the Request (`req`)

The `req` object represents the HTTP request and has properties for the request query string, parameters, body, HTTP headers, and so on.

### Middleware for Body Parsing
**CRITICAL:** To read JSON data from the request body, you *must* configure Express to parse JSON by adding this built-in middleware at the top of your file (before your routes):

```javascript
// Add this to parse incoming JSON payloads
app.use(express.json()); 

// Add this if you are parsing URL-encoded data (like form submissions)
app.use(express.urlencoded({ extended: true }));
```

### Extracting Data
Here is how you read different parts of the incoming request:

```javascript
app.post('/api/data/:userId', (req, res) => {
  // 1. Reading Headers
  // Headers are usually converted to lowercase in Express
  const myHeader = req.headers['authorization']; 
  const userAgent = req.headers['user-agent'];

  // 2. Reading URL Parameters (Dynamic routing parts)
  // e.g., /api/data/123 -> req.params.userId will be '123'
  const userId = req.params.userId;

  // 3. Reading Query Strings
  // e.g., /api/data/123?search=apple -> req.query.search will be 'apple'
  const searchQuery = req.query.search;

  // 4. Reading the Body
  // Requires app.use(express.json()) to be set up
  const requestBody = req.body; 

  console.log('Body:', requestBody);

  res.send('Data received!');
});
```

---

## 7. Making a Response (`res`)

The `res` object represents the HTTP response that an Express app sends when it gets an HTTP request.

```javascript
app.get('/response-examples', (req, res) => {
  
  // 1. Send plain text or HTML
  // res.send('<h1>Hello World</h1>');

  // 2. Send JSON (Most common for APIs)
  // res.json({ message: "Success", data: [1, 2, 3] });

  // 3. Set a specific Status Code and send JSON
  // res.status(404).json({ error: "User not found" });
  
  // 4. Send a Status Code without a body
  // res.sendStatus(200); // Sends 'OK'
  
  // 5. Redirect the user
  // res.redirect('https://google.com');

  // Example of a complete response:
  res.status(201).json({
    status: 'success',
    message: 'Resource created successfully'
  });
});
```