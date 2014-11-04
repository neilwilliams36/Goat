__author__ = 'nwilliams1'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a coll new online to-do app.
        #she goes to check out the homepage
        #added a change here
        self.browser.get('http://127.0.0.1:8000')
        #She notices the page title and header mention to-do list
        self.assertIn('To Do List', self.browser.title)
        page_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To Do', page_text)


        #she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')

        #she type "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")
        #she hit enter and the page updates
        inputbox.send_keys(Keys.ENTER)
        #Now the page lists "1. Buy peacock feathers" as an item on the to-do list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Buy Peacock feathers' for row in rows), "New to-do item did not appear in table")
        #There is still a text box inviting her to add another item
        #She enters "Use peacock feathers to make a fly"

        #The page updates and shows both items

        #Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.


        # She visits that URL - her to-do list is still there.


        # Satisfied, she goes back to sleep
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')