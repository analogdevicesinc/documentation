:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Import SigmaStudio Projects
===========================

This action allows the user to rebuild the SigmaStudio project into SigmaStudio+ project. The function call takes in 1 arguments. This will import the SigmaStudio exported xml file and recreate the schematic in SigmaStudio+. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult Import(string modXMLPath)

| 
| ===Arguments====

-  modXMLPath- Exported SigmaStudio xml file. This path should include the file name along with path.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the Import action.

::

   -IsSuccess is 'True' if the project imported successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
