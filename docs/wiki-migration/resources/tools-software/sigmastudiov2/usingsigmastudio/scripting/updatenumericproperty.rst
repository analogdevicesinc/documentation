:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Update Numeric Property
=======================

This action allows the user to update a numeric property of a given plugin. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult UpdateNumericProperty(string elementUid, string propertyName, double propertyVal);

| 
| ===Arguments====

-  elementUid - Uid of shape whose property must be updated.
-  propertyName - Name of the property to be updated.
-  propertyVal - New numeric value for the property.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the UpdateNumericProperty action.

::

   -IsSuccess is 'True' if the property updated successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
