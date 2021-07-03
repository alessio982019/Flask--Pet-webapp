# DeregisterFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cli_auth** | [**CliAuth**](CliAuth.md) |  | 
**api_password** | [**CardApiPassword**](CardApiPassword.md) |  | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + cli_auth + language + verification code) where + means concatenation. | 
**language** | [**Language**](Language.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


