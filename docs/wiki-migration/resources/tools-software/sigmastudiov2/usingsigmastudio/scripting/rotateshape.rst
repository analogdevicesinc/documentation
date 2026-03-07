:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Rotate Shape
============

This action allows the user to rotate a specified shape on the parent canvas or schematic page according to the angle given. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult RotateShape(string shapeUid, Position newPosition, double newAngle)

| 
| ===Arguments====

-  shapeUid- Uid of the plugin to be moved.
-  newPosition -Position in the form of (double X, double Y) coordinates of the canvas.
-  newAngle -Angle of rotation in degrees.

| 

Result
------

SSPResult contains 'IsSuccess' flag and 'Message' information of the RotateShape action.

::

   -IsSuccess is 'True' for successful shape rotation, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

|
