import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Test if the environment variables are loaded correctly
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")
allowed_hosts = os.getenv("ALLOWED_HOSTS")

print("Database URL:", database_url)
print("Secret Key:", secret_key)
print("Debug Mode:", debug_mode)
print("Allowed Hosts:", allowed_hosts) 