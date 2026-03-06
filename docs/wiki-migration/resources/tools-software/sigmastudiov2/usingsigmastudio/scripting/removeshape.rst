:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Remove Shape
============

This action allows the user to remove/delete a given element or plugin from the parent canvas or schematic page specified. The function call takes in 2 arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult RemoveShape(string parentUid, string shapeUid)

| 
| ===Arguments====

-  parentUid - The Uid of the parent canvas/Schematic from which the plugin must be removed
-  shapeUid- Uid of the plugin to be removed.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the RemoveShape action.

::

   -IsSuccess is 'True' if the shape was removed successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
