from time import sleep
import os
import pymongo

# Cosmos DB
MONGO_CONNECTION_STRING = os.environ['MONGO_CONNECTION_STRING']

# Build Mongo DB client
client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['hello-osba']

while True:

    db.data.insert_one({"hello":"osba"})
    sleep(30)

