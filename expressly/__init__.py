from expressly.resources import CountryCodes
from expressly.models import (
    FieldValue,
    Customer,
    Email,
    Phone,
    Address)
from expressly.api import Api
from expressly.responses import (
    CustomerDataResponse)
from expressly.errors import (
    GenericError,
    AuthenticationError,
    UuidError,
    InvalidApiKeyError,
    InvalidHTMLError)
from expressly.version import VERSION

api_url = 'prod.expresslyapp.com'
