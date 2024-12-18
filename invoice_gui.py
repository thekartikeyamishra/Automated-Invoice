import tkinter as tk
from tkinter import filedialog, messagebox
from utils.ocr_engine import extract_text_from_image, extract_text_from_pdf
from utils.file_handler import save_extracted_data


class InvoiceProcessApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Automated Invoice Processing")

        # File Upload
        tk.Label(self.root, text="Upload Invoice(Image/PDF):", font=("Helvetica", 12)).pack(pady=5)
        self.upload_button = tk.Button(self.root, text="Browse", command=self.upload_file)
        self.upload_button.pack(pady=5)

        # Extracted Data Display
        tk.Label(self.root, text="Extracted Data:", font=("Helvetica", 12)).pack(pady=5)
        self.result_text = tk.Text(self.root, height=15, width=60, wrap=tk.WORD, state=tk.DISABLED)
        self.result_text.pack(pady=5)

        # Save Extracted Data
        self.save_button = tk.Button(self.root, text="Save Data", command=self.save_data, state=tk.DISABLED)
        self.save_button.pack(pady=5)

        self.extracted_data = None

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg, *.png"), ("PDF Files", "*.pdf")])
        if file_path:
            if file_path.endswith(".pdf"):
                text = extract_text_from_pdf(file_path)
            else:
                text = extract_text_from_image(file_path)

            self.extracted_data = {"text": text}
            self.display_data(text)
            self.save_button.config(state=tk.NORMAL)

    def display_data(self, text):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)
        self.result_text.config(state=tk.DISABLED)

    def save_data(self):
        if self.extracted_data:
            save_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
            if save_path:
                save_extracted_data(self.extracted_data, save_path)
                messagebox.showinfo("Success", "Data saved successfully!")
            else:
                messagebox.showerror("Error", "No data to save.")

    def run(self):
        self.root.mainloop()
