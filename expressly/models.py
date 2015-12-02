import json
from schematics.models import Model
from schematics.types import StringType, IntType, DateType, DateTimeType, DecimalType, EmailType
from schematics.types.compound import ListType, ModelType
from expressly.resources import CountryCodes


class JsonModel(Model):
    def __str__(self):
        return json.dumps(self.serialize())


class FieldValue(JsonModel):
    field = StringType(required=True)
    value = StringType(required=True)


class Email(JsonModel):
    email = EmailType(required=True)
    alias = StringType(required=True)


class Phone(JsonModel):
    type = StringType(required=True)
    number = StringType(required=True)
    country_code = StringType(required=True, serialized_name="countryCode")


class Address(JsonModel):
    first_name = StringType(required=True, serialized_name="firstName")
    last_name = StringType(required=True, serialized_name="lastName")
    address1 = StringType(required=True)
    address2 = StringType()
    city = StringType()
    company_name = StringType(serialized_name="companyName")
    zip = StringType()
    phone = IntType()
    alias = StringType(required=True, default="primary")
    state = StringType(serialized_name="stateProvence")
    country = StringType(required=True, choices=CountryCodes().iso3())

    class Options:
        serialize_when_none = False


class Customer(JsonModel):
    first_name = StringType(required=True, serialized_name="firstName")
    last_name = StringType(required=True, serialized_name="lastName")
    gender = StringType(choices=['M', 'F'])
    billing_address = IntType(serialized_name="billingAddress")
    shipping_address = IntType(serialized_name="shippingAddress")
    company = StringType()
    dob = DateType()
    online_presence = ListType(ModelType(FieldValue), serialized_name="onlinePresence")
    date_updated = DateType(serialized_name="dateUpdated")
    date_last_order = DateType(serialized_name="dateLastOrder")
    number_ordered = IntType(serialized_name="numberOrdered")
    emails = ListType(ModelType(Email))
    phones = ListType(ModelType(Phone))
    addresses = ListType(ModelType(Address))

    class Options:
        serialize_when_none = False


class Order(JsonModel):
    id = StringType()
    date = DateTimeType(required=True)
    item_count = IntType(min_value=1, required=True, serialized_name="itemCount")
    coupon = StringType()
    currency = StringType()
    total = DecimalType(required=True, serialized_name="preTaxTotal")
    tax = DecimalType(required=True)

    class Options:
        serialize_when_none = False


class Invoice(JsonModel):
    email = EmailType(required=True)
    order_count = IntType(min_value=0, default=0, serialized_name="orderCount")
    total = DecimalType(required=True, serialized_name="preTaxTotal")
    tax = DecimalType(required=True)
    orders = ListType(ModelType(Order))

    class Options:
        serialize_when_none = False
