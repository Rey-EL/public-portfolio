# VMware Workstation and Kali Linux Setup

## Overview

This document details the step-by-step process of installing VMware Workstation on a Linux host system and subsequently setting up a Kali Linux virtual machine using a pre-built VMware image. This lab demonstrates proficiency in virtualization software installation, virtual machine deployment, and basic system preparation for cybersecurity-focused environments.

## Installation Steps

### 1. Download Verification

Ensured the necessary files were downloaded and present in the working directory:
*   `VMware-Workstation-Full-25H2-24995812.x86_64.bundle`
*   `kali-linux-2025.3-vmware-amd64.7z`

### 2. Install VMware Workstation

The VMware Workstation installer bundle was made executable and then run with superuser privileges.

#### 2.1 Make the bundle executable:
```bash
chmod +x VMware-Workstation-Full-25H2-24995812.x86_64.bundle
```

#### 2.2 Run the installer:
```bash
sudo ./VMware-Workstation-Full-25H2-24995812.x86_64.bundle
```
The graphical installer was followed, accepting license agreements and providing necessary system credentials.

### 3. Install Kali Linux

The Kali Linux VMware image, provided as a 7z archive, was extracted and prepared for use with VMware Workstation.

#### 3.1 Install 7zip (if not already installed):
```bash
sudo apt update
sudo apt install p7zip-full
```

#### 3.2 Extract the Kali Linux VMware image:
```bash
7z x kali-linux-2025.3-vmware-amd64.7z -okali-linux-vm
```
This command extracted the virtual machine files into a new directory named `kali-linux-vm`.

#### 3.3 Open Kali Linux in VMware Workstation:
1.  Launched VMware Workstation.
2.  Navigated to `File` -> `Open...`.
3.  Selected the `.vmx` file (e.g., `Kali-Linux-2025.3-vmware-amd64.vmx`) from the `kali-linux-vm` directory.
4.  Powered on the Kali Linux virtual machine.

## Conclusion

This lab successfully demonstrates the process of setting up a virtualized environment with VMware Workstation and deploying a Kali Linux virtual machine. This setup provides a robust platform for cybersecurity training, penetration testing, and other security-related activities.

## License
This project is licensed under the MIT License - see the [LICENSE.md](../../LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to enhance this documentation, please feel free to open an issue or submit a pull request.
