from schematics.models import Model
from schematics.types import StringType, IntType, DateType, DateTimeType, DecimalType, EmailType
from schematics.types.compound import ListType, ModelType


class FieldValue(Model):
    field = StringType(required=True)
    value = StringType(required=True)


class Email(Model):
    email = StringType(required=True)
    alias = StringType(required=True)


class Phone(Model):
    type = StringType(required=True)
    number = StringType(required=True)
    country_code = StringType(required=True, serialized_name="countryCode")


class Address(Model):
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
    country = StringType(required=True)

    class Options:
        serialize_when_none = False


class Customer(Model):
    first_name = StringType(required=True, serialized_name="firstName")
    last_name = StringType(required=True, serialized_name="lastName")
    gender = StringType()
    billing_address = IntType(serialized_name="billingAddress")
    shipping_address = IntType(serialized_name="shippingAddress")
    company = StringType()
    dob = DateType()
    online_presence = ListType(ModelType(FieldValue))
    date_updated = DateType()
    date_last_order = DateType()
    number_ordered = IntType()
    emails = ListType(ModelType(Email))
    phones = ListType(ModelType(Phone))
    addresses = ListType(ModelType(Address))

    class Options:
        serialize_when_none = False


class Order(Model):
    id = StringType()
    date = DateTimeType(required=True)
    item_count = IntType(min_value=1, required=True, serialized_name="itemCount")
    coupon = StringType()
    currency = StringType()
    total = DecimalType(required=True, serialized_name="preTaxTotal")
    tax = DecimalType(required=True)

    class Options:
        serialize_when_none = False


class Invoice(Model):
    email = EmailType(required=True)
    order_count = IntType(min_value=0, default=0, serialized_name="orderCount")
    total = DecimalType(required=True, serialized_name="preTaxTotal")
    tax = DecimalType(required=True)
    orders = ListType(ModelType(Order))

    class Options:
        serialize_when_none = False
