import json
from flask import Flask, request
from readability import lix_score
# from translator import translate_text
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
        # if abs(float(score)-float(readability))<1: #THRESHOLD
        #     translation= translate_text(target) #STOPS AT UNICODE
        #     ans.append([target,translation])
    return json.dumps({"data":ans})

if __name__ == '__main__':  
   app.run(debug=True)