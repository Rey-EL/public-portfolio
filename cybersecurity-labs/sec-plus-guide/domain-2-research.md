
# Domain 2: Threats, Vulnerabilities, and Mitigations

## 1. Threat Actors and Motivations

### Who are Threat Actors?

Threat actors are individuals, groups, or entities responsible for malicious cyber activities that impact the security of others. They can range from lone individuals to well-organized, state-sponsored groups.

*   **Nation-states:** Government-funded and highly sophisticated, often referred to as Advanced Persistent Threats (APTs). They possess enormous resources and can conduct constant, multi-location attacks.
*   **Unskilled Attackers (Script Kiddies):** Individuals with limited technical skills who often use automated tools or pre-made scripts. They typically lack the understanding of how these scripts work.
*   **Hacktivists:** Individuals or groups motivated by philosophical, social, or political beliefs, using cyberattacks to promote an agenda or draw attention to a cause. Their skill levels and resources can vary.
*   **Insider Threats:** Authorized internal users (employees, contractors, third-party vendors) who intentionally or unintentionally misuse their access to harm an organization.
*   **Organized Crime (Criminal Syndicates):** Well-funded, skilled external groups that operate like businesses, focused on financial gain. They often have corporate structures and significant resources.
*   **Shadow IT:** Employees leveraging unauthorized or unmanaged IT resources within an organization, which can inadvertently create security vulnerabilities. While not always malicious, it poses a significant risk.
*   **Company Competitors:** Businesses that may engage in unethical tactics to gain an advantage.

### What do Threat Actors do?

Threat actors engage in various malicious activities, including malware development, data theft, extortion, and denial-of-service attacks. Their actions are intended to steal, alter, or destroy data, or disrupt services.

### Where do Threats Originate?

Threats can originate from both outside and inside an organization.

*   **External Threats:** Nation-states, unskilled attackers, hacktivists, and organized crime typically operate from outside the organization.
*   **Internal Threats:** Insider threats and shadow IT originate from within the target network.

### When do Attacks Occur?

Attacks can occur at any time. Some threat actors, particularly nation-states employing APTs, aim to infiltrate and maintain a persistent presence in a target network for extended periods, sometimes months or years, to collect specific data.

### Why do Threat Actors Act? (Motivations)

Threat actors are driven by diverse motivations, which often dictate their targets and methods. Key motivations include:

*   **Financial Gain:** One of the most common motivations for cybercriminals and organized crime, achieved through ransomware, identity theft, banking Trojans, or selling stolen data on the dark web.
*   **Data Exfiltration:** The unauthorized transfer of sensitive data, such as intellectual property (IP), personally identifiable information (PII), or trade secrets, for various purposes including sale or competitive advantage.
*   **Espionage:** Stealing confidential information, often conducted by nation-states or corporations, to gain a competitive or political edge.
*   **Philosophical/Political Beliefs (Hacktivism):** Promoting social or political agendas, drawing attention to perceived issues, or disrupting services for ideological reasons.
*   **Service Disruption/Chaos:** Causing outages or disruptions to essential services, sometimes for political reasons or simply to create problems.
*   **Blackmail:** Obtaining sensitive information and threatening its release unless demands (often financial) are met.
*   **Revenge:** Disgruntled employees or individuals seeking to harm an organization or adversary.
*   **Ethical Reasons:** Some hackers may act to expose vulnerabilities, aiming to enhance security.
*   **Warfare:** Nation-states may use cyberattacks as a form of cyber warfare to achieve geopolitical objectives, disrupt critical infrastructure, or destabilize governments.
*   **Curiosity/Proving Skills:** Unskilled attackers, or script kiddies, may be motivated by a desire to test their abilities or simply out of curiosity.

### How do Threat Actors Operate?

The methods and resources available to threat actors vary significantly based on their type and funding.

*   **Resources and Funding:** Can range from minimal (unskilled attackers) to extensive (nation-states, organized crime). Well-funded actors can sustain constant attacks and target multiple locations.
*   **Skill Level:** Varies from low (script kiddies) to highly sophisticated (APTs).
*   **Tactics:** May involve using automated tools, exploiting vulnerabilities, social engineering, or advanced persistent techniques to bypass security measures and maintain access. Understanding these motivations helps in developing appropriate countermeasures.

## 2. Threat Vectors and Attack Surfaces

A **threat vector**, also known as an attack vector, is the specific method or pathway that a cybercriminal uses to gain unauthorized access to a system, network, or application. These vectors exploit vulnerabilities to carry out malicious activities.

An **attack surface** refers to the sum of all possible points, pathways, or methods (attack vectors) that an unauthorized user can use to gain access to a network, system, or sensitive data, or to carry out a cyberattack. It encompasses all hardware, software, and network interfaces with known security flaws, representing an organization’s overall exposure to potential threats. The larger and more complex an organization’s digital environment, the larger its attack surface.

### 1. Message-Based Vectors (Email, SMS, Instant Messaging)

*   **Who:** Cybercriminals, often employing social engineering tactics, are the primary actors.
*   **What:** These are attacks delivered through common communication channels such as email (phishing), Short Message Service (SMS) (smishing), and instant messaging (IM).
*   **Where:** These attacks manifest in user inboxes, on mobile devices, and within various instant messaging applications.
*   **When:** Message-based attacks are a constant threat due to their reliance on human vulnerability and the ease with which they can be distributed.
*   **Why:** The goal is to trick recipients into clicking malicious links, opening infected files, or divulging sensitive information by exploiting trust and creating a false sense of urgency.
*   **How:** Attackers craft deceptive messages that appear legitimate, containing malicious links, infected attachments, or requests for confidential data.

### 2. Unsecure Networks (Wireless, Wired, Bluetooth)

*   **Who:** Attackers actively seek out and exploit misconfigured network components, insecure wireless setups, or outdated protocols.
*   **What:** This vector involves exploiting weaknesses in network configurations, protocols, or physical access points to gain unauthorized entry.
*   **Where:** Vulnerabilities can exist in wired networks (e.g., physical ports), wireless networks (Wi-Fi, Bluetooth), and remote access connections.
*   **When:** Networks are most vulnerable when security protocols are weak, configurations are incorrect, or credentials for access are stolen.
*   **Why:** The primary motivations include intercepting data, gaining unauthorized access to systems, or transmitting exploit code across the network.
*   **How:** Attackers might attach unauthorized devices to physical network ports, crack wireless security keys, or exploit known misconfigurations in network devices.

### 3. Social Engineering

*   **Who:** Threat actors who meticulously research their targets to understand their behaviors and vulnerabilities.
*   **What:** Social engineering is the psychological manipulation of individuals into performing actions or divulging confidential information, often by exploiting human emotions like trust, fear, or urgency.
*   **Where:** These attacks can occur through a wide range of mediums, including email, phone calls, SMS messages, social media platforms, and even direct in-person interactions.
*   **When:** Social engineering is a consistently effective and common attack vector, frequently targeting new employees or individuals with access to sensitive data.
*   **Why:** Attackers aim to gain access to accounts, steal private information, facilitate malware installation, or cause financial losses.
*   **How:** Common tactics include phishing, pretexting (creating a fabricated scenario), baiting (luring with false promises), smishing (SMS phishing), and vishing (voice phishing), all relying on deception and impersonation.

### 4. File-Based Vectors

*   **Who:** Cybercriminals who embed malicious code within seemingly innocuous files.
*   **What:** This vector involves malicious activities executed through files that contain embedded harmful code designed to exploit vulnerabilities.
*   **Where:** Malicious code can be hidden in various file types, including executable files, PDFs, compressed archives (e.g., ZIP, RAR), office documents with macros, and even image files (e.g., SVG, or within image descriptions). Removable devices like USB drives are also common carriers.
*   **When:** These threats are activated when users open, execute, or interact with these seemingly harmless files.
*   **Why:** The objective is to exploit software vulnerabilities, install various forms of malware (such as viruses, Trojans, ransomware, spyware, or worms), steal data, or disrupt system operations.
*   **How:** Attackers embed malicious code within legitimate-looking files, which then exploit software vulnerabilities when the file is opened. This often occurs after users are tricked into downloading and opening infected files, frequently through phishing or other social engineering schemes.

### 5. Voice Call Vectors

*   **Who:** Cybercriminals, often financially motivated groups, are increasingly leveraging voice communication for attacks.
*   **What:** These threats exploit voice communication channels, frequently incorporating social engineering techniques.
*   **Where:** Attacks target traditional phone systems and Voice over IP (VoIP) systems.
*   **When:** Voice-based threats are on the rise as voice communication remains a critical, yet often overlooked, security concern.
*   **Why:** Attackers aim to trick victims into revealing sensitive information (vishing), intercept private conversations (eavesdropping), or disrupt communication services (Denial of Service attacks).
*   **How:** Tactics include vishing (voice phishing), caller ID spoofing, eavesdropping on calls, automated robocalls, and DoS attacks specifically targeting VoIP infrastructure.

### 6. Supply Chain Vectors

*   **Who:** Threat actors who identify and exploit vulnerabilities within the supply chain, often targeting third-party vendors or less secure elements.
*   **What:** These attacks target the less secure components within a software or hardware supply network, leveraging the inherent trust relationships between organizations.
*   **Where:** Attacks can occur at any stage of the software development lifecycle, including compromised source code, vulnerable third-party dependencies (e.g., open-source components), insecure build pipelines, and post-release configurations. Hardware components can also be compromised.
*   **When:** The risk increases significantly when organizations rely heavily on third-party suppliers, expanding the potential for exploitation.
*   **Why:** The objective is to inject malicious code into software or hardware, gain unauthorized access to sensitive systems or data, or deploy malware to a wide range of downstream targets.
*   **How:** Methods include compromising a vendor’s systems, injecting malicious code into software updates, tampering with code during transmission (Man-in-the-Middle attacks), or exploiting vulnerabilities found in open-source dependencies.

### 7. Vulnerable Software Vectors

*   **Who:** Attackers who actively scan for systems running outdated software or exploit known vulnerabilities.
*   **What:** This vector involves exploiting existing flaws (bugs, design weaknesses) in software, operating systems, or applications.
*   **Where:** Any software, operating system, or application can be a target, particularly those that are unpatched, unsupported by vendors, or configured with default credentials.
*   **When:** Systems are vulnerable when software is not regularly updated, patches are not applied promptly, or when vendors cease support for older systems.
*   **Why:** Attackers aim to bypass access controls, crash processes, execute malicious code, install malware, steal data, or establish persistent access to compromised systems.
*   **How:** This is achieved by exploiting known vulnerabilities (often publicly documented Common Vulnerabilities and Exposures - CVEs), zero-day exploits (previously unknown vulnerabilities), or misconfigurations within the software. These exploits can be delivered remotely or locally.

## 3. Vulnerabilities

### What are Vulnerabilities?
Vulnerabilities are weaknesses or flaws in a system, application, or process that could be exploited by a threat actor to compromise the security of an asset. These weaknesses can exist in various forms, including design flaws, configuration errors, or implementation mistakes.

### Who is Affected by Vulnerabilities?
Anyone using or relying on systems with vulnerabilities can be affected. This includes individuals, organizations, and even nation-states. Threat actors, ranging from unskilled attackers to sophisticated nation-states and organized crime, actively seek out and exploit these weaknesses.

### Where are Vulnerabilities Found?
Vulnerabilities can be found across a wide range of technological components and environments. The SY0-701 exam specifically highlights:
*   **Application vulnerabilities:** Flaws within software applications.
*   **Hardware vulnerabilities:** Weaknesses in physical components.
*   **Mobile device vulnerabilities:** Security gaps in smartphones, tablets, and other mobile devices.
*   **Virtualization vulnerabilities:** Issues within virtualized environments and hypervisors.
*   **Operating system (OS)-based vulnerabilities:** Weaknesses inherent in operating systems like Windows, Linux, or macOS.
*   **Cloud-specific vulnerabilities:** Security concerns unique to cloud computing environments (e.g., misconfigured S3 buckets, insecure APIs).
*   **Web-based vulnerabilities:** Flaws in web applications and services (e.g., SQL injection, cross-site scripting).
*   **Supply chain vulnerabilities:** Risks introduced through third-party vendors, software, or hardware components.

### When do Vulnerabilities Occur?
Vulnerabilities can exist at any stage of a system’s lifecycle, from design and development to deployment and ongoing operation. They can be introduced during coding, configuration, integration of different components, or even through outdated software and hardware. New vulnerabilities are constantly discovered as technology evolves and new attack methods emerge.

### Why are Vulnerabilities Important?
Understanding vulnerabilities is crucial because they represent potential entry points for attacks. If left unaddressed, vulnerabilities can lead to:
*   **Data breaches:** Unauthorized access to sensitive information.
*   **System compromise:** Attackers gaining control over systems.
*   **Service disruption:** Denial of service or other operational impacts.
*   **Financial loss:** Costs associated with recovery, legal fees, and reputational damage.
*   **Reputational damage:** Loss of trust from customers and partners.
*   **Compliance violations:** Failure to meet regulatory requirements.

### How are Vulnerabilities Managed and Mitigated?
Managing vulnerabilities involves a continuous process of identification, assessment, and remediation. Key strategies include:
*   **Vulnerability scanning and penetration testing:** Regularly identifying weaknesses.
*   **Patch management:** Applying security updates and patches promptly.
*   **Secure coding practices:** Developing applications with security in mind.
*   **Configuration hardening:** Securing systems by disabling unnecessary services and applying secure configurations.
*   **Security awareness training:** Educating users about common attack vectors.
*   **Implementing security controls:** Utilizing firewalls, intrusion detection/prevention systems, and access controls.
*   **Supply chain risk management:** Vetting third-party vendors and components.

## 4. Malicious Activity and Attacks

### What: Malicious Activity and Attacks

Malicious activity refers to any intentional action designed to cause harm to networks, systems, devices, or users. Attacks are the methods employed to achieve this harm. The SY0-701 syllabus categorizes these into:

*   **Malware Attacks:** This broad term encompasses any software or code intentionally designed to cause harm, such as gaining information, access, or restricting functionality. Examples include ransomware, which encrypts files and demands payment, and Trojans, which hide behind legitimate software.
*   **Password Attacks:** These aim to obtain credentials, often through methods like password spraying or brute force.
*   **Application Attacks:** These target vulnerabilities in the application layer (Layer 7 of the OSI model) to gain system or network access. Common types include injection attacks (e.g., SQL injection), buffer overflows, cross-site scripting (XSS), cross-site request forgery (CSRF), and privilege escalation.
*   **Physical Attacks:** These involve gaining information or access through tangible means, such as RFID cloning, environmental attacks (e.g., cutting power or manipulating HVAC), or brute force to bypass physical barriers.
*   **Network Attacks:** These exploit vulnerabilities in network protocols, interfere with network operations, or create false access points to gain entry or steal information. Examples include deauthentication attacks and RF jamming on wireless networks.
*   **Cryptographic Attacks:** These exploit weaknesses in cryptographic implementations or algorithms. Examples include downgrade attacks, SSL stripping (an on-path attack), and hash collisions (like the birthday attack).

### Who: Threat Actors

Various individuals or groups, known as threat actors, are responsible for malicious activities. They are differentiated by their motivation, skill set, funding, and whether they are internal or external to the target. Common threat actors include:

*   **Nation-states:** Government-funded and often highly skilled, these are typically Advanced Persistent Threats (APTs) targeting governmental entities, motivated by political or economic considerations.
*   **Unskilled attackers (Script Kiddies):** These individuals have limited technical skills and often use automated tools. Their motivations can include proving their abilities or simple curiosity.
*   **Hacktivists:** Motivated by philosophical or political beliefs, they often use disruptive tactics like Denial of Service (DoS) attacks or website defacement to promote social or political change.
*   **Insider threats:** These originate from within an organization, such as disgruntled employees, third-party vendors, or contractors, with varied motivations including ethical concerns, personal grievances, or financial gain.
*   **Organized crime (Criminal Syndicates):** Typically well-funded and skilled external groups primarily motivated by financial gain through activities like theft and fraud.
*   **Shadow IT:** Employees using IT services without the knowledge or management of the official IT department, which can inadvertently create vulnerabilities.

### Why: Motivations Behind Attacks

The motivations for malicious activities are diverse and can include:

*   **Financial gain:** A primary driver for organized crime, seeking profit through fraud, theft, or blackmail.
*   **Data exfiltration:** Stealing sensitive data, potentially for espionage or sale.
*   **Espionage:** Gaining intelligence, often by competitors or nation-states.
*   **Disruption/Chaos:** Causing disorder or destabilizing normal operations, sometimes for philosophical or political reasons.
*   **Political ideology/Philosophical beliefs:** Driving hacktivist activities.
*   **Ethical concerns:** Acting upon perceived acceptable standards of behavior or morality.
*   **Revenge:** Seeking retaliation for a perceived injustice or wrongdoing.
*   **Blackmail:** Threatening to disclose damaging information unless demands are met.

### Where/When: Attack Vectors and Scenarios

Malicious activities can occur across various environments and at different stages of interaction:

*   **Network-based:** Attacks like deauthentication or RF jamming occur on wireless networks. On-path attacks, such as SSL stripping, involve an attacker positioned between communicating parties.
*   **Application-based:** Attacks target web applications and their underlying servers, often exploiting vulnerabilities during user input or session management.
*   **Physical locations:** Physical attacks can occur at data centers, offices, or any location with physical access to systems or infrastructure.
*   **User interaction:** Many attacks, especially malware and social engineering, rely on users clicking malicious links, downloading infected files, or falling for deceptive tactics.
*   **Supply chain:** Vulnerabilities can be introduced through the supply chain, affecting software or hardware before it reaches the end-user.

### How: Mechanisms and Techniques

Each attack type employs specific techniques:

*   **Malware:**
    *   **Ransomware:** Encrypts data or locks systems, demanding payment for restoration.
    *   **Trojans:** Disguise malicious software as legitimate programs.
    *   **Keyloggers:** Record keystrokes to capture sensitive information.
    *   **Worms:** Self-propagating malware that spreads across networks.
*   **Password Attacks:**
    *   **Brute Force:** Systematically trying every possible password combination until the correct one is found. This is often done offline after obtaining password hashes to avoid account lockouts.
    *   **Password Spraying:** Attempting a few common passwords against many accounts to avoid triggering lockouts on a single account.
*   **Application Attacks:**
    *   **Injection Attacks (e.g., SQL Injection):** Inserting malicious code into data input fields to manipulate application behavior or access databases.
    *   **Buffer Overflow:** Sending more data to an application than its buffer can handle, potentially overwriting adjacent memory and executing malicious code.
    *   **Cross-Site Scripting (XSS):** Injecting malicious scripts into web pages viewed by other users, often to steal session cookies or deface websites.
    *   **Cross-Site Request Forgery (CSRF/XSRF):** Tricking a user’s browser into sending an authenticated request to a vulnerable web application.
    *   **Directory Traversal:** Exploiting vulnerabilities to access files and directories outside the intended web root directory.
    *   **Privilege Escalation:** Gaining higher-level access than initially authorized.
    *   **Replay Attacks:** Capturing and retransmitting valid data (like session IDs or password hashes) to gain unauthorized access.
*   **Physical Attacks:**
    *   **RFID Cloning:** Duplicating access badges or key fobs to gain unauthorized entry.
    *   **Environmental Attacks:** Disrupting services by manipulating environmental controls like power or HVAC systems.
    *   **Brute Force (Physical):** Forcing open locked doors or windows.
    *   **Tailgating/Piggybacking:** An unauthorized person following an authorized person into a secure area.
*   **Network Attacks:**
    *   **Deauthentication Attacks:** Disconnecting users from a wireless network by sending deauthentication frames.
    *   **RF Jamming:** Interfering with wireless signals to disrupt communication.
*   **Cryptographic Attacks:**
    *   **Downgrade Attacks:** Forcing a system to use a weaker or unencrypted communication protocol.
    *   **SSL Stripping:** An on-path attack where an attacker intercepts HTTPS traffic and downgrades it to HTTP, allowing them to read sensitive information.
    *   **Hash Collisions (Birthday Attack):** Finding two different inputs that produce the same hash output, which can be used for forgery.

## 5. Mitigation Techniques

Mitigation techniques are strategies and controls implemented to reduce the likelihood or impact of a threat exploiting a vulnerability.

### 1. Segmentation

*   **What:** Segmentation involves dividing a network into smaller, isolated segments or zones. This can be done logically (e.g., VLANs) or physically.
*   **Why:** To limit the "blast radius" of an attack, meaning if one segment is compromised, the attack is contained and cannot easily spread to other parts of the network. It also allows for more granular security policies and improved monitoring.
*   **How:** Implemented using Virtual Local Area Networks (VLANs), firewalls, network access control lists (ACLs), and Software-Defined Networking (SDN) to create logical boundaries and control traffic flow between segments.
*   **Who:** Typically managed by network administrators and security engineers.
*   **Where:** Applied across the entire network infrastructure, including data centers, cloud environments, and user networks.
*   **When:** During network design, infrastructure upgrades, and as part of ongoing security architecture improvements.

### 2. Access Control

*   **What:** Access control is the process of restricting access to resources based on user identity and predefined permissions. It ensures that only authorized individuals or systems can access specific data or functionalities.
*   **Why:** To enforce the principle of least privilege, preventing unauthorized access, modification, or destruction of sensitive information and systems.
*   **How:** Implemented through authentication mechanisms (e.g., passwords, multi-factor authentication (MFA)), authorization policies (e.g., Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC)), and access control lists (ACLs) on files, folders, and network devices.
*   **Who:** Managed by security administrators, system administrators, and Identity and Access Management (IAM) teams.
*   **Where:** Applied at every point where access to resources is granted, including operating systems, applications, databases, and network devices.
*   **When:** Continuously, as users join or leave an organization, roles change, and new resources are provisioned.

### 3. Configuration Enforcement

*   **What:** Configuration enforcement ensures that systems and applications adhere to predefined secure configurations and security baselines. This prevents deviations from established security standards.
*   **Why:** To maintain a consistent and strong security posture across all systems, prevent misconfigurations that could introduce vulnerabilities, and ensure compliance with organizational policies and regulatory requirements.
*   **How:** Achieved using configuration management tools (e.g., Ansible, Puppet, Chef), Group Policies (in Windows environments), security templates, and automated auditing tools that check for compliance against baselines.
*   **Who:** System administrators, security engineers, and DevOps teams are responsible for defining and enforcing configurations.
*   **Where:** Applied to all endpoints, servers, network devices, cloud resources, and applications within an organization’s IT environment.
*   **When:** During system deployment, after major updates, and continuously as part of ongoing security operations and compliance monitoring.

### 4. Hardening

*   **What:** Hardening is the process of securing a system by reducing its attack surface. This involves disabling unnecessary services, closing unused ports, removing default accounts, and applying secure configurations.
*   **Why:** To minimize potential entry points for attackers, reduce the likelihood of successful exploitation of vulnerabilities, and improve the overall security posture of a system.
*   **How:** Involves steps such as disabling default accounts, removing unnecessary software and services, closing unused network ports, encrypting data at rest and in transit, implementing strong password policies, and using secure protocols.
*   **Who:** System administrators, security engineers, and IT operations teams.
*   **Where:** Applied to operating systems (servers, workstations), applications, network devices (routers, switches, firewalls), and cloud instances.
*   **When:** During the initial deployment of a system, after major software installations or updates, and periodically as part of security audits and maintenance.

### 5. Isolation

*   **What:** Isolation involves separating critical systems, processes, or data from other parts of the network or system to limit the impact of a compromise.
*   **Why:** To contain threats, protect highly sensitive assets, prevent lateral movement of attackers within a network, and ensure the continued operation of critical services even if other systems are compromised.
*   **How:** Achieved through network segmentation (as described above), virtual machines (VMs), containers, air gapping (physical separation), sandboxing (for untrusted code execution), and dedicated hardware.
*   **Who:** Security architects, network engineers, and system administrators.
*   **Where:** Used for critical servers, sensitive data repositories, untrusted applications, and specific network segments requiring enhanced security.
*   **When:** For high-risk systems, during incident response to contain a breach, and as a proactive security measure for critical infrastructure.

### 6. Patching

*   **What:** Patching is the process of applying updates to software, operating systems, and firmware to fix known vulnerabilities, bugs, and improve performance or add new features.
*   **Why:** To eliminate known security flaws that attackers could exploit, thereby preventing successful attacks, maintaining system stability, and ensuring compliance with security policies.
*   **How:** Involves establishing a robust patch management process, using automated patch management systems, regularly monitoring vendor security advisories, and applying updates after appropriate testing.
*   **Who:** System administrators, IT operations teams, and security teams.
*   **Where:** Applied to all software applications, operating systems (Windows, Linux, macOS), firmware on hardware devices, and network equipment.
*   **When:** Regularly and promptly, as soon as patches are released by vendors and have undergone internal testing, often during scheduled maintenance windows.
