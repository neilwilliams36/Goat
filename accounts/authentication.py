__author__ = 'nwilliams1'

import requests
import sys
from accounts.models import ListUser

PERSONA_VERIFY_URL = 'https://verifier.login.persona.org/verify'
DOMAIN = '127.0.0.1'

class PersonalAuthenticationBackend(object):

    def authenticate(self, assertion):
        #send the assertion to Mozilla's verifier service
        data = {'assertion': assertion, 'audience': DOMAIN}
        #print ('sending to mozilla', data, file=sys.stderr)
        resp = requests.post(PERSONA_VERIFY_URL, data=data)
        print ('got in authenticate', resp.content, file=sys.stderr)
        #Did the verifier respond?
        if resp.ok:
            #Parse the response
            verification_data = resp.json()
            #Check if the assertion is valid?
            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)
