# MasspaymentCreateFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv** | **str** | Transfers list encoded with base64. Format has been described in metchod description | 
**api_password** | [**ApiPassword**](ApiPassword.md) |  | 
**sign** | **str** | Checksum to verify parameters received from Merchant. Generated according to outline below using SHA1 function: SHA1(seller_id + transfers list (before encrypting in base64) + Merchant confirmation code) Implementing checksum in PHP: sha1($seller_id. $csv . $confirmation_code)  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


