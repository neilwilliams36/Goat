__author__ = 'nwilliams1'

from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore
from functionalTests.base import FunctionalTest

class MyListTest(FunctionalTest):

    def create_login(self, email):
        self.open_browser()
        self.browser.find_element_by_id('login').click()
        self.switch_to_new_window("Mozilla Persona")
        self.browser.find_element_by_id('authentication_email').send_keys(email)
        self.browser.find_element_by_tag_name('button').click()
        self.switch_to_new_window('To Do Lists')
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@mockmyid.com'
        self.create_login(email)


