from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sources.elasticsearch import load_elasticsearch
from elasticsearch import helpers


client = load_elasticsearch()


loader = DirectoryLoader(
    path="./elastic_docs",
    glob="**/*.txt",
    loader_cls=TextLoader,
    show_progress=True
)


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



