from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.Basepage import BaseDriver


class HomePage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    GLOBAL_SEARCH_BOX  = (By.XPATH, "//input[@id='twotabsearchtextbox']")

    #click the global search box
    def wait_forelementclickable(self):
       return self.wait_for_element_to_be_clickable(self.GLOBAL_SEARCH_BOX)

    #input global search box
    def input_searchtextbox(self):
        self.click_enter_value(self.wait_forelementclickable(),'Nokia')

    def input_searchtextbox2(self):
        self.click_enter_value(self.wait_forelementclickable(),'Samsung')

    #def input_searchtextbox(self,searchinput):
        #self.click_enter_value(self.wait_forelementclickable(),searchinput)



