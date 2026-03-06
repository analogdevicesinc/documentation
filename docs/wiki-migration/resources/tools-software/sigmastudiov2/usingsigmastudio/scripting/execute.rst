:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Execute
=======

This action allows the user to perform the specific operation on a given module/shape. The function call takes in 2 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult  Execute(string uid, string action)

| 
| ===Arguments====

-  uid- Uid of the shape/module which user wants to perform any specific action.
-  action- Name of the action to be performed on the module/shape.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the Execute action.

::

   -IsSuccess is 'True' if the execute operation is successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
