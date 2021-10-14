from os import getenv
from dotenv import load_dotenv
from pathlib import Path


if Path('database/.env').exists():
    load_dotenv() # carregando arquivo com as variáveis (necessita do arquivo .env)

    credentials = {
        "host": getenv('host'),
        "user": getenv('user'),
        "password": getenv('password'),
        "database": getenv('database')
    }
else:
    print('File of configuration .env not found.')
    exit(1)