from social.backends.oauth import BaseOAuth2
from django.utils.http import urlencode
import json

class LifelongeduOAuth2(BaseOAuth2):
    """Lifelongedu OAuth authentication backend"""

    print "## called LifelongeduOAuth2"

    name = 'lifelongedu'
    AUTHORIZATION_URL = 'http://desktop20:8082/o/authorize'
    ACCESS_TOKEN_URL = 'http://desktop20:8082/o/token/'
#    AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
#    ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
    SCOPE_SEPARATOR = ','
#    STATE_PARAMETER = 'random_state_string'
#    STATE_PARAMETER = False
#    REDIRECT_STATE = False
#    STATE_PARAMETER = True
#    REDIRECT_STATE = True
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires'),
    ]

    def get_user_details(self, response):
        """Return user details from Github account"""
        return {'username': response.get('login'),
                'email': response.get('email') or '',
                'first_name': response.get('name'),
                'fullname': response.get('fullname'),
                'last_name': response.get('last_name'),
                'id': response.get('id'),
                'uid': response.get('id') }
#        return {'username': response.get('login'),
#                'email': response.get('email') or '',
#                'first_name': response.get('name'),
#                'fullname': response.get('name'),
#                'provider': response.get('name'),
#                'uid': response.get('id') }

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'http://desktop20:8082/api/hello?' + urlencode({
#        url = 'http://api.github.com/user?' + urlencode({
            'access_token': access_token
        })
#        url = 'https://desktop20:8082/api/hello?' + {
#            'access_token': access_token
#        }
        try:
            return self.get_json(url)
        except ValueError:
            return None
