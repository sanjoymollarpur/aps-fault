import pymongo
import pandas as pd
import json
from dataclasses import dataclass
# Provide the mongodb localhost url to connect python to mongodb.
import os

import os
from dotenv import load_dotenv
print(f"Loading environment variable from .env file")
load_dotenv()


# Access environment variables
database_url = os.getenv("MONGO_db_url")

# Use the variables in your code
print(f"Database URL: {database_url}")
# print(f"API Key: {api_key}")
# print(f"Debug Mode: {debug_mode}")




# @dataclass
# class EnvironmentVariable:
#     mongo_db_url:str = os.getenv("mongodb+srv://sanjoy:sanjoyy@cluster0.kftnejs.mongodb.net/?retryWrites=true&w=majority")
#     aws_access_key_id:str = os.getenv("AWS_ACCESS_KEY_ID")
#     aws_access_secret_key:str = os.getenv("AWS_SECRET_ACCESS_KEY")





# env_var = EnvironmentVariable()
# print(env_var.mongo_db_url)
# mongo_client = pymongo.MongoClient("mongodb+srv://sanjoy:sanjoyy@cluster0.kftnejs.mongodb.net/?retryWrites=true&w=majority")
mongo_client = pymongo.MongoClient(database_url)
TARGET_COLUMN = "class"

print(mongo_client)