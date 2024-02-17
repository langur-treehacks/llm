import json
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!!</p>"

    
@app.route("/recommend",methods=['POST'])
def recommend():
    try:
        searchHistory= request.json['SearchHistory'] #list
    except:
        return "Search History not found",400
    try:
        readability= request.json['Readability']
    except:
        return "readability not found",400
    return json.dumps({"data":{"summary": "this is a summary of the article", "readability": 3,"link":"https://cnnespanol.cnn.com/2024/02/17/putin-navalny-nombre-amenaza-trax/"}})

@app.route("/translate",methods=['POST'])
def translate():
    try:
        article= request.json['Article']
        print(article)
        articleList= article.split(".")
        ans=[]
        for i in range(1,3):
            target= articleList[i]
            translation="This is a translated sentence"
            ans.append([target,translation])
    except:
        return "Article not found",400
    try:
        readability= request.json['Readability']
    except:
        return "readability not found",400
    return json.dumps({"data":ans})

if __name__ == '__main__':  
   app.run(debug=True)