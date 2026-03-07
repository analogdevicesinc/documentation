:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Add Sequence Mode
=================

| This action allows the user to add a sequence mode in the SS+ sequence window. The function call doesn't have any arguments. This API returns the SSPResult type.
| ===API===

::

   SSPResult AddSequenceMode()            

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the AddSequenceMode action.

::

   -IsSuccess is 'True' if the sequence mode added successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
