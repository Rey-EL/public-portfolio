# Copyright (c) 2025 Elvis Reyes
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import filedialog, messagebox
import mammoth
from markdownify import markdownify as md
import os

class DocxToMarkdownConverter(tk.Tk):
    """
    A desktop application for converting Microsoft Word (.docx) files
    to clean Markdown (.md) files.
    """
    def __init__(self):
        super().__init__()
        self.title("Word to Markdown Converter")
        self.geometry("500x250")
        self.configure(bg="#f0f0f0")

        self.input_file_path = None

        # --- Widgets ---
        self.main_frame = tk.Frame(self, padx=20, pady=20, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.select_button = tk.Button(
            self.main_frame,
            text="1. Select .docx File",
            command=self.select_file,
            bg="#0078d4",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        self.select_button.pack(fill=tk.X, pady=5)

        self.file_label = tk.Label(
            self.main_frame,
            text="No file selected",
            bg="#f0f0f0",
            fg="#333",
            font=("Segoe UI", 9)
        )
        self.file_label.pack(fill=tk.X, pady=5)

        self.convert_button = tk.Button(
            self.main_frame,
            text="2. Convert and Save as Markdown",
            command=self.convert_file,
            state=tk.DISABLED,
            bg="#2b8a3e",
            fg="white",
            font=("Segoe UI", 10, "bold")
        )
        self.convert_button.pack(fill=tk.X, pady=10)

        self.status_bar = tk.Label(
            self,
            text="Ready",
            bd=1,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#e9ecef",
            font=("Segoe UI", 8)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def select_file(self):
        """Opens a file dialog to select a .docx file."""
        self.update_status("Selecting file...")
        file_path = filedialog.askopenfilename(
            title="Select a Word Document",
            filetypes=(("Word Documents", "*.docx"), ("All files", "*.*"))
        )
        if file_path:
            # Basic input validation
            if not file_path.lower().endswith('.docx'):
                messagebox.showerror("Invalid File Type", "Please select a valid .docx file.")
                self.update_status("Error: Invalid file type selected.")
                return

            self.input_file_path = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.convert_button.config(state=tk.NORMAL)
            self.update_status("File selected. Ready to convert.")
        else:
            self.update_status("File selection cancelled.")

    def convert_file(self):
        """Converts the selected .docx file to Markdown and saves it."""
        if not self.input_file_path:
            messagebox.showerror("Error", "No file selected to convert.")
            return

        output_path = filedialog.asksaveasfilename(
            title="Save Markdown File As...",
            defaultextension=".md",
            filetypes=(("Markdown Files", "*.md"), ("All files", "*.*"))
        )

        if not output_path:
            self.update_status("Save operation cancelled.")
            return

        self.update_status("Converting, please wait...")
        self.main_frame.update_idletasks() # Refresh UI

        try:
            # 1. Open and read the .docx file
            with open(self.input_file_path, "rb") as docx_file:
                # 2. Convert .docx to HTML using mammoth
                result = mammoth.convert_to_html(docx_file)
                html = result.value

            # 3. Convert HTML to Markdown using markdownify
            markdown_text = md(html, heading_style="ATX")

            # 4. Write the Markdown to the output file
            with open(output_path, "w", encoding="utf-8") as md_file:
                md_file.write(markdown_text)

            self.update_status(f"Successfully converted and saved to {os.path.basename(output_path)}")
            messagebox.showinfo("Success", "File converted successfully!")

        except Exception as e:
            self.update_status(f"An error occurred: {e}")
            messagebox.showerror("Conversion Error", f"An unexpected error occurred during conversion:\n\n{e}")

        finally:
            # Reset for next conversion
            self.input_file_path = None
            self.file_label.config(text="No file selected")
            self.convert_button.config(state=tk.DISABLED)

    def update_status(self, message):
        """Updates the text in the status bar."""
        self.status_bar.config(text=message)

if __name__ == "__main__":
    app = DocxToMarkdownConverter()
    app.mainloop()
