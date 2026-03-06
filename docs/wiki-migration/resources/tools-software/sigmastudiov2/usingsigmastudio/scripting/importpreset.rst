:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Import Preset
=============

This action allows the user to import the Preset file to the given preset. The function call takes in 2 arguments. Return type is a SSPResult which contains a IsSuccess flag for success/failure and Message in the form of list of strings.

| 
| ===API===

::

   SSPResult ImportPreset(string path, string presetName)

| 
| ===Arguments====

-  path- The location/file path along with file name to import the preset file.
-  presetName- Name of the Preset (PresetA,B,C,D).

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information of the ImportPreset action.

::

   -IsSuccess is 'True' if the preset file imported successfully, else 'False'.
   -Message contains the Success/Failure information in the form of list of string.

| 
