import pytest
@pytest.fixture(scope='class')
def state():
    print('开始执行用例')
    yield
    print('用例执行结束')