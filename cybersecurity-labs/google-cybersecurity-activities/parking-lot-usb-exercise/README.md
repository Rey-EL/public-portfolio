# Parking lot USB exercise
________________________________________

## Activity Overview: Understanding USB Baiting and Attack Vectors

This activity served as a practical exploration into the significant cybersecurity threat known as **USB baiting**. USB baiting is a social engineering attack where malicious actors intentionally leave infected USB drives in public places, hoping curious individuals will plug them into their computers. The inherent convenience of USB drives for data storage and transfer also makes them a potent vector for delivering malware, damaging hardware, or gaining unauthorized control over systems. This exercise was designed to assess these attack vectors by examining a simulated scenario from both the perspective of a potential attacker and a cybersecurity defender. It highlighted how easily an organization's security can be compromised through human curiosity and the critical need for robust defensive strategies.

## Scenario

As part of the security team at Rhetorical Hospital, I arrived at work one morning and found a USB stick with the hospital's logo printed on it on the ground of the parking lot. There was no one else around who might have dropped it, so I decided to pick it up out of curiosity. I brought the USB drive back to the office where the team had virtualization software installed on a workstation. Virtualization software was used for this purpose because it is one of the only ways to safely investigate an unfamiliar USB stick. The software worked by running a simulated instance of the computer on the same workstation. This simulation was not connected to other files or networks, so the USB drive could not affect other systems if it happened to be infected with malicious software.

## Contents

The USB drive contained a mix of personal and work files, including family photos, a resume, employee shift schedules, and budget documents. These files contained Personally Identifiable Information (PII) such as contact details and work history, alongside sensitive work files like internal financial data. It was fundamentally unsafe to store sensitive work files and personal files together on a single unencrypted, portable device, as it dramatically increased the risk of a data breach that impacts both an individual's privacy and the organization's security.

## Attacker mindset

An attacker could have leveraged the information to launch a spear-phishing attack against Jorge or his colleagues by impersonating him, or used personal details from his resume and photos to guess passwords for critical business systems. The information on the drive could also have been used to create convincing pretexts to target Jorge's relatives in sophisticated social engineering schemes. Ultimately, by exploiting this information, an attacker's goal would have been to gain unauthorized access to the hospital's network, escalate privileges, and exfiltrate sensitive data.

## Risk analysis

To mitigate these types of attacks, an organization must implement layered controls. Technical controls include disabling autorun on workstations and using endpoint security software to scan all removable media for malicious software like ransomware or keyloggers. Managerial controls should include a clear policy that prohibits mixing personal and work data on unsecured devices and mandates encryption for all data in transit. Operationally, security awareness training is crucial to teach employees to report found devices immediately and understand that plugging one into a networked computer could lead to a catastrophic network-wide infection, potentially compromising sensitive patient or financial information.

## Reflection

This activity showed how USB baiting works and why it is a serious security risk. I learned how to safely inspect a USB drive using virtualization software, which acted as a sandbox to protect the system. I also saw how attackers might use the files to target people or systems. The exercise supported key lessons from the Google Cybersecurity Certificate, including how to protect data, recognize attack methods, and respond to real threats.