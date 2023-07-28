import pytest

from utils import arrs

# Создаем фикстуру, которая запускается перед каждым тестом
@pytest.fixture
def coll_four(): # возвращаем список из 4х элементов
    return [1, 2, 3, 4]

@pytest.fixture
def coll_five(): # возвращаем список из 5ти элементов
    return [1, 2, 3, 4, 5]

@pytest.fixture
def coll_none(): # возвращаем пустой список
    return []


def test_get(coll_four, coll_none):
    assert arrs.get(coll_four, 2, "test") == 3
    assert arrs.get(coll_none, -1, "test") == "test"


def test_slice(coll_none, coll_four, coll_five):
    assert arrs.my_slice(coll_four, 1, 4) == [2, 3, 4]
    assert arrs.my_slice(coll_five, 1) == [2, 3, 4, 5]
    assert arrs.my_slice(coll_none, 1, 3) == coll_none
    assert arrs.my_slice(coll_four, -1, 3) == coll_none
    assert arrs.my_slice(coll_four, -5, 2) == [1, 2]