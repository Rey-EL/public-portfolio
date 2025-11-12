# Cybersecurity Lab: The Parking Lot USB Drop

## 1. Overview

This document details a hands-on lab exercise simulating a common physical security threat: the discovery of a potentially malicious USB drive. The objective of this exercise was to apply proper security protocols to investigate an unknown storage device in a controlled environment, analyze its contents, and assess the potential risks from both a defensive and an offensive security perspective.

This exercise is a practical application of the concepts covered in the Google Cybersecurity Certificate, demonstrating the ability to identify attack vectors, utilize sandboxing environments, and analyze potential social engineering tactics.

## 2. Scenario

As a member of the security team at a fictional organization, "Rhetorical Hospital," I discovered a USB stick on the ground in the employee parking lot. The device was branded with the hospital's logo, suggesting it might belong to a colleague and contain work-related files. With no one nearby to claim it, I followed security protocols by taking the device for analysis rather than leaving it or plugging it into a networked workstation.

## 3. Objective

The primary goal was to safely determine the nature of the USB drive and its contents without exposing any hospital systems to potential malware. This involved:
-   **Safely accessing the device:** Using a secure, isolated environment to prevent any potential malware from executing on a live system.
-   **Analyzing the contents:** Identifying the types of files stored on the drive.
-   **Assessing the risk:** Evaluating the potential security threats posed by the files, whether the USB drop was accidental or a deliberate "USB baiting" attack.

## 4. Methodology: The Virtualized Sandbox

To safely inspect the USB drive, I utilized a **virtualization software** installed on a dedicated workstation. This created a sandboxed environment—a simulated computer instance completely isolated from the hospital's network and the host machine's file system.

This approach ensured that if the USB drive contained any malicious software (e.g., ransomware, keyloggers, remote access trojans), it would be confined within the virtual machine, preventing it from infecting the host computer or spreading across the network.

## 5. Findings: A Mix of Personal and Professional Data

Upon mounting the USB drive within the sandboxed environment, I discovered a combination of personal and work-related files belonging to a fictional employee named "Jorge."

-   **Work-Related Files:** Employee shift schedules, budget documents, and a new hire letter.
-   **Personal Files:** Family photos, pet pictures, wedding plans, and Jorge's resume.

The presence of both work and personal files, including Personally Identifiable Information (PII), highlights a common but risky behavior of commingling data on a single, portable device.

## 6. Attacker's Perspective: Exploiting the Find

From an attacker's point of view, this USB drive is a treasure trove of information that can be used for social engineering and other attacks:

-   **Spear Phishing:** Jorge's resume reveals his job title, contact information, and work history. An attacker could use this to craft highly convincing phishing emails, either impersonating Jorge to target other employees or targeting Jorge himself with tailored lures.
-   **Password Guessing & Pretexting:** The personal files (wedding plans, pet photos) provide clues that could be used to guess passwords or answer security questions. They also offer material for pretexting—creating a believable story to manipulate Jorge or his family.
-   **USB Baiting Attack:** If the USB drive was intentionally left by a threat actor, its seemingly harmless contents would serve as a distraction. While the finder browses through the files, hidden malware could be silently installing in the background, establishing a foothold on the system and, potentially, the entire network.

## 7. Risk Analysis and Mitigation Strategies

The discovery of this USB drive highlights several critical security risks:

-   **Malware Delivery:** USB drives are a primary vector for delivering malware. Had this device been plugged into a standard work computer, it could have deployed ransomware, keyloggers, or other malicious payloads.
-   **Data Leakage:** The unencrypted personal and professional data on the drive constitutes a data leak, exposing sensitive information about an employee and the organization.

To mitigate these risks, organizations should implement the following technical and administrative controls:
-   **Disable Autorun/Autoplay:** Prevent devices from automatically executing files upon connection.
-   **Endpoint Security:** Utilize antivirus and anti-malware software to scan all removable media.
-   **User Training:** Educate employees about the dangers of USB baiting and the importance of not plugging unknown devices into their computers.
-   **Policy Enforcement:** Establish clear policies for data handling, including the separation of personal and work files and the encryption of sensitive data on portable media.
-   **Controlled Analysis:** As demonstrated in this exercise, all unknown devices should only be inspected by trained personnel in an isolated, virtualized environment.

## 8. Conclusion and Key Learnings

This exercise was a valuable demonstration of the "USB baiting" attack vector and the correct procedure for handling such an incident. Key takeaways include:

-   **The Importance of Sandboxing:** I learned how to use virtualization software as a critical tool for safely analyzing potential threats without risking system integrity.
-   **Adversarial Thinking:** I practiced thinking like an attacker to understand how seemingly innocuous files could be leveraged for malicious purposes.
-   **Procedural Discipline:** The scenario reinforced the importance of following established security protocols instead of acting on curiosity.

This activity directly supports the core competencies taught in the Google Cybersecurity Certificate, providing practical experience in threat identification, risk assessment, and incident response.

---

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to enhance the lab, please feel free to open an issue or submit a pull request.