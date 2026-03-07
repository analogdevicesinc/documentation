:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Load Shape
==========

This action allows the user to load a saved shape file into their desired shape. The function call takes in 2 arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult LoadShape(string shapeUid, string loadPath)

| 
| ===Arguments====

-  uid- Uid of the Shape the user wants to load it to.
-  loadPath- The path of the shape file the user wants to load it from.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the LoadShape action.

::

   -IsSuccess is 'True' if the shape loaded successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
