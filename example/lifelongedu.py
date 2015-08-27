from social.backends.oauth import BaseOAuth2
from django.utils.http import urlencode
import json
from social.exceptions import AuthMissingParameter


class LifelongeduOAuth2(BaseOAuth2):
    """Lifelongedu OAuth authentication backend"""

    print "## called LifelongeduOAuth2"

    name = 'lifelongedu'
    AUTHORIZATION_URL = 'http://myserver:8082/o/authorize'
    ACCESS_TOKEN_URL = 'http://myserver:8082/o/token/'
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

        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ get_user_details !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

        """Return user details from Github account"""

        print "response.get('login')", response.get('login')
        print "response.get('email')", response.get('email')
        print "response.get('name')", response.get('name')
        print "response.get('fullname')", response.get('fullname')
        print "response.get('id')", response.get('id')

        # '{"username": "'+response['login']+'", "email": "'+response['email']+'" or "", "first_name": "'+response['name']+'", "fullname": "'+response['fullname']+'", "last_name": "'+response['last_name']+'", "id": "'+response['id']+'", "uid": "'+response['id']+'" }'

        jsonString = "{"
        jsonString += '"login":"'+response.get('login')+'"'
        jsonString += ',"email":"'+response.get('email')+'"'
        jsonString += ',"name":"'+response.get('name')+'"'
        jsonString += ',"id":"'+response.get('id')+'"'
        jsonString += '}'

        print "check jsonString = ", jsonString

        print json.loads(jsonString)
        return json.loads(jsonString)
#        return {'username': response.get('login'),
#                'email': response.get('email') or '',
#                'first_name': response.get('name'),
#                'fullname': response.get('name'),
#                'provider': response.get('name'),
#                'uid': response.get('id') }

    def user_data(self, access_token, *args, **kwargs):

        print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ user_data !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

        """Loads user data from service"""
        url = 'http://myserver:8082/api/hello?' + urlencode({
#        url = 'http://api.github.com/user?' + urlencode({
            'access_token': access_token
        })
        print 'url > '
        print url

#        url = 'https://desktop20:8082/api/hello?' + {
#            'access_token': access_token
#        }
        try:
            return self.get_json(url)
        except ValueError:
            return None
