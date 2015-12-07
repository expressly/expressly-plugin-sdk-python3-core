from schematics.models import Model
from schematics.types import StringType, EmailType
from schematics.types.compound import ModelType
from expressly.models import Customer as CustomerModel


class Meta(Model):
    locale = StringType(required=True, max_length=3)
    sender = StringType(required=True)


class Cart(Model):
    product_id = StringType(deserialize_from="productId")
    coupon_code = StringType(deserialize_from="couponCode")


class Customer(Model):
    email = EmailType(required=True)
    data = ModelType(CustomerModel, required=True, deserialize_from="customerData")
    cart = ModelType(Cart)


class CustomerDataResponse(Model):
    meta = ModelType(Meta, required=True)
    data = ModelType(Customer, required=True)
