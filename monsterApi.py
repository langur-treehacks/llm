import json
import requests
import os   
from dotenv import load_dotenv
load_dotenv()
MONSTERAPI_TOKEN= os.getenv('MONSTERAPI_TOKEN')

# Replace this with the actual API endpoint you're targeting
url = "https://88525734-5bc6-42b4-83a0-c3eaf73e9e52.monsterapi.ai/generate"

def monsterapiInference(prompt):
    # The data you want to send in the POST request
    data = {
    "input_variables": {
        "prompt": "This is the user's browsing history: "+ prompt +" summarise user's interest in a concise statement. Output a statement that is less than 5 words"
    },
    "prompt": "This is the user's browsing history: "+ prompt +" summarise user's interest in a concise statement. Output a statement that is less than 5 words",
    "stream": False,
    "max_tokens": 20,
    "n": 1,
    "best_of": 1,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "repetition_penalty": 1,
    "temperature": 1,
    "top_p": 1,
    "top_k": -1,
    "min_p": 0,
    "use_beam_search": False,
    "length_penalty": 1,
    "early_stopping": False
    }

    # The headers to include in the request (if required)
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {MONSTERAPI_TOKEN}",
        # Include other headers here if needed, e.g., authorization headers
    }

    # Make the POST request
    response = requests.post(url, json=data, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        print("Request successful.")
        # Process the response data if needed
        response=json.loads(response.json())["text"][0].replace('\t', '').strip()
        print(response)
        return response
    else:
        print(f"Request failed with status code {response.status_code}.")
        return None
