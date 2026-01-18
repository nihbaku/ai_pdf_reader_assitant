import pdf_reader
import embeddings

if __name__ == "__main__":

    text = pdf_reader.extract_text_from_pdf("../data/sample_backend_developer_cv.pdf")
    chunked_text = pdf_reader.chunk_text(text)

    #print(chunked_text)

    embeddings.test_embedder()

