from dotenv import load_dotenv
import os

load_dotenv() 

class Secrets:
    ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
    CERTS_PATH = os.getenv("CERTS_PATH")

secrets = Secrets()