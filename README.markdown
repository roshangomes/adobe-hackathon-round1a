# Adobe India Hackathon – Round 1A Submission

## 📌 Challenge Information

* **Challenge ID**: round\_1a\_001
* **Persona**: N/A (General PDF Outline Extractor)
* **Job to be Done**: Extract a document outline (headings like H1, H2, H3) from any given input PDF.
* **Expected Execution**:
  python extract\_outline.py input.pdf output.json

---

## 🧠 Our Approach

This script uses `PyMuPDF` to extract the document's visual structure and convert it into a meaningful outline based on font sizes.

### 🔍 Core Components:

1. **PDF Parsing**
   → Using PyMuPDF (`fitz`) to access pages, blocks, lines, and spans with font metadata.

2. **Heading Level Detection**
   → Detects H1, H2, H3 levels based on relative font sizes to the max font size on each page.

3. **Outline Structuring**
   → Each heading is stored with its level, text, and page number in structured JSON format.

4. **Text Cleaning**
   → Filters out long paragraphs and keeps only concise heading lines (less than 15 words).

---

## 📦 Dependencies

PyMuPDF==1.23.9

Install manually with:

pip install -r requirements.txt

---

## 🐳 Docker Instructions

### 🛠️ Build Image

docker build -t pdf-outline-extractor .

### 🚀 Run the Container

docker run --rm&#x20;
-v \$(pwd)/input.pdf:/app/input.pdf&#x20;
-v \$(pwd)/output.json:/app/output.json&#x20;
pdf-outline-extractor python extract\_outline.py input.pdf output.json

---

## 📁 Project Structure

.
├── extract\_outline.py       # Main script logic
├── requirements.txt          # Python dependencies
├── Dockerfile                # Container setup
├── input.pdf                # Sample input PDF
├── output.json               # Extracted outline
└── README.md

---

## ✅ Highlights

* Detects headings even without a proper table of contents
* Font-size based visual hierarchy extraction
* Offline-first, fully containerized
* Clean, structured output in JSON format

---

## 👤 Author

Developed by **Roshan Gomes**
GitHub: [https://github.com/roshangomes](https://github.com/roshangomes)
