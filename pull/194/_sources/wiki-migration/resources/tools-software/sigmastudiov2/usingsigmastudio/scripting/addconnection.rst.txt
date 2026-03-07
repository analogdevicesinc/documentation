:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Add Connection
==============

This action allows the user to add connection between two elements specified on the parent canvas or schematic page. The function call takes in 8 arguments. Return type is a SSPResult.

| 
| ===API===

::

   SSPResult AddConnection(string parentUid, string channelFullName, string sourceUid, string targetUid, string sourcePinType, string targetPinType, string sourcePinName, string targetPinName)

| 
| ===Arguments====

-  parentUid - The Uid of the parent canvas/Schematic onto which the plugin must be added.
-  channelFullName- Full name of the channel with its version number (i.e., in the form of “FullName_vw.x.y.z”, where w, x, y and z are integers).
-  sourceUid -Uid of the source element.
-  targetUid -Uid of the target element.
-  sourcePinType -Pin type of the source element.
-  targetPinType -Pin type of the target element.
-  sourcePinName -Pin name of the source element.
-  targetPinName -Pin name of the target element.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the AddConnection action.

::

   -IsSuccess is 'True' if the connection added successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string. The message information contains newly added channel uid and link uid if IsSuccess is true. 

| 
