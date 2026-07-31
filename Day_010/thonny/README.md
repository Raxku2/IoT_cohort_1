# The Complete Thonny IDE Mastery Guide: Commands, Shortcuts, and Configurations

A self-contained, practice-focused reference manual designed for zero cognitive load. This guide details every essential command, configuration parameter, interface layout, and keyboard shortcut within Thonny, specifically optimized for standard Python and MicroPython/IoT development environments.

---

## 1. Interface Anatomy & View Layouts
To interact effectively with Thonny, you must first set up your workspace. All interface panels are toggled via the top menu path: `View -> [Panel Name]`.

### 1.1 The Primary Panels
*   **The Editor (Central Window)**
    *   **Meaning:** The workspace where you write, edit, and save your Python script files (`.py`).
    *   **Placement:** Fixed in the center upper portion of the screen.
*   **The Shell (Bottom Window)**
    *   **Meaning:** The Interactive Read-Eval-Print Loop (REPL). It displays execution outputs, error logs, and allows you to run single lines of Python code instantly. When a microcontroller is connected, this displays the live device REPL.
    *   **Placement:** Activated via `View -> Shell`. Located at the bottom by default.
*   **The Files Panel (Left Sidebar)**
    *   **Meaning:** A split-view file browser. The top half shows your computer's local file directory (**This Computer**), and the bottom half shows the microcontroller's flash memory storage (**MicroPython Device**).
    *   **Placement:** Activated via `View -> Files`. 
*   **The Variables Panel (Right Sidebar)**
    *   **Meaning:** A real-time debugging inspection tool. It lists all active global variables, objects, and their current values in memory after a script runs or hits a breakpoint.
    *   **Placement:** Activated via `View -> Variables`.
*   **The Plotter Panel (Bottom Right)**
    *   **Meaning:** A real-time data visualizer. If your code prints numbers to the Shell in a tuple format or as raw numbers (e.g., `print(sensor_value)`), the Plotter automatically parses those numbers and draws a live line graph.
    *   **Placement:** Activated via `View -> Plotter`.

---

## 2. Core Execution Commands & Backend Lifecycle
Running and stopping code involves interacting directly with Thonny's backend interpreter.

### 2.1 Running Scripts
*   **Run Current Script**
    *   **Placement:** `Run -> Run current script` or the **Green Play Button** on the main toolbar.
    *   **Keyboard Shortcut:** `F5`
    *   **Meaning:** Saves the open file automatically and executes the entire script from the first line to the last line. 
*   **Run Current Script as Script (Inline)**
    *   **Placement:** `Run -> Run current script as script`
    *   **Keyboard Shortcut:** `Ctrl + R`
    *   **Meaning:** Runs the file directly in the Shell context without completely resetting the global memory variables beforehand.

### 2.2 Halting and Resetting
*   **Stop / Restart Backend**
    *   **Placement:** `Run -> Stop/Restart backend` or the **Red Stop Button** on the main toolbar.
    *   **Keyboard Shortcut:** `Ctrl + F2` (Alternative: Click inside the Shell and press `Ctrl + C` to send a keyboard interrupt signal).
    *   **Meaning:** Forces the current execution to terminate immediately. It wipes the active memory clean, resets the environment variables, and restarts the backend process.
*   **Soft Reboot (MicroPython Exclusive)**
    *   **Placement:** Click inside the **Shell panel** and execute the shortcut.
    *   **Keyboard Shortcut:** `Ctrl + D`
    *   **Meaning:** Performs a software-level reset of a connected microcontroller (like an ESP8266 or ESP32) without cutting physical power. It clears the board's RAM and re-runs the hardware boot sequences (`boot.py` followed by `main.py`).

---

## 3. Configuring the Interpreter (Parameters & Flags)
Configuring how Thonny runs your code is done through the Options window. 
*   **Menu Path Location:** `Tools -> Options... -> Interpreter (Tab)`

When you open this tab, you are presented with two primary configuration parameters that act as flags for Thonny's execution engine:

### 3.1 Parameter 1: "Which kind of interpreter should Thonny use to run your code?"
This dropdown menu tells Thonny exactly where to route your code execution.
*   **Option: Local Python 3**
    *   *Meaning:* Uses the standard Python installation bundled with Thonny on your laptop or desktop computer. Used for standard desktop applications, math processing, and file handling.
*   **Option: MicroPython (ESP8266) / MicroPython (ESP32)**
    *   *Meaning:* Instructs Thonny to stop looking at your local machine and instead target an attached Espressif microcontroller chip.
*   **Option: Raspberry Pi Pico**
    *   *Meaning:* Optimizes the connection protocols specifically for the RP2040/RP2350 silicon architectures.

### 3.2 Parameter 2: "Port" or "Details"
This dropdown tells Thonny the precise hardware communication channel to use to talk to the device.
*   **Option: `<try to detect port automatically>`**
    *   *Meaning:* Thonny scans all active USB Serial communication systems to find a valid microcontroller bootloader signature. Highly reliable for single-board setups.
*   **Option: Specific Serial Port (e.g., `COM3`, `COM4` on Windows / `/dev/ttyUSB0`, `/dev/tty.usbserial` on Linux/macOS)**
    *   *Meaning:* Hardcodes the selection to a specific physical USB port. Essential if you have multiple microcontrollers plugged into the same machine simultaneously.

---

## 4. Visual Debugging Commands (Step-by-Step Tracing)
Debugging allows you to slow time down and watch your code execute line-by-line, showing you exactly how expressions resolve.

*   **Debug Current Script**
    *   **Placement:** `Run -> Debug current script` or the **Bug Icon** on the main toolbar.
    *   **Keyboard Shortcut:** `Ctrl + F5`
    *   **Meaning:** Starts execution in debug mode, pausing at the very first operational line of code and highlighting it in yellow.

### 4.1 The Tracing Commands
Once a debug session is active, use these four commands to navigate the code path:

| Command Name | Menu Path | Keyboard Shortcut | Operational Meaning (Zero Cognitive Load) |
| :--- | :--- | :--- | :--- |
| **Step Over** | `Run -> Step over` | `F6` | Executes the currently highlighted line completely and moves straight to the next line. If the line contains a function call, it runs the entire function in the background without jumping inside it. |
| **Step Into** | `Run -> Step into` | `F7` | If the highlighted line contains a custom function call, this command forces the cursor to jump *inside* the function body so you can inspect its inner lines one-by-one. |
| **Step Out** | `Run -> Step out` | `F8` | If you are currently stepping through lines *inside* a function body, this executes all remaining lines of that function instantly and returns your cursor back up to the main script level. |
| **Resume** | `Run -> Resume` | `F9` | Exits the line-by-line stepping mode and lets the script run normally at full speed until it finishes or hits a declared breakpoint. |

### 4.2 Breakpoint Command
*   **Toggle Breakpoint**
    *   **Placement:** Click directly on the grey margin area to the left of the line numbers in the Editor, or choose `Run -> Toggle breakpoint`.
    *   **Keyboard Shortcut:** `Ctrl + F8`
    *   **Meaning:** Places a small red dot next to the line number. When you run the debugger (`Ctrl + F5`), the engine will run at full speed until it encounters this exact line, where it will instantly pause.

---

## 5. File Management & Package Extensions
Thonny includes specialized modules for handling physical files and external libraries.

### 5.1 Device File Operations
When using a MicroPython interpreter, interacting with the **Files Panel** (`View -> Files`) activates special contextual commands via a **Right-Click** on any file:
*   **Upload to /**
    *   *Where:* Right-click a file inside the upper "This Computer" pane.
    *   *Meaning:* Copies the chosen script directly from your computer's hard drive onto the microcontroller's internal flash storage.
*   **Download to...**
    *   *Where:* Right-click a file inside the lower "MicroPython Device" pane.
    *   *Meaning:* Pulls a script out of the microcontroller storage and saves a copy onto your local computer.

### 5.2 Package Management Parameters
*   **Manage Packages Module**
    *   **Placement:** `Tools -> Manage packages`
    *   **Flags/Parameters:** Contains a search input field and an "Install" button.
    *   **Meaning (Local Context):** Searches PyPI (Python Package Index) to install libraries like `requests` or `pandas` onto your local machine via `pip`.
    *   **Meaning (MicroPython Context):** Automatically switches its backend to search `micropython-lib`. When you click install, Thonny handles downloading the constrained code version and transfers it directly into the `/lib` folder of your attached microcontroller automatically.

---

## 6. Complete Keyboard Shortcut Reference Sheets
Categorized cheat sheets organized for fast visual scanning.

### 6.1 File and Editor Manipulation
| Shortcut | Action Context | Meaning |
| :--- | :--- | :--- |
| `Ctrl + N` | File Operations | Creates a brand-new, untitled blank tab in the Editor. |
| `Ctrl + O` | File Operations | Opens an existing local or microcontroller script. |
| `Ctrl + S` | File Operations | Saves modifications made to the active tab. |
| `Ctrl + W` | File Operations | Closes the active Editor tab window. |
| `Tab` | Text Selection | Indents the highlighted block of code to the right by 4 spaces. |
| `Shift + Tab` | Text Selection | Outdents (shifts) the highlighted block of code to the left by 4 spaces. |
| `Ctrl + 3` | Text Selection | Comments out the selected lines of code by prepending `#`. |
| `Ctrl + 4` | Text Selection | Removes the comment marker `#` from the selected lines of code. |

### 6.2 Execution and Debugging Workflow
| Shortcut | Action Context | Meaning |
| :--- | :--- | :--- |
| `F5` | Script Execution | Standard Run: Wipes environment clean and runs file. |
| `Ctrl + R` | Script Execution | Inline Run: Runs file while maintaining active variable values. |
| `Ctrl + F2` | Operational Halt | Absolute Stop: Kills the backend interpreter and clears RAM. |
| `Ctrl + D` | Shell (MicroPython) | Soft Reboot: Resets microcontroller board logic safely. |
| `Ctrl + F5` | Debug Launch | Initiates line-by-line visual inspection mode. |
| `F6` | Debug Stepping | Step Over: Advance to next statement on the same level. |
| `F7` | Debug Stepping | Step Into: Dive inside the highlighted function loop. |
| `F8` | Debug Stepping | Step Out: Complete function and return to main level. |
| `F9` | Debug Stepping | Resume standard execution speeds. |
| `Ctrl + F8` | Margin Selection | Toggle a hard breakpoint at the current code row. |

### 6.3 Workspace Adjustments
| Shortcut | Action Context | Meaning |
| :--- | :--- | :--- |
| `Ctrl + +` | Global Display | Increases the font size across the Editor and Shell panes. |
| `Ctrl + -` | Global Display | Decreases the font size across the Editor and Shell panes. |
| `F11` | Application Mode | Toggles full-screen display focus on or off. |
