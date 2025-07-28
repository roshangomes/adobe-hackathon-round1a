import fitz  # PyMuPDF
import json
import sys
from typing import Dict


def detect_heading_level(font_size: float, max_font: float) -> str:
    """
    Classify heading level based on font size relative to maximum font size in the document.
    """
    if font_size >= max_font * 0.95:
        return "H1"
    elif font_size >= max_font * 0.75:
        return "H2"
    elif font_size >= max_font * 0.55:
        return "H3"
    else:
        return None


def extract_outline(pdf_path: str) -> Dict:
    doc = fitz.open(pdf_path)
    outline = []
    title = "Unknown Title"
    all_font_sizes = []

    # Step 1: Scan all font sizes to find the maximum font size
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    size = span["size"]
                    if span["text"].strip():
                        all_font_sizes.append(size)

    max_font = max(all_font_sizes) if all_font_sizes else 12

    # Step 2: Extract title from largest font on the first page
    title_candidates = []
    for block in doc[0].get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if span["size"] >= max_font * 0.95:
                    title_candidates.append(span["text"].strip())
    if title_candidates:
        title = " ".join(title_candidates)

    # Step 3: Detect headings and group spans properly
    for i, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                full_line_text = " ".join(span["text"].strip() for span in line.get("spans", []) if span["text"].strip())
                if not full_line_text or len(full_line_text.split()) > 15:
                    continue

                font_sizes = [span["size"] for span in line.get("spans", []) if span["text"].strip()]
                if not font_sizes:
                    continue

                font_size = max(font_sizes)
                level = detect_heading_level(font_size, max_font)
                if level:
                    outline.append({
                        "level": level,
                        "text": full_line_text,
                        "page": i
                    })

    return {
        "title": title.strip(),
        "outline": outline
    }


def save_outline(outline: Dict, output_path: str):
    """
    Save the extracted outline to a JSON file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(outline, f, indent=2, ensure_ascii=False)


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_outline.py <input_pdf> <output_json>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_json = sys.argv[2]
    outline = extract_outline(input_pdf)
    save_outline(outline, output_json)
    print(f"Outline saved to {output_json}")


if __name__ == "__main__":
    main()
