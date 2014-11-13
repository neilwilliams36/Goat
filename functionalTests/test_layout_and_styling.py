__author__ = 'nwilliams1'
from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        #Edith goes to the home page
        if self.server_url[7:12] == 'local':
            self.browser.get("http://127.0.0.1:8000")
        else:
            self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        #she notices that teh input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(inputbox.location['x'] + (inputbox.size['width']/2), 512, delta=15)

        #she starts a new list and sees teh input is nicely centered there as well
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(inputbox.location['x'] + (inputbox.size['width']/2), 512, delta=15)
