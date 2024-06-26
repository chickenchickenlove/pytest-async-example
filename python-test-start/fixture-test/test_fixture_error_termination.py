import pytest


@pytest.fixture
def fixture_a():
    return 1

@pytest.fixture
def fixture_b(fixture_a):
    _a = 1/0
    return 2

def test_fixture_termination(fixture_b):
    assert 1 == 1
