:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Get All Plugins
===============

This action allows the user to get a list of all the plugins(with their version numbers) of a given interface type. The function call takes in 1 argument. This action will return all the available plugins of mentioned interface type.

| 
| ===API===

::

   list<string> GetAllPlugins(string interfaceType)

| 
| ===Arguments====

-  interfaceType- Interface type of the plugins to be listed

| 
| ===Result=== This API will return the list of available plugins.
