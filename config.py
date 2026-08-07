import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
FILE_PATH = Path(os.getenv("FILE_PATH"))
LIMIT = int(os.getenv("LIMIT"))
