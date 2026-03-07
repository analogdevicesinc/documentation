:doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/designermodule>`

Build Plugin
============

| Once the module(s) to be used as SigmaStudio+ plugins are configured using the Algorithm Designer, it can be converted into a DLL for redistribution and reuse. Click the 'Build' button from the group of buttons on the top left corner of Algorithm Designer window. The build window will open up and list all the modules in the current Algorithm Designer Project.
| |image1|
| ===== Selective Building =====

-  User may choose to include one or more modules in the DLL
-  For each of the module, the user may choose to whether to include the Algorithm, Parameter Computation and UI
-  Whenever UI or Parameter Computation is not selected, the plugin name of the external UI or Parameter computation plugin to be referenced should be mentioned.

Assembly Information
--------------------

The assembly information (details) of the generated DLL can be configured in the 'Assembly Information' section. Following details are supported:

-  Description
-  Version
-  Company
-  Product
-  Copyright

Generate DLL
------------

Once the details are entered, click the 'Generate' button to generate the module(s) as a DLL. The Save file dialog that opens up can be used to choose the path and name of the DLL.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/build.png
   :width: 600px
