# CreateFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Merchant ID in Tpay.com system | 
**amount** | **float** | Transaction amount. Please always send the amount with two decimal places like 10.00 | 
**description** | **str** | Transaction description | 
**md5sum** | **str** | md5 sum calculated from id.amount.crc.security_code where dots means concatenation (security code can be found in merchant panel). | 
**group** | **int** | Transaction group number see the \&quot;id\&quot; element in https://secure.tpay.com/groups-{id}0.js . For example https://secure.tpay.com/groups-10100.js or https://secure.tpay.com/groups-10100.js?json | 
**email** | [**Email**](Email.md) |  | 
**name** | [**Name**](Name.md) |  | 
**api_password** | [**ApiPassword**](ApiPassword.md) |  | 
**crc** | **str** | Auxiliary parameter to identify the transaction on the merchant side. We do recommend to encode your crc value in base64. The exact value of crc used to create transaction will be returned in tpay payment notification as tr_crc parameter. | [optional] 
**result_url** | **str** | Merchant endpoint for payment notification | [optional] 
**result_email** | **str** | Email address where notification after payment will be sent (overrides defined in merchant panel). You can add more addresses by comma concatenation. | [optional] 
**merchant_description** | **str** | Name of merchant displayed in transaction panel (overrides defined in merchant panel) | [optional] 
**custom_description** | **str** | Additional info to be displayed in transaction panel (overrides defined in merchant panel) | [optional] 
**return_url** | [**PowUrl**](PowUrl.md) |  | [optional] 
**return_error_url** | [**PowUrlBlad**](PowUrlBlad.md) |  | [optional] 
**language** | **str** | Customer language | [optional]  if omitted the server will use the default value of "pl"
**address** | **str** | customer address (parameter is empty if this field was not send with create method) | [optional] 
**city** | **str** | customer city (parameter is empty if this field was not send with create method) | [optional] 
**zip** | **str** | customer postal code (parameter is empty if this field was not send with create method) | [optional] 
**country** | **str** | Two letters - see ISO 3166-1 document | [optional] 
**phone** | **str** | customer phone number (parameter is empty if this field was not send with create method) | [optional] 
**accept_tos** | **int** | Acceptance of Tpay.com regulations done by customer on Merchant site | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


