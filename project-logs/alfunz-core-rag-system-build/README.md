# Project Log: Alfunz-Core RAG System Build

## Phase 1: Foundation and Initial Failure (The Speed vs. Intelligence Paradox)

### Initial Setup & Diagnostics:
The project commenced with the deployment of the Ollama LLM service within the Ubuntu instance of WSL 2, utilizing the Windows 11 host (Alfunz). Resource verification was performed via PowerShell (Get-CimInstance Win32_VideoController) confirming the NVIDIA RTX 4080 GPU (16GB VRAM) and 64GB System RAM. This validated the foundational environment for GPU-accelerated workloads. The largest model, llama3:70b (bigllama), was pulled and configured as the default LLM.

### The First Test (Critical Failure):
Upon running a simple text generation query, the system exhibited unacceptable token latency.
**Rationale:** Diagnostics confirmed the Critical Memory Bottleneck. The 40GB model size exceeded the 16GB VRAM capacity, forcing the LLM to continuously page data across the slower PCIe bus into System RAM. This created the "freight train" performance profile—high potential power but crippled responsiveness—a direct result of the VRAM limitation.
**Immediate Decision:** Prioritized user experience and speed.
**Action:** Swapped the default model to the optimized llama3 (8B - babyllama) to ensure the entire model fit within the GPU VRAM.

### Initial RAG Setup Failure (Cross-OS Sync):
The next challenge was integrating data from the Linux home directory into AnythingLLM. An initial attempt to use standard Windows network paths (\\wsl.localhost\Ubuntu...) for synchronization failed.
**Rationale:** AnythingLLM relies on Windows file system change notifications, which are not reliably propagated from the Linux kernel to the Windows kernel across the virtualization layer. This necessitated a change in data architecture.
**Action:** Abandoned native cross-OS monitoring. Adopted a professional, cloud-native synchronization workflow by configuring AnythingLLM to connect directly to private GitHub repositories via API key for secure, robust data ingestion.

## Phase 2: The Logic Crisis (The Hallucination Event)

### System Governance Implementation:
With the physical architecture stabilized, the focus shifted to behavioral control. A comprehensive V3 System Prompt was implemented to act as the primary governance layer, enforcing strict compliance. This included complex conditional logic and mandatory formatting rules (e.g., OWASP checks, investment exclusions, detailed code commentary). Simultaneously, AnythingLLM Slash Commands (/owasp, /briefing, etc.) were created to trigger these complex prompts efficiently.

### The Web Search Test (Soft Failure):
A test query asked for "today's news." The fast babyllama failed to execute the conditional logic in the System Prompt. It did not use the web tool and instead hallucinated current events from its pre-trained memory, proving its inadequacy as a reliable "agent."
**Rationale:** The 8B model lacked the reasoning capacity to correctly interpret the complex instruction: "IF keyword 'news' THEN MUST use tool." This confirmed the intelligence gap.

### The Agent Test (Failure Recourse):
To obtain reliable complex execution, I performed a deliberate recourse action.
**Action:** The Workspace Agent LLM Provider was temporarily switched to the intelligent llama3:70b (bigllama). This was an explicit test of the "smart agent" capacity. The subsequent test query was accurate, but the result was a severe, unacceptable delay.
**Rationale:** The reliance on the heavy bigllama model, even for single agent actions, destroyed the daily workflow efficiency. The accuracy was gained, but the speed was lost.

### Decision (The Final Strategy - System Lock-Down):
Faced with two untenable options (fast/unreliable vs. slow/accurate), the final strategic decision was made to sacrifice external capability for maximum internal stability.
**Rationale:** I accepted the limitation that the AI cannot be relied upon for real-time web search in this setup. The entire system must be simplified to its core strength.
**Action:** Reverted both LLM providers to the fast llama3. Crucially, I permanently disabled the Web Search skill within the AnythingLLM Agent configuration. This action removed the source of hallucination and locked the system into its primary function: fast, accurate retrieval from internal documents.

## Phase 3: Final System Audit and Lock-Down

### Final Configuration Lock-Down:
With the model selection solidified, the final architecture was implemented to ensure performance and permanence.
**Action:** Both the Workspace LLM Provider and the Workspace Agent LLM Provider were definitively set to the high-speed llama3 (8B) model. The slow, complex model was entirely removed from the active workflow.

### Audit of Tools and Governance:
A comprehensive audit of the system governance was performed to remove points of failure:
*   **Web Search Tool:** Confirmed that the external web search skill was permanently disabled in the AnythingLLM Agent configuration, eliminating any possibility of the AI attempting a hallucination-prone external search.
*   **System Prompt Integrity:** The V3 System Prompt was reviewed and maintained. While the AI is now too fast to perfectly obey all complex logic, the prompt's remaining instructions still successfully enforce formatting standards (e.g., numbered lists, code blocks, executive summary structure).

### Final Technical Outcome:
The project concluded with the successful establishment of the Alfunz-Core system. The technical trajectory revealed that for high-performance, private RAG applications on consumer-grade hardware, stability must be prioritized over advanced autonomy. The final setup is optimized for speed and reliability, delivering fast, highly-formatted, and auditable responses rooted exclusively in the secure GitHub data.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contributing
Contributions are welcome! Please see the [CONTRIBUTING.md](../../../CONTRIBUTING.md) for guidelines.
