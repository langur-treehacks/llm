import json
from flask import Flask, request
from readability import lix_score
# from translator import translate_text
from openRouter import openRouterTranslate
from openAIChain import openAIQuery
from chromeQuery import searchDB
from flask_cors import CORS, cross_origin
from deepTranslator import deepTranslator

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!!</p>"
    
@app.route("/recommend",methods=['POST'])
@cross_origin()
def recommend():
    try:
        searchHistory= request.json['SearchHistory'] #list
    except:
        return "Search History not found",400
    try:
        readability= request.json['Readability']
    except:
        return "readability not found",400
    print("starting recommendation")
    query=openAIQuery(searchHistory,"Spanish")
    print("querying with "+ query)
    results= searchDB(query,3,readability)
    return json.dumps({"data":results})

@app.route("/meaning", methods=['GET'])
@cross_origin()
def meaning():
    try:
        target= request.json['Target']
    except:
        return "Target not found",400
    try:
        language= request.json['Language']
    except:
        return "Language not found",400
    print("translating")
    return deepTranslator(target,"spanish"),2000
    #return openRouterTranslate(target,language) ,200

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
    print("translating")
    for i in range(len(articleList)):
        target= articleList[i]
        if not target: 
            continue
        score= lix_score(target)
        if abs(float(score)-float(readability))<1: 
            print("still translating")
            # translation= openRouterTranslate(target,lang) 
            # print(translation)
            translation= deepTranslator(target,"spanish")
            ans.append([target.strip(),translation.strip()])
        if len(ans)==10: 
            break
    return json.dumps({"data":ans}),200

if __name__ == '__main__':  
   app.run(debug=True)