from bs4 import BeautifulSoup
from request_sofascore import get_page


def get_sports() -> dict:
    """
    Получение словаря актуальных видов спорта и ссылок на их страницы

    :return: словарь актуальных видов спорта и путей к их страницам
    """

    sports_dict = dict()
    soup = BeautifulSoup(get_page('/'), 'html5lib')
    sports_headers_blocks = soup.body.header.find('li', 'fSfoQg')
    sport_tags = sports_headers_blocks.find_all('li', 'sc-hLBbgP imkmkx')

    for sport in sport_tags:
        sports_dict[sport.span.text] = sport.a['href']

    return sports_dict

