Access controls worksheet

Note(s)
Objective: Make 1-2 notes of information that can help identify the threat:
? Who caused this incident?
? When did it occur?
? What device was used?
- The incident occurred on 10/03/2023 at 8:29:57 AM.
- The user associated with the event log IP address (152.207.255.255) is Robert Taylor Jr., a former Legal Attorney whose contract ended on 12/27/2019.

Issue(s)
Objective: Based on your notes, list 1-2 authorization issues:
? What level of access did the user have?
? Should their account be active?
- Robert Taylor Jr.'s account was still active and had 'Admin' authorization despite his employment ending in 2019.
- All listed employees, including contractors and seasonal staff, have 'Admin' authorization, indicating a lack of proper role-based access control (RBAC) and least privilege principles.

Recommendation(s)
Objective: Make at least 1 recommendation that could prevent this kind of incident:
? Which technical, operational, or managerial controls could help?
- Implement a robust off-boarding process that includes immediate deactivation or removal of access for terminated employees and contractors.
- Implement Role-Based Access Control (RBAC) to ensure users only have the minimum necessary permissions (least privilege) required for their job functions, rather than granting 'Admin' access to all.
- Regularly audit user accounts and their associated permissions to identify and rectify any discrepancies or unauthorized access.
