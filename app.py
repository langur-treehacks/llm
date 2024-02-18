import json
from flask import Flask, request
from readability import lix_score
# from translator import translate_text
from openRouter import openRouterTranslate
from chromeQuery import searchDB
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
    query="I like sports"#awaiting search history summarizer
    results= searchDB(query,3,readability)
    return json.dumps({"data":results})

@app.route("/meaning", methods=['GET'])
def meaning():
    try:
        target= request.json['Target']
    except:
        return "Target not found",400
    try:
        language= request.json['Language']
    except:
        return "Language not found",400
    return openRouterTranslate(target,language) ,200

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
    try:
        lang= request.json['Language']
    except:
        return "Article not found",400
    articleList= article.split(".")
    ans=[]
    for i in range(len(articleList)):
        target= articleList[i]
        if not target: 
            continue
        score= lix_score(target)
        if abs(float(score)-float(readability))<1: 
            translation= openRouterTranslate(target,lang) 
            # print(translation)
            ans.append([target,translation])
    return json.dumps({"data":ans}),200

if __name__ == '__main__':  
   app.run(debug=True)