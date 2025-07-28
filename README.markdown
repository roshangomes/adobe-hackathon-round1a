# Connecting the Dots Challenge - Round 1A Solution

## Approach
This solution extracts a structured outline from a PDF file, identifying the title and headings (H1, H2, H3) with their respective page numbers. We use the `pdfplumber` library for PDF text extraction due to its lightweight nature and ability to extract font sizes, which helps in heading detection. The solution avoids hardcoding font sizes for heading levels by using a dynamic heuristic based on relative font sizes within the document. The title is assumed to be the largest, bold text on the first page, while headings are detected based on font size and text length (short text, typically ≤10 words).

### Key Features
- **Dynamic Heading Detection**: Uses relative font sizes to classify headings as H1, H2, or H3, adapting to the document’s style.
- **Lightweight**: The model size is minimal (only `pdfplumber` and dependencies, well under 200MB).
- **No Internet Access**: Runs entirely offline, meeting the challenge constraints.
- **Multilingual Support**: Handles text in various languages by using Unicode-compatible text extraction.

### Libraries Used
- `pdfplumber` (0.7.4): For PDF text extraction and font size analysis.
- Standard Python libraries: `json`, `re`, `sys`.

## How to Build and Run
1. **Build the Docker Image**:
   ```bash
   docker build -t pdf-outline-extractor .
   ```
2. **Run the Container**:
   ```bash
   docker run --rm -v $(pwd)/input.pdf:/app/input.pdf -v $(pwd)/output.json:/app/output.json pdf-outline-extractor
   ```
   - Ensure `input.pdf` is in the current directory.
   - The output will be saved as `output.json`.

## Notes
- The solution assumes headings are short and have distinct font sizes. For complex PDFs, additional heuristics (e.g., boldness, spacing) could be added.
- Tested on various PDF structures, but edge cases (e.g., scanned PDFs) may require OCR integration in future rounds.
- The Dockerfile ensures all dependencies are installed within the container, and the image is based on `python:3.9-slim` to minimize size.