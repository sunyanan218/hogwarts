from Script3.calculator import Calculator
import pytest
import yaml
import allure
def getdata(filename):
    with open('./'+filename+'.yaml',encoding='utf-8') as f:
        return yaml.safe_load(f)
def getdata_withkey(key):
    return getdata('data')[key]

class Testcalcu():
    # data = yaml.safe_load(open("./data.yaml"))
    # divdata = yaml.safe_load(open("./divdata.yaml"))
    def setup_class(self):
        print('开始测试')
        self.scl = Calculator()

    def teardown_class(self):
        print('结束测试')
    @pytest.mark.run(order=1)
    @allure.story("数字加")
    @pytest.mark.parametrize(["a", "b", "excepted"], getdata_withkey('add_data'))
    # [(1,2,3)]
    def test_add(self, a, b, excepted):
        result = self.scl.add(a, b)
        assert excepted == round(result, 1)

    @pytest.mark.run(order=3)
    @allure.story("数字减")
    @pytest.mark.parametrize(["a", "b", "excepted"], getdata_withkey('sub_data'))
    def test_sub(self, a, b, excepted):
        result = self.scl.sub(a, b)
        assert excepted == round(result, 1)

    @pytest.mark.run(order=4)
    @allure.story("数字乘")
    @pytest.mark.parametrize(["a", "b", "excepted"], getdata_withkey('mul_data'))
    def test_mul(self, a, b, excepted):
        result = self.scl.mul(a, b)
        assert excepted == round(result, 1)

    @pytest.mark.run(order=2)
    @allure.story("数字除")
    @pytest.mark.parametrize(["a", "b", "excepted"], getdata_withkey('div_data'))
    def test_div(self, a, b, excepted):
        result = self.scl.div(a, b)
        print(result)
        assert excepted == result
