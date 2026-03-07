:doc:`Click here to return to the A2B SSPLUS User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide>`

Drawing A2B schematics
======================

The following steps describe the procedure to draw an A2B schematic in SigmaStudio+. We can also draw the A2B schematic using :doc:`Thrift Automation </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>` either by C# client or Python script.

-  Launch SigmaStudio+ application.
-  Create a new project from File menu.
-  Drag and drop “AD24xx EVAL” standard platform or Custom Platform from Tree ToolBox, under “A2B” to “System” canvas.
-  Drag an A2B-USBi or A2B-Aardvark Communication Adaptors, depending on the Host I2C adapter used to connect to the transceiver, and wire it to AD24xx block.
-  Double click to the platform to get the list of components available for A2B platform. This will list “Generic Devices”, “Transceiver”, “Memory” and “Processor” for custom platform whereas standard platform it is read-only. USBi to main and peripheral interfaces can be changed by clicking in on the interface type shown below.
   |image1|\

.. container:: centeralign

   \ **Figure:** Changing the interface


-  Drag icons from Tree Toolbox into canvas and connect the blocks to make an A2B schematic as shown in the below Figure.
   Select the variant by clicking on the drop-down present within custom platform.
   |image2|\

.. container:: centeralign

   \ **Figure:** Selection of variant


|image3|\

.. container:: centeralign

   \ **Figure :** A2B Schematic tab


-  Define and configure streams by right clicking the node and select the settings. User can also access the stream configuration from the Project window. For configuration details, refer :doc:`slot configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>`.
   |image4|\

.. container:: centeralign

   \ **Figure :** A2B Stream configuration


**Note:** Before Adding/updating the stream configuration, project has to be Link-Compiled.
-  Enter the properties for each A2B node by right clicking and selecting the “Open AD24xx-node Settings”. This will open a window as shown in the below Figure.
   |image5|\

.. container:: centeralign

   \ **Figure :** Device properties window


-  Transceiver properties are grouped under different Tabs. Switch to the required Tab and configure as necessary. Configuration of Upstream and Downstream slots may vary depending on the Transceiver type selected. Refer :doc:`slot configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/stream-and-export-configurations>` for more details.
-  Provide the silicon revision of the A2B Transceiver in the ‘ID’ tab of General View as shown in the below Figure. Optionally, a custom node identifier can be assigned to a Node by selecting the “Custom Node Identifier” checkbox. Refer :doc:`Custom Node ID based Configuration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/transceiversetting>` for more details.
   |image6|\

.. container:: centeralign

   \ **Figure :** Specifying silicon revison


-  The daisy chain for AD243x only network can go up to 16 sub-nodes and an overall distance of up to 80m. For AD2437, it is 300m. AD242x daisy chain is limited to 16 sub-nodes and 80m overall distance and the other transceiver versions of AD242x family supports only 10 sub-nodes .
-  Enter properties for each peripheral node used in the schematic. A peripheral device can be programmed during discovery by providing an XML file having the required configuration information.
-  Once properties for all nodes are entered, check the correctness of the schematic by clicking on the ‘Link’ icon in SigmaStudio+. Make sure that the drawn schematic has no errors.
-  The schematic is now ready for download.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/interface_change.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/tranceiver_varient.png
   :width: 550px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_schematic_tab.png
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/a2b_stream_configuration.png
.. |image5| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/device_properties_window.png
.. |image6| image:: https://wiki.analog.com/_media/resources/tools-software/a2bv2/a2bssplususerguide/specifying_silicon_version.png
