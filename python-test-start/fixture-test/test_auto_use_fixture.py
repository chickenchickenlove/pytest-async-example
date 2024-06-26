import pytest


@pytest.fixture
def empty_list():
    return []

@pytest.fixture(autouse=True)
def append_number(empty_list):
    return empty_list.append(10)


def test_hello_test(empty_list):
    assert len(empty_list) > 0
    assert 10 in empty_list
