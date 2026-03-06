HIL Quick Start Guide
=====================

Prerequisites
-------------

Required Hardware
~~~~~~~~~~~~~~~~~

-  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__ Rev D or later board
-  HIL board
-  16 GB SD Card
-  Ethernet cable
-  1 x Micro-USB cable

Required Software
~~~~~~~~~~~~~~~~~

-  You need a Host PC (Windows or Linux)
-  A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1)
-  IIO Scope `Download <https://wiki.analog.com/https/github.com/analogdevicesinc/iio-oscilloscope/releases>`__

Creating / Configuring the SD Card
----------------------------------

.. tip::

   \ :doc:`Create SD Image for Zynq Boards. (it is a single image for all boards). </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`\


In this case the root of 'BOOT' partition should contain:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   *''uImage file for Zynq''
   *''BOOT.BIN specific to your HIL + ZedBoard''
   *''devicetree.dtb for Zynq specific to your HIL + ZedBoard''

Setting up the hardware (ZedBoard)
----------------------------------

You will need to:

-  Get the `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__.


|zedboard.png|

-  Insert the SD-CARD into the SD Card Interface Connector (J12).
   \* Connect the HIL board into the ZedBoard FMC connector.
   \* Connect USB UART J14 (Micro USB) to your host PC.
   \* Plug your ethernet cable into the RJ45 ethernet connector(J11).
   \* Plug the Power Supply into 12V Power input connector (J20) (DO NOT turn the device on).
   \* Set the jumpers as seen in the below picture:

   |zed_jumpers.jpg|

   \* Loopback the DAC's output channels to the ADC's inputs.
   \* Turn it on.
   \* Wait ~30 seconds for the “DONE” LED to turn blue. This is near the DISP1.

.. esd-warning::


Booting the SD Card
-------------------

Remote IIO Oscilloscope
~~~~~~~~~~~~~~~~~~~~~~~

-  Observe kernel and serial console messages on your UART terminal (use the first ttyUSB or COM port resisted):
   

.. raw:: html

   <details><summary>Complete kernel boot log (Click to expand)</summary>

.. container:: box bggreen

   
   ::
   
      U-Boot 2018.01-21439-gd244ce5 (Jul 29 2021 - 16:33:01 +0100), Build: jenkins-development-build_uboot-1

.. raw:: html

   </details>


| 
| ^ user ^ password ^

==== ======
root analog
==== ======

| 
| \* Run the ifconfig command on your UART terminal and get your board IP.

::


   root@analog:~# ifconfig
   eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet your_board_ip  netmask 255.255.255.0  
           inet6 fe80::b581:6452:5ee2:1237  prefixlen 64  scopeid 0x20<link>
           ether 00:0a:35:07:93:57  txqueuelen 1000  (Ethernet)
           RX packets 8424  bytes 1461028 (1.3 MiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 13137  bytes 13931543 (13.2 MiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
           device interrupt 35  base 0xb000

   lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
           inet 127.0.0.1  netmask 255.0.0.0
           inet6 ::1  prefixlen 128  scopeid 0x10<host>
           loop  txqueuelen 1000  (Local Loopback)
           RX packets 888  bytes 58366 (56.9 KiB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 888  bytes 58366 (56.9 KiB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
   root@analog:~#

| 
| \* Open IIO Scope application and type ip:your_board_ip in the URI tab.

::

   {{ resources:eval:user-guides:hil:hil_remote_login.jpg?650 }} \\

-  From the Dac Data Manager Window window select the output channels of the DAC and enable the cyclic buffer.
-  Load an example file from the IIO Oscilloscope/lib/osc/waveforms folder.

::

   {{ resources:eval:user-guides:hil:dac_data_management_lldk.jpg?650 }} \\

| After the load button has been pressed you should see the data capture window:
| |caputred_loopback_signal_hil.jpg|

.. important::

   Even thought this is Linux, this is a persistent file systems. Care should be taken not to corrupt the file system -- please shut down things, don't just turn off the power switch. Depending on your monitor, the standard power off could be hiding. You can do this from the terminal as well with ``sudo shutdown -h now``


   |image1|

.. |zedboard.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/AD777x-ARDZ/zedboard.png
   :width: 600px
.. |zed_jumpers.jpg| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/adaq8092/zed_jumpers.jpg
   :width: 400px
.. |caputred_loopback_signal_hil.jpg| image:: https://wiki.analog.com/_media/resources/eval/user-guides/hil/caputred_loopback_signal_hil.jpg
   :width: 850px
.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/shutdown.png
   :width: 300px
