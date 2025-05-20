import pytest
from praktikum.burger import Burger
from unittest.mock import Mock

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:
    def test_burger_init(self):
        burger = Burger()

        assert burger.bun is None and burger.ingredients == []

    @pytest.mark.parametrize('b_name, b_price', [('AbCd', 1.5)])
    def test_burger_set_buns(self, b_name, b_price):
        bun = Mock()
        bun.configure_mock(name=b_name, price=b_price)

        burger = Burger()
        burger.set_buns(bun=bun)

        assert burger.bun == bun

    @pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
    def test_burger_add_ingredient(self, i_type, i_name, i_price):
        ingredient = Mock()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        burger = Burger()
        burger.add_ingredient(ingredient=ingredient)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
    def test_burger_remove_ingredient(self, i_type, i_name, i_price):
        ingredient = Mock()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        burger = Burger()
        burger.add_ingredient(ingredient=ingredient)

        burger.remove_ingredient(index=0)

        assert burger.ingredients == []

    @pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
    def test_burger_move_ingredient(self, i_type, i_name, i_price):
        ingredient = Mock()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)

        burger = Burger()
        burger.add_ingredient(ingredient=ingredient)

        burger.move_ingredient(index=0, new_index=1)

        assert burger.ingredients == [ingredient]

    @pytest.mark.parametrize('b_name, b_price', [('AbCd', 1.5)])
    @pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
    def test_burger_get_price(self, i_type, i_name, i_price, b_name, b_price):
        ingredient = Mock()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)
        ingredient.get_price.return_value = i_price

        bun = Mock()
        bun.configure_mock(name=b_name, price=b_price)
        bun.get_price.return_value = b_price

        burger = Burger()
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)

        assert burger.get_price() == b_price * 2 + i_price

    @pytest.mark.parametrize('b_name, b_price', [('AbCd', 1.5)])
    @pytest.mark.parametrize('i_type, i_name, i_price', [(INGREDIENT_TYPE_SAUCE, 'cvn', 1.5)])
    def test_burger_get_receipt(self, i_type, i_name, i_price, b_name, b_price):
        ingredient = Mock()
        ingredient.configure_mock(ingredient_type=i_type, name=i_name, price=i_price)
        ingredient.get_type.return_value = i_type
        ingredient.get_name.return_value = i_name
        ingredient.get_price.return_value = i_price

        bun = Mock()
        bun.configure_mock(name=b_name, price=b_price)
        bun.get_name.return_value = b_name
        bun.get_price.return_value = b_price

        burger = Burger()
        burger.set_buns(bun=bun)
        burger.add_ingredient(ingredient=ingredient)

        receipt = [f'(==== {b_name} ====)', f'= {str(i_type).lower()} {i_name} ='
            , f'(==== {b_name} ====)\n', f'Price: {b_price * 2 + i_price}']
        assert burger.get_receipt() == '\n'.join(receipt)