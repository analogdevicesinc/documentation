:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Add Shape
=========

| This action allows the user to add a shape or plugin onto the canvas or schematic page specified.The function call takes in 3 arguments. This API returns the SSPResult type.
| ===API===

::

   SSPResult AddShape(string parentUid, string shapeFullName, Position newPosition)              

| 
| ===Arguments====

-  parentUid - The Uid of the parent canvas/Schematic onto which the plugin must be added.
-  shapeFullName - Full name of the plugin to be added, as obtained in the documentation provided by Analog Devices.
-  newPosition - Position on the canvas page where the user wishes to add the plugin. Default values are chosen if not specified.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the AddShape action.

::

   -IsSuccess is 'True' if the add shape was successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
