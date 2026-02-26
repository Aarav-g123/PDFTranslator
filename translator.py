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

def translate_pdf(input_path, output_path, target_lang="EN-US"):
    try:
        translator.translate_document_from_filepath(
            input_path,
            output_path,
            target_lang=target_lang
        )
        print(f"Successfully translated '{input_path}' to '{output_path}'")
    except deepl.DocumentTranslationException as error:
        print(f"Error translating document: {error}")
    except deepl.DeepLException as error:
        print(f"DeepL API error: {error}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python translator.py <input.pdf> <output.pdf> [TARGET_LANG_CODE]")
        print("Example: python translator.py document.pdf translated.pdf FR")
        sys.exit(1)
        
    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    target = sys.argv[3].upper() if len(sys.argv) > 3 else "EN-US"
    
    if not os.path.exists(input_pdf):
        print(f"Error: The file '{input_pdf}' does not exist.")
        sys.exit(1)
        
    translate_pdf(input_pdf, output_pdf, target)