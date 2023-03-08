from selenium.webdriver.common.by import By
from Pages.Basepage import BaseDriver


class Searchresults(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    CHECK_FIRST_PAGE_LOAD = (By.XPATH, "//span[@aria-label='Current page, page 1']")

    # verifying 1st search result page is loaded
    def get_searchresults(self):
        self.driver_find_element(*self.CHECK_FIRST_PAGE_LOAD)