from azure.storage.blob import BlockBlobService, PublicAccess
from time import sleep
import os

# Azure Storage
AZURE_STORAGE_ACCT = os.environ['AZURE_STORAGE_ACCT']
AZURE_KEY = os.environ['AZURE_KEY']
CONTAINER = os.environ['CONTAINER']

block_blob_service = BlockBlobService(account_name=AZURE_STORAGE_ACCT, account_key=AZURE_KEY)
f = open("hello-osba","w+")

while True:
    file = block_blob_service.list_blobs(CONTAINER)

    if len(file.items) == 0:
        print("Creating file..")
        block_blob_service.create_blob_from_path(CONTAINER, "hello-osba", "./hello-osba")
    else:
        print("File exsists..")

    sleep(30)