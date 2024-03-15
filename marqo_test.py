import marqo
import pprint

# Set up the client. We tell the Marqo client to connect with the Marqo 
# Docker container that should have been run previously.
mq = marqo.Client(url='http://localhost:8882')

# Tell Marqo to create the multilingual index
mq.create_index("my-first-index")

# Indexing
mq.index("my-first-index").add_documents([
    {
        "Title": "The Travels of Marco Polo",
        "Description": "A 13th-century travelogue describing Polo's travels"
    }, 
    {
        "Title": "Extravehicular Mobility Unit (EMU)",
        "Description": "The EMU is a spacesuit that provides environmental protection, "
                       "mobility, life support, and communications for astronauts",
        "_id": "article_591"
    }],
    tensor_fields=["Description"]
)

results = mq.index("my-first-index").search(
    q="What is the best outfit to wear on the moon?"
)

# Print out the results 
pprint.pprint(results)

# Other basic operators

# Retrieve a document by ID
result = mq.index("my-first-index").get_document(document_id="article_591")

# Get information about an index
results = mq.index("my-first-index").get_stats()

# Perform a keyword search
result = mq.index("my-first-index").search('marco polo', search_method=marqo.SearchMethods.LEXICAL)
