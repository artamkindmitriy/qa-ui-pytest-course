"""
Тема: Pytest
Задача 1: Проверка системы скидок

Условие: Есть функция, которая рассчитывает цену со скидкой.
Если сумма покупки больше 1000, применяется скидка 10%.
Проверить с помощью паттерна Arrange-Act-Assert, что для цены 1200 результат равен 1080.
"""

def get_discounted_price(price):
    if price > 1000:
        return price * 0.9
    return price


def test_discount_is_applied():
    price = 1200

    result = get_discounted_price(price)

    assert result == 1080