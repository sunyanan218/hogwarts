import pytest

@pytest.fixture(scope="session")
def state():
    print('开始执行用例')
    yield
    print('用例执行结束')