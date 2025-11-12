# Parking Lot USB Exercise

## Contents

The USB drive contained a mix of personal and work files. It included family photos, pet pictures, wedding plans, Jorge’s resume, employee shift schedules, budget documents, and a new hire letter. These files contained personally identifiable information. It is not safe to store personal files with work files on the same device.

## Attacker Mindset

An attacker could use Jorge’s resume to learn his job title, contact information, and work history. This could be used to send fake emails pretending to be Jorge or to trick other employees into sharing sensitive data. The wedding plans and pet photos could help guess passwords or create fake messages aimed at Jorge’s family. If the USB was left intentionally by a threat actor, the goal may have been to get a curious person to plug it in without thinking. The mix of casual and professional files could make the USB appear harmless and keep that person focused on browsing through them, while hidden malware quietly installs in the background and gives the attacker access to the computer or the hospital’s network.

## Risk Analysis

USB drives can carry harmful software such as keyloggers, ransomware, or remote access tools. If the device had been infected and plugged into a regular computer, it could have damaged hospital systems. A threat actor could find sensitive information and use it to harm individuals or the organization. To reduce these risks, organizations should disable autorun, use security software, keep personal and business USBs separate, and inspect unknown devices only in virtual environments.

## Reflection

This activity showed how USB baiting works and why it is a serious security risk. I learned how to safely inspect a USB drive using virtualization software, which acted as a sandbox to protect the system. I also saw how attackers might use the files to target people or systems. The exercise supported key lessons from the Google Cybersecurity Certificate, including how to protect data, recognize attack methods, and respond to real threats.

---

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to enhance the lab, please feel free to open an issue or submit a pull request.
