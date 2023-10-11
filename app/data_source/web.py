from langchain.document_loaders import WebBaseLoader


def extract_text_from_web(web_url: str) -> str:
    """
    Function to get text from web url
    Args:
        web_url (str): the web url
    Return:
        web_text (str): the text in the web url
    """

    loader = WebBaseLoader("https://mount2lib.webflow.io/")
    data = loader.load()
    return "".join(f"{page.page_content} " for page in data)
    


