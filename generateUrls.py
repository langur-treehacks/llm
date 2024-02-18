# from trafilatura import fetch_url, extract
# from langchain.schema import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
from readability import lix_score
# from translator import translate_text
from googlesearch import search
import json
import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API= os.getenv('OPENAI_API_KEY_2')
ans=[]
urls=[]
for url in search("carreras de fórmula 1", num_results=10):
    urls.append(url)
#     if not url:
#         continue
#     article={}
#     downloaded = fetch_url(url)
#     result = extract(downloaded,include_formatting=False,include_links=False,include_images=False, include_tables=False,target_language="es")
#     if not result:
#         print(url + " failed")
#         continue
#     score=lix_score(result)
#     article["score"]=score
#     article["text"]=result
#     article["url"]=url
#     ans.append(article)
# print("finished searching for articles")
# print(ans)
with open("items.txt") as feedsjson:
    feeds = json.load(feedsjson)
feeds.append(urls)
with open("items.txt", 'w') as file:
    # Convert the list to a JSON-formatted string and write it to the file
    json.dump(feeds, file)


with open("items.txt", 'r') as file:
    my_retrieved_list = json.load(file)

# my_retrieved_list now contains the original Python list
# print(my_retrieved_list)