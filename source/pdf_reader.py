from pypdf import PdfReader

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
