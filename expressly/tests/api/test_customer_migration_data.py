from unittest import TestCase

from httpretty import GET, register_uri, activate
from schematics.validate import validate

from expressly import CustomerDataResponse, Api
from expressly.tests import dummy_api_key, api_dev_url, dummy_campaign_customer_uuid


class CustomerMigrationDataTest(TestCase):
    def setUp(self):
        self.api = Api(dummy_api_key, api_dev_url, False)

    @activate
    def test_migration_data(self):
        register_uri(
            GET,
            'http://%s/api/v2/migration/%s/user' % (api_dev_url, dummy_campaign_customer_uuid),
            body=bytearray("""
            {
                "meta": {
                    "locale": "UKR",
                    "sender": "https://expresslyapp.com/api/v2/migration/%s}"
                },
                "data": {
                    "email": "john.smith@gmail.com",
                    "customerData": {
                        "firstName": "John",
                        "lastName": "Smith",
                        "gender": "M",
                        "billingAddress": 0,
                        "shippingAddress": 1,
                        "company": "Expressly",
                        "dob": "1987-08-07",
                        "taxNumber": "GB0249894821",
                        "onlinePresence": [
                            {
                                "field": "website",
                                "value": "http://www.myblog.com"
                            }
                        ],
                        "dateUpdated": "2015-07-10T11:42:00+01:00",
                        "emails": [
                            {
                                "email": "john.smith@gmail.com",
                                "alias": "default"
                            },
                            {
                                "email": "john@smithcorp.com",
                                "alias": "work"
                            }
                        ],
                        "phones": [
                            {
                                "type": "M",
                                "number": "020734581250",
                                "countryCode": 44
                            },
                            {
                                "type": "L",
                                "number": "020731443250",
                                "countryCode": 44
                            }
                        ],
                        "addresses": [
                            {
                                "firstName": "John",
                                "lastName": "Smith",
                                "address1": "12 Piccadilly",
                                "address2": "Room 14",
                                "city": "London",
                                "companyName": "WorkHard Ltd",
                                "zip": "W1C 34U",
                                "phone": 1,
                                "alias": "Work address",
                                "stateProvince": "LND",
                                "country": "GBR"
                            },
                            {
                                "firstName": "John C.",
                                "lastName": "Smith",
                                "address1": "23 Sallsberry Ave",
                                "address2": "Flat 3",
                                "city": "London",
                                "companyName": "",
                                "zip": "NW3 4HG",
                                "phone": 0,
                                "alias": "Home address",
                                "stateProvince": "LND",
                                "country": "GBR"
                            }
                        ]
                    },
                    "cart": {
                        "productId": "491",
                        "couponCode": "20OFF"
                    }
                }
            }""" % dummy_campaign_customer_uuid, 'utf-8'),
            status=200,
            content_type='application/json'
        )

        response = self.api.get_customer_data(dummy_campaign_customer_uuid)

        self.assertTrue(response['status'], 200)
        self.assertTrue(validate(CustomerDataResponse, response['data']))
