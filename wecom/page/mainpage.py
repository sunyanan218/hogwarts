from selenium.webdriver.common.by import By

from wecom.page.adresspage import AdRessPage
from wecom.page.basepage import BasePage
from wecom.page.register import Registe


class MainPage(BasePage):
    # def goto_adresspage(self):
    #     self.driver.find_element_by_id(".menu_contacts").click()
    #     return AdRessPage(self.driver)
    def goto_regisete(self):
        self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return Registe(self.driver)


