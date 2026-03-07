:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Export Preset
=============

This action allows the user to export the given preset to a file. The function call takes in 2 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult ExportPreset(string path, string presetName)

| 
| ===Arguments====

-  path- The location/file path along with file name to save the exported preset file.
-  presetName- Name of the Preset (PresetA,B,C,D) to be exported as a file.

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the ExportPreset action.

::

   -IsSuccess is 'True' if the file exported successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
