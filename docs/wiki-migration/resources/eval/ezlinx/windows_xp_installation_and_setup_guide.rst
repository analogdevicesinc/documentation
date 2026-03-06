| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ Quick Start guide for Windows XP
========================================

| Insert the *ez*\ LINX software DVD into the DVD drive of the computer and access its contents using windows explorer. The DVD contains three folders labelled **Documents**, **Hardware** and **Software**. Enter the folder labelled **Software**.
| Two softwares installations are required prior to installing the ezLINX Sample PC Application Software:
| `Windows installer 3.1 <http://www.microsoft.com/en-us/download/details.aspx?id=25>`__
| `.NET Framework v4 <http://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=17851>`__
| The software files for installing these three components have been included on the *ez*\ LINX DVD supplied and are located in the Software/PC Application Installation folder

Windows Installer 3.1 Installation
----------------------------------

| Install Windows installer 3.1 found in the Software/PC Application installation inside windowsinstaller3_1 folder located on the ezLINX DVD. To run the installer, double click on the WindowsInstaller-KB893803-v2-x86.exe file. This will open the window as displayed below:
| |image1|
| Click next to start the installation process. Once the installation process has finished click on the finish button.
| ===== .Net Framework v4 Installation ===== Install .NET Framework v4 found in the Software/PC Application installation inside the dotnetfx40 folder on the ezLINX Package DVD. To run the installer, double click on the dotNetFx40_Full_x86_x64.exe. This will open the window as displayed below:
| |image2|
| Tick the box marked "I have read and accepted the license terms", click on the install button to start the installation process. Once the installation process has finished click on the finish button.
| ===== ezLINX Sample PC Application Installation ===== Install the ezLINX PC Application setup found in the Software/PC Application Installation folder located on the ezLINX Software Package DVD. The latest version of this software can be downloaded from the link below.
|

.. admonition:: Download
   :class: download

   :adi:`Download Sample PC Application Installation files <static/imported-files/eval_boards/ezLINXPCApp.zip>`


Run the setup by double clicking on the setup.exe file. This should start the installation process and when completed the window below will open:



|image3|

| This window indicates that the software installation was successful and is now running.
| ===== Connecting the ezLINX board to the PC =====

-  Connect the ezLINX board to the power supply using the supplied AC adapter
   \* Connect the ezLINX board to the PC using the supplied USB A to USB mini B cable.
-  Ignore the found new hardware prompt that pops up in the bottom right corner of the screen
   ===== Installing the USB drivers =====

.. admonition:: Download
   :class: download

   :adi:`Download the Windows 32-bit driver <static/imported-files/eval_boards/ezLINXGadgetEthernetUSBDriver.zip>`


| Navigate to the device manager of your PC through the following pathway:
| Go to the Startup menu and select Control Panel
| |image4|
| From the Control Panel window, go to System
| |image5|
| The System Properties window is appear, select the Hardware interface.
| |image6|
| The ezLINX board is labelled "linux USB Ethernet/RNDIS Gadget" and can be found under Network adapters
| |image7|
| Right click on the ezLINX board labelled "linux USB Ethernet/RNDIS Gadget" and select update driver. This will open the hardware update wizard window as shown below.
| |image8|
| Select "install from a list or specific locaton (advanced)" and click next
| |image9|
| Select "don't search I will choose the driver to install"
| |image10|
| Select "have disk" and using the browse button on the next window, locate the Windows 32-bit driver on the ezLINX DVD located in the Software/ezLINX drivers/32-bit folder. Click on the OK button. Click on the next button.
| |image11|
| On this screen click "continue anyway". This will install the driver and the PC can now recognize the ezLINX board as the "Linux USB Etheret/RNDIS Gadget".
| ===== Setting up the gadget ethernet IP Address ===== Go to the Control Panel then Navigate to the Network Connections window
| |image12|
| Locate the connection with the device name "Linux USB Ethernet/RNDIS Gadget"
| |image13|
| Right click on the connection and select properties.
| In the following list select "Internet protocol (TCP/IP)"
| |image14|
| Click on the Properties button. This will bring you to the window where the IP address of the windows gadget ethernet driver can be set. Enter the following into the window:
| |image15|
| Click on the OK button and then click on the close button. The IP address of the windows gadget ethernet driver has now been set.

Setting up the ezLINX board IP address
--------------------------------------

| Open the ezLINX application window and click on the board icon in the bottom left corner of the window (or click on Configure button). In the IP address settings enter the following:
| |image16| Now click the "use changes" button then the "connect" button and the status light will turn from red to green. The board and the PC application are now connected.
| ===== Verify Connection ===== To verify the connection perform a simple GPIO test. Click on the GPIO button on the left hand side of the window:
| |image17|
| Tick the box next to GPIO 1 and set the direction to 1 and the value to 0 and click the "use changes" button. The orange LED, LED1 that was previously on on the board should now switch off. To switch it back on again set the value to 1 and click the "use changes" button.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/WINDOWSINSTALLER.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/DotNETFRAMEWORK.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/SW_SuccessInstallation.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/ControlPanel.jpg
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/SystemAccess.jpg
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/SystemProperties.jpg
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/DeviceManager.jpg
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/hardwareupdate.jpg
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/HardwareUpdateWinzar.jpg
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/SelectNetworkAdapter.jpg
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/HardwareInstallation.jpg
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/NetworkConnection.jpg
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/LocalAreaConnection.jpg
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/ConnectionProperties.jpg
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/IPaddress.jpg
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/configinterface.jpg
   :width: 300px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/v1.1.3/xp/GPIOInterface.jpg
   :width: 300px
