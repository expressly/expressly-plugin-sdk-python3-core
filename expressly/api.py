import http.client


class Api:
    def __init__(self, api_key, url, secure=True):
        self.api_key = api_key
        self.http_client = http.client.HTTPSConnection(url, 443, timeout=10) \
            if secure else http.client.HTTPConnection(url, 80, timeout=10)

    def ping(self):
        return self.execute("GET", "/api/admin/ping")

    def install(self, hostname):
        # is this needed for developer interaction required sdks?
        return self.execute("POST", "/api/v2/plugin/merchant")

    def get_customer_popup(self, campaign_uuid):
        return self.execute("GET", "/api/v2/migration/%s" % campaign_uuid)

    def get_customer_data(self, campaign_uuid):
        return self.execute("GET", "/api/v2/migration/%s/user" % campaign_uuid)

    def customer_migration_status(self, campaign_uuid):
        return self.execute("GET", "/api/v2/migration/%s/success" % campaign_uuid)

    def execute(self, method, route, body=None, authorized=False):
        # conn = self.http_client
        conn = http.client.HTTPConnection("dev.expresslyapp.com", 80)
        conn.request(method, route, body)

        if authorized:
            conn.putheader('Authorization', 'Basic %u' % self.api_key)

        response = conn.getresponse()
        conn.close()

        return response
