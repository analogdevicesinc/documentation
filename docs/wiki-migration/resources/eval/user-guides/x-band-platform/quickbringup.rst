X-Band Hybrid Beamforming Development Platform Quick Start Guide
================================================================

Equipment Needed
----------------

Refer to the :doc:`hardware wiki </wiki-migration/resources/eval/user-guides/x-band-platform/hardware>` page for the equipment provided with the platform and the hardware the user is responsible for procuring.

--------------

Software Needed
---------------

Refer to the :doc:`software wiki </wiki-migration/resources/eval/user-guides/x-band-platform/software>` page for the necessary software required to control the platform.

--------------

Test Setup
~~~~~~~~~~

Place holder for block diagram or photos

--------------

Quick Start Bringup with Hardware
---------------------------------

This section assumes the following:

-  Standoffs have been attached to Quad MxFE board
-  ZCU102 and MxFE Eval Board have been attached via a FMC extender on the FMC
-  Ethernet cable has been connected to ZCU102 and connected to USB to Ethernet
-  USB to Ethernet dongle has IP address of 192.168.1.101. For locally connected FPGAs (i.e. Ethernet cable from ZCU102 to USB to Ethernet dongle), the Hostname is ``192.168.1.101``. This assumes that the USB to Ethernet dongle has been configured with an IP address of ``192.168.1.x`` where ``x`` represents a number 0 to 255 (excluding 101). This can be seen in the image. These settings are accessed (in Windows 10) by typing Network into the start menu then choose the "change adapter options" select and right click on the USB to Ethernet dongle. Select properties from the right click menu. Once the IP has been set, it will be remembered on the computer. Click ok on both windows to close and save the Dongle IP settings.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/usb_to_ethernet.png
   :alt: Configuration of USB to Ethernet Dongle IP
   :align: center

-  2x micro USB cables have been connected to PC and VCU118 for JTAG and Serial
-  All required software programs have been installed. See here for full list: :doc:`Software Needed </wiki-migration/resources/eval/user-guides/x-band-platform/software>`

-  Desired clocking configuration has been implemented
-  12V power bricks have been connected to all boards
-  Fans have been turned on

General Board Power Up/Programming Sequence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The power up sequence is not difficult:

-  Power up the 500MHz oscillator
-  Power up the Quad MxFE Board
-  Power on the VCU118 board

Once these are powered up, program the FPGA:

-  Open Putty at the correct COM port and baudrate of 115200. See this section to determine the correct COM port :doc:`Putty Configuration </wiki-migration/resources/eval/user-guides/quadmxfe/quickbringup>`
-  Open Xilinx Command Line Tool (XSCT). Open it from the Start Menu under Xilinx --> Xilinx Software Commandline Tool. Once the prompt is open, type: ``cd Desktop\QuadMxFE``\ If the files were unzipped somewhere else, then change directory to that folder.
-  Run the loading script for the particular build by typing the following (example) in XSCT:``source run.vcu118_quad_ad9081_204c_txmode_11_rxmode_4_revc.tcl``\ The statement above will launch the programming of the first build, but the others can be run by changing the name of the particular .tcl file to be loaded
-  Wait for the programming to finish in XSCT. This should show that the tcfchan#1 was closed as the final step.

|image1|

-  Wait for the build to boot completely by checking the Putty terminal window. The putty window shows the progress of the Linux image booting. Wait for the login prompt as shown at the bottom. |image2| This example output is from the Txmode 11 Rxmode 4 image output. At this point, the image is ready to use in MATLAB or additional debug steps can be performed. To log into the image, the username and password are ``UN: root 
   PW: analog``
-  At this point the FPGA has booted and all of the blue PLL lights should be illuminated. The FPGA is ready to be controlled from MATLAB or from IIO Oscilloscope.
-  To work in IIO Oscilloscope, open IIO Oscilloscope and use the GUI
-  To control through MATLAB, Please refer to the following section. There are a number of example scripts that highlight various aspects of the Quad MxFE.

--------------

MATLAB Control Overview
~~~~~~~~~~~~~~~~~~~~~~~

Controlling Quad-MxFE With MATLAB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Debug
-----

No blue lights are visible on board
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If no blue lights are visible on the board, then the PLLs are not locked. The most likely cause of this is the lack of a 500MHz source into J41. Check the input power and state of the source. It should be 500MHz @ ~0dBm. Once the 500MHz signal is verified, the FPGA programming must be rerun.

:doc:`Back To Quad-MxFE Main Page </wiki-migration/resources/eval/user-guides/quadmxfe>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/running_fpgaload.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/putty_quad_mxfe.png
   :width: 400px
