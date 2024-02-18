import json
import chromadb
client = chromadb.PersistentClient(path="./data")
collection = client.get_collection(name="data")
def searchDB(query,n,score):
    output= collection.query(
        query_texts=[query],
        n_results=3
    )
    # print(output)
    for i in range (len(output["metadatas"][0])):
        output["metadatas"][0][i]["summary"]=output["documents"][0][i]
    scores= output['metadatas'][0]
    sortedScores= sorted(scores, key=lambda x: abs(x['score']-float(score)))
    return sortedScores[:n]
if __name__ == '__main__':
    print(searchDB("I like sports",2,6.9))