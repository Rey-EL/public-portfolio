# 📄 Word to Markdown Converter

A lightweight, secure desktop application for Windows 11 that converts Microsoft Word documents (.docx) into clean Markdown (.md) files. Built with Python and Tkinter.

## 🚀 Features

* **Local Execution:** Runs entirely on the user's machine to ensure data privacy (no cloud uploads).
* **Format Preservation:** Uses mammoth to map Word styles to HTML, then markdownify to generate semantic Markdown (headers, lists, bold/italics).
* **GUI-Based:** Simple, user-friendly interface built with tkinter.
* **Input Validation:** Strict file type checking to prevent processing of non-docx files.

## 💡 Use Cases

* **Developer Workflow:** Quickly convert Product Requirement Documents (PRDs) from Word into repository-friendly Markdown.
* **CMS Migration:** Facilitate moving legacy content into modern Static Site Generators (Hugo, Jekyll) that require Markdown.
* **AI Data Cleaning:** Strip formatting from documents to prepare clean, structured text for Large Language Model (LLM) training data.
* **Privacy-First Conversion:** Convert sensitive legal or financial documents locally without uploading them to third-party cloud services.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** Tkinter (Standard Python Interface)
* **Core Libraries:**
  + [mammoth](https://github.com/mwilliamson/python-mammoth): For semantic conversion of .docx to HTML.
  + [markdownify](https://github.com/matthewwithanm/python-markdownify): For converting HTML to Markdown.
* **Distribution:** PyInstaller (for building the standalone .exe).

## 📦 Installation & Setup

### Prerequisites

* Python 3.x installed on your system.

### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/word-to-markdown-converter.git  
cd word-to-md-converter

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Run the Application

python docx\_to\_md\_converter.py

## 🏗️ Building the Executable

To compile this project into a standalone .exe for Windows:

pyinstaller docx\_to\_md\_converter.spec

*The output file will appear in the dist/ folder.*

## 🔒 Security Considerations (OWASP)

* **Input Validation:** The application explicitly validates file extensions before processing to mitigate the risk of processing malicious executables masquerading as documents.
* **Supply Chain Security:** Dependencies are pinned in requirements.txt to ensure consistent environments.
* **Data Privacy:** This tool follows a "Privacy by Design" approach. No data is transmitted over the network; all file operations occur within the local file system scope.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.