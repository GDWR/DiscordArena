from os import environ

TOKEN = environ.get("TOKEN")
if not TOKEN:
    raise EnvironmentError("Missing Environment Variable: TOKEN")

API_URL = environ.get("API_URL")
if not API_URL:
    raise EnvironmentError("Missing Environment Variable: API_URL")
