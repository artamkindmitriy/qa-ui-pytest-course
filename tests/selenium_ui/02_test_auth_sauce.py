from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

"""
Тема: Selenium
Задача 4: Вход в систему

Условие: Зайти на сайт saucedemo.com, ввести логин и пароль, нажать кнопку входа.
"""


def test_sauce_login():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element("id", "user-name")
        username_field.send_keys("standard_user")

        password_field = driver.find_element("id", "password")
        password_field.send_keys("secret_sauce")

        button = driver.find_element("id", "login-button")
        button.click()

        assert "inventory.html" in driver.current_url
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 5: Выбор из списка

Условие: Зайти в каталог товаров, найти все товары с классом 'inventory_item', 
вывести количество и кликнуть на кнопку добавления второго товара.
"""


def test_sauce_item_selection():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element("id", "user-name").send_keys("standard_user")
        driver.find_element("id", "password").send_keys("secret_sauce")
        driver.find_element("id", "login-button").click()

        items = driver.find_elements("class name", "inventory_item")
        assert len(items) > 0, "Товары не найдены!"

        all_buttons = driver.find_elements("class name", "btn_inventory")
        all_buttons[1].click()
    finally:
        driver.quit()