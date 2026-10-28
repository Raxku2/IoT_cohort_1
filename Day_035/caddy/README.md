# 🌐 The Ultimate Caddy Guide for Developers

Caddy is a modern, ridiculously easy-to-use web server. If you are used to writing massive Nginx or Apache configuration files, Caddy will feel like magic.

**Why Caddy?**

1. **Automatic HTTPS:** It automatically provisions and renews SSL certificates from Let's Encrypt. Zero setup required.
2. **Simple Syntax:** A production-ready config is often less than 5 lines long.
3. **Written in Go:** It's a single static binary. No dependencies to install.

## 🚀 1. Installation

**Mac (Homebrew):**

```bash
brew install caddy
```

**Ubuntu/Debian:**

```bash
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update && sudo apt install caddy
```

**Windows:**
Download the executable from [caddyserver.com](https://caddyserver.com) and add it to your System PATH.

**To run Caddy locally:**
Create a file named `Caddyfile` in your project root, then run:

```bash
caddy run --watch
```

*(The `--watch` flag automatically reloads the server if you edit the Caddyfile).*

---

## 🔄 2. The `reverse_proxy` Deep Dive

The `reverse_proxy` directive is what you use to put Caddy in front of your Node.js, Python, Go, or Java backend. It catches incoming web traffic on port 80/443 and securely forwards it to your app running on a local port (like 3000 or 8000).

### The Basics

Forward all traffic on `example.com` to a local Node.js server running on port 3000.

```caddyfile
example.com {
    reverse_proxy localhost:3000
}
```

### Routing by Path

You can run multiple backends on the same domain by matching the URL path.

```caddyfile
example.com {
    # Send /api/* requests to the Python backend
    reverse_proxy /api/* localhost:8000

    # Send everything else to the Next.js frontend
    reverse_proxy * localhost:3000
}
```

### Modifying Headers

Sometimes your backend needs to know the original user's IP, or you need to hide a header that your backend leaks. You can modify headers as traffic passes through Caddy.

```caddyfile
example.com {
    reverse_proxy localhost:3000 {
        # Add a header to the request going TO your backend
        header_up X-My-Custom-Header "Hello Backend"

        # Remove a header from the response going BACK to the user
        header_down -X-Powered-By
    }
}
```

*Note: Caddy automatically sets headers like `X-Forwarded-For` and `X-Forwarded-Proto` for you. You rarely need to configure these manually.*

### WebSockets

Unlike Nginx, **Caddy supports WebSockets out of the box.** You do not need any special configuration for Socket.io, WS, or other websocket libraries. Just use a standard `reverse_proxy`.

### Load Balancing & Failover

If you scale up and run multiple instances of your app, Caddy can balance the traffic between them.

```caddyfile
example.com {
    reverse_proxy 10.0.0.1:8000 10.0.0.2:8000 10.0.0.3:8000 {
        lb_policy least_conn
        health_uri /health
        health_interval 5s
    }
}
```

*For a full breakdown of load balancing, see [Load Balancing Policies].*

---

## 📁 3. Serving Static Files (React/Vue/HTML)

If you have a compiled frontend (like a React `build/` folder) or just plain HTML/CSS, use `file_server`.

```caddyfile
example.com {
    # Point Caddy to your build directory
    root * /var/www/my-react-app/build
    
    # Enable static file serving
    file_server

    # For SPA (Single Page Applications) routing like React Router:
    # If a file isn't found, serve index.html instead of a 404
    try_files {path} /index.html
}
```

---

## 🛠 4. The "Ultimate Starter" Caddyfile

Here is a master template for a standard student stack: a static React frontend, a Node.js API, and automatic HTTPS. Copy and paste this to get started immediately.

```caddyfile
# 1. Global options block (optional)
{
    email admin@myproject.com # Used for Let's Encrypt SSL recovery
}

# 2. Your main domain
myproject.com {
    
    # -----------------------------------------
    # BACKEND: Route all /api/* requests to Node
    # -----------------------------------------
    handle /api/* {
        # Strip the "/api" prefix before hitting the backend 
        # (so the backend just sees "/users", not "/api/users")
        uri strip_prefix /api
        reverse_proxy localhost:5000
    }

    # -----------------------------------------
    # FRONTEND: Serve React static files
    # -----------------------------------------
    handle {
        root * /path/to/project/frontend/build
        
        # Enable gzip/zstd compression for faster load times
        encode zstd gzip
        
        file_server
        try_files {path} /index.html
    }
}

# 3. Redirect www to non-www
www.myproject.com {
    redir https://myproject.com{uri} permanent
}
```