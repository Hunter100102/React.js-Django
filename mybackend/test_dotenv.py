from dotenv import load_dotenv
import os

print("Loading .env file...")

load_dotenv()

secret_key = os.getenv('SECRET_KEY')

print("Secret Key:", secret_key if secret_key else "Not found")
