:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Update Properties
=================

This action allows the user to update a specific property of a given plugin. The function call takes in 4 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult UpdateProperties(string elementUid, string propertyName, string propertyType, string propertyValue)

| 
| ===Arguments====

-  elementUid - Uid of shape whose property must be updated.
-  propertyName - Name of the property to be updated.
-  propertyType - Data type of the property’s value
-  propertyValue - New value for the property

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the UpdateProperties action.

::

   -IsSuccess is 'True' if the property updated successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
