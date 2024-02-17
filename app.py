import json
from flask import Flask, request
from readability import lix_score
from googletrans import Translator
app = Flask(__name__)

def translate_text(text, target_language='es'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

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
    except:
        return "Article not found",400
    try:
        readability= request.json['Readability']
    except:
        return "readability not found",400
    articleList= article.split(".")
    ans=[]
    for i in range(len(articleList)):
        target= articleList[i]
        if not target: 
            continue
        score= lix_score(target)
        if abs(float(score)-float(readability))<1: #THRESHOLD
            translation= translate_text(target) #STOPS AT UNICODE
            ans.append([target,translation])
    return json.dumps({"data":ans})

if __name__ == '__main__':  
   app.run(debug=True)