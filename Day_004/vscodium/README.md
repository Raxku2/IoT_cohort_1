# The Foolproof Guide to Installing VSCodium on Any OS

**VSCodium** is a community-driven, freely-licensed binary distribution of Microsoft’s editor VS Code, but with telemetry (tracking) disabled. This guide provides the most reliable, error-free methods to install VSCodium across Windows, macOS, and Linux.

---

## 🪟 Windows Installation

The most foolproof way to install VSCodium on Windows is using a package manager. It handles environment variables and updates automatically.

### Method 1: Winget (Recommended - Built into Windows 10 & 11)
`winget` is the official Windows Package Manager and comes pre-installed on most modern Windows systems.

1. Open **PowerShell** or **Command Prompt** (search for it in the Start menu).
2. Run the following command:
  ```powershell
   winget install vscodium.vscodium
```

3. Follow the on-screen prompts. Once finished, you can launch it from the Start Menu or by typing `codium` in your terminal.

### Method 2: Scoop (For Power Users)

If you use Scoop, installing is just as easy:

```powershell
scoop bucket add extras
scoop install vscodium
```

### Method 3: Manual Installer (.exe / .zip)

If you don't want to use the terminal:

1. Go to the [VSCodium GitHub Releases page](https://github.com/VSCodium/vscodium/releases).
2. Download the latest `VSCodiumUserSetup-x64-*.exe` (for 64-bit Intel/AMD) or `arm64` (for Windows on ARM).
3. Double-click the `.exe` file and follow the standard installation wizard.

---

## 🍏 macOS Installation

### Method 1: Homebrew (Recommended)

Homebrew is the standard package manager for macOS. If you don't have it, install it from [brew.sh](https://brew.sh/).

1. Open the **Terminal** app.
2. Run the following command:
```bash
brew install --cask vscodium
```



*Note: Homebrew automatically detects if you are using an Intel or Apple Silicon (M1/M2/M3) Mac and fetches the correct version.*

### Method 2: Manual Download (.dmg)

1. Go to the [VSCodium GitHub Releases page](https://github.com/VSCodium/vscodium/releases).
2. Download the correct `.dmg` file:
* **Apple Silicon (M1/M2/M3):** Look for `VSCodium-darwin-arm64-*.zip` or `.dmg`.
* **Intel Macs:** Look for `VSCodium-darwin-x64-*.zip` or `.dmg`.


3. Open the downloaded file and drag the **VSCodium** icon into your **Applications** folder.

**🍎 Foolproof Mac Tip (Gatekeeper Error):**
If macOS says *"VSCodium can't be opened because the developer cannot be verified"*:

1. Open **System Settings** > **Privacy & Security**.
2. Scroll down to the Security section and click **Open Anyway** next to the VSCodium notice.

---

## 🐧 Linux Installation

Because there are many Linux distributions, there are a few ways to install. **Flatpak is the most foolproof method for all distros.**

### Method 1: Flatpak (Universal & Foolproof for all Distros)

If your distribution supports Flatpak (like Linux Mint, Fedora, Pop!_OS, or Ubuntu), this is the most secure and easiest method.

1. Make sure Flatpak is installed and Flathub is enabled.
2. Run this command in your terminal:
```bash
flatpak install flathub com.vscodium.codium
```


3. Run it using: `flatpak run com.vscodium.codium` (or launch from your app menu).

### Method 2: Debian / Ubuntu / Mint / Pop!_OS (APT Repository)

To install VSCodium like a native app so it updates with `apt upgrade`, add the official repository:

1. Open your terminal and add the GPG key:
```bash
wget -qO - [https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg) \
    | gpg --dearmor \
    | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg
```


2. Add the repository:
```bash
echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] [https://download.vscodium.com/debs](https://download.vscodium.com/debs) vscodium main' \
    | sudo tee /etc/apt/sources.list.d/vscodium.list
```


3. Update and install:
```bash
sudo apt update && sudo apt install codium

```



### Method 3: Fedora / RHEL / CentOS / Rocky Linux (RPM)

Add the repository and install using `dnf`:

1. Add the GPG key:
```bash
sudo rpmkeys --import [https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg)

```


2. Add the repo:
```bash
printf "[gitlab.com_paulcarroty_vscodium_repo]\nname=download.vscodium.com\nbaseurl=[https://download.vscodium.com/rpms/](https://download.vscodium.com/rpms/)\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=[https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg](https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/-/raw/master/pub.gpg)\nmetadata_expire=1h" | sudo tee -a /etc/yum.repos.d/vscodium.repo

```


3. Install:
```bash
sudo dnf install codium

```



### Method 4: Arch Linux / Manjaro / EndeavourOS (AUR)

Arch users can easily install VSCodium using an AUR helper like `yay` or `paru`:

```bash
yay -S vscodium-bin

```

### Method 5: Snap (Ubuntu / Universal)

If you prefer Snaps, you can install the community-maintained snap package:

```bash
sudo snap install codium --classic

```

---

## 🛠️ Post-Installation & Troubleshooting

### 1. Launching VSCodium

* **GUI:** Search your application menu for "VSCodium".
* **Terminal:** Type `codium` (or `codium .` to open the current directory).

### 2. Extensions (Open VSX Registry)

VSCodium does not use the Microsoft Extension Marketplace due to licensing restrictions. Instead, it uses the **Open VSX Registry** (an open-source alternative).

* **95% of extensions** (like Python, Prettier, GitLens) are available out of the box.
* **Proprietary Extensions** (like Microsoft's official C# or Live Share) might not be available or may require manual installation.

### 3. Migrating from VS Code

If you are moving from VS Code to VSCodium and want to keep your settings:

1. Locate your VS Code `settings.json` file.
2. Copy its contents.
3. Open VSCodium, press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac), type `Preferences: Open Settings (JSON)`, and paste the contents.
