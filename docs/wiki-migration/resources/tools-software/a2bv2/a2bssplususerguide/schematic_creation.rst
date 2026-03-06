Schematic Creation

The following steps describe the procedure to draw an A2B schematic in SigmaStudioPlus.

1. Launch SigmaStudioPlus application.

2. Create a new project from File menu.

3. Drag and drop “AD245x-EV-B” or "AD245x EV-A1CA" standard platform or Custom Platform from Tree ToolBox, under “A2BPlus” to “System” canvas.

4. Drag a USBi or Aardvark Communication Adaptors, depending on the Host I2C adapter used to connect to the transceiver, and wire it to AD245x block in system canvas.

5. Drag icons from Tree Toolbox into canvas and connect the blocks to make an A2B schematic as shown in the below Figure

6. Double-click on the platform to get the list of components available for A2B platform. This will list “Generic Devices”, “Transceiver”, “Memory” and "SigmaDSP 1452" for the chosen standard platform. Whereas custom platform is fully buildable from scratch. 7. Double-click on ADAU1452 to design audio modules Configure the ADAU1452 by right-clicking the ADAU1452 and select the settings

8. Double click on programmable peripheral to provide XML file

9. Define and configure streams by right clicking the node and select the settings. User can also access the stream configuration from the Project window. 

       

         Note: Before Adding/updating the stream configuration, project has to be Link-Compiled.

10. Enter the properties for each A2B node by right-clicking and selecting “Open Settings → Settings”. This will open a window as shown in the below Figure. There are 3 ways to configuration 

 
