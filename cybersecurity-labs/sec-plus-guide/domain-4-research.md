# Domain 4: Security Operations

## 4.1 Computing Resources

### Secure Baselines

*   **What:** A secure baseline is a standardized level of minimum security configuration for a system or application.
*   **Who:** Security professionals, system administrators, and developers.
*   **Where:** Applied to operating systems, applications, and network devices.
*   **When:** Established during initial setup and continuously maintained.
*   **Why:** To ensure consistent security, reduce vulnerabilities, and streamline compliance.
*   **How:** Created based on industry standards and organizational needs, deployed manually or with configuration management tools, and maintained through patching and monitoring.

### Mobile Solutions Security

*   **What:** Protecting mobile devices and the data they access.
*   **Who:** IT administrators, security teams, and end-users.
*   **Where:** On the devices, networks they connect to, and applications.
*   **When:** Throughout the device lifecycle.
*   **Why:** Mobile devices are portable and susceptible to loss, theft, and attack.
*   **How:** Through Mobile Device Management (MDM) for policy enforcement (e.g., screen locks, encryption, remote wipe), and managing device models like BYOD, COPE, and CYOD.

### Hardening

*   **What:** The process of reducing a system's attack surface.
*   **Who:** System administrators and security engineers.
*   **Where:** Applied to operating systems, network devices, cloud environments, and IoT devices.
*   **When:** Immediately after installation and throughout the system's life.
*   **Why:** Default configurations are often insecure. Hardening minimizes exploitation risk.
*   **How:** Applying patches, enforcing strong passwords, using least privilege, encrypting data, and configuring firewalls and EDR.

### Wireless Security

*   **What:** Protecting wireless networks from unauthorized access and attacks.
*   **Who:** Network administrators and security professionals.
*   **Where:** Implemented on wireless access points (WAPs) and clients.
*   **When:** Continuously, whenever a wireless network is active.
*   **Why:** Wireless signals can be intercepted, making them vulnerable.
*   **How:** Using strong encryption (WPA3), authentication (802.1X with RADIUS), and conducting site surveys to find rogue access points.

### Application Security

*   **What:** Protecting software applications from threats.
*   **Who:** Developers, security analysts, and QA teams.
*   **Where:** Applies to web, mobile, and SaaS applications.
*   **When:** Throughout the entire software development lifecycle (SDLC).
*   **Why:** Applications are a primary target for attackers seeking to access sensitive data.
*   **How:** Through secure coding practices, input validation (to prevent XSS), and regular security testing.

### Sandboxing

*   **What:** Running programs in an isolated environment.
*   **Who:** Developers, security testers, and system administrators.
*   **Where:** Implemented in operating systems, browsers, and virtual environments.
*   **When:** When testing untrusted code or new applications.
*   **Why:** To prevent potentially malicious software from affecting the host system.
*   **How:** By creating a contained environment that restricts access to system resources.

### Monitoring

*   **What:** Continuously observing system, network, and application activities.
*   **Who:** Security Operations Center (SOC) analysts and IT administrators.
*   **Where:** Across all computing resources, applications, and network traffic.
*   **When:** Continuously, in real-time.
*   **Why:** For early detection of security incidents, ensuring compliance, and providing data for incident response.
*   **How:** Using Security Information and Event Management (SIEM) systems to aggregate and analyze logs, and setting up alerts for suspicious activity.

## 4.2 Asset Management

*   **What:** The process of managing the entire lifecycle of hardware, software, and data assets.
*   **Who:** IT departments, management, and asset owners.
*   **Where:** Across all departments and locations within an organization.
*   **When:** Continuously, from acquisition to disposal.
*   **Why:** To reduce risk, ensure compliance, and maintain an inventory of all assets.
*   **How:**
    *   **Acquisition:** Securely procuring assets, including vendor vetting.
    *   **Assignment:** Assigning ownership and classifying assets based on sensitivity.
    *   **Monitoring/Tracking:** Maintaining an inventory and using asset tags.
    *   **Disposal:** Securely sanitizing or destroying assets and obtaining certificates of destruction.

## 4.3 Vulnerability Management

*   **What:** The continuous process of identifying, analyzing, remediating, validating, and reporting on security vulnerabilities.
*   **Who:** Security professionals and IT administrators.
*   **Where:** Across all IT assets, including systems, networks, and applications.
*   **When:** As an ongoing, continuous process.
*   **Why:** To proactively reduce the organization's attack surface before vulnerabilities are exploited.
*   **How:**
    *   **Identify:** Using vulnerability scanners (e.g., Nessus, Qualys) and penetration testing.
    *   **Analyze:** Evaluating vulnerabilities using scoring systems like CVSS to prioritize.
    *   **Remediate:** Applying patches, making configuration changes, or implementing workarounds.
    *   **Validate:** Scanning again to confirm the fix.
    *   **Report:** Communicating findings and progress to stakeholders.

## 4.4 Alerting and Monitoring

*   **What:** The continuous observation of computing environments to detect and react to security events.
*   **Who:** Security Operations Center (SOC) teams and IT departments.
*   **Where:** Across systems, applications, and infrastructure, with data consolidated in a SIEM.
*   **When:** In real-time, continuously.
*   **Why:** To detect threats, maintain system health, ensure compliance, and provide a holistic view of the security posture.
*   **How:** Using tools like SIEMs, vulnerability scanners, DLP, and IDS/IPS to collect, aggregate, and analyze log data, and then generating alerts based on predefined rules or anomalies.

## 4.5 Enterprise Security

### Firewalls
*   **What:** A network security system that controls traffic based on rules. Next-Generation Firewalls (NGFWs) operate at the application layer, and Web Application Firewalls (WAFs) protect against web-based attacks.
*   **Who:** Network administrators and security analysts.
*   **Where:** At the network perimeter, between segments, or in front of web servers.
*   **When:** Continuously, in real-time.
*   **Why:** To prevent unauthorized access and block malicious traffic.
*   **How:** By applying rules based on IP addresses, ports, protocols, and applications.

### IDS/IPS
*   **What:** Intrusion Detection Systems (IDS) monitor for threats and alert, while Intrusion Prevention Systems (IPS) actively block them.
*   **Who:** Security analysts manage and respond to alerts.
*   **Where:** Can be network-based (NIDS/NIPS) or host-based (HIDS/HIPS).
*   **When:** Continuously, in real-time.
*   **Why:** To identify and/or prevent malicious activity and exploits.
*   **How:** Using signature-based detection (known attacks) and anomaly-based detection (behavioral).

### DNS Filtering
*   **What:** Blocking access to malicious or inappropriate websites by preventing DNS resolution.
*   **Who:** Network administrators.
*   **Where:** At the DNS server level.
*   **When:** When a user or device requests to resolve a domain name.
*   **Why:** To enforce internet usage policies and block malware communication.
*   **How:** By returning no IP address or a sinkhole address for blocked domains.

### Data Loss Prevention (DLP)
*   **What:** Tools and processes to prevent unauthorized access and transfer of sensitive data.
*   **Who:** Security teams.
*   **Where:** Across endpoints, networks, and cloud services.
*   **When:** Continuously monitors data in use, in motion, and at rest.
*   **Why:** To mitigate the risk of data exfiltration.
*   **How:** By monitoring and controlling attempts to copy, print, email, or upload sensitive data.

### Network Access Control (NAC)
*   **What:** A solution that restricts network access to compliant endpoints only.
*   **Who:** Network and security teams.
*   **Where:** At the point of network access (switches, wireless access points).
*   **When:** When a device attempts to connect to the network.
*   **Why:** To prevent unauthorized or compromised devices from accessing the network.
*   **How:** By authenticating devices and assessing their security posture before granting access.

### EDR/XDR
*   **What:** Endpoint Detection and Response (EDR) monitors endpoints, while Extended Detection and Response (XDR) integrates security data from multiple layers (endpoints, network, cloud).
*   **Who:** Security analysts.
*   **Where:** EDR is on endpoints; XDR is across the entire security stack.
*   **When:** Continuously, in real-time.
*   **Why:** To detect, investigate, and respond to advanced threats.
*   **How:** By recording activity, using behavioral analysis and machine learning to detect anomalies, and providing tools for response and remediation.

## 4.6 Identity and Access Management (IAM)

### Provisioning
*   **What:** The process of creating, managing, and deleting user accounts and their access rights.
*   **Who:** IT and HR departments.
*   **Where:** In identity management systems and applications.
*   **When:** When an employee joins, changes roles, or leaves the organization.
*   **Why:** To ensure users have the appropriate level of access based on the principle of least privilege.
*   **How:** Through automated workflows that grant or revoke access based on user roles and attributes.

### Single Sign-On (SSO)
*   **What:** An authentication scheme that allows a user to log in with a single ID and password to any of several related, yet independent, software systems.
*   **Who:** End-users.
*   **Where:** Across multiple applications and services.
*   **When:** When a user needs to access different applications.
*   **Why:** To improve user experience and centralize authentication management.
*   **How:** Using standards like SAML, OAuth, or OpenID Connect to securely exchange authentication and authorization data between an identity provider and service providers.

### Multifactor Authentication (MFA)
*   **What:** A security process that requires users to provide two or more verification factors to gain access to a resource.
*   **Who:** End-users.
*   **Where:** During the login process for applications, systems, and VPNs.
*   **When:** When a user attempts to authenticate.
*   **Why:** To add an extra layer of security beyond just a password, making it much harder for unauthorized users to gain access.
*   **How:** By combining something you know (password), something you have (phone, token), and/or something you are (biometrics).

### Privileged Access Management (PAM)
*   **What:** Tools and practices for securing, controlling, and monitoring access to an organization's critical assets.
*   **Who:** Administrators, developers, and other users with elevated permissions.
*   **Where:** For access to servers, databases, network devices, and other critical infrastructure.
*   **When:** Whenever a user needs to perform administrative tasks.
*   **Why:** To prevent misuse of privileged accounts, which are a primary target for attackers.
*   **How:** Through solutions that provide credential vaulting, session monitoring, and just-in-time access to privileged accounts.

## 4.7 Automation and Orchestration

*   **What:**
    *   **Automation:** Executing individual security tasks without manual intervention.
    *   **Orchestration:** Coordinating multiple automated tasks across different systems into a cohesive workflow.
*   **Who:** Security teams.
*   **Where:** Applied across various security domains, often managed by Security Orchestration, Automation, and Response (SOAR) platforms.
*   **When:** For tasks that are repeatable and stable.
*   **Why:** To improve efficiency, reduce human error, enhance security posture, and allow security teams to focus on more strategic work.
*   **How:** Using scripts and APIs to automate tasks like user provisioning, vulnerability scanning, and incident response actions. SOAR platforms integrate various security tools to create automated playbooks.

## 4.8 Incident Response

*   **What:** A structured methodology for managing security incidents. The phases are typically: Preparation, Detection, Analysis, Containment, Eradication, Recovery, and Post-Incident Activity (Lessons Learned).
*   **Who:** Incident response teams and other organizational stakeholders.
*   **Where:** Across the entire IT infrastructure.
*   **When:** Initiated upon detection of a security incident.
*   **Why:** To minimize the impact of incidents, restore normal operations, and prevent recurrence.
*   **How:** By following a predefined incident response plan (IRP) that outlines the steps to take during and after an incident. This includes training staff, testing the plan with exercises, performing root cause analysis, proactive threat hunting, and using digital forensics.

### Digital Forensics
*   **What:** The process of investigating digital devices to uncover evidence for legal or investigative purposes.
*   **Who:** Forensic analysts.
*   **When:** During and after an incident.
*   **Why:** To preserve the integrity of evidence and support investigations.
*   **How:** Following a process of Identification, Collection (following the order of volatility), Analysis, and Reporting. A key concept is maintaining the Chain of Custody.

## 4.9 Data Sources for Investigations

*   **What:** Using log data and other sources to support security investigations.
*   **Who:** Security analysts, incident responders, and forensic investigators.
*   **Where:** Logs originate from endpoints, network devices, applications, and cloud environments. They are often centralized in a SIEM.
*   **When:** Throughout the incident response lifecycle, as well as for proactive threat hunting.
*   **Why:** Log data provides a historical record of activity, which is crucial for detecting malicious activity, determining the scope of an incident, and performing root cause analysis.
*   **How:** By collecting, normalizing, and correlating log data from various sources to identify anomalies, match known indicators of compromise (IOCs), and reconstruct the timeline of an event.
