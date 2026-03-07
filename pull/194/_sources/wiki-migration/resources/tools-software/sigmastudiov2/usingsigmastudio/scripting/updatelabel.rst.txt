:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Update Label
============

This action allows the user to change the label of the specified shape. The function call takes in 2 arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult UpdateLabel(string shapeUid, string label)

| 
| ===Arguments====

-  shapeUid- Uid of the Shape where the user wants to change the label.
-  label- The new changed label.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the UpdateLabel action.

::

   -IsSuccess is 'True' if the label is changed successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
