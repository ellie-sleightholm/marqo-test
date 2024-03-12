from datasets import load_dataset 
from marqo import Client

# Loading validation splits for English and Deutsch datasets
dataset_en = load_dataset('multi_eurlex', 'en', split="validation")
dataset_de = load_dataset('multi_eurlex', 'de', split="validation")

# Set up the client. We tell the Marqo client to connect with the Marqo 
# Docker container that should have been run previously.
mq = Client("http://localhost:8882")

# Tell Marqo to create the multilingual index
mq.create_index(index_name='my-multilingual-index', model='stsb-xlm-r-multilingual')


mq.index(index_name="my-multilingual-index").add_documents(
    device="cuda", auto_refresh=False,
    documents=[{
        "_id": doc_id,
        "language": lang,
        "text": sub_doc,
        "celex_id": doc["celex_id"],
        "labels": str(doc["labels"])
    }]
)