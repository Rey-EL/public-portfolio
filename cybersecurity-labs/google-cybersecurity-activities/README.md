# Google Cybersecurity Certificate Labs

This repository contains a collection of scenario-based projects, labs, and activities completed as part of the **Google Cybersecurity Certificate program**.

The purpose of this portfolio is to demonstrate the practical application of cybersecurity principles and tools in realistic scenarios. Each project is self-contained in its own directory and includes a detailed `README.md` explaining its objectives, the methodology used, and the skills demonstrated.

## Projects

*   **[Vulnerability Assessment for a Small Business](./vulnerability-assessment-activity/README.md)**
    *   **Scenario:** An e-commerce company has a database server containing customer information that has been openly accessible to the public internet for three years to support a global remote workforce.
    *   **Task:** Analyzed this critical vulnerability by applying the NIST SP 800-30 Rev. 1 framework to conduct a formal risk assessment. The analysis involved identifying threat actors, evaluating the likelihood and impact of data exfiltration, and calculating risk scores.
    *   **Outcome:** The analysis produced a professional report for stakeholders with a clear "defense-in-depth" remediation plan. Key recommendations included network segmentation, enforcing secure access via a VPN with MFA, and implementing a robust AAA framework. This demonstrates the ability to translate a technical vulnerability into a business-impact assessment and provide actionable security solutions.

*   **[Data Leak Incident Report & Remediation](../google-data-leak-incident-activity/README.md)**
    *   **Scenario:** A sales manager at an educational tech company gave a team member temporary access to a folder with confidential business plans. The manager forgot to revoke access, and the team member later accidentally shared the folder with an external partner, who then posted the link on social media.
    *   **Task:** Analyzed the data leak scenario to produce a formal report for stakeholders. The analysis deconstructed the incident to identify root causes (human error, lack of access control) and structured recommendations around the NIST framework, specifically citing the failure to enforce AC-6 (Least Privilege).
    *   **Outcome:** The resulting incident report recommended specific technical controls, including automated access revocation for temporary shares and the enforcement of strict Role-Based Access Control (RBAC). This showcases the ability to conduct a thorough incident post-mortem and produce a professional, actionable report based on industry-standard frameworks.

*   **[SQL for Security Investigations](../google-sql-filtering-lab/README.md)**
    *   **Scenario:** A security analyst needs to investigate potential security incidents by querying a database of employee records and login attempts.
    *   **Task:** The exercise involved writing a series of SQL queries to filter the database for specific, security-relevant information. Queries were designed to answer investigative questions like, "Identify all failed login attempts outside of business hours" or "Retrieve all login activity from a specific date range" to hunt for threats and audit user activity.
    *   **Outcome:** The analysis demonstrates how to use SQL with `WHERE`, `AND`, `OR`, and `NOT` clauses to successfully isolate suspicious login patterns. This project demonstrates knowledge of practical SQL skills for security analysis and an awareness of related vulnerabilities like SQL Injection.

*   **[Linux File Permission Hardening](../linux-least-privilege-lab/README.md)**
    *   **Scenario:** A security audit of a user's project directory in a Linux environment reveals several permission misconfigurations that violate the Principle of Least Privilege, including world-writable files and directories with excessive group permissions.
    *   **Task:** The analysis involved identifying the insecure permissions using `ls -la` and outlining the systematic remediation for each finding. The correct, secure permissions were defined using the `chmod` command in both symbolic and numeric modes.
    *   **Outcome:** The analysis demonstrated how to harden the project directory by correcting all permission flaws, mitigating the risk of unauthorized access. This project demonstrates knowledge of core Linux security administration skills, including file system auditing and access control management.

*   **[Parking Lot USB Baiting Analysis](./parking-lot-usb-exercise/README.md)**
    *   **Scenario:** A security team member at a hospital finds a lost USB stick in the parking lot with the hospital's logo printed on it.
    *   **Task:** Analyzed the simulated USB baiting incident from both an attacker's and a defender's perspective. The analysis outlined the secure procedure for handling the device, emphasizing the use of a sandboxed environment (virtualization) to inspect its contents, which included sensitive PII.
    *   **Outcome:** The analysis articulated the potential attack vectors an adversary could exploit, such as social engineering or hidden malware. This exercise showcases a strong understanding of threat analysis, secure handling procedures for unknown media, and the importance of employee awareness training.

*   **[Access Control Remediation Plan](./completed-access-control-worksheet.md)**
    *   **Scenario:** An anomalous event log shows that a former Legal Attorney, whose contract ended three years prior, successfully accessed the system.
    *   **Task:** Analyzed the event log to identify the authorization issue. The analysis revealed that the user's account was never deactivated and still retained full 'Admin' privileges, uncovering a systemic failure in off-boarding and access control.
    *   **Outcome:** The analysis resulted in a clear remediation plan recommending: 1) A formal off-boarding process, 2) The implementation of Role-Based Access Control (RBAC), and 3) Regular user access reviews. This demonstrates the ability to diagnose security failures from logs and prescribe specific, effective controls.

*   **[Data Leak Incident Analysis](./completed-data-leak-worksheet.md)**
    *   **Scenario:** A sales manager shared a folder of internal-only documents with their team. The manager did not revoke access, and a team member later accidentally shared the folder with a business partner, who posted it on social media.
    *   **Task:** Performed a post-mortem analysis of the simulated data leak. The analysis traced the incident to its root causes (failure to revoke access, lack of link verification) and framed the issue using the NIST Cybersecurity Framework, referencing NIST SP 800-53: AC-6 (Least Privilege).
    *   **Outcome:** The analysis resulted in recommendations for two key controls: automatically revoking access after a set period and implementing strict role-based access controls (RBAC). This demonstrates the ability to deconstruct a security incident and propose targeted, preventative controls based on a recognized framework.

*   **[Ransomware Incident Handler's Journal](./incident-handler-journal.md)**
    *   **Scenario:** A small U.S. healthcare clinic was hit by a ransomware attack initiated by a phishing email. The attack encrypted critical files, including medical records, and led to a complete shutdown of business operations.
    *   **Task:** Documented and analyzed the simulated ransomware attack using the "5 W's" framework. The analysis identified the attack vector, detailed the impact, and attributed the event to a known threat actor.
    *   **Outcome:** The resulting journal entry serves as a concise incident report, highlighting the root cause (employee error) and articulating the critical need for both technical (email filtering, backups) and non-technical (security awareness training) controls. This demonstrates a methodical approach to incident documentation and deriving strategic recommendations from a tactical event.

---

## Security Context

The labs and activities within this repository emphasize fundamental cybersecurity principles that are crucial for mitigating common vulnerabilities, including those outlined in the OWASP Top 10. By applying secure design, robust configurations, and continuous monitoring, the practices demonstrated here contribute to building more resilient and secure systems.

---

## License

This project is licensed under the [MIT License](./LICENSE.md) - see the LICENSE.md file for details.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug reports, or want to add new features, please feel free to open an issue or submit a pull request.
