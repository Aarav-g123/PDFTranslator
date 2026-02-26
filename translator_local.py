import sys
import os
import fitz
from deep_translator import GoogleTranslator

def translate_pdf_local(input_path, output_path, target_lang="en"):
    doc = fitz.open(input_path)
    translator = GoogleTranslator(source='auto', target=target_lang.lower())

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if b.get('type') == 0:
                for line in b["lines"]:
                    for span in line["spans"]:
                        original_text = span["text"].strip()
                        if original_text:
                            try:
                                translated_text = translator.translate(original_text)
                                rect = fitz.Rect(span["bbox"])
                                
                                page.add_redact_annot(rect, text="")
                                page.apply_redactions()
                                
                                page.insert_text(
                                    (rect.x0, rect.y1),
                                    translated_text,
                                    fontsize=span["size"],
                                    fontname="helv"
                                )
                            except Exception:
                                pass

    doc.save(output_path)
    print(f"Successfully translated '{input_path}' to '{output_path}'")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python translator_local.py <input.pdf> <output.pdf> [target_lang]")
        sys.exit(1)
        
    in_pdf = sys.argv[1]
    out_pdf = sys.argv[2]
    target = sys.argv[3] if len(sys.argv) > 3 else "en"
    
    if not os.path.exists(in_pdf):
        print(f"Error: '{in_pdf}' does not exist.")
        sys.exit(1)
        
    translate_pdf_local(in_pdf, out_pdf, target)