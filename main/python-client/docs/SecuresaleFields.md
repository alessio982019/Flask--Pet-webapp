# SecuresaleFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**Name**](Name.md) |  | 
**email** | [**Email**](Email.md) |  | 
**desc** | [**Desc**](Desc.md) |  | 
**amount** | [**Amount**](Amount.md) |  | 
**api_password** | [**CardApiPassword**](CardApiPassword.md) |  | 
**sign** | **str** | Sign is calculated from cryptographic hash function set in Merchant panel (default SHA-1) hash_alg (method + card + name + email + desc + amount + currency + order_id + onetimer + language + enable_pow_url + verification code) where + means concatenation.  | 
**currency** | [**Currency**](Currency.md) |  | 
**card** | **str** | Card hash calculated by schema described in method description | 
**onetimer** | [**Onetimer**](Onetimer.md) |  | [optional] 
**pow_url** | [**PowUrl**](PowUrl.md) |  | [optional] 
**pow_url_blad** | [**PowUrlBlad**](PowUrlBlad.md) |  | [optional] 
**order_id** | [**OrderId**](OrderId.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**enable_pow_url** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


