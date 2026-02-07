import uuid
from pathlib import Path
from pypdf import PdfReader

UPLOADS_DIR = '.instance/uploads'

def extract_text_from_pdf(file_path: str) -> str:
    """Reads text from PDF file strips whitespace and returns it."""

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text.strip()

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """Splits text into overlapping chunks."""

    word_list = text.split()
    chunk_list = []
    start = 0

    while start < len(word_list):
        end = min(start + chunk_size, len(word_list))
        chunk = " ".join(word_list[start:end])
        chunk_list.append(chunk)
        start += chunk_size - overlap

    return chunk_list

async def save_upload(file) -> str:
    """Saves an uploaded file for storage in UPLOADS_DIR.
    Returns the path to saved file as string."""

    uploads_dir = Path(UPLOADS_DIR)
    uploads_dir.mkdir(parents=True, exist_ok=True)

    original_path = Path(file.filename)
    unique_filename = (
        f'{original_path.stem}_{uuid.uuid4().hex[:8]}{original_path.suffix}'
    )
    file_path = uploads_dir / unique_filename

    with open(file_path, 'wb') as f:
        f.write(await file.read())
    return str(file_path)
