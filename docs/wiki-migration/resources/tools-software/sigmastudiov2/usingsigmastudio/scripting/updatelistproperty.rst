:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Update List Property
====================

This action allows the user to update the list of numeric values of a given plugin. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult UpdateListProperty(string elementUid, string propertyName, List<double> propertyVal)

| 
| ===Arguments====

-  elementUid - Uid of shape whose property must be updated.
-  propertyName - Name of the property to be updated.
-  propertyVal - New list of double values for the property

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the UpdateListProperty action.

::

   -IsSuccess is 'True' if the property updated successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
