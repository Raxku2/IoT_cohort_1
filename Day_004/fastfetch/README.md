# The Ultimate, Foolproof Guide to Installing Fastfetch

`fastfetch` is a neofetch-like tool for fetching system information and displaying it in a pretty way, written mostly in C. It is highly praised for being significantly faster and more actively maintained than the classic `neofetch`.

This guide provides foolproof, step-by-step instructions to install Fastfetch on Windows, macOS, and virtually every Linux distribution. We have also included fallback methods in case your OS version is older or repositories are out of date.

---

## 🪟 1. Windows

The easiest way to install Fastfetch on Windows is through a command-line package manager. Open your terminal (PowerShell or Command Prompt) as an Administrator and choose ONE of the following methods:

### Method A: Using Winget (Recommended & Pre-installed on Windows 10/11)
```powershell
winget install fastfetch
```

### Method B: Using Scoop

If you prefer the Scoop package manager for portable apps:

```powershell
scoop install fastfetch
```

### Method C: Using Chocolatey

```powershell
choco install fastfetch
```

### Method D: MSYS2 (For MinGW environments)

```bash
pacman -S mingw-w64-ucrt-x86_64-fastfetch
```

*Note: After installation on Windows, you may need to restart your terminal for the `fastfetch` command to be recognized.*

---

## 🍏 2. macOS

To install Fastfetch on a Mac, you will need a package manager. Homebrew is the industry standard.

### Method A: Using Homebrew (Recommended)

If you don't have Homebrew installed, install it first via: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Then run:

```bash
brew install fastfetch
```

### Method B: Using MacPorts

If you are a MacPorts user instead:

```bash
sudo port install fastfetch
```

---

## 🐧 3. Linux

Because Linux has many different distributions, find your specific package manager below.

### Debian & Ubuntu-based (Ubuntu, Linux Mint, Pop!_OS, Zorin)

**Note:** Fastfetch is available in the official repositories for Ubuntu 24.04+ and Debian 13+.

```bash
sudo add-apt-repository ppa:zhangsongcui3371/fastfetch
sudo apt update
sudo apt install fastfetch
```

*Foolproof Fallback for Older Ubuntu/Debian:* If the PPA fails or you don't want to add it, download the precompiled `.deb` file directly:

1. Go to the [Fastfetch Releases page](https://github.com/fastfetch-cli/fastfetch/releases).
2. Download the `fastfetch-linux-amd64.deb` file.
3. Install it using: `sudo dpkg -i fastfetch-linux-amd64.deb` (run `sudo apt install -f` if you get dependency errors).

### Arch Linux-based (Arch, Manjaro, EndeavourOS)

Fastfetch is in the official Arch community repositories.

```bash
sudo pacman -S fastfetch
```

### Fedora, Red Hat, & CentOS-based (RHEL, AlmaLinux, Rocky)

```bash
sudo dnf install fastfetch
```

### openSUSE

```bash
sudo zypper install fastfetch
```

### Alpine Linux

```bash
apk add fastfetch
```

### NixOS (or Nix Package Manager)

```bash
nix-env -iA nixos.fastfetch
```

### Gentoo

```bash
emerge --ask app-misc/fastfetch
```

---

## 🛠️ 4. The Universal "No-Error" Fallbacks

If absolutely none of the above package managers work for you, use these universal methods.

### Universal Method A: Download the Pre-compiled Binary (Linux only)

This method works on almost ANY Linux distribution without needing root/sudo for the package manager.

```bash
# 1. Download the latest tar.gz from GitHub (replace URL if there's a newer version)
wget [https://github.com/fastfetch-cli/fastfetch/releases/latest/download/fastfetch-linux-amd64.tar.gz](https://github.com/fastfetch-cli/fastfetch/releases/latest/download/fastfetch-linux-amd64.tar.gz)

# 2. Extract the archive
tar -xf fastfetch-linux-amd64.tar.gz

# 3. Move the binary to your local bin directory
sudo cp fastfetch-linux-amd64/usr/bin/fastfetch /usr/local/bin/

# 4. (Optional) Copy the shares/configs for logos and presets
sudo cp -r fastfetch-linux-amd64/usr/share/fastfetch /usr/share/

```

### Universal Method B: Homebrew for Linux

If you use Homebrew on Linux:

```bash
brew install fastfetch
```

---

## ✅ 5. Verification & Configuration

Once installed, simply type the following into your terminal and hit Enter:

```bash
fastfetch
```

### Making it run on startup

To make Fastfetch run every time you open a terminal:

1. Open your shell configuration file (e.g., `nano ~/.bashrc` or `nano ~/.zshrc`).
2. Scroll to the very bottom of the file.
3. Add a new line and type: `fastfetch`
4. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).

### Customizing Fastfetch

Fastfetch is highly customizable. To generate a default config file:

```bash
fastfetch --gen-config
```

This will create a `config.jsonc` file (usually in `~/.config/fastfetch/config.jsonc`). You can edit this file to change logos, colors, and the exact modules (CPU, GPU, RAM, etc.) that are displayed.
