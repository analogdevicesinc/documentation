Contiki Operating System
========================

Presentation
------------

Contiki is an open source operating system that runs on tiny low-power microcontrollers and makes it possible to develop applications that make efficient use of the hardware while providing standardized low-power wireless communication for a range of hardware platforms.

Contiki is used in numerous commercial and non-commercial systems, such as city sound monitoring, street lights, networked electrical power meters, industrial monitoring, radiation monitoring, construction site monitoring, alarm systems, remote house monitoring, and so on.

For more information, see `the Contiki website <http://contiki-os.org>`__.

Installation of Contiki on the RL78/G14 Demonstration Kit
---------------------------------------------------------

Obtaining the sources
~~~~~~~~~~~~~~~~~~~~~

Analog Devices has a fork of Contiki, with some basic support for the RL78/G14 Demonstration Kit from Renesas. The GIT tree is available on `Github <https://github.com/analogdevicesinc/contiki>`__.

The latest sources can be obtained at the following URL: :git-contiki:`archive/master`.zip

Extract the ZIP to the desktop (the extracted folder should be named 'contiki-master').

Installing the dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~

IAR toolchain
^^^^^^^^^^^^^

To compile Contiki, the IAR toolchain for RL78 is required (as of August 2014, the GCC-based toolchain for RL78 leads to extremely unstable builds).

You can install it from the DVD that came with your RL78/G14 Demonstration Kit. Please follow the instructions described in the chapter named "Software Installation" of the RL78/G14 Quick Start Guide. This manual can be found on the DVD at the following URI:

::

   CD DRIVE\QSG\RL78G14_RDK_V21_QSG.pdf

Alternatively, it can be downloaded from Renesas' website, at the following URL: http://documentation.renesas.com/doc/products/tools/r20uw0117eu0200_yrdkrl78g14_qsg.pdf

.. important::

   Note that the final binary of Contiki will be way above 16 KiB. If you choose to subscribe to the evaluation license for IAR, you must choose the time-constrained license and not the size-constrained one.


GNU tools for Windows
^^^^^^^^^^^^^^^^^^^^^

Compiling Contiki requires a few additional tools generally found on UNIX based operating systems. You will need to download and install the following GnuWin32 components:

-  http://gnuwin32.sourceforge.net/downlinks/coreutils.php
-  http://gnuwin32.sourceforge.net/downlinks/findutils.php
-  http://gnuwin32.sourceforge.net/downlinks/make.php
-  http://gnuwin32.sourceforge.net/downlinks/sed.php

Compiling Contiki OS
~~~~~~~~~~~~~~~~~~~~

To compile Contiki, launch a terminal console. To do so, click the Start button and type "cmd"; the program "cmd.exe" should appear in the search results.

In the terminal console, type the following:

::

   cd %HOMEPATH%\Desktop\contiki-master\examples\er-rest-example
   set PATH="%ProgramFiles(x86)%\GnuWin32\bin";%PATH%
   set IAR_PATH="%ProgramFiles(x86)%\IAR Systems\Embedded Workbench 6.5\rl78"
   make TARGET=yrdkrl78-g14 IAR=1 er-example-server.yrdkrl78-g14.srec

This will generate a file named **er-example-server.yrdkrl78-g14.srec**. This sample program is a simple example of a CoAP server, that will allow you to change the color of a LED and optionally control a :doc:`CN0337 </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0337>` PMOD plugged into the PMOD2 connector.

Flashing
~~~~~~~~

Hardware setup
^^^^^^^^^^^^^^

The ADF7242 PMOD should be plugged in the PMOD1 slot, as seen here:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/rl78g14_adf7242.jpg
   :align: center

To flash a new program file, you have to switch the board to a specific mode. This can be done by setting the DIP switch #2 to OFF (the switches are located on the bottom right of the screen). The three other switches should stay in position ON.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/dipswitch.png
   :align: center

Then, plug the board to USB. The screen should lit and display nothing, and Windows might detect that a new device was plugged and install the driver consequently.

You can flash the srec file to the RL78/G14 Demonstration Kit using the Renesas Flash Programmer utility, available on the DVD or at the following address: https://www.renesas.com/us/en/software-tool/renesas-flash-programmer-programming-gui

Once installed, start it, select "Create new workspace" and "full mode" (or "open workspace" if you already created one). In the workspace creation wizard, you will have to select the model of the CPU, which is written on and under the CPU chip on the board. It *should* be **R5F104PJ**.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/renesas2.png
   :align: center

Then, choose the communication interface, which should be **COM** followed by a number (here COM6):


|image1|

Finally:

-  Right click on the project name and select "Set program file". In the file selector, open the **er-example-server.yrdkrl78-g14.srec** file that we just compiled.
-  Click on Microcontroller -> Erase NAND
-  Click on Microcontroller -> Write program

When it's done, unplug the USB cable, revert the DIP switch #2 to its original ON position, then re-plug the cable to see the Contiki example program run on the board.

Communication
-------------

6loWPAN
~~~~~~~

Those few steps will allow you to communicate between Contiki OS and a Linux based board equipped with a second adf7242 module.

If not done previously, compile the adf7242 driver for the Linux kernel of your board, following the instructions available here: :doc:`ADF7242 Network MAC802154 Linux Driver </wiki-migration/resources/tools-software/linux-drivers/networking-mac802154/adf7242>`.

Double-check that you installed the firmware file, and that the platform data and/or devicetree is correct (including the IRQ number).

If the adf7242 driver was compiled as a module, load it:

::

   modprobe adf7242

If the loading was successful, the output of the "iz listphy" command should be similar to the following:

::

   root@linaro-ubuntu-desktop:~# iz listphy
   wpan-phy0  IEEE 802.15.4 PHY object
       page: 0  channel: 11
       channels on page 0: 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

Then, setup the 6lowpan interface:

::

   # Parameters
   MAC_ADDR="a0:0:0:0:0:0:0:1"
   PAN_ID=777 # hexadecimal
   DEVICE_ADDR=8001 # hexadecimal
   CHANNEL=11

   # Configuration of the IEEE 802.15.4 and 6lowpan interfaces
   iz add wpan-phy0
   ip link set wpan0 address ${MAC_ADDR}
   iz set wpan0 ${PAN_ID} ${DEVICE_ADDR} ${CHANNEL}
   ifconfig wpan0 up
   sleep1
   ip link add link wpan0 name lowpan0 type lowpan
   ip link set lowpan0 address ${MAC_ADDR}
   ifconfig lowpan0 up

   # Setup of IPv6 address and routes
   ip addr add 2001::1/128 dev lowpan0
   ip route add 2001::/64 dev lowpan0

If everything went correctly, you should now be able to ping Contiki:

::

   CONTIKI_DEFAULT_ADDR="fe80::a200:0:0:3%lowpan0"
   ping6 ${CONTIKI_DEFAULT_ADDR}

CoAP
~~~~

The program that we flashed here on the RL78/G14 Demonstration Kit is a simple CoAP server. CoAP stands for *Constrained Application Protocol*. It is a software protocol designed to allow very simple electronic devices to communicate over the Internet. For more information about CoAP: `Constrained_Application_Protocol <https://en.wikipedia.org/wiki/Constrained_Application_Protocol>`__

To communicate with Contiki using the CoAP protocol, you need a CoAP client. The one used here is an addon to Firefox, named Copper: https://addons.mozilla.org/fr/firefox/addon/copper-270430/

Install it by following the previous URL, and click "Add to Firefox". A restart of the browser might be required.

Once done, you can start the client by typing the following URI in the address bar (adapt the IPv6 address adequately):

::

   coap://[2001::3]/

You will arrive at the following screen:


|image2|

If the resources don't appear on the left tree area, click **Discover**.

You can now receive ASCII text from the available resources, by selecting the resource and then clicking **GET**.

-  The *hello* resource will return the message: **Hello World!**
-  The *led* resource will return information about the state of the LED 11 of the RL78/G14 Demonstration Kit.

You can also send ASCII messages. For instance, the *led* resource allows you to turn ON and OFF the LED 11. To do so, click on the **Outgoing** tab and type one of the two messages to turn the LED 11 ON or OFF:

::

   mode=on
   # or
   mode=off

Then click on **POST**; If successful the state of the LED will be updated.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/comm6.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/coap1.png
