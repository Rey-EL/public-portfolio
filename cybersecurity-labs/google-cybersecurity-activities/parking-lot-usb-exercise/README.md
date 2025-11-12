# Parking lot USB exercise
________________________________________

## Activity Overview

In this activity, the goal was to assess the attack vectors of a USB drive. The exercise considered a scenario of finding a USB drive in a parking lot from both the perspective of an attacker and a target. USBs, or flash drives, are commonly used for storing and transporting data. However, some characteristics of these small, convenient devices can also introduce security risks. Threat actors frequently use USBs to deliver malicious software, damage other hardware, or even take control of devices. USB baiting is an attack in which a threat actor strategically leaves a malware USB stick for an employee to find and install to unknowingly infect a network. It relies on curious people to plug in an unfamiliar flash drive that they find.

## Scenario

As part of the security team at Rhetorical Hospital, I arrived at work one morning and found a USB stick with the hospital's logo printed on it. I brought the USB drive back to the office where the team had virtualization software installed on a workstation. This software was used to create a **sandbox**—a simulated instance of a computer that is isolated from other files and networks. This sandboxing technique is one of the only ways to safely investigate an unfamiliar USB stick because it ensures that if the drive is infected with malicious software, it cannot affect other systems.

## Contents

The USB drive belonged to Jorge Bailey, the human resource manager at Rhetorical Hospital, and contained a mix of personal and work-related files. These included family photos, pet pictures, a new hire letter, employee shift schedules, an employee budget, vacation ideas, wedding plans, and Jorge's resume. Many of these files contained Personally Identifiable Information (PII). Storing personal and sensitive work files together on such a device is unsafe.

## Attacker mindset

An attacker could have used the files on Jorge's USB drive as a distraction, potentially having staged the entire event. For example, while an unsuspecting target browsed the family photos, hidden malware could establish a backdoor into the company's systems. The sensitive information, including PII, could also be used to target Jorge or others around him. For instance, an attacker could use Jorge's resume to craft a convincing phishing email to his colleagues, or use details from the wedding plans to manipulate a relative into revealing more information.

## Risk analysis

USB baiting attacks can deliver malicious software like malware, which could infect a computer if an employee plugged in an infected device. To mitigate these risks, organizations should implement controls such as disabling Autorun, using security software, and keeping personal and business USB drives separate. It is also crucial to use passwords and encryption on USB drives and to train employees not to plug unknown USB drives into their computers, instead reporting them to IT for analysis in a **sandbox** environment.

## Key Terms

*   **USB Baiting:** An attack where a threat actor strategically leaves a malware USB stick for an employee to find and install to unknowingly infect a network.
*   **Attack Vectors:** The means by which an attacker can gain access to a computer or network.
*   **Malware:** Malicious software that can infect computers.
*   **PII (Personally Identifiable Information):** Sensitive information that can be used to target a data owner or others around them.
*   **Sandboxing:** The practice of running software in an isolated environment (a "sandbox") to safely observe its behavior without affecting the main system.
*   **Virtualization Software:** Software used to create a simulated instance of a computer, often for sandboxing purposes.
*   **Autorun:** A feature that causes removable media to open automatically when inserted.
*   **Encryption:** A security feature used to protect data on a USB drive.

## Reflection

This activity highlighted the importance of understanding attack vectors related to removable media. Analyzing the scenario demonstrated how a seemingly innocent object like a lost USB drive can represent a security risk. It reinforced the concept that security is not just about technical controls, but also about user awareness and having established procedures for handling such incidents, like using a **sandbox** for analysis. The exercise served as a valuable reminder of the adversarial mindset needed in cybersecurity to anticipate and mitigate potential threats.

---

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to enhance the lab, please feel free to open an issue or submit a pull request.