# Automated-Invoice
For the next 15 days, I'll be creating and sharing 15 projects – one per day! Free versions will be open to all on my GitHub, and a low-cost paid version will be available too. Can't wait to hear your thoughts!

Welcome to Automated Invoice Processing! This project is designed to help small businesses and MSMEs efficiently process invoices by extracting key information (e.g., invoice number, date, total amount) using OCR (Optical Character Recognition) technology.

### **Automated Invoice Processing: Basic Version**

Welcome to **Automated Invoice Processing**! This project is designed to help small businesses and MSMEs efficiently process invoices by extracting key information (e.g., invoice number, date, total amount) using **OCR (Optical Character Recognition)** technology.

With this tool, you can:
1. Extract data from invoices (images or PDFs).
2. View the extracted information in a structured format.
3. Use a simple GUI for uploading invoices and managing results.

---

### **Features**

1. **Input Options**:
   - Supports uploading invoices as images (`.jpg`, `.png`) or PDFs (`.pdf`).

2. **Text Extraction**:
   - Extracts text using OCR.

3. **Data Saving**:
   - Save extracted data as `.json` files.

4. **User-Friendly GUI**:
   - A clean, intuitive interface built with **Tkinter**, making it accessible even for non-technical users.

---

### **File and Folder Structure**

```bash
AutomatedInvoiceProcessing/
├── data/
│   ├── sample_invoices/           # Folder for storing sample invoices (images/PDFs)
├── output/
│   ├── extracted_data/            # Folder for storing extracted data as JSON
├── utils/
│   ├── __init__.py                # Initializes the utils module
│   ├── ocr_engine.py              # Handles OCR and data extraction
│   ├── file_handler.py            # Handles file uploads and saves extracted data
├── gui/
│   ├── __init__.py                # Initializes the GUI module
│   ├── invoice_gui.py             # GUI implementation using Tkinter
├── main.py                        # Entry point for the application
├── requirements.txt               # Dependencies required for the project
├── README.md                      # Documentation for the project
```

---

### **Installation Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/thekartikeyamishra/Automated-Invoice.git
   cd AutomatedInvoiceProcessing
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

### **How It Works**

#### **1. Upload Invoices**
- Use the GUI to upload invoices as images or PDFs.
- The tool accepts common formats like `.jpg`, `.png`, and `.pdf`.

#### **2. Extract Data**
- The OCR engine processes the uploaded files and extracts text into a structured format.

#### **3. Save Extracted Data**
- Save the extracted text as `.json` files for further processing or integration.

#### **4. View Results**
- View extracted text directly within the GUI for a seamless experience.

---

### **Future Enhancements**

This project is a **basic version**, but here’s what’s planned for the future:
1. **Advanced Field Extraction**:
   - Extract specific fields such as invoice number, date, total amount, and more.
2. **Multi-Language OCR Support**:
   - Support for invoices in multiple languages.
3. **Integration with Bookkeeping Tools**:
   - Direct integration with platforms like QuickBooks or Zoho Books.
4. **Batch Processing**:
   - Handle multiple invoices simultaneously for faster processing.

---

### **Dependencies**

The project uses the following Python libraries:
- `pytesseract`: For OCR-based text extraction.
- `pdf2image`: To convert PDF pages into images.
- `opencv-python`: For image pre-processing.
- `Pillow`: For image handling in Python.

Install them with:
```bash
pip install -r requirements.txt
```

---

### **Contribution**

Feel free to contribute to this project! Fork the repository, submit pull requests, or raise issues for any bugs or feature requests.


---

### **Support**

If you find this project helpful, consider giving it a ⭐ on GitHub! Your support means a lot.  

[Star the repository here!](https://github.com/thekartikeyamishra/Automated-Invoice)

---

Happy coding and happy invoicing! 🚀
