:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Download Sequence
=================

This action allows the user to download the Sequence window details in SS+ sequence window. The function doesn't have any arguments. This API returns the SSPResult type.

| 
| ===API===

::

   SSPResult DownloadSequence()


   | 

|

| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the DownloadSequence action.

::

   -IsSuccess is 'True' if the download is successful, else 'False'.
   -Message contains the Success/Failure information in the form of a list of strings.

| 
