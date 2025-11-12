# Parking lot USB exercise
________________________________________

## Activity Overview: Understanding USB Baiting and Attack Vectors

This activity served as a practical exploration into the significant cybersecurity threat known as **USB baiting**. USB baiting is a social engineering attack where malicious actors intentionally leave infected USB drives in public places, hoping curious individuals will plug them into their computers. The inherent convenience of USB drives for data storage and transfer also makes them a potent vector for delivering malware, damaging hardware, or gaining unauthorized control over systems. This exercise was designed to assess these attack vectors by examining a simulated scenario from both the perspective of a potential attacker and a cybersecurity defender. It highlighted how easily an organization's security can be compromised through human curiosity and the critical need for robust defensive strategies.

## Scenario

As part of the security team at Rhetorical Hospital, I found a USB stick with the hospital's logo on it in the parking lot. I brought the USB drive back to the office for safe analysis. To do this, I used virtualization software to create a **sandbox**, which is an isolated, simulated computer instance. This sandboxing technique is critical because it allows for the safe investigation of a suspicious device without connecting it to the hospital's network or files, preventing any potential malware from causing harm.

## Contents

The USB drive contained a mix of personal and work files, including family photos, a resume, employee shift schedules, and budget documents. These files contained Personally Identifiable Information (PII) such as contact details and work history, alongside sensitive work files like internal financial data. It was fundamentally unsafe to store sensitive work files and personal files together on a single unencrypted, portable device, as it dramatically increased the risk of a data breach that impacts both an individual's privacy and the organization's security.

## Attacker mindset

An attacker could have leveraged the information on the drive in several ways. For example, they could launch a **spear-phishing** attack by using the resume to impersonate the employee, "Jorge," and email a colleague from a fake but similar address to request a sensitive file. Personal details from photos, like a pet's name, could be used to guess passwords for business systems (e.g., "Buddy123!"). An attacker could also use details from wedding plans to create a convincing pretext, perhaps calling a relative while posing as a hospital administrator to trick them into revealing more information. The ultimate goal would be to use this initial access to infiltrate the hospital's network and steal valuable data.

## Risk analysis

To mitigate these types of attacks, an organization must implement layered controls. Technical controls include disabling autorun on workstations and using endpoint security to scan all removable media for malicious software like ransomware or keyloggers. Managerial controls should include a clear policy that prohibits mixing personal and work data on unsecured devices and mandates encryption. Operationally, security awareness training is crucial to teach employees to report found devices and to understand that the only safe way to inspect them is within a controlled **sandbox** environment, preventing a network-wide infection.

## Key Terms for the Non-Technical Reader

*   **USB Baiting:** The act of leaving an infected USB drive for someone to find and use, which then infects their computer.
*   **Attack Vector:** A path or means by which an attacker can gain access to a computer or network.
*   **Social Engineering:** The act of tricking people into giving up confidential information or taking a specific action.
*   **Spear Phishing:** A targeted email scam sent to a specific person or organization, often containing personalized information to make it seem legitimate.
*   **Sandboxing:** A security practice where a program or file is run in an isolated environment (a "sandbox") to see how it behaves without risking harm to the main system.
*   **Personally Identifiable Information (PII):** Any data that could be used to identify a specific person, such as a name, address, or phone number.

## Reflection

This activity showed how USB baiting works and why it is a serious security risk. I learned how to safely inspect a USB drive using virtualization software, which created a **sandbox** to protect the system. I also saw how attackers might use the files to target people or systems. The exercise supported key lessons from the Google Cybersecurity Certificate, including how to protect data, recognize attack methods, and respond to real threats.
