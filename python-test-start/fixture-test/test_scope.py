import pytest



class Hello:
    pass

@pytest.fixture(scope="class")
def class_scope():
    return Hello()

@pytest.fixture(scope="session")
def session_scope():
    return Hello()

@pytest.fixture(scope="function")
def function_scope():
    return Hello()

@pytest.fixture(scope="package")
def package_scope():
    return Hello()

@pytest.fixture(scope="module")
def module_scope():
    return Hello()


class TestOne:

    def test_one(self,
                 class_scope,
                 session_scope,
                 function_scope,
                 package_scope,
                 module_scope):
        print('\n')
        print(f'{id(class_scope)=} / {id(session_scope)=} / {id(function_scope)=} / {id(package_scope)=} / {id(module_scope)=}')
        assert 1 == 1

    def test_two(self, class_scope,
                 session_scope,
                 function_scope,
                 package_scope,
                 module_scope):
        print('\n')
        print(f'{id(class_scope)=} / {id(session_scope)=} / {id(function_scope)=} / {id(package_scope)=} / {id(module_scope)=}')
    assert 1 == 1
