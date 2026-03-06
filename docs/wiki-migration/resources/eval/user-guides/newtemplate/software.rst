**\*BOARD_NAME**\ \* Software User Guide
========================================

Introduction
------------

| The `board_name <https://wiki.analog.com/board_name>`__ is an 18-bit, 15 MSPS, 2 ppm linear data acquisition system with an easy to drive input impedance of 1.1 kΩ. The analog input range is 8.096 V peak-to-peak and can be driven in either single-ended or differential mode, providing flexibility for many different applications.
| The circuit is in field programmable gate array (FPGA) mezzanine card (FMC) form factor, powered with 12 V either from the FMC connector or an external supply. The digital interface uses serial low voltage differential signaling (LVDS), minimizing the input/output requirements and enabling easy integration with other FPGA designs.
| A separate data clock eases the timing requirements of the host FPGA. An on-board 120 MHz clock is forwarded to the FPGA and a CONVERT retiming flip-flop reduces jitter from the convert signal of the FPGA.

--------------

Software Setup
--------------

| For the device to run, the SD card should be loaded with Analog Devices Kuiper Linux image, a distribution based on Raspbian from the Raspberry Pi Foundation. It incorporates Linux device drivers for ADI products as well as tools and other software products designed and created with ease of use in mind. The reasoning behind creating this distribution is to minimize the barriers to integrating ADI hardware devices into a Linux-based embedded system. Access to the embedded system can be through ​a remote PC connected ​either via LAN cable or Wi-Fi. ​
| ==== Resources ====

.. admonition:: Download
   :class: download

   
   -  :doc:`Analog Devices Kuiper Linux image </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
   -  :doc:`IIO Oscilloscope Installation Guide </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
   -  :git-iio-oscilloscope:`Latest version of IIO-Oscilloscope <releases>`
   -  :doc:`Python (via Pyadi-iio) </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`
   -  :git-pyadi-iio:`CN0577 Python Example <examples/ltc2387_example.py>`
   -  :doc:`CN0577 HDL Reference Design </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0577/hdl>`
   
   |


| ==== Software Installation ==== In order to control the `board_name <https://wiki.analog.com/board_name>`__, you will need to install ADI Kuiper Linux image on an SD card. Complete instructions, including where to download the SD card image, how to write it to the SD card, and how to configure the system are provided at :doc:`Kuiper Images </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`. Write the image and follow the system configuration procedure.

The `board_name <https://wiki.analog.com/board_name>`__ is also supported with the Libiio library. This library is cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python, MATLAB, and others. Two easy to examples that can be used with the :adi:`EVAL-CN0577-FMCZ` are:

-  :doc:`IIO Oscilloscope </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`
-  :doc:`Python (via Pyadi-iio) </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`

| 
| === Establishing Connection === To be able to connect your device, the software must be able to create a context. The context creation in the software depends on the backend used to connect to the device as well as the platform where the EVAL-CN0577-FMCZ is attached. The platform currently supported for the CN0557: ZedBoard using the ADI Kuiper Linux. The user needs to supply a URI which will be used in the context creation. The Libiio is a library for interfacing with IIO devices.

.. admonition:: Download
   :class: download

   Install the :git-libiio:`Libiio package <releases>` on your machine.


The :doc:`iio_info </wiki-migration/resources/tools-software/linux-software/libiio/iio_info>` command is a part of the libIIO package that reports all IIO attributes.

| Upon installation, simply enter the command on the terminal command line to access it.
| === For Windows machine connected to ZedBoard via Ethernet cable: ===

Using SSH Terminal Software:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Open SSH Terminal Software (PuTTY, TeraTerm or similar). User should now start the PuTTY application and enter certain values in the configuration window. In the terminal, run:

::

   analog@analog:~$ iio_info -u ip:<ip_address>

| 
| ==Using command terminal:==

::

   iio_info -s

Prompting this on the command terminal in your windows PC will give you the ip address to access the EVAL-CN0577-FMCZ.

::

   ssh analog@<ip_address>

::

   analog@analog:~$ iio_info -u ip:<ip_address>


   | 

IIO Commands
^^^^^^^^^^^^

There are different commands that can be used to manage the device being used. The :doc:`iio_attr </wiki-migration/resources/tools-software/linux-software/libiio/iio_attr>` command reads and writes IIO attributes.

::

   analog@analog:~$ iio_attr [OPTION]...

Example:

-  To look at the context attributes, enter this code on the terminal:

::

   analog@analog:~$ iio_attr -a -C

|

| ----

Software Operation
""""""""""""""""""

.. admonition:: Download
   :class: download

   Make sure to download/update to the latest version of IIO-Oscilloscope.

   
   :git-iio-oscilloscope:`releases`


-  Once done with the installation or an update of the latest IIO-Oscilloscope, open the application. The user needs to supply a URI which will be used in the context creation of the IIO Oscilloscope and the instructions can be seen from the previous section.
-  Press refresh to display available IIO Devices, once ltc2387 appeared, press connect.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/577_osc.png
   :align: center
   :width: 500px

Debug Panel
^^^^^^^^^^^

Below is the Debug panel of ltc2387 wherein you can directly access the attributes of the device.


|image1|

DMM Panel
^^^^^^^^^

Access the DMM panel to see the instantaneous reading of the ADC voltages and the device temperature.


|image2|

Pyadi-IIO
"""""""""

| :doc:`PyADI-IIO </wiki-migration/resources/tools-software/linux-software/pyadi-iio>` is a python abstraction module for ADI hardware with IIO drivers to make them easier to use. This module provides device-specific APIs built on top of the current libIIO python bindings. These interfaces try to match the driver naming as much as possible without the need to understand the complexities of libIIO and IIO.
| === Running the Example === After installing and configuring pyADI-IIO in your machine, you are now ready to run python script examples. In our case, run the ltc2387_example.py found in the examples folder.

-  Connect the :adi:`EVAL-CN0577-FMCZ` to the ZedBoard.
-  Open command prompt or terminal and navigate through the examples folder inside the downloaded or cloned *pyadi-iio* directory.
-  Run the example script using the command.

::

   .../pyadi-iio/examples $ python3 ltc2387_example.py

| Running example with ADALM2000 with the setting below: |image3|
| === Sample Output === |image4|

--------------

.. tip::

   **If you want to go back to the HARDWARE SETUP procedure, please visit:** :doc:`CN0577 Hardware User Guide </wiki-migration/resources/eval/user-guides/newtemplate/hardware>`


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/577_debug_panel.png
   :width: 500px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/577_dmm_panel.png
   :width: 500px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/scopy_diff_input.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0577/output_time_domain.png
   :width: 600px
