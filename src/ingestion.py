import fitz
from docx import Document


def extract_pdf_text(file_path):

    doc = fitz.open(file_path)

    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def extract_docx_text(file_path):

    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_text(file_path):

    file_type = file_path.split(".")[-1].lower()

    if file_type == "pdf":
        return extract_pdf_text(file_path)

    elif file_type == "docx":
        return extract_docx_text(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {file_type}"
        )