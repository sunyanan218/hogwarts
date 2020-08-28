from wecom.page.mainpage import MainPage

class TestRegist:
    def setup(self):
       self.main = MainPage()
    def testregist(self):
        self.main.goto_regisete()


