from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'FastAPI Notes'
