import requests
from typing import Optional
from config import BASE_URL, logging_config
import logging.config

logging.config.dictConfig(logging_config)
logger = logging.getLogger('request_logger')


def get_page(page_path: str) -> Optional[str]:
    """
    Запрос страницы с сайта sofascore.com

    :param page_path: путь до страницы
    :type page_path: str
    :return: html-код страницы или ничего в случае ошибки
    :rtype: Optional[str]
    """

    full_url = BASE_URL + page_path
    try:
        response = requests.get(full_url, timeout=5)
        return response.text
    except requests.exceptions.ConnectionError as error:
        logger.error(error)
        exit(1)


print(get_page(''))
