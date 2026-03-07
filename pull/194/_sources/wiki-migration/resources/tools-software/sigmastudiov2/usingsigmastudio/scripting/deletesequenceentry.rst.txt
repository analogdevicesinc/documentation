:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Delete Sequence Entry
=====================

| This action allows the user to delete sequence entry from the selected sequence mode in the SS+ sequence window. The function call takes 1 argument. This API returns the SSPResult type.
| ===API===

::

   SSPResult DeleteSequenceEntry(int index)         

| 
| ===Arguments====

-  index- Index of the sequence entry.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the DeleteSequenceEntry action.

::

   -IsSuccess is 'True' if the sequence entry deleted successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
