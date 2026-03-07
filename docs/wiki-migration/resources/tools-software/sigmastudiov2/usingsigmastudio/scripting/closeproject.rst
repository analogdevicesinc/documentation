:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Close Project
=============

This action allows the user to close the project opened in the SigmaStudioPlus application. The function doesn't have any arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult CloseProject()


   | 

|

| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the CloseProject action.

::

   -IsSuccess is 'True' if the project is closed successfully, else 'False'.
   -Message contains the Success/Failure information in the form of a list of strings.

| 
