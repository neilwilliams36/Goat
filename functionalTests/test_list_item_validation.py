__author__ = 'nwilliams1'
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #edith goes to the home page and accidentally tries to submit and empty list.
        #She hits Enter on the input box

        #The home page refreshes, and there is an error message say that the list cannot be blank

        #She tries again with some text in the item, which now works

        #Perversely, she now decides to submit a second blank list

        #She receives a similar warning on the list page

        #And she corrects is by filling n some text

        #she is finished
        self.fail('Finish the test')