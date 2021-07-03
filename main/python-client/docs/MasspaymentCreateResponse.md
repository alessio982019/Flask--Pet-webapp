# MasspaymentCreateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | [optional] 
**sum** | **float** | Sum of transfers in the package | [optional] 
**count** | **int** | Number of transfers defined in CSV file | [optional] 
**pack_id** | **int** | ID of created pack using method create. | [optional] 
**referers** | **str** | Field visible if transfersID has been sent (see chap. \&quot;Exemplary CSV file\&quot;) in JSON format as following: ID in transfer : ID of transfers in tpay.com system. This allows tracking single transfers.  | [optional] 
**error** | [**MasspaymentErrCode**](MasspaymentErrCode.md) |  | [optional] 
**desc** | [**MasspaymentErrDesc**](MasspaymentErrDesc.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


