import urllib, urllib2, json

class API:

    header = {'apikey':''}
    url = 'https://api.wbsrvc.com/'

    def call(self, method, params):
        request = urllib2.Request(
            self.url + method[0] + '/' + method[1],
            urllib.urlencode(params),
            self.header
        )
        try:
            response = json.loads(urllib2.urlopen(request).read())
            return response
        except urllib2.HTTPError as error:
            return json.loads('{"Error": "%s"}' % error)
        