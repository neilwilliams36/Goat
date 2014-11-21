__author__ = 'nwilliams1'

from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        #Edith goes to the To DO site and notices a "signin link
        self.open_browser()
        self.browser.find_element_by_id('login').click()

        #A persona login box appears
        self.switch_to_new_window("Mozilla Persona")

        #Edith logs in with her email address using mockmyid.com
        self.browser.find_element_by_id('authentication_email').send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        #The persona window closes
        self.switch_to_new_window('To Do Lists')

        #SHe can see that she is logged in
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)

        #Refreshed the page shees that its a real session log in
        self.browser.refresh()
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)

        #Clicks log out
        self.browser.find_element_by_id('logout').click()
        self.wait_for_element_with_id('login')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn('edith@mockmyid.com', navbar.text)

        #The logout also persists after refresh
        self.browser.refresh()
        self.wait_for_element_with_id('login')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn('edith@mockmyid.com', navbar.text)