CN0540 and the CoraZ7-07s
=========================

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_cora.jpg
   :align: center
   :width: 600px

Requirements
------------

Hardware:

-   :adi:`EVAL-CN0540-ARDZ <en/design-center/reference-designs/circuits-from-the-lab/CN0540.html>`
-  `CoraZ7-07s FPGA Board <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`_
-  `Class 10 16GB SD Card <https://www.amazon.com/gp/product/B073K14CVB/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1>`_
-  Ethernet cable (with network access)
-  Micro USB to USB Type A cable
-  IEPE Compatible Sensor

Software

-  `ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/cn0540.tar.gz>`_
-  :git-iio-oscilloscope:`IIO-Oscilloscope <releases>`

Setup
-----

SD-Card
~~~~~~~

To prepare the SD-card for the CoraZ7-07s board:

-  `Download ADI Kuiper Image for CN0540 <https://swdownloads.analog.com/cse/kuiper/cn0540.tar.gz>`_
-  Validate, Format, and Flash the SD Card

   -  :doc:`Format and flash the SD Card using Windows </wiki-migration/resources/tools-software/linux-software/zynq_images/windows_hosts>`

      -  :doc:`Format and flash the SD Card using Linux </wiki-migration/resources/tools-software/linux-software/zynq_images/linux_hosts>`

| 
| Once microSD card has been imaged, safely remove the hardware from the SD card writer, and insert the card directly into the microSD card slot on the CoraZ7-07s.

| |image1|\ |image2|

Download and Install IIO-Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Down the latest :git-iio-oscilloscope:`IIO-Oscilloscope release <releases>` from Github, and install it on your PC. (You may need to right-click the installer, and run as "Elevated" in order to get it to install. )

CoraZ7-07s Hardware Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few jumpers that need to be placed properly in order to use the Cora Z7s as described in this guide.


|image3|

+-----------------+--------------------------------------------------------------------------------+---------------------------------+
| Jumper Location | Description                                                                    | Shunt Placement                 |
+=================+================================================================================+=================================+
| JP2             | Selects how the CoraZ7-07s board boots. We want to boot from the microSD card  | Across Pins 1 & 2               |
+-----------------+--------------------------------------------------------------------------------+---------------------------------+
| JP3             | Selects how the CoraZ7-07s board is powered. We are powering from the USB port | Across Pins 3 & 2 (labeled USB) |
+-----------------+--------------------------------------------------------------------------------+---------------------------------+

Cables & Connectors
~~~~~~~~~~~~~~~~~~~

Connect the power, cables, and sensor according to the diagram below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_cora_stacked_input_numbers2.jpg
   :align: center
   :width: 600px

-  Ethernet Cable
-  Sensor Input
-  Micro USB cable

Boot Sequencing
~~~~~~~~~~~~~~~

Once the microSD card and cables have been connected to the CoraZ7-07s and CN0540 its now time to boot the system.

-  Connect the other end of the Ethernet cable into a router or other network connection. This will be the easiest way to stream and save the data.

.. note::

   
   If you don't have a network available and want to stream data directly from the Ethernet port of the CoraZ7-07s to the Ethernet port of your PC that is still possible, but requires some extra configuration. Please see the :doc:`Network Configuration </wiki-migration/resources/tools-software/linux-software/network-config>` page for complete details.


-  Using the Arduino pins, plug in the EVAL-CN0540-ARDZ on top of the CoraZ7-07s.
-  Plug in your sensor into the SMA connector on the EVAL-CN0540-ARDZ.

   -  (You may also connect your sensor into the 2-Pin header found at P1 if your sensor isn't an SMA output)

-  Plug in the UART cable into your PC's USB port.

   -  A driver for the board should automatically be detected and installed on your PC. If this does not happen you may have to manually install that driver in order to continue. Here is a link to the `UART Serial Driver <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>`_

-  Plug the power supply into the wall outlet and power up the setup

Finding your CN0540
~~~~~~~~~~~~~~~~~~~

Before you can start streaming data, you first must locate the CN0540 on your network.

-  Setup a UART serial communication between your PC and the Cora board using the micro USB cable to USB type A
-  Using your device manager, locate the COM port assigned to the CoraZ7-07s board\

|image4|

-  Open Putty, Tera Term, or other serial terminal program and open a terminal between the COM port the Cora board by setting the Baud rate to 115200, and connect.
-  The serial terminal connection will default to auto login and will place you in the root directory of the SD card.
-  From here its a good idea to check to see if your devices can be found using the command **iio_info** into the terminal, and hitting "Enter"

   -  This should provide a list of devices along with their channels and attributes

-  Type **ifconfig** into the terminal, hit "Enter"
-  That should echo back some information where you can pull out the inet address of eth0.\

|image5|

-  Open up the IIO-Oscilloscope application on your PC
-  Set the radio button for “Remote Devices” and type the inet address you just found, hit the "Refresh" button, and then click "Ok".\ |image6|\

|image7|

Using the System with IIO Oscilloscope
--------------------------------------

Now its time to start communicating with the CN0540 so you can start streaming data. When you first open IIO-Oscilloscope you'll see two windows.

-  CN0540 Plugin / DMM / DEBUG Window
-  IIO Capture Window

CN0540 IIO-Oscilloscope Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CN0540 IIO Plugin automatically configures the CN0540, so it is ready to use as soon as you run the application. Calibration of the sensor is also automatically performed so that a user can start using the capture window to collect and analyze data. No other configuration is required for the application.

If you want to re-calibrate the system, shut the system down, or modify individual registers of the devices on the CN0540 that can also be done either using the CN0540 Plugin or using the DEBUG panel to write/read specific registers. This is optional and typically application specific.

Below is a picture of what the CN0540 IIO Plugin looks like.

|image8|\ |image9|

User interface
^^^^^^^^^^^^^^

+---------------------+--------------------+---------------------------------------------------+-----------------------+
| Section             | User Control       | Description                                       | Value                 |
+=====================+====================+===================================================+=======================+
| Power Control       | SW_FF              | Checks the current status of the ADG5421's FF Pin | Low(normal)           |
|                     |                    |                                                   | High(over voltage)    |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Shutdown           | Shutdowns power from the AD7768-1                 | Disabled(Power On)    |
|                     |                    |                                                   | Enabled(Power down)   |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
| ADC Driver Settings | FDA Status         | ADA4945 Operational Status                        | Checked(Enable)       |
|                     |                    |                                                   | Un-Checked(Disabled)  |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | FDA Mode           | ADA4945 Power Mode                                | Checked(Full Power)   |
|                     |                    |                                                   | Un-Checked(Low Power) |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
| Sensor Calibrations | Calibration Result | The Calibration is set for a 10V calibration      | 10.0V                 |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Input Voltage(mV)  | Calibrated AD7768-1 Input voltage offset          | ~ 0.0V                |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Shift Voltage(mV)  | Calibrated LTC2606 Level Shifting Voltage         | ~ 0.0V                |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Sensor Voltage(mV) | Calibrated Sensor Input voltage                   | ~ 10.0V               |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
| Voltage Monitor     | Vin+ (mV)          | Input voltage coming from the sensor              |                       |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Vgpoi2 (mV)        | Not Used                                          | N/A                   |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Vgpoi3 (mV)        | Not Used                                          | N/A                   |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Vcom (mV)          | ADA4945 Common Mode input voltage                 | ~2.5 V                |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Vfda+ (mV)         | AD7768-1 Ain+ input voltage                       |                       |
+---------------------+--------------------+---------------------------------------------------+-----------------------+
|                     | Vfda- (mV)         | AD7768-1 Ain- input voltage                       |                       |
+---------------------+--------------------+---------------------------------------------------+-----------------------+

IIO Capture Window
~~~~~~~~~~~~~~~~~~

For CbM applications, most customers are typically interested in the frequency domain plots. To obtain a FFT plot, do the following:

-  Use the drop down menu labeled "Plot Type" and select "Frequency Domain".
-  Set the number of samples to 16384
-  Set the averaging to 3

You should see a nice plot like this when connected to the CN0532 sensor.\


|image10|

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cora_sdcard_insert.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cora_sdcard_connected.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cora_hw_config.jpg
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/com_port.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/serial_terminal_linux_ifconfig_inet.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_login.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_board_found.png
   :width: 475px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_cn0540_plugin_controls.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_cn0540_plugin_block_diagram.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/iio_oscilloscope_capture_cn0532.png
   :width: 500px
