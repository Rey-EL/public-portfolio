# Project Overview

This directory, `Public_Portfolio`, is a collection of Python utility scripts and a comprehensive study guide for the CompTIA Security+ (SY0-701) exam.

## Projects

### FileJanitor
*   **Purpose:** A Python script to clean and organize folders by finding and removing duplicate files and empty directories.
*   **Technologies:** Python, `tkinter` (for GUI folder selection), `tqdm` (for progress bars).
*   **How to Run:** `python3 FileJanitor.py`

### MediaTidy
*   **Purpose:** A Python script to organize photo and video libraries by renaming files based on EXIF data and moving them into a structured `Images` and `Videos` directory.
*   **Technologies:** Python, `Pillow` (for EXIF data), `tkinter`, `tqdm`.
*   **How to Run:** `python3 MediaTidy.py`
*   **Deployment:** Includes a `.spec` file for creating a standalone Windows executable using PyInstaller.

### pdf-merger
*   **Purpose:** A Python script to merge multiple PDF files into a single PDF.
*   **Technologies:** Python.
*   **How to Run:** `python3 merge_pdfs.py`
*   **Deployment:** Includes a `.spec` file for creating a standalone Windows executable using PyInstaller.

### ppt-to-pdf-converter
*   **Purpose:** A Python script to convert PowerPoint presentations (`.ppt`, `.pptx`) to PDF files.
*   **Technologies:** Python.
*   **How to Run:** `python3 convert_to_pdf.py`
*   **Deployment:** Includes a `.spec` file for creating a standalone Windows executable using PyInstaller.

### sec_plus_guide
*   **Purpose:** A study guide for the CompTIA Security+ (SY0-701) exam.
*   **Structure:** The guide is organized by the official exam domains. Each topic is broken down using the "5 W's and H" (Who, What, Where, When, Why, How) format.
*   **Key Files:**
    *   `Study_Guide_Main.md`: The main entry point for the study guide.
    *   `DOMAIN_1_RESEARCH.md`, `DOMAIN_2_RESEARCH.md`, etc.: Detailed notes for each exam domain.
    *   `01.1_Security_Controls_Research.md`, etc.: Deeper research on specific topics.

## Directory Usage

This directory serves as a portfolio of Python projects and a dedicated study resource. The Python scripts are standalone utilities designed for file and media management. The `sec_plus_guide` is a structured knowledge base for cybersecurity certification preparation.
