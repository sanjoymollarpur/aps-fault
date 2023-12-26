import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
database_url = os.getenv("MONGO_db_url")

# Use the variables in your code
print(f"Database URL: {database_url}")
# print(f"API Key: {api_key}")
# print(f"Debug Mode: {debug_mode}")
