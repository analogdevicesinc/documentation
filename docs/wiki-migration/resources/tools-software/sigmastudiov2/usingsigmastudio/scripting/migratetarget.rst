:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Migrate Target
==============

This action allows the user to migrate the target of a specified module in the canvas. The function call requires 3 arguments to be passed. This API returns the SSPResult type

| 
| ===API===

::

   SSPResult  MigrateTarget(string shapeUid, string targetName, bool copyPlatformSpecificProperties)

| 
| ===Arguments====

-  shapeUid- Uid of the Shape where the user wants to change the label.
-  targetName- Target Platform name.
-  copyPlatformSpecificProperties - used to determine whether to copy platform-specific settings

| 
| ===Result=== SSPResult contains 'IsSuccess' flag and 'Message' information for the MigrateTarget action.

::

   -'IsSuccess' is 'True' if the Target is migrated successfully, else 'False'.
   -Message contains the Success/Failure information in the form of a list of strings.

| 
