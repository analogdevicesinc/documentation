:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Get Pin Collections
===================

| This action allows the user to get input and output pins details of a specified module which is present in the canvas. The function call takes in 1 arguments. This API returns the SSPResult type.
| ===API===

::

   SSPResult GetPinCollections(string ModuleUid)            

| 
| ===Arguments====

-  ModuleUid- The Uid of the module to fetch pin details.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the GetPinCollections action.

::

   -IsSuccess is 'True' if the pin details are fetched successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
