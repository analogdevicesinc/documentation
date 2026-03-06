| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ Quick Start guide for Windows Vista 32-bit/64-bit
=========================================================

| Insert the *ez*\ LINX software DVD into the DVD drive of the computer and access its contents using windows explorer. The DVD contains three folders labelled **Documents**, **Hardware** and **Software**. Enter the folder labelled **Software**.
| A single software installation is required prior to installing the *ez*\ LINX Sample PC Application Software:
| `.NET Framework v4 <http://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=17851>`__
| The software files for installing the .NET framework v4 are included on the *ez*\ LINX DVD supplied and are located in the Software/PC Application Installation folder
| |image1| } ===== .Net Framework v4 Installation ===== Install the **.NET Framework v4** found in the Software/PC Application installation inside the dotnetfx40 folder on the ezLINX Package DVD. To run the installer, double click on the dotNetFx40_Full_x86_x64.exe. This will open the window as displayed below:
| Tick the box marked “I have read and accepted the license terms”, click on the install button to start the installation process. Once the installation process has finished click on the finish button.

ezLINX Sample PC Application Installation
-----------------------------------------

| Install the ezLINX PC Application setup found in the Software/PC Application Installation folder located on the ezLINX Software Package DVD. The latest version of this software can be downloaded from the link below.
|

.. admonition:: Download
   :class: download

   :adi:`Download Sample PC Application Installation files <static/imported-files/eval_boards/ezLINXPCApp.zip>`


Run the setup by double clicking on the setup.exe file. This will start the installation process and when completed the window below will open:
| |image2|
| This window indicates that the software installation was successful and is now running.
| ===== Connecting the ezLINX board to the PC =====

-  Connect the ezLINX board to the power supply using the supplied AC adapter
   \* Connect the ezLINX board to the PC using the supplied USB A to USB mini B cable.
-  Ignore the found new hardware prompt that pops up in the bottom right corner of the screen

Installing the USB drivers
--------------------------

.. admonition:: Download
   :class: download

   :adi:`Download the Windows 32-bit driver <static/imported-files/eval_boards/ezLINXGadgetEthernetUSBDriver.zip>`


| There are two different drivers for the 32-bit and 64-bit versions of Windows Vista so if you are unsure which version of the OS the PC is running then check in the system settings before attempting to install the driver.
| Navigate to the device manager by searching for it in the start menu:
| |image3|
| The ezLINX board is labelled “linux USB Ethernet/RNDIS Gadget” and can be found under Other Device \\\\\ |image4|
| Right click on the ezLINX board labelled “linux USB Ethernet/RNDIS Gadget” and select update driver. This will open the hardware update wizard window as shown below.
| Choose to browse the computer for driver software
| |image5|
| In the "search in this location" browse for the location of the folder containing the downloaded driver software
| |image6|
| Click next and when prompted to choose to install the driver choose "install the driver anyway"
| |image7|
| The driver software will now be installed and the PC will recognize the board
| |image8|
| =====Setting up the Gadget Ethernet IP Address=====

| Navigate to the network connections window (type controlpanel\\networkconnections into the address bar) and right-click on the device labelled "Linux USB Ethernet/RNDIS Gadget" and select properties
| |image9|
| Select Internet protocol v4 (TCP/IP) from the list and click on properties
| |image10|
| In the IP address settings enter the following:
| |image11|
| Click on the OK button and then click on the close button. The IP address of the windows gadget ethernet driver has now been set.
| =====Setting up the ezLINX Board IP Address===== Open the ezLINX application window and click on the board icon in the bottom left corner of the window. In the IP address settings enter the following:
| |image12|
| Now click the “use changes” button then the “connect” button and the status light will turn from red to green. The board and the PC application are now connected.
| =====Verify Connection===== To verify the connection perform a simple GPIO test. Click on the GPIO button on the left hand side of the window:
| |image13|
| Tick the box next to GPIO 1 and set the direction to 1 and the value to 0 and click the “use changes” button. The orange LED, LED1 that was previously on on the board will now switch off. To switch it back on again set the value to 1 and click the “use changes” button.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/DotNETFRAMEWORKV4INSTALLATION.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/win7/ezLINXOpenWindow.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/DeviceManagerLocation.jpg
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/usbethernetrndisgadget.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/browsefordriversoftware.jpg
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/BrowseTheDriverSoftware.jpg
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/installthedriveranyway.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/UpdateDriverSoftware.jpg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/networkconnectionswindow.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/localconnectionproperties.jpg
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/vista/ipaddresssettings.jpg
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/win7/BoardConfigurationWindow.jpg
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/win7/GPIOInterface.jpg
   :width: 600px
