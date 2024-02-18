from langchain.schema import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openRouter import openRouterTranslate
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API= os.getenv('OPENAI_API_KEY_2')

articles=["Hall of Fame coach 'Lefty' Driesell dies at 92","Hall of Fame coach 'Lefty' Driesell dies at 92","Spieth DQ'd from Genesis for signing wrong score"]

prompt1 = ChatPromptTemplate.from_template("Generate a search term tailored to the user's interests, drawing from their past articles. Ensure the suggested term does not replicate any topics covered previously. The user's article history is provided as: {articles}")
model = ChatOpenAI(api_key=OPENAI_API)
chain1 = prompt1 | model | StrOutputParser()


def openAIQuery(language,searchHistory):
    query=chain1.invoke({"articles": articles})
    translation = openRouterTranslate(query, "spanish")
    return translation