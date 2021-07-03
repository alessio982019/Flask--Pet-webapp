# openapi_client.RegistrationApi

All URIs are relative to *https://docs.tpay.com/Proxy.php*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_gw_api_key_registration_inputs_post**](RegistrationApi.md#api_gw_api_key_registration_inputs_post) | **POST** /api/gw/{api_key}/registration/inputs | inputs
[**api_gw_api_key_registration_register_post**](RegistrationApi.md#api_gw_api_key_registration_register_post) | **POST** /api/gw/{api_key}/registration/register | register


# **api_gw_api_key_registration_inputs_post**
> RegistrationInputsResponse api_gw_api_key_registration_inputs_post(api_key)

inputs

This method returns branches list and legal forms list which are available in Tpay.com. These data are required to correctly merchant registration. Branch id and legal form id should be sent in register method.

### Example

```python
import time
import openapi_client
from openapi_client.api import registration_api
from openapi_client.model.registration_inputs_response import RegistrationInputsResponse
from openapi_client.model.registration_input_fields import RegistrationInputFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registration_api.RegistrationApi(api_client)
    api_key = "api_key_example" # str | The api key.
    basic_data = RegistrationInputFields(
        api_password=RegistrationApiPassword("QlxXs4omRqBf2HTlxCTj"),
    ) # RegistrationInputFields | Registration inputs. (optional)

    # example passing only required values which don't have defaults set
    try:
        # inputs
        api_response = api_instance.api_gw_api_key_registration_inputs_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationApi->api_gw_api_key_registration_inputs_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # inputs
        api_response = api_instance.api_gw_api_key_registration_inputs_post(api_key, basic_data=basic_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationApi->api_gw_api_key_registration_inputs_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **basic_data** | [**RegistrationInputFields**](RegistrationInputFields.md)| Registration inputs. | [optional]

### Return type

[**RegistrationInputsResponse**](RegistrationInputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**403** | Access denied |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_gw_api_key_registration_register_post**
> RegistrationRegisterResponse api_gw_api_key_registration_register_post(api_key)

register

This method allows register new account in Tpay.com system. In response, the method returns data which can be used to generate new transactions. Optionally method returns access data for API transactions

### Example

```python
import time
import openapi_client
from openapi_client.api import registration_api
from openapi_client.model.registration_register_response import RegistrationRegisterResponse
from openapi_client.model.register_fields import RegisterFields
from pprint import pprint
# Defining the host is optional and defaults to https://docs.tpay.com/Proxy.php
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://docs.tpay.com/Proxy.php"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = registration_api.RegistrationApi(api_client)
    api_key = "api_key_example" # str | The api key.
    registrtation_register_data = RegisterFields(
        email="merchant@example.com",
        name="Example Company",
        nip="1537590473",
        regon="191732137",
        krsedg="901911",
        legal_form="sc",
        branche=78,
        website="https://shop.tpay.com",
        phone="666444555",
        address_street="ul. Szkolna",
        address_block="11",
        address_nr="7",
        address_city="Warszawa",
        address_code="55-100",
        create_api=1,
        offer_code="OFF3R",
        test=1,
        api_password=RegistrationApiPassword("QlxXs4omRqBf2HTlxCTj"),
    ) # RegisterFields | Register data (optional)

    # example passing only required values which don't have defaults set
    try:
        # register
        api_response = api_instance.api_gw_api_key_registration_register_post(api_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationApi->api_gw_api_key_registration_register_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # register
        api_response = api_instance.api_gw_api_key_registration_register_post(api_key, registrtation_register_data=registrtation_register_data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RegistrationApi->api_gw_api_key_registration_register_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key** | **str**| The api key. |
 **registrtation_register_data** | [**RegisterFields**](RegisterFields.md)| Register data | [optional]

### Return type

[**RegistrationRegisterResponse**](RegistrationRegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | tpay response |  -  |
**403** | Access denied |  -  |
**404** | Invalid api key or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

