# SecuresaleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_3ds_url** | **str** |  | [optional] 
**result** | [**Result**](Result.md) |  | [optional] 
**test_mode** | **str** | This parameter is present in response and included in sign calculation only when the merchant account is in test mode. | [optional] 
**sale_auth** | [**SaleAuth**](SaleAuth.md) |  | [optional] 
**cli_auth** | [**CliAuth**](CliAuth.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**date** | [**Date**](Date.md) |  | [optional] 
**status** | **str** |  | [optional] 
**reason** | **str** | Acquirer (Elavon / eService) rejection code - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**card** | **str** | Card number last 4 digits - for example ****1234 | [optional] 
**sign** | **str** | sign is calculated from cryptographic hash function set in Merchant panel (default SHA-1) hash_alg(test_mode + sale_auth + cli_auth + card + currency + amount + date + status + verification code)  | [optional] 
**err_code** | [**CardsErrCode**](CardsErrCode.md) |  | [optional] 
**err_desc** | **str** | Error code description if an error occurs or not present in response. - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


