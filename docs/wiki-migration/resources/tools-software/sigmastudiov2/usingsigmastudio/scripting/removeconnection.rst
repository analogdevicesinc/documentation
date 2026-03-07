:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Remove Connection
=================

| This action allows the user to remove a specified connection between two elements on the parent canvas or schematic page. The function call takes in 3 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.
| ===API===

::

   SSPResult RemoveConnection(string parentUid, string channelUid, string linkUid)

| 
| ===Arguments====

-  parentUid - The Uid of the parent canvas/Schematic onto which the plugin must be added
-  channelUid- Uid of the channel which the link belongs to.
-  linkUid -Uid of the link that is to be removed

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the RemoveConnection action.

::

   -IsSuccess is 'True' if the remove/delete connection was successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
