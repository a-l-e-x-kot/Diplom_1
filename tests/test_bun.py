import pytest
from praktikum.praktikum import Bun
from tests.data_test import name_price_bun


class TestBun:
    @pytest.mark.parametrize('name, price', name_price_bun)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', name_price_bun)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price