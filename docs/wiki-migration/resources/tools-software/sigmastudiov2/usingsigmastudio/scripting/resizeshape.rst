:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Resize Shape
============

This action allows the user to resize a specified shape on the parent canvas or schematic page according to the angle given. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult ResizeShape(string shapeUid, Position newPosition, Size newSize)

| 
| ===Arguments====

-  shapeUid- Uid of the plugin to be moved.
-  newPosition -Position in the form of (double X, double Y) coordinates of the canvas.
-  newSize -Desired size of the shape in the form of (double Width, double Height).

| 

Result
------

SSPResult contains 'IsSuccess' flag and 'Message' information of the ResizeShape action.

::

   -IsSuccess is 'True' if the resize on the shape was successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

|
