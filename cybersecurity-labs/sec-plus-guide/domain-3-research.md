# Domain 3: Security Architecture

## 3.1 Architecture Models

### On-Premises vs. Cloud Security Architecture

**What is it?**

*   **On-premises security architecture** refers to IT resources and systems, including hardware, software, networking, and security measures, that are hosted and managed internally by an organization, typically within its own physical facilities.
*   **Cloud security architecture** encompasses all hardware, software, and infrastructure designed to protect data, workloads, and systems within cloud platforms.

**Who is responsible?**

*   In an **on-premises** model, the organization's IT team is solely responsible for all aspects of security.
*   For **cloud security**, a shared responsibility model is typically followed. The cloud provider handles the security *of* the cloud, while the customer is responsible for security *in* the cloud.

**Where is the infrastructure and data located?**

*   With **on-premises** security, servers and data are housed on-site.
*   In **cloud security**, computing relies on remote data centers that may span multiple regions.

**When are these architectures chosen?**

*   **On-premises** solutions are often chosen by organizations that handle highly sensitive data or need to adhere to strict regulatory requirements.
*   **Cloud security** is increasingly adopted by businesses seeking scalability, flexibility, and cost-effectiveness.

**Why choose one over the other?**

*   **On-premises advantages** include a higher degree of control over data and infrastructure.
*   **On-premises disadvantages** include significant upfront capital investment and limited scalability.
*   **Cloud security advantages** include scalability, flexibility, and a pay-as-you-go model.
*   **Cloud security disadvantages** include entrusting data to a third party and potential for high costs with large workloads.

**How is security implemented?**

*   In **on-premises** environments, security implementation involves managing all hardware, software, and networking internally.
*   **Cloud security** implementation involves a framework of technologies and practices to protect cloud-based systems, such as Identity and Access Management (IAM), encryption, and secure configurations.

### Virtualization Security Architecture

**Benefits:**

*   **Cost-effectiveness:** Generally cheaper to implement and maintain than hardware-based solutions.
*   **Flexibility and Agility:** Security functions can follow workloads as they migrate.
*   **Operational Efficiency:** Quicker and easier to deploy than hardware-based security.
*   **Enhanced Security and Isolation:** VM isolation, application isolation, and micro-segmentation enhance security.
*   **Better Data Protection and Disaster Recovery:** Snapshots and quick restoration on different hardware.
*   **Regulatory Compliance:** Can help meet compliance requirements in virtual and cloud environments.

**Risks:**

*   **Increased Complexity:** Adds layers of software and configurations, increasing the attack surface.
*   **VM Sprawl:** Unmanaged and unpatched VMs can become vulnerabilities.
*   **Malware and Ransomware Attacks:** Can spread across the entire virtual infrastructure.
*   **Network Misconfigurations:** Can create security holes.
*   **Security of Offline Virtual Machines:** May lack the latest security updates.
*   **Hypervisor Vulnerabilities:** A breach in the hypervisor can compromise all VMs.
*   **Unauthorized Access:** Requires strong access controls.
*   **Guest Hopping and Hijacking:** An attacker can move from one compromised VM to another.
*   **Man-in-the-Middle Attacks:** VM migrations can be vulnerable.

### IoT Security Architecture

**Best Practices:**

*   **Endpoint Protection:** Hardening individual IoT devices.
*   **Gateway Security:** Implementing security at the network edge.
*   **Secure Cloud API:** Protecting communication interfaces.
*   **Secure Network Design:** Robust access controls, firewalls, and monitoring.
*   **Data Encryption:** Encrypting data in transit and at rest.
*   **Protected Data Storage:** Secure storage of IoT-generated data.
*   **Secure Boot and Firmware Validation:** Ensuring only authorized firmware can execute.
*   **Zero Trust Architecture:** "Never trust, always verify."
*   **Multi-Factor Authentication (MFA):** Additional layers of security.
*   **Network Segmentation and Isolation:** Limiting the impact of breaches.
*   **Secure Device Provisioning and Identity Binding:** Assigning unique, verifiable identities to devices.
*   **Secure Firmware Management and Patch Governance:** Regular and secure updates.
*   **Continuous Vulnerability Assessment and Penetration Testing:** Proactively identifying weaknesses.
*   **Security by Design:** Integrating security from the initial design phase.
*   **Strong, Unique Passwords:** Enforcing complex and unique passwords.
*   **Monitoring and Management:** Remotely monitoring device fleets.
*   **Public Key Infrastructure (PKI) and Digital Certificates:** Securing connections and establishing device identities.

### ICS Security Architecture

**Design and Implementation:**

*   **Defense-in-Depth:** A multi-layered security approach.
*   **Network Segmentation and Segregation:** Strict separation of ICS and IT networks.
*   **Zero Trust Architecture:** Assuming threats can originate from inside and outside the network.
*   **Access Control and Authentication:** Implementing Role-Based Access Control (RBAC) and Multi-Factor Authentication (MFA).
*   **Secure Communication:** Utilizing secure protocols and encryption.
*   **Vulnerability Management and Patching:** Regularly identifying and applying security updates.
*   **Monitoring and Incident Response:** Continuous monitoring and well-defined incident response plans.
*   **Asset Management:** Maintaining a comprehensive inventory of all assets.
*   **Configuration Management:** Enforcing secure configurations.
*   **Compliance with Standards:** Adhering to standards like NIST SP 800-82 and ISA/IEC 62443.
*   **Training and Awareness:** Specialized cybersecurity training for all personnel.

### Infrastructure as Code (IaC) Security

**Risks:**

*   **Misconfigurations:** Errors in IaC templates can lead to security vulnerabilities.
*   **Hardcoded Secrets:** Embedding sensitive information in IaC files.
*   **Overly Permissive Access Controls:** Creating unnecessary privilege escalation opportunities.
*   **Configuration Drift:** Manual changes leading to inconsistencies.
*   **Vulnerable Dependencies:** Outdated or unverified third-party modules.

**Mitigation:**

*   **Implement Secure Coding Practices:** Avoid hardcoding secrets and apply the principle of least privilege.
*   **Automate Security Scanning and Policy Enforcement:** Integrate static analysis tools into CI/CD pipelines.
*   **Leverage Version Control and Change Management:** Track all changes and implement peer review workflows.
*   **Implement Continuous Monitoring and Auditing:** Detect configuration drift and unauthorized changes.
*   **Ensure Infrastructure Immutability:** Treat infrastructure as immutable once provisioned.
*   **Manage Dependencies Securely:** Regularly update and patch all components.
*   **Develop IaC-Specific Incident Response:** Create automated incident response plans.
*   **Provide Training and Education:** Educate teams on IaC security best practices.

## 3.2 Enterprise Infrastructure

### Security Principles for Enterprise Infrastructure

*   **Confidentiality, Integrity, and Availability (CIA):** The core tenets of information security.
*   **Non-repudiation, Authentication, Authorization, and Accounting (AAA):** A framework for intelligently controlling access to computer resources.
*   **Zero Trust:** A security model that requires strict verification for every person and device trying to access resources on a private network, regardless of whether they are sitting within or outside of the network perimeter.
*   **Principle of Least Privilege:** A user should only have access to the specific data, resources, and applications needed to complete a required task.
*   **Attack Surface Reduction:** Minimizing the number of attack vectors.
*   **Secure Connectivity:** Ensuring that all connections to and from the network are secure.
*   **Managing Failure Modes (Fail-Open/Fail-Closed):** Determining the state of a system in the event of a failure.

### Control Selection for Enterprise Security

**What:** Choosing and implementing appropriate security controls to protect an organization's assets.

**Why:** To mitigate identified risks and achieve a desired security posture.

**Who:** Security architects, engineers, risk managers, compliance officers, and IT administrators.

**When:** An ongoing process throughout the lifecycle of a security program.

**Where:** Across all layers of an enterprise's infrastructure.

**How:**
1.  **Risk Assessment:** Identifying threats and vulnerabilities.
2.  **Control Identification:** Researching potential security controls.
3.  **Control Evaluation:** Assessing the effectiveness, feasibility, and cost of controls.
4.  **Control Selection:** Choosing the most appropriate controls.
5.  **Implementation:** Deploying the selected controls.
6.  **Monitoring and Review:** Continuously monitoring the effectiveness of controls.

### Secure Communication Protocols in Enterprise Networks

*   **SSL/TLS (Secure Sockets Layer/Transport Layer Security):** Establishes encrypted connections for web traffic.
*   **HTTPS (Hypertext Transfer Protocol Secure):** The secure version of HTTP, using SSL/TLS.
*   **IPsec (Internet Protocol Security):** Secures data at the network layer, often used for VPNs.
*   **SSH (Secure Shell):** Enables secure remote login connections and file transfers.
*   **SFTP (SSH File Transfer Protocol):** A secure protocol for transferring files, leveraging SSH.
*   **SNMPv3 (Simple Network Management Protocol version 3):** Provides security features for network management.
*   **WPA/WPA2/WPA3 (Wi-Fi Protected Access):** Security protocols for wireless networks.

## 3.3 Data Protection

### Data Types in Cybersecurity

*   **Personally Identifiable Information (PII):** Data that can identify an individual.
*   **Protected Health Information (PHI):** Health status, medical conditions, and treatment information.
*   **Financial Information:** Bank account details, credit card numbers, and tax filings.
*   **Business Sensitive Information:** Trade secrets, proprietary processes, and strategic plans.
*   **Credential Data:** Usernames, passwords, and PINs.
*   **Government Information:** Classified government data.

### Data Securing Methods

*   **Encryption:** Converting sensitive information into a coded, unreadable format.
*   **Access Control:** Restricting who can access sensitive data.
*   **Backup and Recovery:** Creating copies of data to protect against loss.
*   **Network Security:** Protecting data and assets on computer networks.
*   **Physical Security:** Safeguarding the physical devices and facilities where data is stored.
*   **Data Loss Prevention (DLP):** Detecting and preventing sensitive data from being transmitted outside the organization's control.
*   **Data Masking and Tokenization:** Replacing sensitive data elements with non-sensitive substitutes.
*   **Security Awareness Training:** Educating employees on best practices.
*   **Endpoint Security:** Protecting devices such as computers, smartphones, and tablets.
*   **Secure Disposal:** Ensuring that all personal data is completely removed from old IT equipment.

### Data Classification Levels and Standards

*   **Public:** Data that can be openly shared without causing harm.
*   **Internal/Internal Use Only:** Data meant for internal organizational use.
*   **Confidential:** Sensitive information that could cause harm to the organization or its customers if disclosed.
*   **Restricted/Highly Confidential:** The most sensitive information requiring the highest level of security.

## 3.4 Resilience and Recovery

### High Availability and Disaster Recovery

*   **High Availability (HA):** The ability of a system or service to remain operational with minimal downtime.
*   **Disaster Recovery (DR):** A comprehensive strategy focused on restoring IT services after a major disruption.

**Key Differences:** HA is a preventative approach, while DR is a corrective approach.

### Disaster Recovery Site Considerations

*   **Cold Sites:** Basic facilities with essential utilities but no pre-installed hardware or software.
*   **Warm Sites:** Contain some hardware, software, and communication equipment, but may require additional setup.
*   **Hot Sites:** Fully equipped, functional replicas of the primary site, allowing for near-instant failover.
*   **Mobile Sites:** Trailers that can be deployed to specific locations.
*   **Cloud-based Recovery Sites (DRaaS):** Leverage cloud infrastructure to minimize the need for physical data centers.

### Disaster Recovery Testing Types

*   **Plan Review/Checklist Test:** A preliminary review of the DR plan.
*   **Tabletop Exercise:** A discussion-based test where stakeholders walk through the plan.
*   **Walk-Through Testing:** Physically following the protocols outlined in the DR plan.
*   **Simulation Test:** Simulating a specific disaster scenario in a controlled environment.
*   **Parallel Testing:** Creating and running duplicate recovery systems alongside production systems.
*   **Full Interruption/Full-Scale Testing:** Shutting down primary systems and executing recovery processes on real production data and equipment.
*   **Sandbox Testing:** Testing in an isolated, partitioned virtual machine environment.

### Backup Strategies for Business Continuity

*   **3-2-1-1-0 Backup Rule:** Maintain three copies of data, on two different types of media, with one copy stored off-site, one copy being immutable, and zero backup errors.
*   **Define RPO and RTO:** Establish clear Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO).
*   **Regular Testing:** Regularly test backups to verify their integrity and functionality.
*   **Diverse Backup Types:** Utilize a combination of full, incremental, and differential backups.
*   **Hybrid Solutions:** Employ a mix of cloud and local backup solutions.
*   **Security Measures:** Encrypt backup data and implement robust access controls.
*   **Data Prioritization:** Identify and prioritize critical data for backup.
*   **Automation:** Implement automated backup solutions.
*   **Comprehensive Documentation:** Maintain detailed records of all backup procedures.
*   **Business Impact Analysis (BIA):** Conduct a BIA to identify critical business functions.
*   **Incident Response Planning:** Develop a clear incident response plan.
*   **Continuous Improvement:** Regularly review and update backup strategies.
