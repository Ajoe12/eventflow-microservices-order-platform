from dotenv import load_dotenv
import os

load_dotenv()

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")
ITEM_SERVICE_URL = os.getenv("ITEM_SERVICE_URL")