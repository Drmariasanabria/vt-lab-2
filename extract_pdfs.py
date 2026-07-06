import sys
from pypdf import PdfReader
import json
import os

pdf_paths = {
    "lomloe": "/Users/mariasanabria/Desktop/PhD-Cursos-Master/Oposiciones/decretos/LOMLOE.pdf",
    "metodologia": "/Users/mariasanabria/Desktop/curso 25-26/master secundaria/metodologias/metodologia todo.pdf",
    "programacion": "/Users/mariasanabria/Desktop/curso 25-26/uds/programacion_didactica.pdf"
}

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

extracted_data = {}

for key, path in pdf_paths.items():
    print(f"Extracting {key} from {path}...")
    try:
        reader = PdfReader(path)
        text_content = []
        # Just extract first 10 pages for now to avoid massive files during scaffolding
        # We can increase this later or extract specific sections
        num_pages = min(len(reader.pages), 10)
        for i in range(num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                text_content.append(text)
        
        extracted_data[key] = {
            "title": key.upper(),
            "pages": num_pages,
            "content": "\n".join(text_content)
        }
        print(f"Successfully extracted {num_pages} pages for {key}.")
    except Exception as e:
        print(f"Error reading {path}: {e}")

# Save to JS file so we can load it directly in the browser without a server
with open(os.path.join(output_dir, 'pdf_content.js'), 'w', encoding='utf-8') as f:
    f.write("const pdfData = " + json.dumps(extracted_data, ensure_ascii=False, indent=2) + ";")
    
print("Extraction complete. Saved to data/pdf_content.js")
