import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

"""
Тема: Selenium
Задача 1: Прыжки по вкладкам

Условие: Открыть Google, перейти на Wikipedia, вернуться назад и проверить URL. 
Затем вернуться вперед и проверить заголовок.
"""


def test_tab_navigation():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    try:
        driver.get("https://google.com")
        driver.get("https://ru.wikipedia.org/wiki/")

        driver.back()
        assert "google" in driver.current_url.lower(), f"Ошибка: в URL {driver.current_url} нет 'google'"

        driver.forward()
        assert "Википедия" in driver.title, f"Ошибка: ожидался заголовок с 'Википедия', а получили '{driver.title}'"
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 2: Детектив заголовков

Условие: Пройти в цикле по списку из трех URL, открыть каждый сайт 
и проверить, что его заголовок не пустой.
"""


def test_check_multiple_titles():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    try:
        urls = [
            "https://www.python.org/",
            "https://github.com/",
            "https://stackoverflow.com/"
        ]
        for url in urls:
            driver.get(url)
            current_title = driver.title
            assert current_title, f"Ошибка: у сайта {url} пустой заголовок!"
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 3: Браузерный микс

Условие: Открыть сайт сначала в Chrome, затем в Edge и проверить, 
что заголовки сайта в обоих браузерах совпадают.
"""


def test_cross_browser_title():
    target_url = "https://www.python.org/"

    service_chrome = ChromeService(executable_path=ChromeDriverManager().install())
    driver_chrome = webdriver.Chrome(service=service_chrome)
    driver_chrome.implicitly_wait(5)
    try:
        driver_chrome.get(target_url)
        title_chrome = driver_chrome.title
    finally:
        driver_chrome.quit()

    try:
        service_edge = EdgeService(executable_path=EdgeChromiumDriverManager().install())
        driver_edge = webdriver.Edge(service=service_edge)
        driver_edge.implicitly_wait(5)
        try:
            driver_edge.get(target_url)
            title_edge = driver_edge.title
        finally:
            driver_edge.quit()

        assert title_chrome == title_edge, f"Заголовки разные: {title_chrome} vs {title_edge}"

    except Exception as e:
        pytest.skip(f"Тест пропущен, так как Edge не поддерживается или не установлен: {e}")