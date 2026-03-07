:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

New Sequence
============

This action allows the user to reset the Sequence window which will remove all the existing details and provide a fresh sequence window. The function doesn't have any arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult NewSequence()


   | 

|

| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the NewSequence action.

::

   -IsSuccess is 'True' if the reset is successful, else 'False'.
   -Message contains the Success/Failure information in the form of a list of strings.

| 
