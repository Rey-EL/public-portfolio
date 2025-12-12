# Google Cybersecurity Certificate Labs

This repository contains a collection of scenario-based projects, labs, and activities completed as part of the **Google Cybersecurity Certificate program**.

The purpose of this portfolio is to demonstrate the practical application of cybersecurity principles and tools in realistic scenarios. Each project is self-contained in its own directory and includes a detailed `README.md` explaining its objectives, the methodology used, and the skills demonstrated.

## Projects

*   **[Vulnerability Assessment for a Small Business](./vulnerability-assessment-activity/README.md)**
    *   **Objective:** Analyzed a scenario involving a critical vulnerability for a small e-commerce business: a publicly accessible database server containing sensitive customer information.
    *   **Process:** The analysis applied the NIST SP 800-30 Rev. 1 framework to perform a formal risk assessment. This involved identifying potential threat actors, analyzing the likelihood and impact of threat events like data exfiltration, and calculating a risk score for each scenario.
    *   **Outcome:** The outcome was a professional report suitable for stakeholders with a clear "defense-in-depth" remediation plan. Key recommendations included network segmentation (placing the server behind a firewall), enforcing secure access via a VPN with MFA, and implementing a robust AAA framework to apply the principle of least privilege. This project demonstrates a strong ability to translate technical risks into business impact and provide actionable, layered security solutions.

*   **[Data Leak Incident Report & Remediation](../google-data-leak-incident-activity/README.md)**
    *   **Objective:** Analyzed a data leak scenario where confidential business plans were accidentally shared on social media by an external partner, resulting in a formal report for stakeholders.
    *   **Process:** The analysis deconstructed the incident to identify the root causes: a manager's failure to revoke temporary folder access and a team member's error in sharing the wrong link. The analysis and recommendations were structured around the NIST framework, specifically citing the failure to enforce AC-6 (Least Privilege).
    *   **Outcome:** The result was a detailed incident report that recommended specific, technical control enhancements. The primary recommendations were to implement automated access revocation for temporary shares and enforce strict Role-Based Access Control (RBAC) to limit access to sensitive data. This project showcases the ability to conduct a thorough incident post-mortem and produce a professional, actionable report based on industry-standard frameworks.

*   **[SQL for Security Investigations](../google-sql-filtering-lab/README.md)**
    *   **Objective:** Analyzed a scenario that required using SQL to query a simulated employee database to perform security-related tasks, such as threat hunting and data auditing.
    *   **Process:** The exercise involved writing a series of SQL queries using `WHERE` clauses with `AND`, `OR`, and `NOT` operators. The queries were designed to answer specific investigative questions, such as: "Identify all failed login attempts that occurred outside of business hours" or "Retrieve all login activity from a specific date range."
    *   **Outcome:** The queries successfully filtered the database to isolate suspicious login patterns and audit user activity. This project demonstrates knowledge of practical SQL skills for security analysis and highlights an awareness of related vulnerabilities like SQL Injection.

*   **[Linux File Permission Hardening](../linux-least-privilege-lab/README.md)**
    *   **Objective:** Analyzed a scenario involving a security audit of a user's project directory in a Linux environment to identify permission misconfigurations and enforce the Principle of Least Privilege.
    *   **Process:** The process involved assessing file permissions with `ls -la`, which uncovered several issues including a world-writable file, and outlining the systematic remediation for each finding using the `chmod` command with both symbolic and numeric modes.
    *   **Outcome:** The analysis demonstrated how to secure the project directory by correcting all permission flaws, mitigating the risk of unauthorized access and modification. This project demonstrates knowledge of core Linux security administration skills, including file system auditing and access control management.

*   **[Parking Lot USB Baiting Analysis](./parking-lot-usb-exercise/README.md)**
    *   **Objective:** Analyzed a simulated USB baiting incident from both an attacker's and a defender's perspective, involving a lost USB drive from a hospital's HR manager.
    *   **Process:** The analysis outlined the secure procedure for handling such an incident, emphasizing the use of a sandboxed environment (virtualization) to inspect the drive's contents without risking infection of the host system.
    *   **Outcome:** Articulated the potential attack vectors an adversary could exploit, such as using the PII for social engineering or embedding hidden malware. This exercise showcases a strong understanding of threat analysis, secure handling procedures for unknown media, and the importance of employee awareness training.

*   **[Access Control Remediation Plan](./completed-access-control-worksheet.md)**
    *   **Objective:** Analyzed a scenario involving an anomalous access event log to identify and resolve an authorization issue.
    *   **Process:** The analysis of the event log showed a former employee, whose contract ended years prior, accessing the system. The investigation revealed that the user's account was never deactivated and retained full 'Admin' privileges, uncovering a systemic issue of over-provisioned access.
    *   **Outcome:** The analysis resulted in a clear remediation plan recommending: 1) A formal off-boarding process. 2) The implementation of Role-Based Access Control (RBAC) to enforce the principle of least privilege. 3) Regular user access reviews. This demonstrates the ability to diagnose security failures from logs and prescribe specific, effective controls.

*   **[Data Leak Incident Analysis](./completed-data-leak-worksheet.md)**
    *   **Objective:** Performed a post-mortem analysis of a simulated data leak incident where a sensitive internal folder was accidentally shared publicly by a business partner.
    *   **Process:** The analysis traced the incident to its root causes: a manager failing to revoke access after a meeting and a sales representative sharing the wrong link. The analysis was framed using the NIST Cybersecurity Framework (Protect Function) and specifically referenced NIST SP 800-53: AC-6 (Least Privilege).
    *   **Outcome:** The analysis resulted in recommendations for two key controls to prevent future incidents: 1) Automatically revoking access to sensitive information after a set period. 2) Implementing strict role-based access controls (RBAC). This project demonstrates the ability to deconstruct a security incident and propose targeted, preventative controls based on a recognized framework (NIST).

*   **[Ransomware Incident Handler's Journal](./incident-handler-journal.md)**
    *   **Objective:** Documented and analyzed a simulated ransomware attack on a small healthcare clinic to practice foundational incident response procedures.
    *   **Process:** Applied the "5 W's" (Who, What, When, Where, Why) framework to structure the incident report. The analysis identified the attack vector as a phishing email, detailed the impact (file encryption, operational shutdown), and attributed the event to a known threat actor group targeting the healthcare sector.
    *   **Outcome:** The journal entry serves as a concise incident report, highlighting the root cause (employee error) and articulating the critical need for both technical controls (e.g., email filtering, endpoint protection) and non-technical controls (e.g., employee security awareness training, robust backup and recovery plans). This project demonstrates a methodical approach to incident documentation and the ability to derive strategic security recommendations from a tactical event.

---

## Security Context

The labs and activities within this repository emphasize fundamental cybersecurity principles that are crucial for mitigating common vulnerabilities, including those outlined in the OWASP Top 10. By applying secure design, robust configurations, and continuous monitoring, the practices demonstrated here contribute to building more resilient and secure systems.

---

## License

This project is licensed under the [MIT License](./LICENSE.md) - see the LICENSE.md file for details.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug reports, or want to add new features, please feel free to open an issue or submit a pull request.
