from Script3.calculator import Calculator
import pytest
import yaml
class Testcalcu:
    data=yaml.safe_load(open("./data.yaml"))
    divdata=yaml.safe_load(open("./divdata.yaml"))
    def setup(self):
        print('开始测试')
        self.scl=Calculator()
    def teardown(self):
        print('结束测试')

    @pytest.mark.parametrize(["a","b","excepted"],data)
    #[(1,2,3)]
    def test_add(self,a,b,excepted):
        result=self.scl.add(a,b)
        assert excepted ==round(result,1)
    @pytest.mark.parametrize(["a","b","excepted"],divdata)
    def test_div(self,a,b,excepted):
        result = self.scl.div(a, b)
        print(result)
        assert excepted == result