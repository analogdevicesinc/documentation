:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>`

Read
====

This action allows the user to Read the value of the given property in a specific module/shape. The function call takes in 2 arguments. This action returns the property value and it's type.

| 
| ===API===

::

   Param Read(string uid, string propertyName)

| 
| ===Arguments====

-  uid- Uid of the Shape from which user wants to perform read.
-  propertyName- Name of the property to get the value.

| 
| ===Result=== Param result includes property value and it's type.
