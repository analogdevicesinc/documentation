:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

Using SigmaStudio as a LabVIEW .NET Server
==========================================

| To use SigmaStudio as a LabVIEW automation client, both applications must be installed and running on the same machine. In this configuration, LabVIEW is a .NET automation client and SigmaStudio (via SigmaStudioServer) becomes a .NET automation server.
| To create a virtual instrument to control SigmaStudio, follow the steps given below:
| 1. Launch LabVIEW and SigmaStudio on the same machine, and then open a new VI file in LabVIEW
| 2. Open the .NET palette to access the .NET objects.
| 3. Insert a Constructor Node which will open the Select .NET Constructor dialog box.
| |image1|
| 4. Click the Browse… button.
| 5. Navigate to the SigmaStudio installation directory, select Analog.SigmaStudioServer.dll and press OK.
| |image2|
| 6. Next choose SigmaStudioServer from the object list, SigmaStudioServer() should be displayed in the constructors list.
| 7. Click OK to select the SigmaStudioServer constructor.
| 8. Insert an Invoke Node and connect the constructor Node to it.
| 9. Click on Method to display and select the accessible SigmaStudioServer commands.
| |image3|
| 10. Example for a single method "Open Project"
| |image4|
| 11. Example VI for sequence of operations "open project" -> "Compile ->"Download"
| |image5|
| Please download the following example LabView 2015 and edit paths as necessary `labvieweaxample.rar <https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/labvieweaxample.rar>`_
| Refer to the LabVIEW online help and tutorials for more information; the “Using .NET with LabVIEW” online help topic is a good place to start.
|

.. note::

   All APIs in SigmaStudioServer.dll might not be exposed to LabView interface. Still, these APIs can be accessed by calling the using the RUN_SCRIPT() method which accesses these APIs internally.


.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/constructor_node.jpg
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/sigmastudioserver.jpg
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/createmethod.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/5_1.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/sampleopen_compile_download.jpg
