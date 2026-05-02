import pytest

"""
Тема: Pytest
Задача 6: Тестирование поиска по списку

Условие: Есть класс Searcher, который проверяет наличие слова в списке без учета регистра. 
Использовать фикстуру с именами и параметризацию для проверки поиска.
"""

class Searcher:
    def __init__(self, data_list):
        self.data = data_list

    def is_present(self, word):
        return word.lower() in [item.lower() for item in self.data]

@pytest.fixture
def my_searcher():
    return Searcher(["Dmitriy", "Max", "Artem"])

class TestSearchSystem:
    @pytest.mark.parametrize("name, expected", [
        ("dmitriy", True),
        ("Max", True),
        ("Ivan", False)
    ])
    def test_search_results(self, my_searcher, name, expected):
        assert my_searcher.is_present(name) == expected


"""
Тема: Pytest
Задача 7: Валидатор email

Условие: Функция is_valid_email возвращает True, если есть символы @ и '.' 
С помощью параметризации проверить список невалидных имейлов и подтвердить, что возвращается False.
"""

def is_valid_email(email):
    return "@" in email and "." in email

@pytest.mark.parametrize("email, expected", [
    ("art-82inbox.ru", False),
    ("artamkindima@gmailcom", False)
])
def test_check_valid_email(email, expected):
    assert is_valid_email(email) == expected