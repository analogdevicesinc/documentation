:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Save Sequence
=============

| This action allows the user to save a sequence file in XML format, which contains all the details from the sequence window. The function call takes in 1 arguments. This API returns the SSPResult type.
| ===API===

::

   SSPResult SaveSequence(string seqXmlPath)            

| 
| ===Arguments====

-  seqXmlPath- Sequence file path.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the SaveSequence action.

::

   -IsSuccess is 'True' if the sequence file is saved successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
