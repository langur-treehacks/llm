from trafilatura import fetch_url, extract
from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from readability import lix_score
from googlesearch import search
import json
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API= os.getenv('OPENAI_API_KEY_2')
prompt = ChatPromptTemplate.from_template(
    "Give an english summary of this article {text}. Keep it within 50 words"
)
model = ChatOpenAI(api_key=OPENAI_API)
chain1 = prompt | model | StrOutputParser()

ans=[]
urls=[]
with open("items.txt", 'r') as file:
    urlList = json.load(file)
urlList = urlList[3]
print(urlList)
for url in urlList:
    if not url:
        continue
    article={}
    downloaded = fetch_url(url)
    result = extract(downloaded,include_formatting=False,include_links=False,include_images=False, include_tables=False,target_language="es")
    if not result:
        print(url + " failed")
        continue
    score=lix_score(result)
    article["score"]=score
    article["summary"]=query=chain1.invoke({"text": result[:16000//4]})
    article["url"]=url
    ans.append(article)
print("finished searching for articles")
print(ans)

with open("articles3.txt", 'w') as file:
    json.dump(ans, file)