from pydantic import BaseSettings, Field


class TestSettings(BaseSettings):
    es_host: str = Field('http://127.0.0.1', env='ELASTIC_HOST')
    es_port: str = Field('9200', env='ELASTIC_PORT')
    redis_host: str = Field('http://127.0.0.1', env='REDIS_HOST')
    redis_port: str = Field('6379', env='REDIS_PORT')
    app_host: str = Field('http://127.0.0.1', env='APP_HOST')
    app_port: str = Field('8000', env='APP_PORT')

