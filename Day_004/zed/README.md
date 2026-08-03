# How to Install Zed Editor: The Foolproof Guide

Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. Written in Rust, it is designed for speed, low latency, and built-in AI assistance. 

Whether you are on Linux, macOS, or Windows, installing Zed is simple. Follow this foolproof, no-error guide to get Zed up and running on your machine.

---

## 🍏 macOS

On macOS, you have two simple ways to install Zed.

### Method 1: Homebrew (Recommended)
If you use [Homebrew](https://brew.sh/), installing Zed is just one command away. This is the easiest way to keep your editor updated alongside your other packages.

1. Open **Terminal**.
2. Run the following command:
  ```bash
   brew install --cask zed
```

3. *(Optional)* If you want the preview build to test upcoming features:
  ```bash
  brew install --cask zed@preview
```



### Method 2: Direct Download

1. Visit the official download page: [zed.dev/download](https://zed.dev/download)
2. Click **Download for macOS**.
3. Once downloaded, open the `.dmg` file and drag the **Zed** app icon into your **Applications** folder.

---

## 🐧 Linux

The Zed team provides an official installation script that works across most major distributions (Ubuntu, Arch, Debian, RedHat, CentOS, Fedora, etc.) and supports both `x86_64` and `AArch64` architectures.

### The Official Install Script (Recommended)

1. Open your terminal.
2. Run the following single command:
```bash
curl -f [https://zed.dev/install.sh](https://zed.dev/install.sh) | sh

```


3. To install a specific version, you can pass an environment variable:
```bash
curl -f [https://zed.dev/install.sh](https://zed.dev/install.sh) | ZED_VERSION=0.216.0 sh

```


4. *(Optional)* If you want the preview build (updates about a week ahead of stable):
```bash
curl -f [https://zed.dev/install.sh](https://zed.dev/install.sh) | ZED_CHANNEL=preview sh

```



*Note on requirements:* Zed for Linux requires a Vulkan 1.3 compatible driver and standard freedesktop portals (`FileChooser`, `OpenURI`, `Secrets`).

**Uninstalling on Linux:**
If you ever want to remove Zed installed via the script, simply run:

```bash
zed --uninstall

```

---

## 🪟 Windows

Zed now officially supports Windows (Windows 10/11) as a native application.

### Method 1: Winget (Recommended)

The Windows Package Manager (`winget`) makes installing Zed incredibly easy and ensures you get the official package.

1. Open **PowerShell** or **Command Prompt** (Run as Administrator is recommended for package installations).
2. Type the following command and press Enter:
```powershell
winget install -e --id ZedIndustries.Zed

```


3. Follow the on-screen prompts if any appear. Zed will be installed and added to your start menu.

### Method 2: Direct Download

1. Visit the [Zed releases page](https://zed.dev/releases) or the main download page.
2. Download the Windows installer.
3. Run the installer and follow the standard Windows setup wizard.

*Note on requirements:* Zed on Windows requires a DirectX 11 compatible GPU. Ensure your graphics drivers are up to date and that you aren't using the fallback Microsoft Basic Display Adapter.

---

## 🛠️ Post-Installation: Installing the CLI Tool

Once you have Zed installed, you'll likely want to be able to open files directly from your terminal (e.g., typing `zed .` to open the current directory).

**On macOS / Linux:**

1. Open the Zed application.
2. Press `Command + Shift + P` (Mac) or `Ctrl + Shift + P` (Linux/Windows) to open the Command Palette.
3. Type **"Install CLI"** and select `zed: install cli`.
4. Now you can type `zed <filename>` in your terminal to open it instantly.

**To use Zed as your default Git editor:**
Add the following to your `~/.bashrc` or `~/.zshrc`:

```bash
export EDITOR="zed --wait"
```

