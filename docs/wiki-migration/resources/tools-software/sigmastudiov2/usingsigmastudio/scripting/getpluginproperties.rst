:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Get Plugin Properties
=====================

This action allows the user to get all the available properties of a given plugin. The function call takes in 1 argument. Function will return the plugin property name, type, and it's value.

| 
| ===API===

::

   Dictionary<string, Param> GetPluginProperties(string elementUid)

| 
| ===Arguments====

-  elementUid- Uid of the plugin whose properties are to be known.

| 
| ===Result=== The collection of result contains the collection of property name in the form of string, (Param) value and it's type of the property.
