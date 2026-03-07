:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Export System files
===================

This action allows the user to export the project files to a specified file location. The function call takes in 2 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult Export(string exportName, string exportFolder);

| 
| ===Arguments====

-  exportName- Name of the exported files.
-  exportFolder- Folder path where the exported files to be saved.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the Export action.

::

   -IsSuccess is 'True' if the system files exported successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
