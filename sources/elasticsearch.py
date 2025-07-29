from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def load_elasticsearch(): 
    es = Elasticsearch (
        "https://hyperflex-project-de8318.es.us-east-1.aws.elastic.cloud:443",
        api_key=api_key
    )
    return es

