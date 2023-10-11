import cohere 
from langchain.embeddings import CohereEmbeddings


def init_cohere_embedding(COHERE_API_KEY: str):
    return CohereEmbeddings(model="small", cohere_api_key=COHERE_API_KEY)
