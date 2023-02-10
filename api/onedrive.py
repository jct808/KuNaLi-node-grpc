import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    print("Azure Blob Storage Python quickstart sample")

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)


def upload_file_to_one_drive(file_name):
    print("one_drive")
