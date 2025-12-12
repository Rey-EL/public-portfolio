# Access Control Remediation Plan

## Project Overview

This document outlines an analysis of an access control scenario, identifying authorization issues and recommending appropriate technical, operational, and managerial controls. It showcases an understanding of concepts like Role-Based Access Control (RBAC) and the principle of least privilege, as part of the Google Cybersecurity Certificate program.

---

## Scenario

The analysis begins with an event log entry indicating an incident on 10/03/2023, where a user associated with IP address 152.207.255.255, identified as Robert Taylor Jr. (a former Legal Attorney whose contract ended on 12/27/2019), accessed the system.

---

## Analysis and Recommendations

### Notes
Objective: Make 1-2 notes of information that can help identify the threat:
? Who caused this incident?
? When did it occur?
? What device was used?
- The incident occurred on 10/03/2023 at 8:29:57 AM.
- The user associated with the event log IP address (152.207.255.255) is Robert Taylor Jr., a former Legal Attorney whose contract ended on 12/27/2019.

### Issues Identified
Objective: Based on your notes, list 1-2 authorization issues:
? What level of access did the user have?
? Should their account be active?
- Robert Taylor Jr.'s account was still active and had 'Admin' authorization despite his employment ending in 2019.
- All listed employees, including contractors and seasonal staff, have 'Admin' authorization, indicating a lack of proper role-based access control (RBAC) and least privilege principles.

### Recommendations
Objective: Make at least 1 recommendation that could prevent this kind of incident:
? Which technical, operational, or managerial controls could help?
- Implement a robust off-boarding process that includes immediate deactivation or removal of access for terminated employees and contractors.
- Implement Role-Based Access Control (RBAC) to ensure users only have the minimum necessary permissions (least privilege) required for their job functions, rather than granting 'Admin' access to all.
- Regularly audit user accounts and their associated permissions to identify and rectify any discrepancies or unauthorized access.

---

## Summary of Skills Demonstrated

*   **Access Control Analysis:** Ability to diagnose and identify authorization issues from event logs and access control policies.
*   **Principle of Least Privilege:** Understanding and application of the concept of granting users only the minimum necessary permissions.
*   **Role-Based Access Control (RBAC):** Knowledge of RBAC principles for structuring user permissions.
*   **Incident Diagnosis:** Capability to interpret security logs to pinpoint the root cause of an access control incident.
*   **Security Policy Recommendation:** Formulating actionable recommendations for technical, operational, and managerial controls to prevent future incidents.

---

## Security Context

This analysis directly addresses "Broken Access Control," which is consistently listed as a top vulnerability in the OWASP Top 10. By identifying and providing solutions for over-privileged and stale accounts, this project emphasizes the critical importance of robust access control mechanisms as a fundamental layer of security. The recommendations align with best practices for identity and access management, aiming to prevent unauthorized access, data breaches, and ensure compliance with security policies.

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](../../../LICENSE.md) file for details.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to enhance the analysis, please feel free to open an issue or submit a pull request.
