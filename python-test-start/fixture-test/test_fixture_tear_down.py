import pytest

def print_f(msg):
    print('fixture_' + msg)

@pytest.fixture
def fixture_a():
    print_f('a_before')
    yield 1
    print_f('a_tear_down')

@pytest.fixture
def fixture_b(fixture_a):
    print_f('b_before')
    yield 2
    print_f('b_tear_down')

@pytest.fixture
def fixture_c(fixture_b):
    print_f('c_before')
    yield 3
    print_f('c_tear_down')

@pytest.fixture
def fixture_d(fixture_c):
    _a = 1/0
    print_f('d_before')
    yield 4
    print_f('d_tear_down')

def test_fixture_termination(fixture_d):
    assert 1
