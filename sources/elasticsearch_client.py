from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def load_elasticsearch(): 
    es = Elasticsearch (
        "https://2bad39def63f4e83b74866d9fcd13749.us-central1.gcp.cloud.es.io:443",
        api_key=api_key
    )
    return es

