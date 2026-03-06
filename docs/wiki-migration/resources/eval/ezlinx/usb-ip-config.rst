.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



| 
| :doc:`ezLINX™ iCoupler® Isolated Interface Development Environment Homepage </wiki-migration/resources/eval/ezlinx>`

ezLINX™ USB Device Configuration
================================

Device Driver Installation
--------------------------

A driver must be installed in order to connect to the *ez*\ LINX Development Platform using the sample PC Application. Instructions to install this device driver are given below.

.. admonition:: Download
   :class: download

   |Download USB Gadget Driver|

.. important::

   **Warning:** During install or uninstall of a new Ethernet gadget, Windows will reset all network connections. If there are any large downloads or sensitive connections (like VPN) in progress they will be interrupted.


| 
| First download and extract the above USB Gadget Driver file. To install the USB gadget plug it into the target PC. A pop-up will appear (see below) saying that Windows has found a new hardware device called a "RNDIS/Ethernet Gadget".

.. image:: https://wiki.analog.com/_media/ezlinx/usb-popup.jpg
   :alt: Figure 1. New Hardware Found Pop-up
   :align: center
   :width: 150px

The device can also be found by accessing the device manager (Control Panel -> System -> Hardware) and looking for the Linux USB Ethernet/RNDIS Gadget under Network Adapters. Right click on the Linux USB Ethernet/RNDIS Gadget and select "update driver".

| |image1| |image2|
| |Figure 4. Locating USB Gadget|

| 

Click on the pop-up which brings up the "Found New Hardware" dialog, select "Install from a list or specific location (Advanced)". Next select "Don't Search, I will choose the driver to install". Alternatively the driver can also be installed by selecting the "Search for the best driver in these locations", ticking the box marked "include this location in the search" and then selecting the folder which contains the extracted contents of the USB Gadget Driver File.

|image3| |image4|

| 

If a "Hardware Type" dialog appears, scroll down and select "Network Adapters". Next select "Have Disk" and select the *linux.inf* file provided. Ignore any messages about digitally signed drivers.

| 
| |image5| |image6|

| 

Once the USB driver is sucessfully installed, the IP address for the device must be configur ed.

Network Adapter IP Configuration
--------------------------------

| To set up the network adapter to connect with the *ez*\ LINX Development Platform, go to "Control Panel->Network Connections". Right click on the "Local Area Connection" which is a "Linux USB Ethernet/RNDIS Gadget" and select "Properties". The below menu will appear. Highlight Internet Protocol (TCP/IP) and select Properties.

.. image:: https://wiki.analog.com/_media/ezlinx/ipsetup2.jpg
   :align: center
   :width: 600px

|

| The below window should then open. Select "Use the following IP address". The network adapter must be on the same network as the Development Platform. The default IP address of the hardware platform is 192.168.1.21, therefore the network adapter must be placed on the 192.168.1.xxx network. And example configuration is given below:

| **IP Address:** 192.168.1.100
| **Subnet mask:** 255.255.255.0
| **Default gateway:** 192.168.1.1
| |image7|
| Select Ok to confirm. Now the host and the device are on the same network.

.. important::

   **Note:** Switching the USB port used for the Gadget Ethernet device will require you to perform the above steps again, setting up the appropriate IP address and gateway for the USB device.


**Note:** When connecting two *ez*\ LINX Development Platforms to the same P.C. for board to board communication, the two boards must be placed on a different network to allow for simultaneous connection. To do this you must connect to one of the development platforms individually using the Sample PC Application and change both the board's IP address and the network adapter IP address, as shown above.

| **Example Configuration:**
| **ez\ LINX Development Platform 1:**
| **IP Address:** 192.168.1.21
| **Subnet Mask:** 255.255.255.0
| **Default Gateway:** 192.168.1.1
| **Isolated USB Network Adapter 1:**
| **IP Address:**\ 192.168.1.100
| **Subnet Mask:**\ 255.255.255.0
| **Default Gateway:** 192.168.1.1

| 
| **ez\ LINX Development Platform 2:**
| **IP Address:** 192.168.2.21
| **Subnet Mask:** 255.255.255.0
| **Default Gateway:** 192.168.2.1

| 
| **Isolated USB Network Adapter 2:**
| **IP Address:** 192.168.2.100
| **Subnet Mask:** 255.255.255.0
| **Default Gateway:** 192.168.2.1

.. |Download USB Gadget Driver| image:: http://www.analog.com/static/imported-files/eval_boards/ezLINXGadgetEthernetUSBDriver.zip
.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/accessingsystemsweb.png
   :width: 500px
   :height: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/accessingdevicemanagerweb.png
   :width: 400px
   :height: 400px
.. |Figure 4. Locating USB Gadget| image:: https://wiki.analog.com/_media/resources/eval/ezlinx/locatingusbgadgetweb.png
   :width: 600px
   :height: 400px
.. |image3| image:: https://wiki.analog.com/_media/ezlinx/usb-popup2.jpg
   :width: 435px
.. |image4| image:: https://wiki.analog.com/_media/ezlinx/usb-popup3.jpg
   :width: 435px
.. |image5| image:: https://wiki.analog.com/_media/ezlinx/usb-popup4.jpg
   :width: 435px
.. |image6| image:: https://wiki.analog.com/_media/ezlinx/usb-popup5.jpg
   :width: 435px
.. |image7| image:: https://wiki.analog.com/_media/ezlinx/ipsetup3.jpg
   :width: 600px
