from openai import OpenAI
from os import getenv
import os
from dotenv import load_dotenv
load_dotenv()

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)

def openRouterTranslate(targetSentence, targetLanguage):
    completion = client.chat.completions.create(
    model="recursal/eagle-7b",
    messages=[
        {
        "role": "user",
        "content": "Translate this to "+ targetLanguage +" :"+ targetSentence,
        },
    ],
    )
    return completion.choices[0].message.content
if __name__=="__main__":
    print(openRouterTranslate("I like to play soccer","spanish"))