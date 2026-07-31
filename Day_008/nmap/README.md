# Zero to Recon: The Practical Nmap Masterclass

Welcome to the foundational guide on network mapping. Nmap (Network Mapper) is the industry standard tool for discovering devices on a network and finding open doors (ports). 

This guide is designed for **zero cognitive load**. You will learn exactly what to type, where to type it, and why it works.

> 🛑 **THE GOLDEN RULE OF NMAP:** > **Never scan a target you do not own or do not have explicit permission to test.** > For this guide, we will only use safe, legal targets:
> 1. `localhost` or `127.0.0.1` (Your own computer)
> 2. `scanme.nmap.org` (Nmap's official, legal testing server)

---

## Part 1: Core Concepts (The "Why")

Before running commands, you must understand three basic terms:

* **IP Address:** The street address of a device (e.g., `192.168.1.5`).
* **Port:** The specific "apartment number" or door at that address (e.g., Port `80` for web traffic). There are 65,535 possible ports.
* **State:** When Nmap checks a door, it reports one of three states:
    * 🟢 **Open:** A program is actively listening behind this door.
    * 🔴 **Closed:** The door is there, but no program is listening.
    * 🟡 **Filtered:** A firewall is blocking Nmap, so it can't tell if it's open or closed.

---

## Part 2: The Anatomy of an Nmap Command

Every Nmap command follows the exact same structure. Read it from left to right:

`nmap` `[FLAGS]` `[TARGET]`

1.  **`nmap`**: The trigger word. It wakes up the program.
2.  **`[FLAGS]`**: The instructions. These start with a dash (`-`). They tell Nmap *how* to scan.
3.  **`[TARGET]`**: The destination. This is the IP address, website, or network you are pointing Nmap at.

---

## Part 3: The Practical Arsenal (Actionable Commands)

Open your terminal or command prompt. Let's build your commands from basic to advanced.

### Level 1: The Quick Look
* **Goal:** Scan the top 1,000 most common ports to see what is open.
* **The Command:** 
  ```bash
  nmap scanme.nmap.org
    ```

* **Explanation:** Notice there are no flags here. If you don't give Nmap specific instructions, it defaults to a fast, basic scan of the most popular ports.

### Level 2: The "Scan Everything" Approach

* **Goal:** Scan all 65,535 possible ports to find hidden services.
* **The Command:** 
  ```bash
  nmap -p- 127.0.0.1
    ```




* **Keyword Breakdown:**
* `-p-`: The `p` stands for **Port**. The extra `-` tells Nmap "scan every port from 1 to 65,535." Use this when you suspect a service is hiding on a strange port.



### Level 3: Service & Version Interrogation (The Most Important Scan)

* **Goal:** Don't just find open doors; find out *exactly* what software is running behind them.
* **The Command:** 
  ```bash 
  nmap -sV scanme.nmap.org
    ```




* **Keyword Breakdown:**
* `-sV`: Stands for **Service Version**. Nmap knocks on the open door and asks the software, "Who are you and what version are you?" (e.g., It will tell you if it's running Apache v2.4 or v2.2).
* *Why it matters:* Hackers use version numbers to find known exploits for that specific software.



### Level 4: The Kitchen Sink (Aggressive Scan)

* **Goal:** Throw everything at the target. Get OS details, versions, and run default scripts.
* **The Command:** 

  ```bash
  nmap -A scanme.nmap.org
    ```




* **Keyword Breakdown:**
* `-A`: Stands for **Aggressive**. It combines version detection, operating system detection, and basic script scanning.
* *Warning:* This is highly visible and noisy. Firewalls will easily detect this scan.



---

## Part 4: Network Discovery (Finding Connected Devices)

How do you find a headless device—like a NodeMCU ESP8266 or a Raspberry Pi—that just connected to your Wi-Fi but has no screen to show you its IP address? You use a **Ping Sweep**.

* **Goal:** Map the entire local network to see every active IP address and its hardware manufacturer.
* **The Command:** 
  ```bash
  nmap -sn 192.168.1.0/24
  ```




* **Keyword Breakdown:**
* `-sn`: Stands for **Scan No-ports** (formerly known as a ping scan). This tells Nmap: "Do not scan ports. Just shout 'Is anyone there?' to the whole network and list who replies."
* `192.168.1.0/24`: This represents your entire network subnet. *(Note: Replace `192.168.1` with your actual network base, which you can find by running `ipconfig` on Windows or `ip a` on Linux/Mac).*



---

## Part 5: Advanced Recon (Vulnerabilities and Hidden Web Pages)

Nmap has a built-in engine called **NSE (Nmap Scripting Engine)**. You can attach powerful scripts to your scans to automate vulnerability finding.

### Finding Hidden Website Directories

* **Goal:** Find hidden admin panels (like `/admin` or `/dashboard`) on a web server.
* **The Command:**
  ```bash
  nmap -sV --script http-enum scanme.nmap.org
    ```


* **Keyword Breakdown:**
* `--script`: Tells Nmap to load an external script.
* `http-enum`: The name of the script. It tests the web server against a massive list of common hidden folders.



### Scanning for Exploits

* **Goal:** Automatically check the software running on the target against a database of known vulnerabilities (CVEs).
* **The Command:**
  ```bash
  nmap -sV --script vuln scanme.nmap.org
    ```


* **Keyword Breakdown:**
* `vuln`: This isn't just one script; it's an entire category. Nmap will run every script in its library designed to spot known vulnerabilities on the services it finds. If the target is broken, this command will tell you exactly how.



---

## Summary Cheat Sheet

Keep this quick-reference guide handy:

| Command / Flag | What it actually means | When to use it |
| --- | --- | --- |
| `nmap <target>` | Basic Scan | Quick look at top 1000 ports. |
| `-p-` | Scan all ports | Finding hidden services on high ports. |
| `-sV` | Service Version | Identifying software versions for exploits. |
| `-A` | Aggressive | Gathering maximum info (Noisy). |
| `-sn` | Ping Sweep | Finding headless devices on local Wi-Fi. |
| `--script vuln` | Vulnerability Scan | Finding known security flaws automatically. |
