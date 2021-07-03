# RegisterSaleResponse

Successful response schema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | [optional] 
**sale_auth** | [**SaleAuth**](SaleAuth.md) |  | [optional] 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): sha1(sale_auth + verification code) where + means concatenation. | [optional] 
**err_code** | [**CardsErrCode**](CardsErrCode.md) |  | [optional] 
**err_desc** | **str** | Error code description if an error occurs or not present in response. - see \&quot;Card Payments Rejection Codes\&quot; for more details | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


