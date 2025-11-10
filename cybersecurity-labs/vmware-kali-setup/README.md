# VMware Workstation and Kali Linux Setup (Windows Host)

## Overview

This document details the step-by-step process of installing VMware Workstation Pro on a Windows 11 Pro host system and subsequently setting up a Kali Linux virtual machine using a pre-built VMware image. This lab demonstrates proficiency in virtualization software installation, virtual machine deployment, and basic system preparation for cybersecurity-focused environments on a Windows host.

## Installation Steps

### 1. Download Verification (on Windows Host)

Ensured the necessary files were downloaded and present on the Windows host system:
*   `VMware-Workstation-Full-25H2-XXXXXX.exe` (Windows installer for VMware Workstation Pro)
*   `kali-linux-2025.3-vmware-amd64.7z`

### 2. Install VMware Workstation Pro on Windows

The VMware Workstation Pro installer for Windows was executed on the Windows 11 Pro host.

#### 2.1 Run the installer:
*   Located the downloaded `.exe` file (e.g., `VMware-Workstation-Full-25H2-XXXXXX.exe`).
*   Double-clicked the `.exe` file to start the installation.
*   Followed the on-screen prompts, accepting license agreements, choosing installation options, and completing the setup. A system restart may have been required.

### 3. Extract Kali Linux VMware Image on Windows

The Kali Linux VMware image, provided as a 7z archive, was extracted on the Windows host.

#### 3.1 Install 7-Zip (if not already installed on Windows):
*   Downloaded and installed 7-Zip from `www.7-zip.org` on the Windows host.

#### 3.2 Extract the Kali Linux VMware image:
*   Located the `kali-linux-2025.3-vmware-amd64.7z` file on the Windows host.
*   Right-clicked the file and used 7-Zip to "Extract Here" or "Extract to kali-linux-2025.3-vmware-amd64\" into a chosen directory (e.g., `C:\VMs\Kali-Linux`).

### 4. Open Kali Linux in VMware Workstation Pro (Windows)

#### 4.1 Launch VMware Workstation Pro:
*   Opened VMware Workstation Pro from the Windows Start Menu.

#### 4.2 Open the Virtual Machine:
*   In VMware Workstation Pro, navigated to `File` -> `Open...`.
*   Browsed to the folder where the Kali Linux files were extracted (e.g., `C:\VMs\Kali-Linux`).
*   Selected the `.vmx` file (e.g., `Kali-Linux-2025.3-vmware-amd64.vmx`) and clicked `Open`.

#### 4.3 Power on the Virtual Machine:
*   With the Kali Linux virtual machine loaded, clicked the "Power on this virtual machine" button.
*   Logged into Kali Linux using default credentials (typically `kali`/`kali`).

## Conclusion

This lab successfully demonstrates the process of setting up a virtualized environment with VMware Workstation Pro on a Windows host and deploying a Kali Linux virtual machine. This setup provides a robust platform for cybersecurity training, penetration testing, and other security-related activities.

## License
This project is licensed under the MIT License - see the [LICENSE.md](../../LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to enhance this documentation, please feel free to open an issue or submit a pull request.
