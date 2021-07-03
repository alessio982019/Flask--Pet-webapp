# openapi_client.TransactionAPIApi

All URIs are relative to *https://docs.tpay.com/Proxy.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_gw_api_key_chargeback_any_post**](TransactionAPIApi.md#api_gw_api_key_chargeback_any_post) | **POST** /api/gw/{api_key}/chargeback/any | any
[**api_gw_api_key_chargeback_status_post**](TransactionAPIApi.md#api_gw_api_key_chargeback_status_post) | **POST** /api/gw/{api_key}/chargeback/status | status
[**api_gw_api_key_chargeback_transaction_post**](TransactionAPIApi.md#api_gw_api_key_chargeback_transaction_post) | **POST** /api/gw/{api_key}/chargeback/transaction | transaction
[**api_gw_api_key_transaction_blik_post**](TransactionAPIApi.md#api_gw_api_key_transaction_blik_post) | **POST** /api/gw/{api_key}/transaction/blik | blik
[**api_gw_api_key_transaction_create_post**](TransactionAPIApi.md#api_gw_api_key_transaction_create_post) | **POST** /api/gw/{api_key}/transaction/create | create
[**api_gw_api_key_transaction_get_post**](TransactionAPIApi.md#api_gw_api_key_transaction_get_post) | **POST** /api/gw/{api_key}/transaction/get | get
[**api_gw_api_key_transaction_report_post**](TransactionAPIApi.md#api_gw_api_key_transaction_report_post) | **POST** /api/gw/{api_key}/transaction/report | report


# **api_gw_api_key_chargeback_any_post**
> RefundAnyResponse api_gw_api_key_chargeback_any_post(api_key)

any

The method used to refund part of the transaction amount. <br/><br/><b>NOTICE:</b> This method works only in production mode!<br/>To test this method, you need to create the transaction in production mode with your own API access.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.refund_any_fields import RefundAnyFields
from openapi_client.model.refund_any_response import RefundAnyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    refund_any_data = RefundAnyFields(
        title="TR-BRA-KGZK0X",
        chargeback_amount=7.0,
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # RefundAnyFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # any
        api_response = api_instance.api_gw_api_key_chargeback_any_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_any_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # any
        api_response = api_instance.api_gw_api_key_chargeback_any_post(api_key, refund_any_data=refund_any_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_any_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **refund_any_data** | [**RefundAnyFields**](RefundAnyFields.md)| Request body. | [optional]

### Return type

[**RefundAnyResponse**](RefundAnyResponse.md)

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

# **api_gw_api_key_chargeback_status_post**
> RefundStatusResponse api_gw_api_key_chargeback_status_post(api_key)

status

The method used to check transaction refunds statuses.<br/>Some refunds statuses may be not available immediately after calling refund methods due to gathering refund details process.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.refund_status_response import RefundStatusResponse
from openapi_client.model.refund_transaction_fields import RefundTransactionFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    refund_transaction_data = RefundTransactionFields(
        title="TR-BRA-KGZK0X",
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # RefundTransactionFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # status
        api_response = api_instance.api_gw_api_key_chargeback_status_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_status_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # status
        api_response = api_instance.api_gw_api_key_chargeback_status_post(api_key, refund_transaction_data=refund_transaction_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **refund_transaction_data** | [**RefundTransactionFields**](RefundTransactionFields.md)| Request body. | [optional]

### Return type

[**RefundStatusResponse**](RefundStatusResponse.md)

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

# **api_gw_api_key_chargeback_transaction_post**
> RefundAnyResponse api_gw_api_key_chargeback_transaction_post(api_key)

transaction

The method used to refund full transaction amount. You can get transaction title from 'create' method when generating the transaction.<br/><br/><b>NOTICE:</b> This method works only in production mode!<br/>To test this method, you need to create the transaction in production mode with your own API access.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.refund_transaction_fields import RefundTransactionFields
from openapi_client.model.refund_any_response import RefundAnyResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    refund_transaction_data = RefundTransactionFields(
        title="TR-BRA-KGZK0X",
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # RefundTransactionFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # transaction
        api_response = api_instance.api_gw_api_key_chargeback_transaction_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_transaction_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # transaction
        api_response = api_instance.api_gw_api_key_chargeback_transaction_post(api_key, refund_transaction_data=refund_transaction_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_chargeback_transaction_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **refund_transaction_data** | [**RefundTransactionFields**](RefundTransactionFields.md)| Request body. | [optional]

### Return type

[**RefundAnyResponse**](RefundAnyResponse.md)

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

# **api_gw_api_key_transaction_blik_post**
> BlikResponse api_gw_api_key_transaction_blik_post(api_key)

blik

This method allows sending a BLIK code in direct communication between merchant and BLIK system. In ‘create’ method you should set 150 as a value for parameter ‘group’, this is a BLIK payment channel. Method returns parameter ‘result’ equal to 1 which means that payment popup has been successfully displayed at customer mobile application. After accepting payment by the customer, tpay.com system sends a standard notification to merchant's endpoint declared in wyn_url parameter (this parameter should be sent in 'create' method.)<br/><br/><b>NOTICE:</b> to test this method, you need to create the transaction with 'create' method and replace title parameter value with the returned title.<br/>Blik method works with the specific set of parameters depending on payment type case. Please see BLIK workflow section.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.blik_fields import BlikFields
from openapi_client.model.blik_response import BlikResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    blik_data = BlikFields(
        title="TR-BRA-KGZK0X",
        code="123456",
        api_password=ApiPassword("p@$$w0rd#@!"),
        alias=[
            BlikAlias(
                value="TPAY_TEST_ALIAS_REGISTER",
                type="UID",
                key="1",
            ),
        ],
        type=0,
    ) # BlikFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # blik
        api_response = api_instance.api_gw_api_key_transaction_blik_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_blik_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # blik
        api_response = api_instance.api_gw_api_key_transaction_blik_post(api_key, blik_data=blik_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_blik_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **blik_data** | [**BlikFields**](BlikFields.md)| Request body. | [optional]

### Return type

[**BlikResponse**](BlikResponse.md)

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

# **api_gw_api_key_transaction_create_post**
> CreateResponse api_gw_api_key_transaction_create_post(api_key)

create

This method allows you to prepare transaction for a customer. The method returns transaction title required for other API methods and redirection link for a customer.<br/>This method also returns account details for manual money transfers.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.create_fields import CreateFields
from openapi_client.model.create_response import CreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = CreateFields(
        id=1010,
        amount=13.99,
        description="Payment for order X",
        crc="3214",
        md5sum="d061eb61099105315e87d72aeb41ceca",
        group=150,
        result_url="https://shop.tpay.com/shop-endpoint",
        result_email="overwrites_default@tpay.com",
        merchant_description="the best fruit shop",
        custom_description="custom_description_example",
        return_url=PowUrl("https://shop.tpay.com/success"),
        return_error_url=PowUrlBlad("https://shop.tpay.com/error"),
        language="en",
        email=Email("customer@example.com"),
        name=Name("john doe"),
        address="Sunny street 25/7",
        city="New York",
        zip="61-505",
        country="US",
        phone="123456789",
        accept_tos=1,
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # CreateFields | Transaction data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.api_gw_api_key_transaction_create_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_create_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # create
        api_response = api_instance.api_gw_api_key_transaction_create_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_create_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**CreateFields**](CreateFields.md)| Transaction data. | [optional]

### Return type

[**CreateResponse**](CreateResponse.md)

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

# **api_gw_api_key_transaction_get_post**
> GetResponse api_gw_api_key_transaction_get_post(api_key)

get

This method allows you to get all information about the transaction by sending previously generated title.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.get_response import GetResponse
from openapi_client.model.get_fields import GetFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    get_data = GetFields(
        title="TR-BRA-KGZK0X",
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # GetFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.api_gw_api_key_transaction_get_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_get_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get
        api_response = api_instance.api_gw_api_key_transaction_get_post(api_key, get_data=get_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_get_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **get_data** | [**GetFields**](GetFields.md)| Request body. | [optional]

### Return type

[**GetResponse**](GetResponse.md)

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

# **api_gw_api_key_transaction_report_post**
> ReportResponse api_gw_api_key_transaction_report_post(api_key)

report

This method returns payments report for the declared time range, generated in CSV format (semicolon separators) and encoded in base64 - the same format as in merchant panel. If you like to arrange result as an associative array, you can use the ready <a href=\"https://github.com/tpay-com/tpay-php/blob/master/tpayLibs/examples/TransactionReportsApi.php\" target=\"_blank\">script</a> from Tpay PHP library.

### Example

```python
import time
import openapi_client
from openapi_client.api import transaction_api_api
from openapi_client.model.report_response import ReportResponse
from openapi_client.model.report_fields import ReportFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api_api.TransactionAPIApi(api_client)
    api_key = "api_key_example" # str | The api key.
    report_data = ReportFields(
        from_date=dateutil_parser('Fri Sep 01 00:00:00 UTC 2017').date(),
        to_date=dateutil_parser('Fri Sep 22 00:00:00 UTC 2017').date(),
        api_password=ApiPassword("p@$$w0rd#@!"),
    ) # ReportFields | Request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # report
        api_response = api_instance.api_gw_api_key_transaction_report_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_report_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # report
        api_response = api_instance.api_gw_api_key_transaction_report_post(api_key, report_data=report_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TransactionAPIApi->api_gw_api_key_transaction_report_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **report_data** | [**ReportFields**](ReportFields.md)| Request body. | [optional]

### Return type

[**ReportResponse**](ReportResponse.md)

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

