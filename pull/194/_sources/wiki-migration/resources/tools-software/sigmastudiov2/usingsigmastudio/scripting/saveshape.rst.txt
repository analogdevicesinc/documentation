:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Save Shape
==========

This action allows the user to save a shape as a .Shape file into their desired path. The function call takes in 2 arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult SaveShape(string shapeUid, string savePath)

| 
| ===Arguments====

-  shapeUid- Uid of the Shape the user wants to save.
-  savePath- The path where the user wants to save the shape.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the SaveShape action.

::

   -IsSuccess is 'True' if the shape saved successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
