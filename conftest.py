from praktikum.burger import Burger
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = 'black bun'
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_name.return_value = 'hot sauce'
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock