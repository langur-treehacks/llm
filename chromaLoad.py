import json
import chromadb
client = chromadb.PersistentClient(path="./data")
# client.delete_collection(name="data")
collection = client.create_collection(name="data")

with open("articles2.txt", 'r') as file:
    articlesList = json.load(file)
documents = [article["summary"] for article in articlesList]
metadatas = [{"score": article["score"], "url": article["url"]} for article in articlesList]
ids = [f"id{i+1}" for i in range(len(articlesList))]
# collection.add(
#     documents=documents,
#     metadatas=metadatas,
#     ids=ids
# )
print(collection.count())
