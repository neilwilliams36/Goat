__author__ = 'nwilliams1'
from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from unittest import skip
from lists.forms import DUPLICATE_ITEM_ERROR


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        #edith goes to the home page and accidentally tries to submit and empty list.
        #She hits Enter on the input box
        self.open_browser()
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        #The home page refreshes, and there is an error message say that the list cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        #She tries again with some text in the item, which now works
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Milk \n')
        self.check_for_row_in_list_table("1. Buy Milk")
        #Perversely, she now decides to submit a second blank list
        inputbox = self.get_item_input_box()
        inputbox.send_keys(Keys.ENTER)

        #She receives a similar warning on the list page
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        #And she corrects is by filling in some text
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Cheese \n')
        self.check_for_row_in_list_table("1. Buy Milk")
        self.check_for_row_in_list_table("2. Buy Cheese")
        #she is finished
        #self.fail('Finish the test')

    def test_cannot_add_duplicate_items(self):
        #Edit goes to the home page and starts a new list
        self.open_browser()

        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table("1. Buy wellies")

        #She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        #she sees a helpful error message
        self.check_for_row_in_list_table("1. Buy wellies")
        error = self.get_error_element()
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)

    def test_error_messages_are_cleared_on_input(self):
        #Edith starts a new list in a way tat causes a validation error
        self.open_browser()
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        #she start typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        #She is pleased to see that the error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())

