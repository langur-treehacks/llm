import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
OPENAI_API= os.getenv('OPENAI_API_KEY_2')

def openAIChat(conversation):
    url = "https://api.openai.com/v1/chat/completions"
    # The data you want to send in the POST request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation
    }

    # The headers to include in the request (if required)
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {OPENAI_API}",
        # Include other headers here if needed, e.g., authorization headers
    }

    # Make the POST request
    response = requests.post(url, json=data, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        # print("Request successful.")
        # Process the response data if needed
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Request failed with status code {response.status_code}.")
        return None
if __name__=="__main__":
    openAIChat