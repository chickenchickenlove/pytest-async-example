import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5])
def my_fixture(request):
    print(f'{request.param=}')
    return request.param


def test_hello(my_fixture):
    print('\n')
    print(f'{my_fixture=}')


'''
collecting ... collected 5 items

test_request_fixture.py::test_hello[1] 
request.param=1
PASSED                            [ 20%]
my_fixture=1

test_request_fixture.py::test_hello[2] 
request.param=2
PASSED                            [ 40%]
my_fixture=2

test_request_fixture.py::test_hello[3] 
request.param=3
PASSED                            [ 60%]
my_fixture=3

test_request_fixture.py::test_hello[4] 
request.param=4
PASSED                            [ 80%]
my_fixture=4

test_request_fixture.py::test_hello[5] 
request.param=5
PASSED                            [100%]
my_fixture=5
'''
