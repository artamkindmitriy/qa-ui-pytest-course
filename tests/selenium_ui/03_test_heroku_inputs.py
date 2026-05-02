from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

"""
Тема: Selenium
Задача 6: Форма с секретом

Условие: Ввести в числовое поле значение 1000, очистить его, ввести 999 
и проверить через get_attribute('value').
"""
def test_numeric_input():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://the-internet.herokuapp.com/inputs")

        field = driver.find_element("xpath", "//input[@type='number']")
        field.send_keys("1000")
        field.clear()
        field.send_keys("999")

        current_value = field.get_attribute("value")
        assert current_value == "999", f"Ожидали 999, но получили {current_value}"
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 7: Выбор и проверка

Условие: Проверить состояние чекбоксов. Если первый не выбран — выбрать его. 
Если второй выбран — снять выделение.
"""
def test_checkboxes_state():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")

        checkboxes = driver.find_elements("xpath", "//input[@type='checkbox']")

        if not checkboxes[0].is_selected():
            checkboxes[0].click()

        if checkboxes[1].is_selected():
            checkboxes[1].click()

        assert checkboxes[0].is_selected() is True
        assert checkboxes[1].is_selected() is False
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 8: Работа с мышкой (Hover на первый профиль)

Условие: С помощью ActionChains навести курсор на первую аватарку 
и проверить, что появился текст 'name: user1'.
"""
def test_hover_first_user():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://the-internet.herokuapp.com/hovers")

        hovers = driver.find_elements("xpath", "//div[@class='figure']")
        actions = ActionChains(driver)
        actions.move_to_element(hovers[0]).perform()

        user_info = driver.find_element("xpath", "//h5[text()='name: user1']")
        assert user_info.text == "name: user1"
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 9: Задача на инпуты

Условие: Зайти на страницу восстановления пароля, ввести email, 
прочитать его через get_attribute и очистить поле.
"""
def test_forgot_password_input():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://the-internet.herokuapp.com/forgot_password")

        field = driver.find_element("id", "email")
        field.send_keys("test@test.com")

        current_value = field.get_attribute("value")
        assert current_value == "test@test.com"

        field.clear()
    finally:
        driver.quit()


"""
Тема: Selenium
Задача 10: Задача на Hover (Hover на третий профиль)

Условие: С помощью ActionChains навести мышку на третью карточку 
и проверить появление текста 'name: user3'.
"""
def test_hover_third_user():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://the-internet.herokuapp.com/hovers")

        figures = driver.find_elements("class name", "figure")
        actions = ActionChains(driver)
        actions.move_to_element(figures[2]).perform()

        user_info = driver.find_element("xpath", "//h5[text()='name: user3']")
        assert user_info.text == "name: user3"
    finally:
        driver.quit()