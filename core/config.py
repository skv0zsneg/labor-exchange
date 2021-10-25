from starlette.config import Config


config = Config(".env")

DATABASE_URL = config("EE_DATABASE_URL", cast=str, default="")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = 'HS256'
SECRET_KEY = config('EE_SECRET_KEY', cast=str, default='e2aa9ef3005fede438d746ba9d5d8519e1f7aa1210093ec79c79d195864a5dba')
