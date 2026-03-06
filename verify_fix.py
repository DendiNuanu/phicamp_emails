import os
from dotenv import load_dotenv

# Path to .env and phicamp_app.py
dotenv_path = r"c:\phicamp-wifi\.env"
app_path = r"c:\phicamp-wifi\phicamp_app.py"

# Load .env
load_dotenv(dotenv_path)

# Mocking the logic in phicamp_app.py
DASHBOARD_PASSWORD = os.getenv("DASHBOARD_PASSWORD", "default-password")

print(f"Password from .env: {DASHBOARD_PASSWORD}")

if DASHBOARD_PASSWORD == "Bali0361":
    print("SUCCESS: Password correctly loaded from .env")
else:
    print(f"FAILURE: Expected 'Bali0361', got '{DASHBOARD_PASSWORD}'")
