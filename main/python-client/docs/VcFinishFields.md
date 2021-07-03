# VcFinishFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_password** | [**CardApiPassword**](CardApiPassword.md) |  | 
**call_id** | **str** | Visa Checkout Call Id | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant’s Panel (default SHA-1): hash_alg (method + call_id + language + enable_pow_url + verification code) where + means concatenation. | 
**summary_data** | [**[VcFinishRequestExample]**](VcFinishRequestExample.md) | Modified summary_data parameter received from visacheckout_prepare. Can be used, when the total amount or other parameters changea in the order process. | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**enable_pow_url** | **int** | If parameter was sent, system will redirect a cutomer to the merchant site after payment. 1 – redirect Adress is set in Merchant Panel. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


