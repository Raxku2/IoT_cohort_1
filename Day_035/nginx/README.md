# Nginx Load Balancer & Reverse Proxy Configuration Guide

This guide provides a complete, step-by-step walkthrough for configuring Nginx as a high-performance reverse proxy and load balancer. It includes the foundational setup, essential MIME-type configurations to prevent static asset blocking, header management, advanced traffic distribution policies, and performance tuning.

## Prerequisites

*   **1 Load Balancer Server:** A server with Nginx installed (e.g., `192.168.1.100`) that faces the public internet.
*   **2+ Backend Servers:** Servers running your web application or APIs (e.g., `10.0.0.1`, `10.0.0.2`) securely isolated on a private network.
*   **Root/Sudo Access:** Required to modify Nginx configuration files and restart the service.

---

## 1. Core Configuration & Reverse Proxy Basics

By default, Nginx routes traffic using a Round Robin algorithm. When acting as a reverse proxy, Nginx strips the original client's IP address. To prevent this, and to ensure static files (CSS, JS) are not blocked by strict browser MIME type checking, we must configure the `http` block correctly.

Open your main Nginx configuration file:

```bash
sudo nano /etc/nginx/nginx.conf
```

Replace or update the `http` block with the following configuration:

```nginx
http {
    # 1. Essential MIME Type Configuration (Prevents CSS/JS blocking errors)
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # 2. Define the Upstream Backend Servers
    upstream backend_servers {
        server 10.0.0.1;
        server 10.0.0.2;
    }

    # 3. Configure the Load Balancer Listening Server
    server {
        listen 80;
        server_name yourdomain.com; # Replace with your domain or LB IP

        location / {
            # Forward all traffic to the upstream group
            proxy_pass http://backend_servers;
            
            # 4. Essential Header Forwarding
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

## 2. Upstream Routing Methods

You can customize how Nginx distributes incoming traffic by defining a routing algorithm inside your `upstream` block.

| Routing Method | Configuration Directive | Best Use Case |
| :--- | :--- | :--- |
| **Round Robin** | *(Default, none needed)* | Equal distribution across identical, stateless servers. |
| **Least Connections** | `least_conn;` | Apps with long-polling, WebSockets, or variable-length processing times. Routes to the server with the fewest active connections. |
| **IP Hash** | `ip_hash;` | Session persistence (sticky sessions). Ensures a specific client IP always hits the same backend server. |
| **Generic Hash** | `hash $request_uri consistent;` | Caching servers. Routes traffic based on the URL path, ensuring the same resource is always fetched from the same server. |

---

## 3. Traffic Control: Weights & Maintenance Flags

You can append parameters directly to the `server` definitions within an `upstream` block to control traffic distribution, handle maintenance, and manage failures.

*   **Weight (`weight=X`):** Directs a disproportionate amount of traffic to a specific server. A server with `weight=3` receives three times as much traffic as a server with the default weight of 1.
*   **Backup (`backup`):** Marks a server as a failover. Nginx will only route traffic here if all primary servers crash or go offline.
*   **Down (`down`):** Temporarily removes a server from the rotation without deleting it from the configuration file. Ideal for rolling updates and maintenance.
*   **Health Checks (`max_fails=X fail_timeout=Ys`):** Automatically marks a server as unavailable if it fails `X` times within `Y` seconds.

---

## 4. Performance & Optimization

To prevent Nginx from bottlenecking under heavy load or dropping large payloads, tune its proxy buffering and connection settings.

```nginx
http {
    upstream api_backends {
        server 10.0.1.1;
        server 10.0.1.2;
        keepalive 32; # Reduces TCP handshake overhead by keeping idle connections open
    }

    server {
        listen 80;
        
        location /api/ {
            proxy_pass http://api_backends;
            proxy_http_version 1.1;         # Required for keepalive
            proxy_set_header Connection ""; # Clear the "close" connection header

            # Buffering: Prevents slow clients from tying up backend threads
            proxy_buffering on;
            proxy_buffer_size 16k;
            proxy_buffers 8 16k;

            # Timeouts
            proxy_connect_timeout 5s;   # Max time to open connection to backend
            proxy_send_timeout 10s;     # Max time to transmit request to backend
            proxy_read_timeout 20s;     # Max time waiting for backend response
        }
    }
}
```

---

## 5. Advanced Configuration Example

This example combines everything: a core algorithm (`least_conn`), server weights, a backup server, maintenance flags, and keepalive optimizations.

```nginx
http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    upstream production_cluster {
        # Core Algorithm
        least_conn; 
        
        # Connection Optimization
        keepalive 32;
        
        # Primary Servers with Weights & Health Checks
        server 10.0.0.1 weight=3 max_fails=3 fail_timeout=10s; # High-capacity server
        server 10.0.0.2 max_fails=3 fail_timeout=10s;          # Standard server
        
        # State Flags
        server 10.0.0.3 backup;   # Failover server, active only if .1 and .2 fail
        server 10.0.0.4 down;     # Maintenance mode, currently receiving 0 traffic
    }

    server {
        listen 80;
        server_name api.yourdomain.com;

        location / {
            proxy_pass http://production_cluster;
            
            # Connection Headers for Keepalive
            proxy_http_version 1.1;
            proxy_set_header Connection "";
            
            # Security & Information Headers
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```

---

## 6. Testing and Deployment

Whenever you modify `/etc/nginx/nginx.conf`, you must validate the syntax before applying it to prevent downtime.

1. Test the configuration for syntax errors:
   ```bash
   sudo nginx -t
   ```
2. If the test returns `syntax is ok` and `test is successful`, reload the Nginx service gracefully. This applies the changes without dropping active user connections:
   ```bash
   sudo systemctl reload nginx
   ```