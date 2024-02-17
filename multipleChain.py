from operator import itemgetter
from trafilatura import fetch_url, extract
from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from readability import lix_score
from web import search_and_extract
from translate import Translator
import os
from dotenv import load_dotenv
load_dotenv()
#chain 1: based on past articles, sugget a relevant search term in spanish
#chain 2: based on the search term, suggest a relevant article that matches user's readability level
#-> pull the top 10 articles
#-> calculate the readability score
#-> suggest the article with the closest readability scor
#chain 3: summarise article
OPENAI_API= os.getenv('OPENAI_API_KEY_2')

articles=["Hall of Fame coach 'Lefty' Driesell dies at 92","Hall of Fame coach 'Lefty' Driesell dies at 92","Spieth DQ'd from Genesis for signing wrong score"]

prompt1 = ChatPromptTemplate.from_template("Generate a search term tailored to the user's interests, drawing from their past articles. Ensure the suggested term does not replicate any topics covered previously. The user's article history is provided as: {articles}")
prompt2 = ChatPromptTemplate.from_template(
    "Give an english summary of this article {text}"
)

model = ChatOpenAI(api_key=OPENAI_API)
chain1 = prompt1 | model | StrOutputParser()
chain2= prompt2 | model | StrOutputParser()
query=chain1.invoke({"articles": articles, "language": "spanish"})
translator= Translator(to_lang="Spanish")
translation = translator.translate(query)
print(translation)
from googlesearch import search
ans=[]
urls=[]
for url in search(translation, num_results=5):
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
    article["text"]=result
    article["url"]=url
    ans.append(article)
print("finished searching for articles")
user_readability= 5
sorted_res = sorted(ans, key=lambda x: abs(x['score'] - user_readability))
top_3_articles = sorted_res[:3]
for article in top_3_articles:
    url= article["url"]
    downloaded = fetch_url(url)
    result = extract(downloaded,include_formatting=False,include_links=False,include_images=False, include_tables=False,target_language="es")
    summary=chain2.invoke({"text": result})
    article["summary"]=summary
print(top_3_articles)