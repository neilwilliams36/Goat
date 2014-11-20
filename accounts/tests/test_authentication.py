__author__ = 'nwilliams1'

from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model, SESSION_KEY
from accounts.models import ListUser
User = get_user_model()

from accounts.authentication import PersonalAuthenticationBackend, PERSONA_VERIFY_URL, DOMAIN

TEST_EMAIL = 'a@b.com'

@patch('accounts.authentication.requests.post')
class AuthenticateTest(TestCase):
    def setUp(self):
        self.backend = PersonalAuthenticationBackend()
        user = User(email='other@user.com')
        user.username = 'otheruser'
        user.save()

    def test_sends_assertion_to_mozilla_with_domain(self, mock_post):
        self.backend.authenticate('an assertion')
        mock_post.assert_called_once_with(PERSONA_VERIFY_URL, data={"assertion": 'an assertion', 'audience' : DOMAIN})

    def test_returns_none_if_response_errors(self, mock_post):
        mock_post.return_value.ok = False
        mock_post.return_value.json.return_value = {}
        user = self.backend.authenticate('an assertion')
        self.assertIsNone(user)

    def test_returns_none_if_status_not_okay(self, mock_post):
        mock_post.return_value.json.return_value = {'status': 'not okay'}
        user = self.backend.authenticate('an assertion')
        self.assertIsNone(user)

    def test_finds_existing_user_with_email(self, mock_post):
        mock_post.return_value.json.return_value = {'status': 'okay', 'email': TEST_EMAIL}
        actual_user = User.objects.create(email = TEST_EMAIL)
        found_user = self.backend.authenticate('an assertion')
        self.assertEqual(found_user, actual_user)

    def test_create_new_user_if_necessary_for_valid_assertions(self, mock_post):
        mock_post.return_value.json.return_value = {"status": 'okay', 'email': TEST_EMAIL}
        found_user = self.backend.authenticate('an assertion')
        new_user = User.objects.get(email=TEST_EMAIL)
        self.assertEqual(found_user, new_user)

    def test_gets_user_by_email(self, mock_post):
        backend = PersonalAuthenticationBackend()
        desired_user = User.objects.create(email=TEST_EMAIL)
        found_user = backend.get_user(TEST_EMAIL)
        self.assertEqual(desired_user,found_user)




