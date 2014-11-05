__author__ = 'nwilliams1'

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def check_for_not_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertNotIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a coll new online to-do app.
        #she goes to check out the homepage
        #added a change here
        self.browser.get("http://127.0.0.1:8000")
        #She notices the page title and header mention to-do list
        self.assertIn('To Do List', self.browser.title)
        page_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', page_text)


        #she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #she type "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")

        #she hit enter and she is taken to a new URL
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, 'lists/.+')

        #Now the page lists "1. Buy peacock feathers" as an item on the to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1. Buy peacock feathers')

        #There is still a text box inviting her to add another item
        #She enters "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        #The page updates and shows both items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make a fly')

        #Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.


        # She visits that URL - her to-do list is still there.


        # Satisfied, she goes back to sleep

        #Now a new user, Francis, comes along to the site
        #We use a new browser session to make sure that no information
        #from Edith's is coming through from the cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #Francis visits the home page.  There is no sign of Edith's list
        self.browser.get("http://127.0.0.1:8000")
        self.check_for_not_in_list_table('1. Buy peacock feathers')
        self.check_for_not_in_list_table('2. Use peacock feathers to make a fly')

        #Francis starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, 'lists/.+')
        self.assertNotEqual(edith_list_url, francis_list_url)

        #Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feather', page_text)
        self.assertIn('Buy milk', page_text)

        #satisfied they both go to sleep
        self.fail('Finish the test')
