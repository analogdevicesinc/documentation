:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Update String Property
======================

This action allows the user to update the string property of a given plugin. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal)

| 
| ===Arguments====

-  elementUid - Uid of shape whose property must be updated.
-  propertyName - Name of the property to be updated.
-  propertyVal - string value for the property

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the UpdateStringProperty action.

::

   -IsSuccess is 'True' if the property updated successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
