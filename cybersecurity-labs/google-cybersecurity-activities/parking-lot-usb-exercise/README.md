# Parking lot USB exercise
________________________________________

## Contents

The USB drive contained a mix of personal and work files, including family photos, a resume, employee shift schedules, and budget documents. These files contained Personally Identifiable Information (PII) such as contact details and work history, alongside sensitive work files like internal financial data. It is fundamentally unsafe to store sensitive work files and personal files together on a single unencrypted, portable device, as it dramatically increases the risk of a data breach that impacts both an individual's privacy and the organization's security.

## Attacker mindset

An attacker could leverage the information to launch a spear-phishing attack against Jorge or his colleagues by impersonating him, or use personal details from his resume and photos to guess passwords for critical business systems. The information on the drive could also be used to create convincing pretexts to target Jorge's relatives in sophisticated social engineering schemes. Ultimately, by exploiting this information, an attacker's goal would be to gain unauthorized access to the hospital's network, escalate privileges, and exfiltrate sensitive data.

## Risk analysis

To mitigate these types of attacks, an organization must implement layered controls. Technical controls include disabling autorun on workstations and using endpoint security software to scan all removable media for malicious software like ransomware or keyloggers. Managerial controls should include a clear policy that prohibits mixing personal and work data on unsecured devices and mandates encryption for all data in transit. Operationally, security awareness training is crucial to teach employees to report found devices immediately and understand that plugging one into a networked computer could lead to a catastrophic network-wide infection, potentially compromising sensitive patient or financial information.
