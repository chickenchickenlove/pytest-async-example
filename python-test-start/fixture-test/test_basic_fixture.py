"""
- Fixture를 이용해 필요한 인스턴스를 준비할 수 있다.
- 심지어 Fixture끼리 의존 관계를 가지고 새로운 Fixture를 만들 수도 있다.
- 테스트 실행 시점에 Fixture가 데코레이팅 된 함수의 이름과 같은 파라메터에 함수 실행 결과가 주입된다.

Basic Fixture를 생성해보면서 위와 같은 사실을 알 수 있다.
나는 여기서 한 가지 의문이 생겼다.
테스트 코드 내에서 함수를 직접 호출해서 인스턴스를 생성하는 것과 비교해,
Fixture를 이용해 파라메터로 주입해주는 것은 어떤 이점을 가질 수 있을까?
여기까지는 그리 큰 이점은 없다고 봐도 될 것 같다.

"""
import pytest

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def fruit_apple():
    print('fruit_apple called.')
    return Fruit('apple')

@pytest.fixture
def fruit_banana():
    print('fruit_banana called.')
    return Fruit('banana')

@pytest.fixture
def fruit_basket(fruit_apple, fruit_banana):
    print('fruit_basket called.')
    return [fruit_apple, fruit_banana]


def test_my_fruits_in_basket(fruit_apple, fruit_banana, fruit_basket):
    print('test1 called')
    assert fruit_apple in fruit_basket
    assert fruit_banana in fruit_basket

def test_my_fruits_in_basket2(fruit_apple, fruit_banana, fruit_basket):
    print('test2 called')
    assert fruit_apple in fruit_basket
    assert fruit_banana in fruit_basket


"""
$ py.test -s test_basic_fixture.py 
>>> 
test_basic_fixture.py::test_my_fruits_in_basket 

fruit_apple called.
fruit_banana called.
fruit_basket called.
test1 called
PASSED

test_basic_fixture.py::test_my_fruits_in_basket2 

fruit_apple called.
fruit_banana called.
fruit_basket called.
test2 called
PASSED


"""
