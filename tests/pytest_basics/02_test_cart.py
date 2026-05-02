"""
Тема: Pytest
Задача 2: Фикстура для "Корзины покупок”

Условие: У нас есть класс Cart, который хранит список товаров. Нам нужно проверять,
что товары добавляются корректно, используя фикстуру для создания объекта корзины.
"""

import pytest

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

@pytest.fixture
def cart():
    return Cart()

def test_add_to_cart(cart):
    cart.add_item("Apple")

    assert "Apple" in cart.items