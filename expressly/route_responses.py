from schematics.types import EmailType
from schematics.types.compound import ListType, ModelType

from expressly.models import JsonModel, Invoice


class PingResponse:
    def __str__(self):
        return '{"expressly": "Stuff is happening!"}'


class RegisteredResponse:
    def __str__(self):
        return '{"registered": true}'


class BatchCustomerResponse(JsonModel):
    existing = ListType(EmailType)
    deleted = ListType(EmailType)
    pending = ListType(EmailType)


class BatchInvoiceResponse(JsonModel):
    invoices = ListType(ModelType(Invoice))
