import os
import psycopg2
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены: проверьте файл .env')
else:
    load_dotenv()

BASE_URL = 'https://www.sofascore.com/'

db_connection = psycopg2.connect(
    database="sofascore",
    user="postgres",
    password=os.getenv('POSTGRES_PASSWORD'),
    host="127.0.0.1",
    port="5433"
)

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'base',
            'filename': 'parsers_error.log',
        },
    },
    'loggers': {
        'db_logger': {
            'level': 'ERROR',
            'handlers': ['file'],
        },
        'request_logger': {
            'level': 'ERROR',
            'handlers': ['file']
        },
    },
}
