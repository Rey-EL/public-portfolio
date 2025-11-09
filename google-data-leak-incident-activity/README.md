# google-data-leak-incident-activity

This project is an exercise from the Google Cybersecurity Certificate program. It involves analyzing a data leak incident, identifying failures in security controls, and recommending improvements based on the NIST Cybersecurity Framework (CSF) and NIST SP 800-53.

---

## Scenario

You are a security professional at an educational technology company. Your team has been alerted to a data leak where confidential business plans were accidentally shared on social media by an external partner.

**Incident Details:**
*   A sales manager gave a team member temporary access to a folder containing sensitive, unannounced product information.
*   The manager forgot to revoke access after the meeting.
*   The team member later intended to share a link to marketing materials with a business partner but accidentally shared the link to the entire internal folder.
*   The partner, unaware of the sensitive nature of the content, posted the link publicly.

## Task

Your task was to analyze the incident and prepare a report for stakeholders. The report needed to:
1.  Identify the issues that led to the leak.
2.  Review the relevant security controls (Principle of Least Privilege).
3.  Recommend specific control enhancements based on NIST SP 800-53.
4.  Justify why these recommendations will prevent future incidents.

---

## Final Report: Data Leak Analysis

Below is the finalized report for management and stakeholders, detailing the analysis of the incident and recommended corrective actions.

### Data Leak Analysis Report

**Date:** November 8, 2025
**Subject:** Analysis of Recent Data Leak and Recommendations

#### 1. Incident Summary

A sales manager shared access to a folder of internal-only documents with their team for a meeting. The folder contained files for a new, unannounced product. After the meeting, the manager did not revoke access. A sales team member later accidentally shared a link to this entire internal folder with an external business partner, who then posted it on social media.

#### 2. Security Control Under Review

The primary security control that failed in this incident is **AC-6: Least Privilege**.

#### 3. Analysis of Issues

The data leak was caused by a combination of human error and procedural gaps:

*   **Prolonged Access:** The manager's failure to revoke temporary access left a critical window of vulnerability.
*   **Lack of Verification:** The sales representative did not verify the link's contents before sharing, indicating a need for better data handling training and procedures.

#### 4. Review of Governing Policy (NIST SP 800-53: AC-6)

NIST SP 800-53: AC-6 (Least Privilege) mandates that users are granted only the minimum access necessary for their job functions. The incident demonstrates a failure in the practical enforcement of this principle.

#### 5. Recommended Control Enhancements

To prevent recurrence, the following two NIST-based control enhancements are recommended:

1.  **Implement Automated Access Revocation:** Configure systems to automatically revoke access to sensitive information after a predetermined period (e.g., 24 hours for temporary shares).
2.  **Enforce Role-Based Access Control (RBAC):** Restrict access to sensitive internal resources based on a user's formally defined role. Sales team members should not have standing access to pre-release product development materials.

#### 6. Justification

These enhancements will significantly strengthen data security:

*   **Automated access revocation** removes reliance on manual de-provisioning and mitigates human error. The link would have been expired and unusable.
*   **Role-based access** ensures that sensitive documents are not accessible to employees whose roles do not require it, strictly adhering to the principle of least privilege and shrinking the attack surface.

By implementing these technical controls, we transition from relying on employee discretion to a more robust, automated, and auditable system for protecting confidential data.

---

## Security Context

This exercise highlights the critical importance of robust access control and incident response, principles central to frameworks like NIST. These concepts are also fundamental to addressing many vulnerabilities outlined in the OWASP Top 10, such as "Broken Access Control" and "Security Logging and Monitoring Failures," by emphasizing proactive measures and effective incident handling.

---

## Summary of Skills Demonstrated

This exercise showcases understanding and application of:
*   **Incident Analysis:** Deconstructing a security incident to identify the attack vector, root cause, and business impact.
*   **NIST Cybersecurity Framework:** Structuring an incident report and response plan according to the five core functions (Identify, Protect, Detect, Respond, Recover).
*   **Access Control Principles:** Understanding and applying the Principle of Least Privilege (NIST SP 800-53: AC-6).
*   **Security Control Enhancement:** Recommending specific control enhancements based on established security frameworks.

---

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to enhance the analysis, please feel free to open an issue or submit a pull request.
