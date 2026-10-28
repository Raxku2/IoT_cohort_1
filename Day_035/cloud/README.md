# ☁️ Cloud VM Provisioning & Configuration Guide

A comprehensive quick-start guide to spinning up, authenticating, and securing Virtual Machines (VMs) across global and regional cloud providers.

## 📖 Fundamentals of Cloud VMs

### 1. VM Spinning (Provisioning)

"Spinning up" a VM refers to allocating cloud compute resources. Regardless of the platform, the core components you must configure are:

* **AMI / OS Image:** The operating system (e.g., Ubuntu 24.04, Debian, Rocky Linux).
* **Instance Type/Size:** The allocation of vCPUs and RAM.
* **Storage (Block Storage):** The root volume size and type (SSD/NVMe).
* **Network / VPC:** The virtual network where the VM lives.

### 2. Authentication (SSH Keys & PEM Files)

Cloud providers rarely use password authentication by default for Linux environments. Instead, they rely on asymmetric cryptography (SSH keys).

* **The Key Pair:** Consists of a Public Key (stored on the cloud VM) and a Private Key (stored on your local machine, often a `.pem` file).
* **Generating a Key:**
```bash
ssh-keygen -t ed25519 -C "admin@kanicodestudio"

```


* **PEM File Permissions:** Linux/macOS will reject a `.pem` file if it is readable by other users. You **must** restrict permissions:
```bash
chmod 400 my-key.pem

```


* **Connecting:**
```bash
ssh -i /path/to/my-key.pem ubuntu@<vm-public-ip>

```



### 3. Firewall Configuration (Security Groups)

Cloud firewalls operate at the network level (outside the OS). They act as a bouncer, dropping traffic before it even reaches your Linux firewall (like `ufw` or `iptables`).

* **Inbound (Ingress) Rules:** Default is usually **Deny All**. You must explicitly open ports.
* **Port 22:** SSH (Restrict to your specific IP for maximum security).
* **Port 80 & 443:** HTTP & HTTPS (Open to `0.0.0.0/0` for web applications).
* **Custom Ports:** E.g., Port `8000` (FastAPI) or `3000` (Express.js/React).


* **Outbound (Egress) Rules:** Default is usually **Allow All**, letting your VM reach out to the internet to download packages (via `apt`, `pip`, `yarn`, etc.).

---

## 🌍 Platform-Specific Workflows

### 🟠 AWS (Amazon EC2)

AWS uses a highly granular, enterprise-grade approach to VMs.

1. **Spinning:** Navigate to EC2 -> "Launch Instance". Choose an Amazon Machine Image (AMI) and an Instance Type (e.g., `t3.micro`).
2. **SSH / PEM:** AWS prompts you to create a new Key Pair or select an existing one right before launch. It downloads as a `.pem` file. You cannot download it again, so keep it safe.
3. **Firewall:** AWS calls these **Security Groups**. They are stateful. You attach a Security Group to the EC2 instance and define Inbound rules. Changes apply instantly.

### 🔵 General Enterprise Cloud (GCP / Azure / DigitalOcean)

*(Applicable to platforms outside AWS ecosystem)*

1. **Spinning:** GCP uses "Compute Engine", Azure uses "Virtual Machines", and DigitalOcean uses "Droplets".
2. **SSH / PEM:**
* **GCP:** Prefers "OS Login" (tying SSH to your Google Account) but allows you to paste a raw public SSH key into the project metadata.
* **DigitalOcean:** You upload your public SSH key before creating the Droplet; it gets injected into the `~/.ssh/authorized_keys` file on boot.


3. **Firewall:**
* GCP uses **VPC Firewall Rules** applied via "Network Tags" (e.g., tagging a VM with `web-server` applies the port 80/443 rules).



### 🇮🇳 Major Indian Cloud Platforms

For localized data residency, lower latency in the subcontinent, and Rupee billing, several Indian platforms provide robust VM services.

#### 1. E2E Networks

Extremely popular among Indian developers and startups for affordable Linux instances and GPU-backed VMs.

* **Spinning:** Handled via the MyAccount portal. You select a "Node" based on Linux distributions.
* **SSH / PEM:** You paste your public SSH key into the portal during Node creation. It does not force you to download a generated `.pem` file; you use your own local keys.
* **Firewall:** Uses a centralized Security Group dashboard where you map ports to specific Nodes.

#### 2. JioCloud

Jio's enterprise cloud offering, heavily utilized for compliance-heavy Indian applications.

* **Spinning:** Instances are launched inside a clearly defined Virtual Private Cloud (VPC).
* **SSH / PEM:** Follows the AWS model—generates a Key Pair during instance creation and provides a `.pem` file download.
* **Firewall:** Managed via Security Groups attached to the virtual network interfaces (vNICs) of the instance.

#### 3. CtrlS & NxtGen

More enterprise-focused, often providing Managed VMs alongside bare metal.

* Configuration is highly customizable but often involves a heavier initial network setup (allocating floating IPs, configuring NAT gateways) before the VM is publicly accessible via SSH.