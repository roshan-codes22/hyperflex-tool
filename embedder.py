from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

loader = DirectoryLoader(
    path="./elastic_docs",
    glob="**/*.txt",
    loader_cls=TextLoader,
    show_progress=True
)

docs=loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=text_splitter.split_documents(docs)

embedding_model= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

vectorstore=FAISS.from_documents(chunks, embedding_model)
vectorstore.save_local("elastic_index")