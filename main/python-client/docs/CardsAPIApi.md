# openapi_client.CardsAPIApi

All URIs are relative to *https://docs.tpay.com/Proxy.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_cards_api_key_check_post**](CardsAPIApi.md#api_cards_api_key_check_post) | **POST** /api/cards/{api_key}/check | check
[**api_cards_api_key_deregister_post**](CardsAPIApi.md#api_cards_api_key_deregister_post) | **POST** /api/cards/{api_key}/deregister | deregister
[**api_cards_api_key_presale_post**](CardsAPIApi.md#api_cards_api_key_presale_post) | **POST** /api/cards/{api_key}/presale | presale
[**api_cards_api_key_refund_post**](CardsAPIApi.md#api_cards_api_key_refund_post) | **POST** /api/cards/{api_key}/refund | refund
[**api_cards_api_key_register_sale_post**](CardsAPIApi.md#api_cards_api_key_register_sale_post) | **POST** /api/cards/{api_key}/register_sale | register sale
[**api_cards_api_key_sale_post**](CardsAPIApi.md#api_cards_api_key_sale_post) | **POST** /api/cards/{api_key}/sale | sale
[**api_cards_api_key_securesale_post**](CardsAPIApi.md#api_cards_api_key_securesale_post) | **POST** /api/cards/{api_key}/securesale | secure sale
[**api_cards_api_key_visacheckout_finish_post**](CardsAPIApi.md#api_cards_api_key_visacheckout_finish_post) | **POST** /api/cards/{api_key}/visacheckout_finish | visacheckout finish
[**api_cards_api_key_visacheckout_prepare_post**](CardsAPIApi.md#api_cards_api_key_visacheckout_prepare_post) | **POST** /api/cards/{api_key}/visacheckout_prepare | visacheckout prepare


# **api_cards_api_key_check_post**
> CheckResponse api_cards_api_key_check_post(api_key)

check

Method, which can be used to ping our API server to establish a monitoring service on the Merchant system.

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.check_fields import CheckFields
from openapi_client.model.check_response import CheckResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = CheckFields(
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
    ) # CheckFields | check method data (optional)

    # example passing only required values which don't have defaults set
    try:
        # check
        api_response = api_instance.api_cards_api_key_check_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_check_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # check
        api_response = api_instance.api_cards_api_key_check_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_check_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**CheckFields**](CheckFields.md)| check method data | [optional]

### Return type

[**CheckResponse**](CheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_deregister_post**
> bool, date, datetime, dict, float, int, list, str, none_type api_cards_api_key_deregister_post(api_key)

deregister

The method used to deregister client credit card token from Tpay and Merchant system.<br/>A client can also do it himself from the link in an email after payment.<br/><br/>After successful deregistration Merchant will not be able anymore to charge client's card. Tpay system sends notification about this deregistration to merchant endpoint, defined in merchant panel settings.<br/><br/><b>NOTICE:</b> To test this method you need to generate client token and calculate sign with your own API access data.

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.deregister_fields import DeregisterFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = DeregisterFields(
        cli_auth=CliAuth("t59c2810d59285e3e0ee9d1f1eda1c2f4c554e24"),
        language=Language("pl"),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="sign_example",
    ) # DeregisterFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # deregister
        api_response = api_instance.api_cards_api_key_deregister_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_deregister_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # deregister
        api_response = api_instance.api_cards_api_key_deregister_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_deregister_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**DeregisterFields**](DeregisterFields.md)| Transaction data. | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_presale_post**
> RegisterSaleResponse api_cards_api_key_presale_post(api_key)

presale

The method used to create a new sale for payment on demand. It can be called after receiving a notification with client registered token (cli_auth parameter). It can not be used if 'onetimer' parameter was sent in register_sale or client has unregistered (by the link in an email sent by tpay.com after registering client’s credit card or by API).<br/><br/><b>Additional information</b> Please feel free to read detailed case study of <a href=\"https://support.tpay.com/en/case-study/wdrozenie-platnosci-rekurencyjnych-cyklicznych\" target=\"_blank\">Implementation of the recurrent payments</a>

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.presale_fields import PresaleFields
from openapi_client.model.register_sale_response import RegisterSaleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = PresaleFields(
        desc=Desc("payment for order xyz"),
        cli_auth=CliAuth("t59c2810d59285e3e0ee9d1f1eda1c2f4c554e24"),
        amount=Amount(10.99),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="1355b3d2584af8a1fa44573171d25b316ef16b4f",
        currency=Currency(985),
        order_id=OrderId("32145"),
        language=Language("pl"),
    ) # PresaleFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # presale
        api_response = api_instance.api_cards_api_key_presale_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_presale_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # presale
        api_response = api_instance.api_cards_api_key_presale_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_presale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**PresaleFields**](PresaleFields.md)| Transaction data. | [optional]

### Return type

[**RegisterSaleResponse**](RegisterSaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_refund_post**
> RefundResponse api_cards_api_key_refund_post(api_key)

refund

The method used to transfer money back to the client. The refund can reference to chosen sale (sale_auth) or directly to the client (cli_auth).<br/><br/> In both cases, the amount is adjustable in parameter amount. If the only cli_auth is sent, the amount parameter is required. If sale_auth is passed amount and currency are not necessary - the system will take default values from the specified sale and make a full amount refund.<br/>If you pass the amount parameter and specific sale_auth, you can create more than one refund until the sum of all refunds reach the transaction amount. <br><br/> In test mode this method has 50% probability of success and the status parameter is picked randomly. <br/>

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.refund_fields import RefundFields
from openapi_client.model.refund_response import RefundResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = RefundFields(
        cli_auth=CliAuth("t59c2810d59285e3e0ee9d1f1eda1c2f4c554e24"),
        sale_auth=SaleAuth("t59c28295aeb071b0cf6471b24f727f6456998de"),
        desc="desc_example",
        currency=Currency(985),
        amount=Amount(10.99),
        language=Language("pl"),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="sign_example",
    ) # RefundFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # refund
        api_response = api_instance.api_cards_api_key_refund_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_refund_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # refund
        api_response = api_instance.api_cards_api_key_refund_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_refund_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**RefundFields**](RefundFields.md)| Transaction data. | [optional]

### Return type

[**RefundResponse**](RefundResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_register_sale_post**
> RegisterSaleResponse api_cards_api_key_register_sale_post(api_key)

register sale

The method used to create sale initialisation in tpay.com system. The successful request returns sale_auth used to redirect a client to transaction panel. <br><br>The parameter sale_auth can be used to redirect a client to payment transaction panel:  <br> <b> https://secure.tpay.com/cards/ </b><br> with argument sale_auth passed with the POST or GET method. <br><br> <b>Test mode notice!</b><br> In test mode, the transaction panel offers multiple system answers. You can choose at the transaction panel (instead of making a real transaction) to accept or decline payment to test all paths. In production mode client will be directly redirected to payment gateway with credit card data form. <br> Notification about positive transaction status will be sent to result URL which is set in account settings. 

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.register_sale_fields import RegisterSaleFields
from openapi_client.model.register_sale_response import RegisterSaleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = RegisterSaleFields(
        name=Name("john doe"),
        email=Email("customer@example.com"),
        desc=Desc("payment for order xyz"),
        amount=Amount(10.99),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="deb0bcd83171226c0df366910a6ee6ef22046d69",
        currency=Currency(985),
        onetimer=Onetimer("1"),
        pow_url=PowUrl("https://shop.tpay.com/success"),
        pow_url_blad=PowUrlBlad("https://shop.tpay.com/error"),
        order_id=OrderId("32145"),
        language=Language("pl"),
    ) # RegisterSaleFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # register sale
        api_response = api_instance.api_cards_api_key_register_sale_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_register_sale_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # register sale
        api_response = api_instance.api_cards_api_key_register_sale_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_register_sale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**RegisterSaleFields**](RegisterSaleFields.md)| Transaction data. | [optional]

### Return type

[**RegisterSaleResponse**](RegisterSaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_sale_post**
> SaleResponse api_cards_api_key_sale_post(api_key)

sale

The method used to execute created sale with presale method. Sale defined with sale_auth can be executed only once. If the method is called second time with the same parameters, the system returns actual sale status - in parameter status - done for correct payment and declined for rejected payment. In that case, client card is not charged the second time. <br><br> Passed cli_auth has to match with cli_auth used while creating a sale in presale method. <br><br><b>Test mode notice!</b> The method will return correct status with 50% probability. The same concerns declined status. In this case, reason value is also randomly picked.

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.sale_fields import SaleFields
from openapi_client.model.sale_response import SaleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = SaleFields(
        cli_auth=CliAuth("t59c2810d59285e3e0ee9d1f1eda1c2f4c554e24"),
        sale_auth=SaleAuth("t59c28295aeb071b0cf6471b24f727f6456998de"),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="231f533d91cf3ec6ce5d02d672beb4b127e1e987",
    ) # SaleFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # sale
        api_response = api_instance.api_cards_api_key_sale_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_sale_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # sale
        api_response = api_instance.api_cards_api_key_sale_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_sale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**SaleFields**](SaleFields.md)| Transaction data. | [optional]

### Return type

[**SaleResponse**](SaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_securesale_post**
> SecuresaleResponse api_cards_api_key_securesale_post(api_key)

secure sale

 This method allows Merchant to host payment form on his website and perform sale without any client redirection to tpay.com  system. Securesale method supports 3D Secure validation which is an additional security layer for online credit and debit card transactions. This approach requires special security considerations. We support secure communication by encrypting card data (card number, validity date and cvv/cvs number) on the client side (javascript) with Merchant public RSA key and send it as one parameter (card) to our API gate. A valid SSL certificate on the Merchant domain is required. Application flow is presented below for clarification:<br/><br/> 1. Generate webpage with your public RSA key in javascript<br/> 2. Before sending payment form, insert new input with encrypted card data using your public key and clear inputs with card data so only encrypted data will be sent and submit form. <br/> 3. In backend prepare parameters and send them with securesale method  <br/> 4. Inform client about payment result<br/> <br/> Card cypher is made from string<br/><br/> card number|expiry date(MM/YY or MM/YYYY)|cvv or cvc|host  <br/><br/> eg. \"1234567891234567|05/17|123|https://merchantwebsite.com\"  <br/><br/> We have published code samples, libraries and instructions to give some insights on the process - see https://github.com/tpay-com/tpay-php . The library used in the example has a limit of 117 input characters for encryption.  <br/> <b>In production mode, this generated hash works only once and should always be generated even for the same card data.</b><br/><br/> There are two ways for performing payment<br/><br/> a)  <b>Pay by card without  3D- Secure.</b> <br/> If input parameters are correct, request is processed correctly and the entered card does not have the 3D-Secure option enabled, method returns parameters in JSON format<br/><br/> b)  <b>Pay by card with 3D-Secure.</b> <br/>If input parameters are correct, the request is processed correctly and the card has enabled the 3D-Secure, the method returns the 3ds_url parameter in JSON format. <br/><br/> An example 3ds URL is presented below <br/><br/> https://secure.tpay.com/cards/?sale_auth=2587bf3a98dfa699ef9d01eba38359b7 <br/><br/> •  The best way to implement 3DS is to open a link to 3D-Secure authentication in a new window. If this method is used, parameter \"enable_pow_url\"  should be sent with value 1.  After a correct authorization, a customer will be redirected to the Merchant’s Site. Return URL is set in Merchant’s Panel or sent dynamically. <br/><br/> •  Do not use an inline frame to implement the 3D-Secure authentication on Merchant’s Site. In this case, some banks can block 3DS authorisation. <br/><br/> The parameters are sent with POST method. Merchant system has to respond to the notification by printing array in JSON format.<br/> See Card's notifications section.<br/><br/> <b>Test mode notice!</b>  <br/>In test mode, transaction panel offers the choice of system answer for transactions with 3D-Secure authentication. You can choose to accept or decline payment to test all paths.<br/><br/><b>Additional information</b> Please feel free to read detailed case study of <a href=\"https://support.tpay.com/en/case-study/wdrozenie-bramki-platnosci-kartami-na-stronie-sklepu\" target=\"_blank\">Implementation of the card payment gateway at the store's website<a/>

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.securesale_fields import SecuresaleFields
from openapi_client.model.securesale_response import SecuresaleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = SecuresaleFields(
        name=Name("john doe"),
        email=Email("customer@example.com"),
        desc=Desc("payment for order xyz"),
        amount=Amount(10.99),
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        sign="e98c24cbd85248ce1304e139d80a3a4c0413b597",
        currency=Currency(985),
        onetimer=Onetimer("1"),
        pow_url=PowUrl("https://shop.tpay.com/success"),
        pow_url_blad=PowUrlBlad("https://shop.tpay.com/error"),
        order_id=OrderId("32145"),
        language=Language("pl"),
        enable_pow_url=1,
        card="SrKhV6VEPiaw4cQEM2Mr0Nj7fuVhRdAdQ9Bk+sv7iM/St12s/W4zRNyqVptN3KIVMqr6coRXNfSPF/o/N9pLy94koY255N5U8wc/ApsBVyo7tlV7xQDxM+I5ksZ3f11qhxzIsk8inmzQGJywrg9CGvZAoiHazgDSVRuy7Tj4vbk=",
    ) # SecuresaleFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # secure sale
        api_response = api_instance.api_cards_api_key_securesale_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_securesale_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # secure sale
        api_response = api_instance.api_cards_api_key_securesale_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_securesale_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**SecuresaleFields**](SecuresaleFields.md)| Transaction data. | [optional]

### Return type

[**SecuresaleResponse**](SecuresaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_visacheckout_finish_post**
> SecuresaleResponse api_cards_api_key_visacheckout_finish_post(api_key)

visacheckout finish

The Method used to finish Visa Checkout payment. <br/><br/> Summary_data has format compliant with Visa Checkout Summary Payment Data. Its structure is described in Visa Checkout documentation at <a href=\"https://developer.visa.com/products/visa_checkout/guides#extracting-consumer-data\">extracting-consumer-data</a><br><br/> The example table with this format can be found at <a href=\"https://developer.visa.com/capabilities/visa_checkout/docs#pdfs_for_merchants_integrating_with_visa_checkout\">Link</a> <br><br>When some data change between visacheckout_prepare and visacheckout_finish, you should send the modified data with the summary_data table. You can only send to tpay.com the data, which changes (i.e. only the amount ) but you need to send it in the summary_data JSON structure. <br/>Other fields if not changed don’t have to be sent.<br/> The response format is the same as in SecureSale method - see the method for more details.<br/><br/><b>NOTICE:</b> To use Visa Checkout methods, you need to have access to cards API at your account and pass Visa requirements (see Visa Checkout Integration section).

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.vc_finish_fields import VcFinishFields
from openapi_client.model.securesale_response import SecuresaleResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = VcFinishFields(
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        summary_data=[
            VcFinishRequestExample([
                {
                    payment_request=[
                        {
                            currency_code="USD",
                            total="100",
                            order_id="abcd1234",
                            description="Payment for order 1234",
                            subtotal="80",
                            shipping_handling="5",
                            tax="5",
                            discount="5",
                            gift_wrap="10",
                            misc="5",
                            promo_code="CampaignPromoCode",
                        },
                    ],
                    risk_data=[
                        {
                            avs_response_code="Y",
                        },
                    ],
                    partial_shipping_address=[
                        {
                            country_code="US",
                        },
                    ],
                },
            ]),
        ],
        call_id="call_id_example",
        language=Language("pl"),
        sign="sign_example",
        enable_pow_url=1,
    ) # VcFinishFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # visacheckout finish
        api_response = api_instance.api_cards_api_key_visacheckout_finish_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_visacheckout_finish_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # visacheckout finish
        api_response = api_instance.api_cards_api_key_visacheckout_finish_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_visacheckout_finish_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**VcFinishFields**](VcFinishFields.md)| Transaction data. | [optional]

### Return type

[**SecuresaleResponse**](SecuresaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_cards_api_key_visacheckout_prepare_post**
> VcPrepareResponse api_cards_api_key_visacheckout_prepare_post(api_key)

visacheckout prepare

The method used to prepare Visa Checkout payment. <br/><br/><b>NOTICE:</b> To use Visa Checkout methods, you need to have access to cards API at your account and pass Visa requirements (see Visa Checkout Integration section).

### Example

```python
import time
import openapi_client
from openapi_client.api import cards_api_api
from openapi_client.model.vc_prepare_fields import VcPrepareFields
from openapi_client.model.vc_prepare_response import VcPrepareResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = cards_api_api.CardsAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = VcPrepareFields(
        api_password=CardApiPassword("XtCns9OAue8zSFJ"),
        call_id="",
        language=Language("pl"),
        sign="sign_example",
    ) # VcPrepareFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # visacheckout prepare
        api_response = api_instance.api_cards_api_key_visacheckout_prepare_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_visacheckout_prepare_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # visacheckout prepare
        api_response = api_instance.api_cards_api_key_visacheckout_prepare_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CardsAPIApi->api_cards_api_key_visacheckout_prepare_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**VcPrepareFields**](VcPrepareFields.md)| Transaction data. | [optional]

### Return type

[**VcPrepareResponse**](VcPrepareResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**401** | Api password is incorrect |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

