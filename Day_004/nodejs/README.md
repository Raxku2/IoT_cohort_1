# Guide to Installing Node.js (Windows, macOS, Linux)

Installing Node.js directly from standard OS installers can sometimes lead to painful `EACCES` permission errors, especially when trying to install global packages via `npm`. 

The universally accepted **best practice** is to use a **Node Version Manager**. This approach allows you to install multiple versions, switch between them with one command, and—most importantly—install global packages safely without needing administrator (`sudo`) rights.

---

## 🪟 Windows

### The Foolproof Method: `nvm-windows`
`nvm-windows` is a separate project from the Mac/Linux `nvm`, designed specifically to manage Node installations seamlessly on Windows.

**Step 1: Uninstall existing Node.js (Crucial)**
If you have installed Node.js previously using an `.msi` installer:
1. Go to **Settings > Apps > Installed apps**.
2. Find Node.js and uninstall it.
3. Delete any remaining installation directories (e.g., `C:\\Program Files\\nodejs` or `C:\\Users\\<User>\\AppData\\Roaming\\npm`).

**Step 2: Download and Install nvm-windows**
1. Go to the [nvm-windows releases page](https://github.com/coreybutler/nvm-windows/releases).
2. Download the `nvm-setup.exe` file from the latest release.
3. Run the installer and complete the setup wizard (leaving default paths is perfectly fine).

**Step 3: Install the latest Node.js**
1. Open PowerShell or Command Prompt **as Administrator**.
2. To see a list of available Node.js versions, run:
   ```powershell
   nvm list available

   ```

3. To install the absolute latest version, run:
   ```powershell
   nvm install latest
   
   ```


*(Alternatively, install the Long Term Support version for better stability: `nvm install lts`)*
4. To activate the version you just installed, run:
```powershell
nvm use latest

```



---

## 🍎 macOS

### The Foolproof Method: `nvm` (Node Version Manager)

**Step 1: Install `nvm**`
Open your terminal (Terminal or iTerm2) and run the official install script via `curl`:

```bash
curl -o- [https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh](https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh) | bash

```

**Step 2: Update your shell profile**
The script usually adds the required configuration to your profile automatically. To apply the changes without restarting your computer:

```bash
source ~/.zshrc   # If you use Zsh (default on macOS Catalina and newer)
source ~/.bashrc  # If you use older macOS with Bash

```

**Step 3: Install Node.js**
To install the latest version of Node.js and set it as your default:

```bash
nvm install node
nvm alias default node

```

*Note: While Homebrew (`brew install node`) is popular on Mac, `nvm` remains the safest route to entirely avoid global package permission issues.*

---

## 🐧 Linux (Ubuntu, Debian, Fedora, Arch, etc.)

### The Foolproof Method: `nvm` (Universal Script)

The same tool used for macOS works flawlessly across almost all Linux distributions.

**Step 1: Install curl (if not already installed)**

* **Ubuntu/Debian:** `sudo apt update && sudo apt install curl -y`
* **Fedora/RHEL:** `sudo dnf install curl -y`
* **Arch Linux:** `sudo pacman -S curl`

**Step 2: Install `nvm**`
Run the install script:

```bash
curl -o- [https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh](https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh) | bash

```

**Step 3: Update your shell profile**
Reload your terminal environment to recognize the `nvm` command:

```bash
source ~/.bashrc

```

*(If you are using Zsh instead of bash, run `source ~/.zshrc`)*

**Step 4: Install Node.js**

```bash
nvm install node
nvm alias default node

```

---

## ✅ Verification & Post-Installation Setup

To ensure Node.js and `npm` (Node Package Manager) were installed correctly, open a **brand new terminal window** and run:

```bash
node -v
npm -v

```

*Both commands should successfully output their respective version numbers (e.g., `v21.x.x`).*

### Keep npm up to date

`npm` receives updates more frequently than Node.js itself. You can easily update `npm` to its latest secure version by running:

```bash
npm install -g npm@latest

```

---

## 🛠️ Troubleshooting Common Errors

* **Error: `nvm: command not found` (Mac/Linux)**
* **Fix:** Your shell profile didn't load the variables. Open your `~/.zshrc` or `~/.bashrc` file in a text editor (like `nano ~/.zshrc`) and paste this at the very bottom:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

```


Save the file, exit, and run `source ~/.zshrc` (or `.bashrc`).


* **Error: `EACCES: permission denied` when running `npm install -g**`
* **Fix:** This happens if you used standard `apt`, `brew`, or `.msi` installers requiring `sudo`. If you strictly followed this `nvm` guide, **you will never see this error!** If you do, uninstall Node.js entirely and reinstall using `nvm` as outlined above. Never use `sudo npm install`.


