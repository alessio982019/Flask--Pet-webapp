# SaleFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_auth** | [**CliAuth**](CliAuth.md) |  | 
**sale_auth** | [**SaleAuth**](SaleAuth.md) |  | 
**api_password** | [**CardApiPassword**](CardApiPassword.md) |  | 
**sign** | **str** | Request sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + sale_auth + verification code); where + means concatenation. Passed cli_auth has to match with cli_auth used while creating sale in presale method.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


