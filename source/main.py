import pdf_reader

if __name__ == "__main__":

    text = pdf_reader.extract_text_from_pdf("../data/sample_backend_developer_cv.pdf")

    print(text)

