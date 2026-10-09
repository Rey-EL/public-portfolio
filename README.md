# Elvis Reyes — Cybersecurity and Python Portfolio

I am a career investigator working at the intersection of investigations and cybersecurity. This is where I keep my hands-on work: Python tools I built, security labs I completed, and study notes I wrote while learning.

## What I can do

**Incident response and analysis.** I work with the NIST Cybersecurity Framework to analyze incidents, assess vulnerabilities, and write formal reports. Examples here include a DDoS incident report and a vulnerability assessment done to NIST SP 800-30.

**Python.** I build small GUI applications with `tkinter` to automate real tasks: finding duplicate files, organizing photo libraries by EXIF data, merging PDFs, converting PowerPoint decks. I work with `pypdf`, `Pillow`, `win32com`, and SHA-256 hashing.

**Linux and Windows administration.** Permissions and least privilege, system hardening, `cron` automation, shell scripting, and virtualized lab setups with Kali Linux.

**Security fundamentals.** SQL for investigations, access control, and the core frameworks (NIST, OWASP). I am currently studying for the CompTIA Security+ (SY0-701).

**AI systems.** I have deployed and troubleshot local LLM setups, including RAG systems built with Ollama and AnythingLLM.

## Python utilities

| Project | What it does | Built with |
| :------ | :----------- | :--------- |
| [file-janitor](./python-utilities/file-janitor/README.md) | Finds duplicate files by content hash and cleans out empty folders. Asks before deleting anything. | Python, `tkinter`, SHA-256 |
| [media-tidy](./python-utilities/media-tidy/README.md) | Sorts photo and video libraries into dated folders using EXIF data. | Python, `Pillow`, `tkinter` |
| [pdf-merger](./python-utilities/pdf-merger/README.md) | Merges every PDF in a folder tree into one document. Skips corrupt files instead of crashing. | Python, `pypdf`, `tkinter` |
| [ppt-to-pdf-converter](./python-utilities/ppt-to-pdf-converter/README.md) | Converts PowerPoint files to PDF and merges them. Windows only, uses PowerPoint itself for the conversion. | Python, `win32com`, `pypdf` |
| [word-to-markdown-converter](./word-to-markdown-converter/README.md) | Turns .docx files into clean Markdown. | Python, `tkinter`, `mammoth` |

## System administration

| Project | What it does | Built with |
| :------ | :----------- | :--------- |
| [Self-Healing Ubuntu](./self-healing-ubuntu/README.md) | A guide to a self-updating Ubuntu setup using cron, logrotate, and shell scripting. | Linux, `cron`, shell |

## Google Cybersecurity Certificate

Labs and scenario exercises from the certificate program.

| Project | What it does | Covers |
| :------ | :----------- | :----- |
| [Certificate activities](./cybersecurity-labs/google-cybersecurity-activities/README.md) | Vulnerability assessment, data leak analysis, SQL filtering lab, Linux permissions lab, USB baiting exercise. | NIST SP 800-30, risk analysis, SQL, `chmod`, access control |

## Other labs and projects

| Project | What it does | Covers |
| :------ | :----------- | :----- |
| [NIST DDoS Incident Report](./cybersecurity-labs/nist-ddos-incident-report/README.md) | Formal incident report on a DDoS scenario, structured on the five NIST CSF functions. | Incident analysis, NIST CSF, response and recovery |
| [CompTIA Security+ Study Guide](./cybersecurity-labs/sec-plus-guide/README.md) | My study notes for the SY0-701 exam, one page per domain. | All five exam domains |
| [VMware and Kali Setup](./cybersecurity-labs/vmware-kali-setup/README.md) | How I set up VMware Workstation Pro with a Kali Linux VM on a Windows host. | Virtualization, lab setup |
| [Fabric AI CLI Install](./fabric-installation-showcase/README.md) | Notes from installing and troubleshooting the Fabric AI CLI. | Debugging, CLI work |
| [RAG System Build Log](./project-logs/alfunz-core-rag-system-build/README.md) | A build log for a local RAG system with Ollama and AnythingLLM. | LLM deployment, RAG, troubleshooting |
| [Cyber Security CTF Lab](https://github.com/Rey-EL/cyber-security-ctf-lab) | A Capture The Flag game in a single HTML file. Simulated Linux terminal, challenge levels, analyst ranks. | HTML/CSS/JS, CTF design |

## Coursework

- [ECPI University coursework](./ecpi-coursework/README.md) — Computer and Information Science, Cyber Security Technology concentration.

## Contact

- LinkedIn: [elvisreyeshernandez](https://www.linkedin.com/in/elvisreyeshernandez)
- Email: [elvis360@gmail.com](mailto:elvis360@gmail.com)

## License

MIT License. See [LICENSE.md](LICENSE.md) for details.
