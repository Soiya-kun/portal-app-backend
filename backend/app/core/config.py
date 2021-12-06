from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")
PROJECT_NAME = "portal app"
VERSION = "1.0.0"
API_PREFIX = "/api"

SECRET_KEY = config("SECRET_KEY", cast=Secret, default="")
POSTGRES_USER = config("POSTGRES_USER", cast=str, default="")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret, default="")
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="")

DATABASE_URL = config(
    "DATABASE_URL",
    default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",
)
