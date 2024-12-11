from flask import request, abort
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ENABLE_TOKEN_BASED_ACCESS = os.getenv("ENABLE_TOKEN_BASED_ACCESS", "False").lower() == "true"
AUTH_ENABLED = os.getenv("AUTH_ENABLED", "True").lower() == "true"
ALLOWED_HOSTS = set(os.getenv("ALLOWED_HOSTS", "").split(","))
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "")
