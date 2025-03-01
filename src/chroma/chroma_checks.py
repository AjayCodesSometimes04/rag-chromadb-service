import chromadb

# Check collection list
client = chromadb.HttpClient(host="localhost", port=8000)
collections = client.list_collections()
print(collections)