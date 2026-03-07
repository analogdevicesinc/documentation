:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Open Existing Project
=====================

| OpenExistingProject takes in one argument(filePath) and allows the user to open a SigmaStudio+ project in the given filepath. This API returns the SSPResult type.

API
---

::

   SSPResult OpenExistingProject(string filePath)             

|

| ===Arguments====

-  filePath- The path along with the file name of the project which has to be opened in the SigmaStudio+ application.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the OpenExistingProject action.

::

   -IsSuccess is 'True' if the project was opened successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
