:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Delete Sequence Mode
====================

| This action allows the user to delete the selected sequence mode from SS+ Sequence window. The function call doesn't have any arguments. This API returns the SSPResult type.
| ===API===

::

   SSPResult DeleteSequenceMode()            

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the DeleteSequenceMode action.

::

   -IsSuccess is 'True' if the sequence mode is deleted successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
