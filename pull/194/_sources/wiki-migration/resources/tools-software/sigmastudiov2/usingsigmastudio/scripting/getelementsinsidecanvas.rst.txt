:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Get Elements Inside Canvas
==========================

This action allows the user to get the list of sub shapes inside the given parent shape. The function call takes in 1 argument. Returns the available sub shape's Uid in the form of list of strings.

| 
| ===API===

::

   list<string> GetCanvasElements( string parentUid)

| 
| ===Arguments====

-  parentUid - Uid of parent element whose children or sub shapes are to be known

| 
| ===Result=== Returns the list of all the sub-shape's uid present under a given parent shape in the current project.
