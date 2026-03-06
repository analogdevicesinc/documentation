Chronous IO Demonstration Platform
==================================

Value Proposition
-----------------

-  Remote Terminal Unit (RTU) that performs Ethernet  to 4-20mA (Packets to Milliamps)
-  Supports and enhances the transition from 4-20mA to industrial ethernet in factory automation brown field developments
-  Where customers need to integrate existing field instruments into new Ethernet based control systems

.. image:: https://wiki.analog.com/_media/resources/demo/reference-designs/adi_chronous.jpg
   :align: center
   :width: 600px

Quick Start Guide
-----------------

Features
~~~~~~~~

-  2 AD74413R Quad Channel Software Configurable Input Output providing 8 channels configurable I/O
-  ADIN2299 RapID Platform Generation 2 industrial network interface with PROFINET

Necessary Equipment
~~~~~~~~~~~~~~~~~~~

-  Chronous-I/O
-  Siemens PLC
-  1 PC

General Description
~~~~~~~~~~~~~~~~~~~

The Chronous-I/O device is a demonstration platform to show the capabilities of the ADIN2299 RapID Platform Generation 2 industrial network interface and AD74413R Quad Channel Software Configurable Input Output. It shows you to access the Input and Output channels from a PLC using PROFINET.

Revision History
~~~~~~~~~~~~~~~~

-  03/2022 Revision 0: Initial Version

Chronous-I/O Setup
------------------

.. image:: https://wiki.analog.com/_media/resources/demo/reference-designs/adi_chronous_pc_plc.png
   :align: center
   :width: 600px

Setting up the PROFINET network with Siemens PRONETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure the Input Output channels of the Chronous-I/O a configuration of the network connection is needed. This can be achieved with Siemens TIA Portal during the creating of the PLC project or with Siemens PRONETA. Setup with Siemens PRONETA is described in the following. Setup with TIA Portal is described further down.

-  Download and install `Siemens PRONETA <https://new.siemens.com/global/en/products/automation/industrial-communication/profinet/proneta.html>`__ and its prerequisites (for PRONETA 3.3.0 these are `.NET 4.6.2 runtime <https://dotnet.microsoft.com/en-us/download/dotnet-framework/net462>`__ and `Npcap <https://npcap.com/#download>`__).
-  Start Siemens PRONETA
-  In Settings configure the Network Adapter to be used
-  Make sure the Chronous-I/O device is connected to the network of your PC
-  The Chronous-I/O device should show up in the Network Analysis view (see Picture below)

|image1|

-   Right click the chronousio item and choose Set Network Parameters (see Picture below)

|image2|

-  Assign a Device Name (see Picture below)

|image3|

-  Open the Set Network Parameters dialog again and set the IP configuration (see Picture below)

|image4|

-  Now the network interface of the Chronous-I/O device is configured (see Picture below) and you can access the web page with your browser

|image5|

Configuring the I/O with the Chronous-I/O Web Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  After configuration of the network connection, open the web page of the Chronous-I/O device with your web browser. The web server uses the https protocol, so accepting the certificate security warning of the browser is necessary. The start page opens and shows the Input or Output values of the eight channels depending on their configuration. (see Picture below)


|image6|

-  Go to the Chronous-I/O configuration page (see Picture below). At first startup all channels are configured to High Impedance mode.

|image7|

-  Set the function for each channel by selecting an option in the drop-down list and click the Submit button (see Picture below). For specific functions there are further configuration options available by the Cfg button. A more detailed description of the configuration options can be found in the datasheet of AD74413R Quad Channel Software Configurable Input Output

|image8|

-  On the Chronous-I/O start page (see Picture below) you can now see the values. The color of the channel names represent the channel direction according to the LEDs on the Chronous-I/O device. High Impedance channels are white, Output channels are yellow, and Input channels are green. Blinking red channels are switched off channels after an error, for example short circuit error. To enable this channels again, remove the cause of the error, go to the configuration, set High Impedance mode for this channel and then reconfigure it to the required settings.

|image9|

Setting up the PROFINET network with Siemens TIA Portal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/demo/reference-designs/adi_chronous_pc_plc.png
   :align: center
   :width: 600px

+-------------+-----------+--------------------+---------------------+------------+--------------+
| Item Number | Item Type | Input size (Bytes) | Output size (Bytes) | Module ID  | Submodule ID |
+=============+===========+====================+=====================+============+==============+
| 500         | Cylic     | 32                 | 32                  | 0x10500000 | 0x10500001   |
+-------------+-----------+--------------------+---------------------+------------+--------------+

The eight I/O values are represented as 32-bit floating point numbers. The ranges for the different functions are listed in the table below (see Table below)

================ ==== ================== ====
Channel function Min. Max.               Unit
================ ==== ================== ====
VOLTAGE          0.0  10.0               V
CURRENT          0.0  24.0*10\ :sup:`-3` A
RESISTANCE       0.0  1.0*10\ :sup:`6`   Ω
DIGITAL          0.0  1.0                
================ ==== ================== ====

Configuring the PLC Setup in the Siemens TIA Portal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Start TIA Portal and create a new project (see Figure below)


|image10|

-  Go to First Steps and open the project view (see Figure below)

|image11|

-  In the left panel, click Add New Device (see Figure below)

|image12|

-  Select the PLC that is connected (see Figure below)

|image13|

Installing the Chronous-I/O general station description file (GSD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Open the Options menu and select Manage general stations descriptions files (see Figure below)


|image14|

-  Browse to file location of the Analog Devices Chronous-I/O GSDML file and install it, then close the dialog and wait until the hardware catalog has been updated (see Figure below)

|image15|

Creating the PROFINET network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to Devices & Networks view and open the Hardware catalog on the right side.
-  Select the Analog Devices Chronous-I/O device and drag it into the Devices & Networks view (see Figure below)

|image16|

-  Click the Not assigned link within the Network view tab to bring up a yellow pop-up with the text appearing in the same format as a URL link, PLC_1.PROFINET_interface_1. Click this yellow pop-up to connect the device to the PLC by using the green line (see Figure below)

|image17|

Going online with the PROFINET network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Select PLC_1 and click Download to device button in the toolbar (see Figure 19). The dialog will open (see Figure below)


|image18|

-  Search for target device, select the appropriate PLC and click Load (see Figure below)

|image19|

-  In the Load preview window, click Load (see Figure below)

|image20|

-  Right-click the Analog Devices PROFINET Network Interface ChronousIO icon across from the PLC and click Assign name to display the assign PROFINET device name window (see Figure below)

|image21|

-  Click the orange Go online button at the top of the window to go online with the PROFINET network. Taking this step causes the outline of the screen to turn orange and green checkmarks appear on all devices, which indicates that the system is actively communicating. Communication between the PC of the user and the Siemens PLC is now working
-  Click the blue Go offline button to complete this process

Creating a first application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  In the Devices & Networks view double click on the chronousio device to see the I/O addresses of the device (see Figure below)


|image22|

-  Got to PLC_1 > PLC Tags > Show all tags and add new tags for the Chronous-I/O device (see Figure below)

|image23|

-  Go to PLC-1 > Program blocks > Main [OB-1] and create a program as shown below (see Figure below), that just sends the value of Chronous-I/O channel 5 to Chronous-I/O channel 7. Note that the two channels must be configured as in the example configuration in chapter “Configuring the I/O with the Chronous-I/O Web interface”, as a matching Input and Output pair (digital input and output in this case).

|image24|

-  Build the program by clicking the Compile button in the tool bar (see Figure below)

|image25|

-  Click the Download button in the tool bar to transfer the program to the PLC (see Figure below)

|image26|

-  Click the Start CPU button and switch the CPU to RUN mode (see Figure below)

|image27|

-  Connect a switch to the digital input channel 5 and see the value change in the web interface of the Chronous-I/O device and the output on channel 7 following the input value due to the example PLC program.

.. |image1| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p01-pronetanetworkanalysis.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p03-pronetanetworkanalysischronousiosetparameter.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p04-pronetanetworkanalysischronousiosetdevicename.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p05-pronetanetworkanalysischronousiosetip.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p06-pronetanetworkanalysischronousioconfigured.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/p07-chronousiowebstartpagedefaultcfg.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/w02-chronouswebdefaultcfg.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/w03-chronouswebexamplecfg.png
   :width: 600px
.. |image9| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/w04-chronouswebstartpageexamplecfg.png
   :width: 600px
.. |image10| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t01-tiaportalcreate.png
   :width: 600px
.. |image11| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t02-tiaportalfirststeps.png
   :width: 600px
.. |image12| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t03-tiaportalprojectview.png
   :width: 600px
.. |image13| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t04-tiaportaladdnewdevice.png
   :width: 600px
.. |image14| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t05-tiaportalselectmanagegsdml.png
   :width: 600px
.. |image15| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t06-tiaportalmanagegsdml.png
   :width: 600px
.. |image16| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t13-tiaportaldevicenetwork.png
   :width: 600px
.. |image17| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t14-tiaportaldevicenetworkconnected.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t15-tiaportaldevicenetworkdownload.png
   :width: 600px
.. |image19| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t16-tiaportaldevicenetworkdownloadreadytoload.png
   :width: 600px
.. |image20| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t17-tiaportaldevicenetworkdownloadcheckbeforeload.png
   :width: 600px
.. |image21| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t18-tiaportaldevicenetworkdevicesetprofinetname.png
   :width: 600px
.. |image22| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t20-tiaportaldeviceoverview.png
   :width: 600px
.. |image23| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t21-tiaportaldeviceiotags.png
   :width: 600px
.. |image24| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t22-tiaportalprogramblock.png
   :width: 600px
.. |image25| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t23-tiaportalcompileprogramblock.png
   :width: 600px
.. |image26| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t24-tiaportalloadprogramblock.png
   :width: 600px
.. |image27| image:: https://wiki.analog.com/_media/resources/demo/reference-designs/t27-tiaportalstartcpu.png
   :width: 600px
