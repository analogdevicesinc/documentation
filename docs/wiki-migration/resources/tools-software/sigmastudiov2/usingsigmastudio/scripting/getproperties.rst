:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Get Properties
==============

This action allows the user to get all the available properties of a given plugin. The function call takes in 1 argument. Returns the shape properties in the form of list of strings.

| 
| ===API===

::

   list<string> GetProperties(string elementUid)

| 
| ===Arguments====

-  elementUid- Uid of the plugin whose properties are to be known
   ===Result===

| Returns all the properties of a given plugin in the form of list of strings.
