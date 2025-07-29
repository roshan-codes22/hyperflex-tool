from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sources.elasticsearch import load_elasticsearch
from elasticsearch import helpers


loader = PyPDFLoader("https://arxiv.org/pdf/2103.15348.pdf")

client = load_elasticsearch()

data = loader.load()

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=512, chunk_overlap=256
)
docs = loader.load_and_split(text_splitter=text_splitter)

helpers.bulk(
    client,
    [
        {
            "_index": "minilm-l12-v2-index",
            "pipeline": "text-embeddings",
            "_source": {
                "text": doc.page_content,
                "page_number": i,
            },
        }
        for i, doc in enumerate(docs)
    ],
    request_timeout=60,
)



