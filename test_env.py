import os
from dotenv import load_dotenv
load_dotenv()
print("DARAJA_CONSUMER_KEY:", os.getenv("DARAJA_CONSUMER_KEY"))