from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    acess_token_expire_minutes: int
    dbprod_url: str
    email_smtp: str
    email_user: str
    email_pass: str
    email_port: int

    class Config:
        env_file = ".env"


settings = Settings()