AD-FMCJESDADC1-EBZ Zynq Quick Start Guide
=========================================

|

.. warning::

   \ **NOTE:**

   | Support for the ad-fmcjesdadc1-ebz was discontinued on all carriers starting with 2022_R2 Kuiper Linux release and it won't be supported anymore in future releases. Latest MicroBlaze images with pre-build files can be downloaded from `here <:doc:`/wiki-migration/resources/tools-software/linux-drivers/platforms/microblaze_loading`>`_. Check this :doc:`link </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>` to see all Kuiper releases. The HDL project source code can still be found on :git-hdl:`hdl_2022_r2 <projects/fmcjesdadc1>` release branch.


This guide provides some quick instructions (still takes awhile to download, and set things up) on how to setup the `ad-fmcjesdadc1-ebz <https://wiki.analog.com/../ad-fmcjesdadc1-ebz>`_ on the:

-  `ZC706 <https://www.xilinx.com/ZC706>`_ (rev 1.0 or higher).

The platforms are limited due to the requirements for 4 high speed serial lanes capable of JESD204B transactions at 5.0Gbps.

Requirements
------------

-  You need a Host PC (Windows or Linux) to write the SD card image. After the image is written, you can put away your Host PC, every other step is done naively on the Zynq.

   -  You need a SD card writer connected to above PC (Supported USB SD readers/writers are OK).

-  USB keyboard/mouse for the Zynq Device. We normally use the `Logitech 400r <http://www.logitech.com/en-hk/product/wireless-touch-keyboard-k400r2>`_
-  HDMI Display (monitor or TV)
-  Signal source for exciting the ADC analog inputs

Make the SD-Card
----------------

Follow the instructions at the :doc:`Create SD Image for Zynq Boards </wiki-migration/resources/tools-software/linux-software/zynq_images>`. This is a generic image, which supports multiple platforms including the :adi:`AD-FMCJESDADC1-EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/Eval-AD-FMCJESDADC1-EBZ.html>`.

Running the demo
----------------

Setting up the hardware.
~~~~~~~~~~~~~~~~~~~~~~~~


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#esd_warning>`_


You will need to:

-  Get the `ZC706 <https://www.xilinx.com/ZC706>`_:

   -


   |http://www.xilinx.com/images/product-images/zc706-base-board.jpg|

-  Insert the SD-CARD into the SD Card Interface Connector (J30)
-  Plug the AD-FMCJESDADC1-EBZ into the HPC FMC Connector (J37)
-  Plug your HDMI display device into the HDMI Video Connector (P1)
-  Plug your USB mouse/keyboard into the USB 2.0 ULPI Controller, w/Micro-B Connector (J21)
-  Plug the Power Supply into 12V Power input connector (J22) (DO NOT turn the device on).
-  Set the jumpers: The main one is: SW11 - Big Blue Switch in the middle, which controls the Boot Mode, it needs to be set: 1: Down, 2: Down, 3: Up, 4: Up, 5: Down. Other Jumpers can be checked via looking at the picture. (click the picture to make it bigger)

|zc706plusfmcjesdadc1.png|

-  Turn it on.
-  Wait ~30 seconds for the "DONE" LED to turn green. This is above the power switch.
-  Wait another ~30 seconds for the HDMI display device to start showing signs of life.
-  The follow the instructions for the type of demo that you want to do.

Standalone
~~~~~~~~~~

Analog Converter Performance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To look at the converter performance, this is not the correct platform, for all the reasons that it describes in the :doc:`Board description </wiki-migration/resources/eval/user-guides/ad-fmcjesdadc1-ebz>`.

To get a gross approximation of what is going on, you can use the :doc:`IIO Oscilloscope application </wiki-migration/resources/tools-software/linux-software/iio_oscilloscope>`.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/fmcjesdadc1-scope.png
   :width: 200px

Note - that the specifications of the converter, are better than most signal generators. Don't be surprised when you see spurs, or performance issues due to not having a good enough source.

JESD204B Link Performance
^^^^^^^^^^^^^^^^^^^^^^^^^

Link performance can also be examined - for this, you should look at the :doc:`eye scan docs </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/jesdadc1_eyescan.png
   :width: 200px

Stream Data to Visual Analog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:adi:`Visual Analog™ <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/visualanalog.html>` is a software package that combines a powerful set of simulation and data analysis tools with a user-friendly graphical interface. VisualAnalog allows designers to measure ADC performance with real input waveforms. Downloading and Installing Visual Analog is done from :adi:`here <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/visualanalog.html>`

The first thing that must be done is to ensure that both the ZC706 and your PC which has Visual Analog on it are on the same network. This can be done in a variety of ways, from using a cross over cable to plugging things into a common network, and having both use DHCP.

DHCP
^^^^

Just plug both platforms (a) your PC running Visual Analog, and (b) your ZC706 into a common network. As long as both systems are connected somehow, without a firewall between them, it's now just a matter of finding out the IP address of the ZC706 - which is pretty easy to do in a terminal (just press CNTL-ALT-T at the same time on the keyboard attached to the ZC706), then:

::

   analog@linaro-ubuntu-desktop:~$ **ip addr show**
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
   2: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
       link/ether 00:0a:35:00:01:22 brd ff:ff:ff:ff:ff:ff
       inet 169.254.2.35/16 brd 169.254.255.255 scope global eth1

Your IP address is on the last line *169.254.2.35*.

This is what you would type into the address box in the IIO client for Visual Analog.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/iio_command_client_settings.png
   :width: 300px

Cross Over Cable
^^^^^^^^^^^^^^^^

Using a `cross over cable <https://en.wikipedia.org/wiki/Ethernet_crossover_cable>`_ is a pretty easy way to do things. The settings on Windows is pretty easy - (a) turn your computer on. (b) plug the cross over cable into both PC and ZC706. That's it.

On the ZC706, it's just a simple matter of configuring the network to use `Link Local <https://en.wikipedia.org/wiki/Link-local_address>`_ addressing. To do this, just:

Goto the systems settings icon on the left side of the screen


|Click for bigger|

| 
| This should bring up the system settings pannel. |image1|

| 
| Click on the "network" settings. |image2|

| 
| Click on the "options" button. This should bring up the "Editing Wired Connection" panel. |image3|

| 
| Move over to the "IPv4 Settings" tab, and change the "Method" to "Link-Local Only". |image4|

| 
| Click "Save". You will normally be asked for the *root* password. This is "analog" (all lower case, no quotes). Then you should see a IP Address of 169.254.x.x in the window. Copy this address down, as it is the address you will need for Visual Analog.\ |image5|

This is what you would type into the address box in the IIO client for Visual Analog.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/iio_command_client_settings.png
   :width: 300px

Debugging
---------

-  Sometimes your SD card doesn't boot. Sometimes it does. See: `AR# 52023 <https://www.xilinx.com/support/answers/52023.html>`_

   -  Fix: Don't use pre-production silicon, update your board.

-  USB/Mouse doesn't work.

   -  Fix: Check the version of board that you have - You need a ZC706 rev 1.0 or higher.

.. |http://www.xilinx.com/images/product-images/zc706-base-board.jpg| image:: http://www.xilinx.com/images/product-images/zc706-base-board.jpg
.. |zc706plusfmcjesdadc1.png| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/zc706plusfmcjesdadc1.png
   :width: 200px
.. |Click for bigger| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/system_settings.png
   :width: 100px
.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/system_settings_2.png
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/network.png
   :width: 100px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/edit_ethernet.png
   :width: 100px
.. |image4| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/edit_ethernet_linklocal.png
   :width: 100px
.. |image5| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz/network.png
   :width: 100px
