__author__ = 'nwilliams1'
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #edith goes to the home page and accidentally tries to submit and empty list.
        #She hits Enter on the input box
        if self.server_url[7:12] == 'local':
            self.browser.get("http://127.0.0.1:8000")
        else:
            self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        #The home page refreshes, and there is an error message say that the list cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        #She tries again with some text in the item, which now works
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Milk \n')
        self.check_for_row_in_list_table("1. Buy Milk")
        #Perversely, she now decides to submit a second blank list
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        #She receives a similar warning on the list page
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        #And she corrects is by filling in some text
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Cheese \n')
        self.check_for_row_in_list_table("1. Buy Milk")
        self.check_for_row_in_list_table("2. Buy Cheese")
        #she is finished
        #self.fail('Finish the test')