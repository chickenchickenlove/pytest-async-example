import pytest

class Hello: pass

@pytest.fixture(scope="class")
def fixture_a():
    return Hello()

@pytest.fixture(scope="session")
def fixture_b(fixture_a):
    return Hello()


def test_anything(fixture_a, fixture_b):
    assert 1 == 1
