# ReportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**Result**](Result.md) |  | [optional] 
**report** | **str** | Report content encoded in base64. Characters encoding is UTF8. After decoding the report you will get: &lt;br&gt; (header[NL], empty line[NL], columns description[NL], transactions list, each in new line, where [NL] is a new line indicator): Summary of transactions and refunds sorted by dates&lt;br/&gt; LP;Transaction ID;Transaction amount;Paid amount;commission %;flat commission; commission taken;Transaction CRC;Transaction description;Payment date;Refund date;E-mail;Customer name;Address;Postal code;City;Country;Phone;Additional description (Acquirer (Elavon / eService));RRN (Acquirer (Elavon / eService)) &lt;br/&gt; Columns are separated by ; (semicolon). | [optional] 
**err** | [**TransactionErrorCodes**](TransactionErrorCodes.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


