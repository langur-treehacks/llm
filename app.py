import json
from flask import Flask, request
from readability import lix_score
# from translator import translate_text
from openRouter import openRouterTranslate
from openAIChain import openAIQuery
from chromeQuery import searchDB
from flask_cors import CORS, cross_origin
from deepTranslator import deepTranslator
from monsterApi import monsterapiRecommender
from openaiChat import openAIChat

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
    #query=openAIQuery(searchHistory,"Spanish")
    query=monsterapiRecommender(" ".join(searchHistory))
    if query==None:
        query="sports"
    query= deepTranslator(query,"spanish")
    print("querying with "+ query)
    results= searchDB(query,3,readability)
    return json.dumps({"data":results})

@app.route("/meaning", methods=['POST'])
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
    return deepTranslator(target,"spanish"),200
    #return openRouterTranslate(target,language) ,200

@app.route("/translate",methods=['POST'])
@cross_origin()
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

conversation=[]
@app.route("/chat", methods=['POST'])
@cross_origin()
def chat():
    if len(conversation)>10:
        conversation.pop(0)
    try:
        userConversation= request.json['UserConversation'] #first message could be user history
    except:
        return "UserConversation not found",400
    try:
        readability= request.json['Readability']
    except:
        return "Readability not found",400
    if len(conversation)==0:
        conversation.append({"role": "system", "content": "You are a friendly conversational agent whose goal is to converse with the user in Spanish. The currently user has a reading ability of "+str(float(readability))+" out of 10. Facilitate the entire conversation in Spanish and in a fun and engaging manner"})
    print("generating response")
    for chat in userConversation:
        conversation.append({"role": "user", "content": chat})
    response= openAIChat(conversation)
    conversation.append({"role": "assistant", "content": response})
    return conversation,200

if __name__ == '__main__':  
   app.run(debug=True)