### Navigation & Directory Management

Commands used to move around the file system and manage folders.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `pwd` | Print Working Directory | Displays the current absolute path of your active directory. | `pwd` | None | N/A | N/A |
| `cd` | Change Directory | Navigates into a different directory or steps back in the file path. | `cd folder_name` | `..`, `/` | Relative/Absolute Path Symbols | `..`: Goes back one hierarchical directory. <br>

<br>`/`: Navigates instantly to the root directory. |
| `ls` | List | Lists out files and directories located in the current path. | `ls -ltr` | `-l`, `-t`, `-r`, `-h` | Long list, Time, Reverse, Human-readable | `-l`: Lists items vertically with file sizes and permissions. <br>

<br>`-t`: Sorts items by latest modified time. <br>

<br>`-r`: Reverses standard sorting order. <br>

<br>`-h`: Formats file sizes to be readable. |
| `mkdir` | Make Directory | Creates a new directory (folder) in the designated path. | `mkdir new_folder` | None | N/A | N/A |
| `rmdir` | Remove Directory | Removes a specified directory exclusively if it is empty. | `rmdir empty_folder` | None | N/A | N/A |

### File Creation, Copying & Moving

Commands used to create, delete, and shift files around the system.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `touch` | Touch | Creates a brand new empty file on the file system. | `touch new.txt` | None | N/A | N/A |
| `rm` | Remove | Deletes a file permanently from the file system. | `rm file.txt` | `-rf` | Recursive Force | `-rf`: Deletes whole directories and their internal contents forcefully. |
| `cp` | Copy | Clones a file from one location path to a completely new location. | `cp f.txt /path/` | None | N/A | N/A |
| `mv` | Move | Relocates a file/folder to a new location or completely renames it. | `mv old.txt new.txt` | None | N/A | N/A |

### File Viewing & Reading

Commands used to look at the contents of files without modifying them.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `cat` | Concatenate | Reads and prints the entire content of a file directly to the terminal. | `cat file.txt` | None | N/A | N/A |
| `less` | Less | Opens a file in a page-by-page reader layout within the terminal. | `less file.txt` | `/`, `?` | Search Operators | `/word`: Initiates a search from top to bottom. <br>

<br>`?word`: Initiates a search from bottom to top. |
| `more` | More | Views the content of a file line-by-line or page-by-page dynamically. | `more file.csv` | None | N/A | N/A |
| `head` | Head | Displays only the top few lines of a targeted file output. | `head -5 f.txt` | `-<num>` | Line Count | `-5`: Commands the terminal to print specifically the top 5 lines. |
| `tail` | Tail | Displays only the bottom few lines of a targeted file output. | `tail -5 f.txt` | `-<num>` | Line Count | `-5`: Commands the terminal to print specifically the bottom 5 lines. |

### Text Processing & Editing

Commands used to edit text inside files, format outputs, or slice data.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `vi` | Vi Editor | Opens the native Vi text editor to insert or modify text in a file. | `vi file.txt` | None | N/A | N/A |
| `nano` | Nano Editor | Opens the Nano text editor, offering on-screen shortcuts for ease of use. | `nano file.txt` | None | N/A | N/A |
| `awk` | AWK | Granular text parser utilized to extract exact columns or structured fields. | `awk -F, '{print $2}' f` | `-F` | Field Separator | `-F`: Isolates the core delimiter separating variables (e.g., `,` for CSV files). |
| `cut` | Cut | Operates on rows to slice distinct starting strings out of each outputted line. | `cut -c 1-2 f.txt` | `-c` | Characters | `-c`: Flags the specific character limit range the terminal needs to extract. |
| `sed` | Stream Editor | Alters text globally or targets word replacements actively inside a data set. | `sed 's/old/new/g' f` | `-n` | No Auto-print | `-n`: Suppresses blanket printing configurations to pull individual lines. |
| `tr` | Translate | Modifies character cases dynamically or shreds symbols natively. | `tr -d '%' < f.txt` | `-d` | Delete | `-d`: Purges the targeted text character fully from the terminal output. |
| `truncate` | Truncate | Synthetically balloons or collapses a file's overarching memory footprint size. | `truncate -s 50M f` | `-s` | Size | `-s`: Hardcodes the generated file target footprint (e.g., 50M). |
| `fold` | Fold | Splits horizontally wide text structures aggressively into rigid vertical columns. | `fold -w 1` | `-w` | Width | `-w`: Restricts output to the specified column numerical width. |
| `split` | Split | Splits a single large file structurally into multiple smaller files. | `split -l 3 f.txt` | `-l` | Line Length | `-l`: Sets exactly how many lines each newly split file should contain. |
| `> / >>` | Redirection Operators | Redirects operational payload strings seamlessly into target files. | `ls > files.txt` | `>` / `>>` | Overwrite / Append | `>`: Overwrites a destination file. <br>

<br>`>>`: Concatentates output onto an existing file. |

### Searching & Sorting

Commands used to find files, filter data, and organize list outputs.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `grep` | Global RegEx Print | Searches for a specific word or pattern match within a file. | `grep "word" f.txt` | None | N/A | N/A |
| `egrep` | Extended Grep | Searches for multiple distinct words or patterns at once using OR logic. | `egrep "w1|w2" f` | None | N/A | N/A |
| `sort` | Sort | Rearranges the text contents of a file sequentially (alphabetically). | `sort file.txt` | `-r` | Reverse | `-r`: Sorts the targeted file in reverse alphabetical order (Z to A). |
| `uniq` | Unique | Removes directly adjacent duplicate lines from file readout. | `uniq file.txt` | None | N/A | N/A |
| `find` | Find | Hunts for a file across specific directory paths based on naming parameters. | `find ./ -name f.csv` | `-name` | Name | `-name`: Specifies the exact, case-sensitive filename variable to hunt for. |
| `locate` | Locate | Rapidly searches for a file across the entire OS using an internal database. | `locate file.csv` | None | N/A | N/A |
| `updatedb` | Update Database | Updates the internal backend database leveraged by the `locate` command. | `sudo updatedb` | None | N/A | N/A |
| `wc` | Word Count | Counts lines, words, or standard characters mapped in a file. | `wc -l file.txt` | `-l` | Lines | `-l`: Returns precisely the total number of lines mapping to the file. |
| `cmp` | Compare | Compares two files to check if they are identical byte-by-byte. | `cmp f1 f2` | None | N/A | N/A |
| `diff` | Difference | Highlights exact differences line-by-line between two similar files. | `diff -u f1 f2` | `-u` | Unified | `-u`: Outputs the specific line differences in a unified, visually clear format. |

### Archiving & Compression

Commands used to package and compress files to save space or transfer data.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `gzip` / `gunzip` | GNU Zip | Compresses or decompresses a designated file into a `.gz` data archive. | `gzip -k file.txt` | `-k` | Keep | `-k`: Commands the tool to keep the original uncompressed file alongside the `.gz` version. |
| `tar` | Tape Archive | Recursively compresses or extracts comprehensive folders/directories. | `tar -czf x.tar.gz folder` | `-c`, `-x`, `-z`, `-f` | Create, Extract, Gzip, File | `-c`: Provisions a new archive. <br>

<br>`-x`: Extracts a pre-existing archive. <br>

<br>`-z`: Injects standard gzip compression. <br>

<br>`-f`: Denotes the final archive filename. |
| `zip` / `unzip` | Zip | Compresses selected independent files into one core `.zip` archive. | `zip file.zip f1 f2` | `-l` | List | `-l`: Peeks at contents mapped inside the zip file without extracting them locally. |

### System & Hardware Information

Commands to check memory, CPU, disk usage, and server details.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `free` | Free Memory | Tracks standard available cache versus utilized RAM memory on the server load. | `free -h` | `-h`, `-t` | Human-readable, Total | `-h`: Displays numbers properly formatted in MB/GB equivalents. <br>

<br>`-t`: Aggregates usage parameters to push a summarized "Total" output line. |
| `top` | Table of Processes | Launches an active dashboard monitor detailing CPU and RAM utilization metrics. | `top` | None | N/A | N/A |
| `du` | Disk Usage | Investigates block storage consumed comprehensively by mapped folders/files. | `du -h folder` | `-h` | Human-readable | `-h`: Translates raw drive bytes into immediately readable KB/MB/GB values. |
| `df` | Disk Free | Quantifies strictly the total allocated and safely available file system space left. | `df -h` | `-h` | Human-readable | `-h`: Refines standard byte formatting into simplified disk readings. |
| `hostname` | Host Name | Surfaces the active configured machine tag operating on the local level network. | `hostname` | None | N/A | N/A |
| `lscpu` | List CPU | Breaks down bare-metal hardware specs including OS thread counts and core data. | `lscpu` | None | N/A | N/A |
| `arch` | Architecture | Scrapes OS parameters to determine if the rig processes natively at 32-bit or 64-bit. | `arch` | None | N/A | N/A |
| `lsblk` | List Block Devices | Catalogs physical block storage drives and logical partitioned disks sequentially. | `lsblk` | None | N/A | N/A |
| `uname` | Unix Name | Exposes core kernel release identifiers and foundational server identification tags. | `uname -a` | `-a` | All | `-a`: Concatenates all possible OS environment metadata into a combined string. |
| `date` | Date | Displays the current system date and time. | `date +%T` | `+%D`, `+%T`, `+%H:%M` | Date Format, Time Format, Custom Format | `+%D`: Shows date only. <br>

<br>`+%T`: Shows time only. <br>

<br>`+%H:%M`: Formats specific hours and minutes. |
| `cal` | Calendar | Generates a visual calendar for the current month or a declared year. | `cal 2020` | None | N/A | N/A |
| `uptime` | Uptime | Outputs the time length the server has been running alongside load averages. | `uptime` | None | N/A | N/A |

### Process & Job Management

Commands to monitor, background, foreground, or terminate active processes.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ps` | Process Status | Populates an active diagnostic readout mapping ongoing backend OS processes. | `ps -ef | grep java` | `-ef` | Every Full | `-ef`: Overrides limitations to map every single system application path across all accounts. |
| `pgrep` | Process Grep | Mines process execution tables to secure an isolated Process ID (PID) number tag. | `pgrep nginx` | None | N/A | N/A |
| `kill` | Kill | Severely terminates active process instances permanently via their PID tag. | `kill -9 8905` | `-9` | Force | `-9`: Signals a kernel SIGKILL directive, ensuring the application breaks instantly. |
| `pkill` | Process Kill | Terminates live programs forcefully relying purely on a recognized app name. | `pkill httpd` | None | N/A | N/A |
| `jobs` | Jobs | Displays active scripts paused or passively generating background calculations. | `jobs` | None | N/A | N/A |
| `bg` | Background | Commences suspended calculations, pushing them to process quietly in the backend. | `bg` | None | N/A | N/A |
| `fg` | Foreground | Pulls a background-processing script immediately forward into the active screen. | `fg` | None | N/A | N/A |
| `nohup` | No Hang Up | Guards a background script, ensuring it compiles properly regardless of OS logouts. | `nohup s.sh &` | None | N/A | N/A |
| `at` | At | Schedules standalone jobs structurally to execute specifically upon a synchronized clock time. | `at 05:10 PM` | None | N/A | N/A |

### User & Permission Management

Commands used to manage users, groups, passwords, and file permissions.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `whoami` | Who Am I | Shows the name of the user currently logged into the active terminal session. | `whoami` | None | N/A | N/A |
| `su` | Switch User | Pivots the terminal access session instantly to an alternate user profile or root. | `su root` | None | N/A | N/A |
| `sudo` | Superuser Do | Leverages elevated, temporary administrative permissions to run blocked commands. | `sudo yum install n` | None | N/A | N/A |
| `exit` | Exit | Unplugs the current session identity and reverses back to the foundational login. | `exit` | None | N/A | N/A |
| `chmod` | Change Mode | Re-engineers the read/write/execute allowance settings across files or scripts. | `chmod o+r f.txt` | None | N/A | N/A |
| `chown` | Change Ownership | Delegates the ownership permissions of a localized file to a completely new user. | `chown user file` | None | N/A | N/A |
| `chgrp` | Change Group | Shuttles the operational group associations tied independently to an OS file. | `chgrp group file` | None | N/A | N/A |
| `useradd` | User Add | Manufactures a fresh user profile entity with standard base defaults internally. | `useradd alex` | None | N/A | N/A |
| `passwd` | Password | Overwrites encrypted baseline login authentication passwords configured to an account. | `passwd alex` | None | N/A | N/A |
| `groupadd` | Group Add | Commits a designated collective group node specifically engineered to bundle user logic. | `groupadd testing` | None | N/A | N/A |
| `id` | ID | Renders numeric UID markers and root GID strings natively bound directly to a user entry. | `id alex` | None | N/A | N/A |
| `userdel` | User Delete | Nukes a user account logically off the host server instance structure permanently. | `userdel alex` | None | N/A | N/A |
| `groupdel` | Group Delete | Exterminates a custom user group logic block originally constructed to house users. | `groupdel testing` | None | N/A | N/A |
| `usermod` | User Modify | Refactors existing administrative identifiers (such as tying a user to secondary teams). | `usermod -G test nick` | `-G` | Groups | `-G`: Binds and links the targeted profile identity definitively into a secondary assigned group list. |

### Networking & Web Downloads

Commands to ping websites, download packages, view network interfaces, and secure remote logins.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `ping` | Ping | Runs ICMP network connection diagnostics to measure host packet response latency. | `ping google.com` | None | N/A | N/A |
| `wget` | Web Get | Triggers an active download of files or packages strictly from an internet URL. | `wget http://link` | None | N/A | N/A |
| `curl` | Client URL | Communicates dynamically with APIs or pulls raw text output from a web host. | `curl site.com` | None | N/A | N/A |
| `ifconfig` | Interface Config | Displays the underlying network interface controllers alongside IPv4 allocations. | `ifconfig` | None | N/A | N/A |
| `ssh` | Secure Shell | Opens a remote authentication bridge into an isolated server securely. | `ssh user@IP` | None | N/A | N/A |
| `scp` | Secure Copy | Beams files encrypted from a host location securely to a destination remote node. | `scp f user@IP:/path` | None | N/A | N/A |
| `telnet` | Telnet | Probes server firewalls to determine if exact application network service ports are open. | `telnet IP PORT` | None | N/A | N/A |
| `netstat` | Network Statistics | Reports all established port listeners and mapped IP connection pathways currently alive. | `netstat -putan` | `-putan` | Process, UDP, TCP, All, Numeric | `-putan`: Exposes total listening sockets, connection layers, protocol logic types, and raw PIDs. |
| `traceroute` | Trace Route | Traces intermediate network router hops a transmission crosses navigating to a target. | `traceroute host` | None | N/A | N/A |

### Utilities, Environment & Package Management

Commands to clear screens, view history, set environment variables, and manage system packages.

| Command | Command Name | Description | Example Usage | Flags Used | Flag Name | Flag Description |
| --- | --- | --- | --- | --- | --- | --- |
| `clear` | Clear | Clears the terminal screen for a clean workspace (Shortcut: Ctrl + L). | `clear` | None | N/A | N/A |
| `history` | History | Lists previously executed commands chronologically in the terminal. | `history` | None | N/A | N/A |
| `--help` | Help | An argument command to view a tool's internal syntax and operational flags. | `ls --help` | None | N/A | N/A |
| `man` | Manual | Triggers the complete manual page for a command within the UI. | `man ls` | None | N/A | N/A |
| `which` | Which | Reveals the exact file path of a system executable command. | `which ls` | None | N/A | N/A |
| `bc` | Basic Calculator | Initiates an interactive numerical calculator inside the terminal environment. | `bc` | None | N/A | N/A |
| `script` | Script | Transcribes all terminal interactions into a continuous log file. | `script` | None | N/A | N/A |
| `alias` | Alias | Binds a personalized, shorter shortcut reference for a long terminal command. | `alias l="ls -ltr"` | None | N/A | N/A |
| `printenv` | Print Environment | Dumps all registered environmental variables presently logged on the OS. | `printenv` | None | N/A | N/A |
| `export` | Export | Transmits or registers a fresh environment variable on the OS. | `export J_HOME=/path` | None | N/A | N/A |
| `source` | Source | Automatically reloads script configuration files (like `.bashrc`) to apply updates. | `source .bashrc` | None | N/A | N/A |
| `yum` | Yellowdog Updater | Software package manager for downloading tools (Used strictly in RedHat distros). | `yum install nginx` | None | N/A | N/A |
| `systemctl` | System Control | Scans status, triggers, or ceases backend system services natively. | `systemctl start nginx` | None | N/A | N/A |