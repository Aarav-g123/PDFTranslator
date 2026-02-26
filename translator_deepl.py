import os
import sys
import deepl
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("DEEPL_API_KEY")

if not API_KEY:
    print("Error: DEEPL_API_KEY not found in .env file.")
    sys.exit(1)

translator = deepl.Translator(API_KEY)

def translate_pdf_deepl(input_path, output_path, target_lang="EN-US"):
    try:
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang=target_lang
        )
        print(f"Successfully translated '{input_path}' to '{output_path}'")
    except Exception as error:
        print(f"Translation failed: {error}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python translator_deepl.py <input.pdf> <output.pdf> [TARGET_LANG]")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    target = sys.argv[3].upper() if len(sys.argv) > 3 else "EN-US"
    
    if not os.path.exists(input_pdf):
        print(f"Error: '{input_pdf}' does not exist.")
        sys.exit(1)
        
    translate_pdf_deepl(input_pdf, output_pdf, target)