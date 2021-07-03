
import time
import openapi_client
from pprint import pprint
from openapi_client.api import cards_api_api
from openapi_client.model.card_api_password import CardApiPassword
from openapi_client.model.check_fields import CheckFields
from openapi_client.model.check_response import CheckResponse
from openapi_client.model.deregister_fields import DeregisterFields
from openapi_client.model.presale_fields import PresaleFields
from openapi_client.model.refund_fields import RefundFields
from openapi_client.model.refund_response import RefundResponse
from openapi_client.model.register_sale_fields import RegisterSaleFields
from openapi_client.model.register_sale_response import RegisterSaleResponse
from openapi_client.model.sale_fields import SaleFields
from openapi_client.model.sale_response import SaleResponse
from openapi_client.model.securesale_fields import SecuresaleFields
from openapi_client.model.securesale_response import SecuresaleResponse
from openapi_client.model.vc_finish_fields import VcFinishFields
from openapi_client.model.vc_prepare_fields import VcPrepareFields
from openapi_client.model.vc_prepare_response import VcPrepareResponse

configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)

with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
basic_data = CheckFields(api_password=CardApiPassword("6c0f5ef6e4d6877abad7fcfb3b5de117ad8b772d"),) # CheckFields | check method data (optional)

try:
    # check
    api_response = api_instance.api_cards_api_key_check_post(api_key, basic_data=basic_data)
    pprint(api_response)
except openapi_client.ApiException as e:
    print("Exception when calling CardsAPIApi->api_cards_api_key_check_post: %s\n" % e)