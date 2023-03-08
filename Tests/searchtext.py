import pytest
from selenium.webdriver.common.by import By
from Pages.amazon_homepage import HomePage
from Pages.searchresultspage import Searchresults
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestSearch():

        #locators:
        GET_ALL_TITLES = (By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
        GET_NOKIA_TITLE = (By.XPATH,"//span[contains(text(),'Nokia') and @class='a-size-medium a-color-base a-text-normal']")

        def test_search_mobiles(self):
            #creating lauch page object
            lp = HomePage(self.driver)
            lp.wait_forelementclickable()
            lp.input_searchtextbox()

            #creating search results page object
            sr = Searchresults(self.driver)
            sr.get_searchresults()

            #creating Utils object
            ut = Utils()

            # get all titles from the search results page
            alltitle = lp.wait_for_presence_of_all_elements_located(self.GET_ALL_TITLES)
            ut.printListItemText(alltitle)

            #get only titles that have 'Nokia' in the search results page
            nokiatitle = lp.wait_for_presence_of_all_elements_located(self.GET_NOKIA_TITLE)
            ut.printListItemText(nokiatitle)

            #get the title that doesnot have 'Nokia' in it
            ut.assertInListItemText(alltitle,"Apple")

# parallel execution using - n command
        #def test_search_mobiles_samsung(self):
            #creating lauch page object
           # lp = HomePage(self.driver)
            #lp.wait_forelementclickable()
            #lp.input_searchtextbox2()




