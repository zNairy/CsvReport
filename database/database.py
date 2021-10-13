from os import getenv
from dotenv import load_dotenv

load_dotenv() # carregando arquivo com as variáveis (necessita do arquivo .env)

credentials = {
    "host": getenv('host'),
    "user": getenv('user'),
    "password": getenv('password'),
    "database": getenv('database')
}