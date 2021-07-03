# SaleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | 
**sale_auth** | [**SaleAuth**](SaleAuth.md) |  | 
**currency** | [**Currency**](Currency.md) |  | 
**amount** | [**Amount**](Amount.md) |  | 
**status** | **str** |  | 
**sign** | **str** | Response sign &#x3D; hash_alg(test_mode + sale_auth + cli_auth + currency + amount + date + status + reason + verification code) | 
**test_mode** | **str** | This parameter is present in response and included in sign calculation only when the merchant account is in test mode. | [optional] 
**cli_auth** | [**CliAuth**](CliAuth.md) |  | [optional] 
**date** | [**Date**](Date.md) |  | [optional] 
**reason** | **str** | Acquirer (Elavon / eService) rejection code - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


