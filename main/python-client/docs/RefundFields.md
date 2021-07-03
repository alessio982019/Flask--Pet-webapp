# RefundFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** |  | 
**api_password** | [**CardApiPassword**](CardApiPassword.md) |  | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + sale_auth + desc + amount + currency + language + verification code); where + means concatenation.  | 
**cli_auth** | [**CliAuth**](CliAuth.md) |  | [optional] 
**sale_auth** | [**SaleAuth**](SaleAuth.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


