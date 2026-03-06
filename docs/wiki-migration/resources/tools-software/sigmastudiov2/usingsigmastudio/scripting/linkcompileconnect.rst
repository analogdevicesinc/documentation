:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Link Compile Connect
====================

This action allows the user to perform linking, compiling and connect on the current project. The function call takes in no arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult LinkCompileConnect()


   | 

Result
------

SSPResult contains 'IsSuccess' flag and 'Message' information of the LinkCompileConnect action.

::

   -IsSuccess is 'True' if the LinkCompileConnect was successful, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

|
