import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

GAME_FILENAME = os.getenv("GAME_FILENAME") or "data.csv"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", GAME_FILENAME)