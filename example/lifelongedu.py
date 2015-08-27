from social.backends.oauth import BaseOAuth2
from django.utils.http import urlencode
import json

class LifelongeduOAuth2(BaseOAuth2):
    """Lifelongedu OAuth authentication backend"""
    name = 'lifelongedu'
    AUTHORIZATION_URL = 'http://myserver:8082/o/authorize'
    ACCESS_TOKEN_URL = 'http://myserver:8082/o/token/'
    SCOPE_SEPARATOR = ','
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('id', 'id'),
        ('expires', 'expires'),
        ('login', 'login')
    ]

    def get_user_details(self, response):
        """Return user details from Github account"""
        jsonString = "{"
        jsonString += '"login":"'+response.get('login')+'"'
        jsonString += ',"email":"'+response.get('email')+'"'
        jsonString += ',"name":"'+response.get('name')+'"'
        jsonString += ',"id":"'+response.get('id')+'"'
        jsonString += '}'

        return json.loads(jsonString)

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = 'http://myserver:8082/api/hello?' + urlencode({
            'access_token': access_token
        })
        try:
            return self.get_json(url)
        except ValueError:
            return None

