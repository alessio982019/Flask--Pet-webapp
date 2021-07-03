# TransfersObject

Each transfer object represents one transfer within specific transfers pack.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | Date of creating payment | [optional] 
**auth_date** | **str** | Date of payment authorization (method authorize). Field can be empty. | [optional] 
**acc_date** | **str** | Date of posting payment | [optional] 
**status** | **str** | Payment status | [optional] 
**accnum** | **str** | Bank account number (format IBAN, 26 digits) | [optional] 
**rcv1** | **str** | Receiver name (first part) | [optional] 
**rcv2** | **str** | Receiver name (second part) | [optional] 
**rcv3** | **str** | Receiver name (third part) | [optional] 
**rcv4** | **str** | Receiver name (fourth part) | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**title1** | **str** | Payment title (first part) | [optional] 
**title2** | **str** | Payment title (second part) | [optional] 
**tr_id** | **float** | Payment ID in tpay.com system | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


