import http.client
import json
import lxml.html
from expressly.errors import InvalidApiKeyError, InvalidHTMLError


class Api:
    def __init__(self, api_key, url, secure=True):
        self.api_key = api_key
        self.http_client = http.client.HTTPSConnection(url, 443, timeout=10) \
            if secure else http.client.HTTPConnection(url, 80, timeout=10)

        if self.api_key is None:
            raise InvalidApiKeyError

    def ping(self):
        return self.execute('GET', '/api/admin/ping')

    def register(self, hostname):
        # is this needed for developer interaction required sdks?
        return self.execute('POST', '/api/v2/plugin/merchant', {
            'apiKey': self.api_key,
            'apiBaseUrl': hostname
        })

    def get_customer_popup(self, campaign_customer_uuid):
        response = self.execute('GET', '/api/v2/migration/%s' % campaign_customer_uuid, None, True)

        # if (lxml.html.fromstring(response['data']).find('.//*')) is None:
        #     raise InvalidHTMLError

        return response

    def get_customer_data(self, campaign_customer_uuid):
        return self.execute('GET', '/api/v2/migration/%s/user' % campaign_customer_uuid)

    def customer_migration_status(self, campaign_customer_uuid, exists=False):
        body = {'status': 'migrated'}
        if exists:
            body = {'status': 'existing_customer'}

        return self.execute('POST', '/api/v2/migration/%s/success' % campaign_customer_uuid, body)

    def get_banner(self, campaign_uuid, email):
        return self.execute('GET', '/api/v2/banner/%s?email=%s' % (campaign_uuid, email))

    def execute(self, method, route, body=None, authorized=False):
        conn = self.http_client

        headers = {
            'Connection': 'close',
            'Content-Type': 'application/json'
        }
        if authorized is True:
            headers['Authorization'] = 'Basic %s' % self.api_key

        conn.request(method, route, json.dumps(body), headers)

        response = conn.getresponse()
        data = response.read().decode('utf-8')
        response.close()

        return {
            'status': response.status,
            'data': json.loads(data) if '{' in data else data
        }
