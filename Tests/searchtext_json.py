import pytest
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ddt import ddt, data, unpack, file_data
from webdriver_manager.chrome import ChromeDriverManager

from Pages.amazon_homepage import HomePage
from Pages.searchresultspage import Searchresults
from Utilities.utils import Utils
import unittest
import allure


@pytest.mark.usefixtures("setup")
@ddt()
class TestSearch(unittest.TestCase):

        #locators:
        GET_ALL_TITLES = (By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")

        # read the json file
        @file_data("../TestData/testdata.json")
        def test_search_mobiles(self, searchinput):
            try:
                #creating lauch page object
                lp = HomePage(self.driver)
                lp.wait_forelementclickable()
                lp.input_searchtextbox(searchinput)

                #creating search results page object
                sr = Searchresults(self.driver)
                sr.get_searchresults()

                #creating Utils object
                ut = Utils()

                # get all titles from the search results page
                alltitle = lp.wait_for_presence_of_all_elements_located(self.GET_ALL_TITLES)
                ut.printListItemText(alltitle)

                #get only titles that have 'searchinput' in the search results page
                ut.assertInListItemText(alltitle,searchinput)

                #get the title that doesnot have 'searchinput' in it
                ut.assertNotInListItemText(alltitle,searchinput)
                self.driver.back()

            except Exception as e:
                print(e)
            print("Inside Exception Block")




