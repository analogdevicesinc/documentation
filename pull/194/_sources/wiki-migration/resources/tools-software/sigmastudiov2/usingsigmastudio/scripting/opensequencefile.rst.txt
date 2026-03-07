:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Open Sequence File
==================

| This action allows the user to open a saved sequence file, which is in XML format, into a sequence window. This API will read the sequence file and display it in the sequence window.The function call takes in 1 argument. This API returns the SSPResult type.
| ===API===

::

   SSPResult OpenSequenceFile(string seqXmlPath)            

| 
| ===Arguments====

-  seqXmlPath- Sequence file path.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the OpenSequenceFile action.

::

   -IsSuccess is 'True' if the sequence file opened successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
