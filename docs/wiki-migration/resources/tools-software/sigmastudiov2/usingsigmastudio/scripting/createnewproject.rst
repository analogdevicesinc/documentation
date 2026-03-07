:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

CreateNewProject
================

| This takes in one argument(project name) and allows the user to create a new SigmaStudio+ project with the given name. This API returns the SSPResult.
| ===API===

::

   SSPResult CreateNewPorject(string projectName)              

| 
| ===Arguments====

-  projectName - The projectName should contain name of the new project along with the file path.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of CreateNewProject action.

::

   -IsSuccess is set to 'True' if the create new project was successful else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
