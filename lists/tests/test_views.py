__author__ = 'nwilliams1'

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_URL(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #
        response = home_page(request) #
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
