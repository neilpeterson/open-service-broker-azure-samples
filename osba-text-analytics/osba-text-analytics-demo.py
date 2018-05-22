import os
import json
import requests
import sys
import time

# Azure Analytics
AZURE_ANALYTICS_URI = os.environ['AZURE_ANALYTICS_URI']
AZURE_ANALYTICS_KEY = os.environ['AZURE_ANALYTICS_KEY']

# Get first argument
if len(sys.argv) > 1:
    arg = str(sys.argv[1])
else:
    arg = "This is a positive statement."

# Get sentiment
def analytics(text):
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': AZURE_ANALYTICS_KEY,
    }

    payload = {
    "documents": [
        {
        "language": "en",
        "id": "apex-demo",
        "text": text
        }
    ]
    }

    r = requests.post(AZURE_ANALYTICS_URI + "/sentiment", data=json.dumps(payload), headers=headers)

    try:
        return json.loads(r.text)['documents'][0]['score']
    except:
       print("Analytics error.")

returned_sentiment = analytics(arg)

print("==============================")

if returned_sentiment > 0.8:
    print("Provided text: " + arg)
    print("Positive sentiment:" + str(returned_sentiment))
else:
    print("Provided text: " + arg)
    print("Negative sentiment:" + str(returned_sentiment))

print("==============================")

# Loop to prevent demo from stopping
while True:
    print("That was cool, please shut me down now.")
    time.sleep(30)
