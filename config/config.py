from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_NAME:        str =   "fastsocial"     
    DB_PASSWORD:    str =   "nill1234"
    DB_USER:        str =   "postgres"
    DB_HOST:        str =   "localhost"
    DB_PORT:        str =   "5432"
    SECRET_KEY:     str =   "i@+ms60tfhs^xfdal_vyp40l^xb8&z)r+cbfwgzr!s_3g3d3bf"
    ALGORITHM:      str =   "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:    int =   30

    # class Config:
    #     env_file    =   ".env"

settings = Settings()
