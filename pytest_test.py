import pytest


def func(x):
    return  x+1


@pytest.mark.parametrize('a,b',[(1,2),(4,5),(3,5),("a",12)])
def test_answer(a,b):
    assert func(a) ==b

def test_answer1():
    assert  func(4) == 5

@pytest.fixture()
def login():
    print("登录操作")
    username = "haha"
    return  username

class TestDemo:
    def test_a(self,login):
        print(f"a login={login}")

    def test_b(self):
        print("b")

if __name__ == '__main__':
    pytest.main(['pytest_test.py::TestDemo::test_a','-v'])