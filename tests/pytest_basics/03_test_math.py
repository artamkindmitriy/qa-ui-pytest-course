import pytest

"""
Тема: Pytest
Задача 3: Параметризация

Условие: Написать один тест test_is_adult, используя декоратор @pytest.mark.parametrize.
Передать в него три набора данных для проверки совершеннолетия (18 -> True, 20 -> True, 17 -> False).
"""

def is_adult(age):
    return age >= 18

@pytest.mark.parametrize("age, expected", [
    (18, True),
    (20, True),
    (17, False)
])
def test_is_adult(age, expected):
    assert is_adult(age) == expected


"""
Тема: Pytest
Задача 4: Группировка тестов в Классы

Условие: Создать фикстуру calc, которая возвращает объект Calculator(). 
Создать тестовый класс TestCalculator и проверить методы add и multiply.
"""

class Calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

@pytest.fixture
def calc():
    return Calculator()

class TestCalculator:
    def test_addition(self, calc):
        assert calc.add(2, 3) == 5

    def test_multiplication(self, calc):
        assert calc.multiply(2, 3) == 6


"""
Тема: Pytest
Задача 5: Граничные значения

Условие: Есть функция check_access(age), возвращающая True при возрасте от 14 лет. 
С помощью параметризации проверить граничные значения: 13 лет, 14 лет и 15 лет.
"""

def check_access(age):
    return age >= 14

@pytest.mark.parametrize("age, expected", [
    (13, False),
    (14, True),
    (15, True),
])
def test_check_age(age, expected):
    assert check_access(age) == expected