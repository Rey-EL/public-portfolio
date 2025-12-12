# Project: Self-Healing Ubuntu

**Author:** Elvis Reyes-Hernandez (Rey-EL)  
**Version:** 1.0.0  
**License:** [MIT](LICENSE.md)

---

## 1. Introduction

In cybersecurity, one of the most critical vulnerabilities is the use of outdated software components (**OWASP Top 10: A06:2021**). Attackers frequently exploit systems that are merely days behind on security patches. Manually managing updates is tedious and prone to human error.

This project outlines a "Self-Healing" system for Ubuntu that automates security compliance and system maintenance. The goal is to create a workstation that automatically patches itself, cleans its own disk space, and backs up its configuration, all without manual intervention.

## 2. Features

This system is built upon four core features that work together to create a robust, automated maintenance cycle.

### Feature 1: The Kill Switch (Manual Override)

A manual override is essential for moments when immediate action is required (e.g., after a critical vulnerability is announced). This is a simple Zsh alias that chains the entire maintenance process into a single, memorable command.

```bash
# ALIAS: System Update Shortcut ("The Kill Switch")
# This alias performs 4 critical tasks in sequence:
# 1. sudo apt update: Refreshes the local list of available packages.
# 2. sudo apt full-upgrade -y: Installs all updates.
# 3. sudo apt autoremove -y: Deletes orphaned packages.
# 4. sudo apt autoclean: Wipes the local cache of downloaded package files.
alias update-all='sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean'
```

### Feature 2: The Heartbeat (Automated Patching)

The core of the "Self-Healing" concept is automation. This is achieved using the root `cron` scheduler to silently run the update script every time the system boots.

*   **Engineering Note:** A 60-second delay (`sleep 60`) is added to prevent the script from running before the network interface is active, which would cause the update to fail.

```bash
# CRON JOB: Silent Update at Startup
# @reboot: Runs once immediately after the system boots.
# sleep 60: Pauses for 60 seconds to ensure network connectivity.
# >> /var/log/auto_update.log 2>&1: Redirects all output (both standard and error) to a log file.
@reboot sleep 60 && (apt update && apt full-upgrade -y && apt autoremove -y && apt autoclean) >> /var/log/auto_update.log 2>&1
```

### Feature 3: The Memory (Audit Logging)

Automation without observability is a risk. To provide a clear audit trail, all actions performed by the automated update script are logged. To prevent the log file from consuming excessive disk space, `logrotate` is configured to manage log archives.

```
# LOGROTATE CONFIG: /etc/logrotate.d/auto_update
/var/log/auto_update.log {
    su root root
    weekly
    rotate 4
    compress
    missingok
    notifempty
    create 0644 root root
}
```

### Feature 4: The Safety Net (Disaster Recovery)

A simple Zsh function allows you to treat a configuration folder (e.g., `~/dotfiles`) as a Git repository. This enables you to snapshot your settings to a private GitHub repository with a single command, ensuring you can always restore your setup.

```bash
# FUNCTION: Backup Dotfiles to GitHub
function backup-config() {
    current_dir=$(pwd)
    cd ~/dotfiles  # Change to your configuration directory
    git add .
    git commit -m "Auto-update: $(date)"
    git push
    cd "$current_dir"
    echo "✅ Configuration backed up successfully!"
}
```

## 3. Getting Started

Follow these steps to implement the Self-Healing Ubuntu system on your machine.

### Prerequisites

*   An Ubuntu-based operating system.
*   `zsh` as your default shell.
*   `git` installed and configured.
*   Administrative (sudo) privileges.

### Installation Steps

1.  **Add the Manual Update Alias:**
    Open your Zsh configuration file (`~/.zshrc`) and add the following line:
    ```bash
    alias update-all='sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean'
    ```
    Reload your shell for the change to take effect: `source ~/.zshrc`.

2.  **Set Up the Automated Cron Job:**
    Open the root crontab for editing:
    ```bash
    sudo crontab -e
    ```
    Add the following line to the file and save it:
    ```bash
    @reboot sleep 60 && (apt update && apt full-upgrade -y && apt autoremove -y && apt autoclean) >> /var/log/auto_update.log 2>&1
    ```

3.  **Configure Log Rotation:**
    Create a new logrotate configuration file:
    ```bash
    sudo nano /etc/logrotate.d/auto_update
    ```
    Add the following content to the file and save it:
    ```
    /var/log/auto_update.log {
        su root root
        weekly
        rotate 4
        compress
        missingok
        notifempty
        create 0644 root root
    }
    ```

4.  **(Optional) Set Up Configuration Backup:**
    If you manage your dotfiles in a Git repository, add the `backup-config` function to your `~/.zshrc` file. Remember to change `~/dotfiles` to the actual path of your repository.

## 4. Usage

Once installed, you can use the following commands to manage and monitor the system:

| Command | Description |
|---|---|
| `update-all` | Manually triggers the full system update and cleaning process. |
| `tail -f /var/log/auto_update.log` | Monitors the silent update log in real-time. |
| `backup-config` | (If configured) Backs up your configuration files to your remote Git repository. |

## 5. Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## 6. License

This project is distributed under the MIT License. See `LICENSE.md` for more information.
