:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Move Shape
==========

This action allows the user to move a specified shape on the parent canvas or schematic page to a given position.The function call takes in 2 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult MoveShape(string shapeUid, Position newPosition)

| 
| ===Arguments====

-  shapeUid- Uid of the plugin to be moved.
-  newPosition -Position in the form of (double X, double Y) coordinates of the canvas.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the MoveShape action.

::

   -IsSuccess is 'True' if the shape moved successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
