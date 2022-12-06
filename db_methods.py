from psycopg2 import sql
from psycopg2 import Error, OperationalError
from config import db_connection, logging_config
import logging.config

logging.config.dictConfig(logging_config)
logger = logging.getLogger('db_logger')


def create_table(table_name: str) -> None:
    """
    Создание таблицы для хранение всех событий:

    :param table_name: имя таблицы
    :type table_name: str
    :return: None
    """

    try:
        with db_connection as connection:
            with connection.cursor() as cursor:
                query = """
                CREATE TABLE IF NOT EXISTS {} (
                    id SERIAL PRIMARY KEY,
                    sport TEXT NOT NULL,
                    country TEXT NOT NULL,
                    cup TEXT NOT NULL,
                    player_1 TEXT NOT NULL,
                    player_2 TEXT NOT NULL
                    );
                """
                cursor.execute(sql.SQL(query).format(sql.Identifier(table_name)))
    except (Error, OperationalError) as db_error:
        logger.error(db_error)


def add_records(table_name: str, records: list) -> None:
    """
    Добавление записей в таблицу

    :param table_name: имя таблицы
    :type table_name: str
    :param records: список записей
    :type records: list

    :return: None
    """

    try:
        with db_connection as connection:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO {} (sport, country, cup, player_1, player_2) 
                VALUES (%s,%s,%s,%s,%s)
                """
                cursor.executemany(sql.SQL(query).format(sql.Identifier(table_name)), records)
    except (Error, OperationalError) as db_error:
        logger.error(db_error)


def clear_live() -> None:
    """
    Очистка таблицы live_events

    :return: None
    """

    try:
        with db_connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE live_events")
    except (Error, OperationalError) as db_error:
        logger.error(db_error)


if __name__ == '__main__':
    create_table('all_events')
    create_table('live_events')
