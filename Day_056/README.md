## ⚡ Valkey: The Complete Industry-Grade Guide

### 1. Installation Across Package Managers

Valkey maintains compatibility with existing Redis environments, allowing you to install the core server alongside compatibility symlinks for legacy toolchains.

**Debian / Ubuntu / Mint (APT)**

```bash
sudo apt update
sudo apt install valkey valkey-redis-compat

```

*(Reference: Valkey APT Installation)*

**Arch Linux / Manjaro (Pacman, Paru, Yay)**

```bash
# Using standard pacman
sudo pacman -Sy valkey

# Using AUR helpers for bleeding edge
paru -S valkey
yay -S valkey

```

*(Reference: Valkey Pacman Installation)*

**Fedora / RHEL (DNF)**

```bash
sudo dnf install valkey valkey-compat-redis valkey-doc

```

*(Reference: Valkey DNF Installation)*

**Void Linux (XBPS)**

```bash
sudo xbps-install -Su valkey

```

*(Reference: Valkey XBPS Installation)*

---

### 2. Service Management (Systemd, Runit, Dinit)

A production installation requires a rock-solid daemon manager setup.

**Systemd (Debian, Fedora, Arch)**
Create or edit `/etc/systemd/system/valkey.service` to ensure execution with proper constraints:

```ini
[Unit]
Description=Valkey Data Structure Store
After=network.target network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/valkey-server /etc/valkey/valkey.conf --supervised systemd
ExecStop=/usr/bin/valkey-cli shutdown
Type=notify
User=valkey
Group=valkey
LimitNOFILE=10032
NoNewPrivileges=yes
PrivateTmp=yes

[Install]
WantedBy=multi-user.target

```

*Enable and start:* `sudo systemctl daemon-reload && sudo systemctl enable --now valkey`

**Runit (Void Linux, Artix)**
Create the service directory and run script at `/etc/sv/valkey/run`:

```bash
#!/bin/sh
exec 2>&1
exec chpst -u valkey:valkey /usr/bin/valkey-server /etc/valkey/valkey.conf

```

*Enable and start:* `sudo chmod +x /etc/sv/valkey/run && sudo ln -s /etc/sv/valkey /var/service/`

**Dinit (Artix Dinit, Chimera Linux)**
Create `/etc/dinit.d/valkey`:

```ini
type = process
command = /usr/bin/valkey-server /etc/valkey/valkey.conf
logfile = /var/log/valkey.log
run-as = valkey
smooth-recovery = true
waits-for = loopback

```

*Enable and start:* `sudo dinitctl enable valkey && sudo dinitctl start valkey`

---

### 3. Driver Installation

Valkey is a drop-in replacement for Redis 7.2. You can use native Valkey drivers or existing Redis drivers interchangeably.

**Node.js / JavaScript**
Install the `iovalkey` client (based on `ioredis`) or the official `@valkey/valkey-glide` module.

* **npm:** `npm install iovalkey express`
* **yarn:** `yarn add iovalkey express`
* **bun:** `bun add iovalkey express`

**Python**
Install the `valkey` module (forked from `redis-py`) and compile with `libvalkey` for faster C-based parsing.

* **pip:** `pip install "valkey[libvalkey]" fastapi uvicorn`
* **uv:** `uv pip install "valkey[libvalkey]" fastapi uvicorn`

---

### 4. Code Snippets & CRUD Examples

**Node.js (Express.js + iovalkey)**
A robust CRUD implementation handling asynchronous connection states.

```javascript
const express = require('express');
const Redis = require('iovalkey');

const app = express();
app.use(express.json());

// Initialize Valkey Client
const valkey = new Redis({
  host: '127.0.0.1',
  port: 6379,
  maxRetriesPerRequest: 3
});

// CREATE & UPDATE
app.post('/item/:id', async (req, res) => {
  const { id } = req.params;
  const { value } = req.body;
  await valkey.set(id, JSON.stringify(value), 'EX', 3600); // 1hr TTL
  res.send({ status: 'saved', id });
});

// READ
app.get('/item/:id', async (req, res) => {
  const data = await valkey.get(req.params.id);
  if (!data) return res.status(404).send({ error: 'Not found' });
  res.send(JSON.parse(data));
});

// DELETE
app.delete('/item/:id', async (req, res) => {
  await valkey.del(req.params.id);
  res.send({ status: 'deleted' });
});

app.listen(3000, () => console.log('Express + Valkey running on :3000'));

```

**Python (FastAPI + valkey-py)**
An async CRUD implementation utilizing FastAPI.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import valkey.asyncio as valkey
import json

app = FastAPI()
client = valkey.Valkey(host='127.0.0.1', port=6379, decode_responses=True)

class Item(BaseModel):
    value: dict

# CREATE & UPDATE
@app.post("/item/{item_id}")
async def create_item(item_id: str, item: Item):
    # Set with 1-hour expiration
    await client.set(item_id, json.dumps(item.value), ex=3600)
    return {"status": "saved", "id": item_id}

# READ
@app.get("/item/{item_id}")
async def read_item(item_id: str):
    data = await client.get(item_id)
    if not data:
        raise HTTPException(status_code=404, detail="Not found")
    return json.loads(data)

# DELETE
@app.delete("/item/{item_id}")
async def delete_item(item_id: str):
    await client.delete(item_id)
    return {"status": "deleted"}

```

---

### 5. Industry-Grade Configuration & Optimization

To move beyond the default installation, modify `/etc/valkey/valkey.conf` and apply OS-level tuning for high-throughput environments.

**1. Memory Optimization & Cleanup**

* **Max Memory:** Set a hard memory limit to prevent out-of-memory kernel panics.
`maxmemory 4gb`
* **Eviction Policy:** For caching workloads, instruct Valkey to drop the least recently used keys when memory fills.
`maxmemory-policy allkeys-lru`
* **Lazy Freeing:** Prevent memory cleanup from blocking the main thread during large deletions.
`lazyfree-lazy-eviction yes`
`lazyfree-lazy-expire yes`

**2. I/O & Thread Tuning**
Valkey features a redesigned I/O threading model. Enable I/O threads to offload network socket reads/writes so the main thread strictly executes commands.

* `io-threads 4` (Optimize based on your CPU core count minus 1 or 2)
* `io-threads-do-reads yes`

**3. OS-Level Tuning (Crucial for production)**
Add these parameters to `/etc/sysctl.conf` to prevent latency spikes and background save failures:

* **Overcommit Memory:** Allows the OS to fork memory for background data saves (RDB/AOF) without throwing `ENOMEM` errors.
`vm.overcommit_memory = 1`
* **TCP Backlog:** Increase connection queue size to handle traffic spikes.
`net.core.somaxconn = 65535`
* **Disable Transparent Huge Pages (THP):** THP causes massive latency spikes during data forks. Run this command on boot:
`echo never > /sys/kernel/mm/transparent_hugepage/enabled`

**4. Scaling & High Availability**

* **Replication:** Add `replicaof <master-ip> 6379` to follower nodes.
* **Clustering:** For datasets exceeding single-node RAM, enable Valkey Cluster:
`cluster-enabled yes`
`cluster-config-file nodes-6379.conf`
`cluster-node-timeout 15000`