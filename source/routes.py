from litestar import post, Request
from litestar.datastructures import UploadFile
from pydantic import BaseModel
from embeddings import add_document
from rag import rag_answer
from pdf_reader import extract_text_from_pdf, chunk_text, save_upload

from pathlib import PurePath

class AskRequest(BaseModel):
    question: str

@post("/ask")
async def ask(data: AskRequest) -> dict:
    answer = rag_answer(data.question)
    return {"question": data.question, "answer": answer}

@post("/upload/pdf")
async def upload_pdf(request: Request) -> dict:
    form_data = await request.form()
    print(form_data)
    file = form_data.get("file")
    if not isinstance(file, UploadFile):
        return {"error": "No file uploaded"}

    path = await save_upload(file)
    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    for chunk in chunks:
        add_document(chunk)
    return {"status": "ok", "chunks_added": len(chunks)}
