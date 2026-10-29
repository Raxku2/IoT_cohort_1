# Advanced Express.js: CORS, Headers, Validation & Best Practices

As your Express application grows, you need to handle cross-origin requests, validate incoming data, manage HTTP headers, and follow architectural best practices. This guide covers these essential advanced topics.

## 1. CORS (Cross-Origin Resource Sharing)

By default, web browsers enforce the **Same-Origin Policy**, which blocks frontend web applications from making API requests to a different domain, port, or protocol than the one they were served from. 

To allow your frontend (e.g., React on port 5173) to communicate with your backend (Express on port 3000), you must enable CORS.

**Installation:**
```bash
npm install cors
```

**Implementation:**
```javascript
const express = require('express');
const cors = require('cors');
const app = express();

// 1. Allow all origins (Easiest, but least secure - good for dev)
app.use(cors());

// 2. Allow specific origins (Best practice for production)
const corsOptions = {
  origin: ['https://myfrontend.com', 'http://localhost:5173'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true // Allow cookies to be sent with requests
};

app.use(cors(corsOptions));
```

## 2. HTTP Headers

Headers pass additional information back and forth between the client and server. 

### Setting Response Headers
You can set custom headers on your responses to control caching, specify content types, or add custom metadata.

```javascript
app.get('/api/data', (req, res) => {
  // Set a single header
  res.set('Cache-Control', 'no-store');
  
  // Set multiple headers
  res.set({
    'X-Custom-Header': 'MySuperSecretValue',
    'Content-Type': 'application/json'
  });

  res.json({ data: 'Secure data' });
});
```

*Note: For security headers, it is highly recommended to use the `helmet` middleware (`npm install helmet`), which automatically sets secure HTTP headers to protect your app from common vulnerabilities.*

## 3. Data Validation

Never trust client input. Always validate data before processing it or saving it to a database. While you can write manual `if` statements, using a validation library like **Zod**, **Joi**, or **express-validator** is a best practice.

**Example using Zod (Modern, schema-based validation):**
```bash
npm install zod
```

```javascript
const { z } = require('zod');

// Define a schema
const userSchema = z.object({
  username: z.string().min(3, "Username must be at least 3 characters"),
  email: z.string().email("Invalid email address"),
  age: z.number().min(18, "Must be at least 18").optional()
});

app.post('/api/users', (req, res) => {
  try {
    // Validate request body against the schema
    const validatedData = userSchema.parse(req.body);
    
    // If successful, proceed with validatedData
    res.status(201).json({ message: "User valid!", data: validatedData });
  } catch (error) {
    // If validation fails, return a 400 Bad Request with error details
    res.status(400).json({ errors: error.errors });
  }
});
```

## 4. Various Types of Responses

Express provides multiple ways to send responses to the client depending on what you are trying to achieve:

```javascript
app.get('/responses', (req, res) => {
  
  // 1. JSON Data (Standard for APIs)
  // res.json({ name: 'Alice', role: 'Admin' });

  // 2. HTML or Plain Text
  // res.send('<h1>Welcome to my App</h1>');

  // 3. Send a File (e.g., an image or PDF to display in browser)
  // const path = require('path');
  // res.sendFile(path.join(__dirname, 'public', 'image.png'));

  // 4. Trigger a File Download (Forces browser to save the file)
  // res.download('/path/to/report.pdf', 'Q1-Report.pdf');

  // 5. Redirect the Client to another URL
  // res.redirect(301, 'https://new-website.com');

  // 6. Render an HTML Template (Requires an engine like EJS or Pug)
  // res.render('index', { title: 'Home Page' });
  
  // 7. End response without data
  // res.status(204).end(); 
});
```

## 5. Express.js Best Practices

1. **Use Environment Variables:** Never hardcode secrets (API keys, database URIs, ports). Use the `dotenv` package.
   ```javascript
   require('dotenv').config();
   const PORT = process.env.PORT || 3000;
   ```
2. **Centralized Error Handling:** Instead of handling errors in every route, use an Express error-handling middleware function at the very bottom of your file.
   ```javascript
   app.use((err, req, res, next) => {
     console.error(err.stack);
     res.status(500).json({ error: 'Something broke!' });
   });
   ```
3. **Separation of Concerns:** Don't put all your code in `index.js`. 
   - Use **Routers** (`express.Router()`) to group related routes (e.g., `/users`, `/products`).
   - Use **Controllers** (separate functions) to handle the business logic of those routes.
4. **Use Gzip Compression:** Decrease the size of the response body and increase web app speed.
   ```javascript
   const compression = require('compression');
   app.use(compression());
   ```
5. **Implement Rate Limiting:** Protect your API from brute-force attacks and DDoS by limiting how often a single IP can make requests (`npm install express-rate-limit`).