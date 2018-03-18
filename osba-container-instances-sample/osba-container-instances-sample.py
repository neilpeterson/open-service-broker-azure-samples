import os
import requests
import time

# ACI Public IP Address
ACI_PIP = os.environ['ACI_PIP']
ACI_URL = "http://" + ACI_PIP

while True:
    r = requests.get(ACI_URL)

    if r.status_code == 200:
        print("Hello OSB ACI Container is UP..")
    else:
        print("Hello OSB ACI Container is Down..")

    time.sleep(5)