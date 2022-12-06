from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_events(sport_name: str, page_path: str, live: bool = False) -> list:
    """
    получение всех событий со страницы sofascore.com

    :param sport_name: название вида спорта
    :type sport_name: str
    :param page_path: путь к странице
    :type page_path: str
    :param live: парсинг всех событий или только live-событий
    :type live: bool

    :return: кортеж с информацией по каждому событию
    :rtype: tuple
    """

    events_list = []

    service = Service(executable_path="chromedriver")
    chrome = Chrome(service=service)

    base_url = 'https://www.sofascore.com'
    full_url = base_url + page_path

    # получаем всю страницу
    chrome.get(full_url)

    # Нажимаем кнопку All или Live в зависимости от параметра
    if live:
        button_live = chrome.find_element(by=By.CLASS_NAME, value='iYMA-DU')
        button_live.click()
    else:
        button_all = chrome.find_element(by=By.CLASS_NAME, value='JMbdj')
        button_all.click()

    chrome.implicitly_wait(1)

    # Поочерёдно кликаем на события
    event_frames = chrome.find_elements(by=By.CLASS_NAME, value='cNGQGm')
    for event_frame in event_frames:
        event_frame.click()

        chrome.implicitly_wait(1)

        # Забираем данные по игре из информационного окна об игре (справа сверху)
        # Набор извлекаемых данных может быть расширен
        event_data = chrome.find_element(by=By.CLASS_NAME, value='gRrJCY')
        event = event_data.find_element(by=By.TAG_NAME, value='ul')
        details = event.find_elements(by=By.TAG_NAME, value='li')
        players = event_data.find_elements(by=By.CLASS_NAME, value='ebVgVl')

        country = details[0].text
        cup = details[1].text
        player_1 = players[0].text
        player_2 = players[1].text

        events_list.append((sport_name, country, cup, player_1, player_2))

    # Выходим из драйвера браузера
    chrome.quit()

    return events_list
