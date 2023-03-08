from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    #element to be clickable - return single element
    def wait_for_element_to_be_clickable(self,locator):
        wait = WebDriverWait(self.driver, 10)
        element_clickable = wait.until(EC.element_to_be_clickable(locator))
        return element_clickable

    #presence of all elements located - return list of elements
    def wait_for_presence_of_all_elements_located(self,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located(locator))
        return list_of_elements

    #find element  - return single element
    def driver_find_element(self,*locator):
        check_page_load = self.driver.find_element(*locator)
        return check_page_load

    #Click the element, enter the test search and click keyboard enter
    def click_enter_value(self,clickelement,inputtext):
        clickelement.click()
        clickelement.send_keys(inputtext)
        clickelement.send_keys(Keys.ENTER)








