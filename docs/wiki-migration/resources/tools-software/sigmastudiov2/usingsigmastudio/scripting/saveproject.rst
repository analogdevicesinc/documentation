:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Save Project
============

| This action takes in one argument(filePath) and allows the user to save a SigmaStudio+ project in the given filepath. This API returns the SSPResult type.
| ===API===

::

   SSPResult SaveProject(string filePath)

| 
| ===Arguments====

-  filePath - The path along with the file name of the project where the given SigmaStudio+ project must be saved
   ===Result===

SSPResult contains 'IsSuccess' flag and 'Message' information of the SaveProject action.

::

   -IsSuccess is 'True' if the save project was successful else 'False'.
   -Message contains the Success/Failure information in the form of list of string.
