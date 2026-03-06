Wireless Vibration Monitoring Platform
======================================

Overview
--------

This document details the function and setup of an Analog Devices wireless Condition Based Monitoring (CBM) evaluation platform. The platform provides a wireless signal chain for MEMS-accelerometer based vibration monitoring. Visualisation of this data for up to three motes (device package containing accelerometer, microcontroller and RF board) is available through a PC-based Graphical User Interface (GUI).

The CBM hardware signal chain consists of a single-axis ADXL1002 accelerometer mounted to the base of the module. The output of the ADXL1002 is read into the ADuCM4050 low power microcontroller where it is buffered, transformed to frequency domain and streamed to the SmartMESH IP mote. From the SmartMESH chip it is wirelessly streamed to the SmartMESH IP Manager. The manager connects to a PC and visualization and saving of the data can take place.

|image1| **Figure 1. CBM Wireless Evaluation Kit**

Features
--------

Smartmesh
~~~~~~~~~

::

   *2.4 GHz multi-hop wireless mesh networking solution
   *Scalability for networks to work in different configurations
   *High data capacity with up to 7.2 kbps of payload data per node

Mote
~~~~

::

   *Low-power motes (wireless nodes) with >10 year battery life, suitable for tough RF environments.
   *Small form factor packages.

GUI
~~~

::

   *GUI which supports real-time plotting of incoming data for up to 3 motes. 
   *GUI options to update mote parameters on-the-fly, save incoming data to database, customise plotting.

--------------

Getting Started
---------------

Equipment
^^^^^^^^^

The following hardware is required to use the evaluation tool.

-  :adi:`SmartMesh IP Manager (DC2274A) </en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/dc2274a-a.html#eb-overview>`

::

   *CBM Hardware Module (referred to as “Mote”)

|image2| **Figure 2. Mote and Manager**

The software required to see the data collected can be accessed by direct download from this wiki. See "Software Installation"

Quickstart
^^^^^^^^^^

-  Plug the manager into any available USB port on your PC
-  Insert a battery into at least one mote.
-  Download the available software below in the software installation section.
-  Save the CBM_app executable anywhere on your PC and launch the program.
-  A window should pop up, prompting you for the COM port of your manager. Search for the manager port number in your computers device manager, under PORTS(COM & LPT). The correct COM port is the *last of four consecutive COM ports*.
-  Click connect.
-  When the Mote's green LED starts blinking, data is plotted, with the default being time and fft plots.
-  While the mote is stationary, double click the remove adc offset checkbox

|image3| **Figure 3. Output with one stationary mote**

Guides
^^^^^^

A setup guide has been created for the Wireless CBM tool which is available on this wiki. This may be used if the quickstart provided here does not result in successful operation of the program, or for more information about this program and its setup.

In addition, a firmware guide with greater detail on the inner workings of the program can be downloaded here.

.. admonition:: Download
   :class: download

   
   ::
   
      *[[https://wiki.analog.com/_media/resources/eval/user-guides/cbm_setup.pdf|cbm_setup.pdf]]
      *[[https://wiki.analog.com/_media/resources/eval/user-guides/wcbm-01_firmware_guide.pdf|wcbm-01_firmware_guide.pdf]]
   


--------------

Software
--------

Software Installation
^^^^^^^^^^^^^^^^^^^^^

The installer for this software can be downloaded from the web page linked to below.

::

   *Click the link "Software Download Directory" to open a web page that contains a number of software downloads. 
   *Click the link under the title "Industrial Wireless CbM (Condition-based Monitoring) Evaluation Software for ADXL1002 Accelerometers"

Note, this web page will be downloaded as a ".htm" file if you are using Google Chrome. Simply open this file after it downloads to access the directory.

.. admonition:: Download
   :class: download

   
   ::
   
      *[[/ftp/ftp.analog.com/pub/imu/imu_ftp_directory.htm|Software Download Directory]]
   


Typical Measurements
^^^^^^^^^^^^^^^^^^^^

If you have the program running, with a mote connected, simply shaking the mote in the direction of the axis (indicated on the mote by a small notch near the base) should update the plots with some meaningful vibration data.

This demo can be improved by using the mote in conjunction with a small motorized device (e.g. electric fan). Simply place the mote as close to the vibration source as possible and observe the results in the GUI.

Below is a typical example of DFT (Discrete Fourier Transform) data for an unbalanced motor rotating at 2000 RPM. Additionally provided is an explanation of where motor and bearing information should appear through the use of DFT.

|image4| **Figure 4. Typical GUI Output**

|image5| **Figure 5. Fourier Transform graph explained**

--------------

Further Information
-------------------

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/smartmesh_layout.png
   :width: 1000px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/mote_and_manager.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/cbm_app_output.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/gui.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/fft_markers.png
   :width: 600px
