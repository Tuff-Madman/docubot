import docx 

def extract_text_from_docx(docx_file: str) -> str:
    """
    Function to get text from docx file
    Args:
        docx_file (str): the filepath of docx file
    Returns:
        docx_text (str): the text from docx file
    """
    doc = docx.Document(docx_file)
    return "".join(f"{docpara.text} " for docpara in doc.paragraphs)
