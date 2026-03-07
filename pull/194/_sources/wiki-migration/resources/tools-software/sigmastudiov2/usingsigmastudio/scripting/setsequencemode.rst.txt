:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Set Sequence Mode
=================

| This action allows the user to select a specific sequence mode from the SS+ sequence window modes. The function call takes 1 argument. This API returns the SSPResult type.
| ===API===

::

   SSPResult SetSequenceMode(int index)         

| 
| ===Arguments====

-  index- Index of the sequence mode.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the SetSequenceMode action.

::

   -IsSuccess is 'True' if the sequence mode selected successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
