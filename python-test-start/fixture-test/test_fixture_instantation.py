import pytest

class Hello:
    pass

@pytest.fixture(scope="session")
def my_order_fixture():
    print('my_order_fixture')
    return []

@pytest.fixture(scope="class")
def class_scope(my_order_fixture):
    my_order_fixture.append('class')
    return Hello()

@pytest.fixture(scope="session")
def session_scope(my_order_fixture):
    my_order_fixture.append('session')
    return Hello()

@pytest.fixture(scope="function")
def function_scope(my_order_fixture):
    my_order_fixture.append('function')
    return Hello()

@pytest.fixture(scope="package")
def package_scope(my_order_fixture):
    my_order_fixture.append('package')
    return Hello()

@pytest.fixture(scope="module")
def module_scope(my_order_fixture):
    my_order_fixture.append('module')
    return Hello()

def test_anything(
        class_scope,
        session_scope,
        function_scope,
        package_scope,
        module_scope,
        my_order_fixture
):

    for k in my_order_fixture:
        print(f'{k} \n')
    assert 1 == 1
