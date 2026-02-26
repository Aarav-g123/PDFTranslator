# Open PDF Translator

A free, open-source tool to translate PDF files while attempting to preserve the original layout. It includes two translation engines: a DeepL Document API version and a free, keyless local version.

## Features
- **DeepL Mode (`translator_deepl.py`)**: The best option, translates entire documents natively. Requires a free DeepL API key.
- **Local Mode (`translator_local.py`)**: No API key required. Uses Google Translate's free endpoint and PyMuPDF to replace text over the original layout.

## Setup
1. Clone the repository.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. *(Optional)* If using DeepL, add your free API key to the `.env` file.

## Usage

**Using the Local (Free/No Key) Translator:**
```bash
python translator_local.py input.pdf output.pdf fr
```

**Using the DeepL Translator:**
```bash
python translator_deepl.py input.pdf output.pdf FR
```

*Note: The third argument is the target language code (e.g., `en`, `fr`, `es`, `de`). Defaults to English if omitted.*

If you like the tool give it a star.

If you find something easy to fix - make a request I'll probably look at it. 