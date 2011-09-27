import urllib, urllib2, json

class API:

    url = 'https://api.wbsrvc.com/'
    user_key = None

    def __init__(self, key):
        """Cake API object construction.
        Param: 
            key : dev portal API key
        """
        self.header = dict(apikey=key)

    def call(self, method, params):
        """Call CakeMail API.
        Params:
            method: what Class/Method to call. Array
                    eg: ['Campaign', 'getInfo']
            params: parameter of the method. Dict
        """
        if not 'user_key' in params and self.user_key is not None:
            params['user_key'] = self.user_key

        request = urllib2.Request(
            self.url + method[0] + '/' + method[1],
            urllib.urlencode(params),
            self.header
        )
        try:
            response = json.loads(urllib2.urlopen(request).read())
            return response
        except urllib2.HTTPError as error:
            return dict(Error=str(error))
   
    def login(self, params):
        """Login to CakeMail and remember the user_key for future uses.
            Params:
                params: Dict containing
                        email:    api user email
                        password: its password
        """
        assert 'email' in params
        assert 'password' in params
        resp = self.call(['User', 'login'], params)

        if not resp['status'] == 'success':
            return dict(Error= resp['data'])
        self.user_key = resp['data']['user_key']
