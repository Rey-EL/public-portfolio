# Google Cybersecurity Certificate Labs

This repository contains a collection of hands-on projects, labs, and activities completed as part of the **Google Cybersecurity Certificate program**.

The purpose of this portfolio is to demonstrate the practical application of cybersecurity principles and tools in realistic scenarios. Each project is self-contained in its own directory and includes a detailed `README.md` explaining its objectives, the methodology used, and the skills demonstrated.

## Projects

*   **[Vulnerability Assessment for a Small Business](./vulnerability-assessment-activity/README.md)**
    *   **Objective:** Stepped into the role of a cybersecurity analyst to assess a critical vulnerability for a small e-commerce business: a publicly accessible database server containing sensitive customer information.
    *   **Process:** Applied the NIST SP 800-30 Rev. 1 framework to conduct a formal risk assessment. This involved identifying potential threat actors, analyzing the likelihood and impact of threat events like data exfiltration, and calculating a risk score for each scenario.
    *   **Outcome:** Delivered a professional report to stakeholders with a clear "defense-in-depth" remediation plan. Key recommendations included network segmentation (placing the server behind a firewall), enforcing secure access via a VPN with MFA, and implementing a robust AAA framework to apply the principle of least privilege. This project demonstrates a strong ability to translate technical risks into business impact and provide actionable, layered security solutions.

*   **[Data Leak Incident Report & Remediation](../google-data-leak-incident-activity/README.md)**
    *   **Objective:** Acted as a security professional to analyze a data leak where confidential business plans were accidentally shared on social media by an external partner, and prepared a formal report for stakeholders.
    *   **Process:** Deconstructed the incident to identify the root causes: a manager's failure to revoke temporary folder access and a team member's error in sharing the wrong link. The analysis and recommendations were structured around the NIST framework, specifically citing the failure to enforce AC-6 (Least Privilege).
    *   **Outcome:** Delivered a detailed incident report that recommended specific, technical control enhancements. The primary recommendations were to implement automated access revocation for temporary shares and enforce strict Role-Based Access Control (RBAC) to limit access to sensitive data. This project showcases the ability to conduct a thorough incident post-mortem and produce a professional, actionable report based on industry-standard frameworks.

*   **[SQL for Security Investigations](../google-sql-filtering-lab/README.md)**
    *   **Objective:** Used SQL to query a simulated employee database to perform security-related tasks, such as threat hunting and data auditing.
    *   **Process:** Wrote a series of SQL queries using `WHERE` clauses with `AND`, `OR`, and `NOT` operators. The queries were designed to answer specific investigative questions, such as: "Identify all failed login attempts that occurred outside of business hours" or "Retrieve all login activity from a specific date range." Other queries supported system administration tasks, like generating employee lists for phased software rollouts.
    *   **Outcome:** Successfully filtered the database to isolate suspicious login patterns, audit user activity, and support asset management. This project demonstrates practical, hands-on SQL skills for security analysis and also highlights an awareness of related vulnerabilities like SQL Injection, as noted in the project's security considerations.

*   **[Linux File Permission Hardening](../linux-least-privilege-lab/README.md)**
    *   **Objective:** Conducted a hands-on security audit of a user's project directory in a Linux environment, identified multiple permission misconfigurations, and hardened the system to enforce the Principle of Least Privilege.
    *   **Process:** Used `ls -la` to perform an initial vulnerability assessment, which uncovered several issues including a world-writable file and a directory with excessive group permissions. Systematically remediated each finding using the `chmod` command with both symbolic (`o-w`) and numeric (`700`) modes to apply the correct, secure permissions.
    *   **Outcome:** Successfully secured the project directory by correcting all permission flaws, mitigating the risk of unauthorized access and modification. This project demonstrates core Linux security administration skills, including file system auditing, access control management, and the practical application of a foundational cybersecurity principle.

*   **[Parking Lot USB Baiting Analysis](./parking-lot-usb-exercise/README.md)**
    *   **Objective:** Analyzed a simulated USB baiting incident from both an attacker's and a defender's perspective. The scenario involved finding a lost USB drive belonging to a hospital's HR manager.
    *   **Process:** Outlined the secure procedure for handling such an incident, emphasizing the use of a sandboxed environment (virtualization) to inspect the drive's contents without risking infection of the host system. Identified a mix of sensitive PII and work-related files on the drive.
    *   **Outcome:** Articulated the potential attack vectors an adversary could exploit, such as using the PII for social engineering or embedding hidden malware. This exercise showcases a strong understanding of threat analysis, secure handling procedures for unknown media, and the importance of employee awareness training to mitigate social engineering attacks.

*   **[Access Control Remediation Plan](./completed-access-control-worksheet.md)**
    *   **Objective:** Investigated an anomalous access event log to identify and resolve an authorization issue.
    *   **Process:** Analyzed an event log that showed a former employee, whose contract ended years prior, accessing the system. The investigation revealed that the user's account was never deactivated and retained full 'Admin' privileges. The analysis also uncovered a systemic issue where all employees, regardless of role, were assigned 'Admin' access.
    *   **Outcome:** Developed a clear remediation plan recommending: 1) A formal off-boarding process to immediately deactivate departing employee accounts. 2) The implementation of Role-Based Access Control (RBAC) to enforce the principle of least privilege. 3) Regular user access reviews and audits. This demonstrates the ability to diagnose security failures from logs and prescribe specific, effective controls.

*   **[Data Leak Incident Analysis](./completed-data-leak-worksheet.md)**
    *   **Objective:** Conducted a post-mortem analysis of a data leak incident where a sensitive internal folder was accidentally shared publicly by a business partner.
    *   **Process:** Traced the incident to its root causes: a manager failing to revoke access after a meeting and a sales representative sharing the wrong link. The analysis was framed using the NIST Cybersecurity Framework (Protect Function) and specifically referenced NIST SP 800-53: AC-6 (Least Privilege).
    *   **Outcome:** Recommended two key controls to prevent future incidents: 1) Automatically revoking access to sensitive information after a set period. 2) Implementing strict role-based access controls (RBAC) to ensure employees can only access data essential to their role. This project demonstrates the ability to deconstruct a security incident, map it to a recognized framework (NIST), and propose targeted, preventative controls.

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
