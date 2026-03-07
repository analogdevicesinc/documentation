:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

2-24 GHz Reference Design Software Resources
============================================

This guide will walk you through setting up a ZCU102 FPGA Evaluation Board for use with the 2-24 GHz X-Microwave (XMW) TX/RX Platform.

--------------

SD Card Setup
-------------

XHIDDENSTART Click to expand XHIDDENSTARTSTOP You will need to image an SD Card with ADI Kuiper Linux and configure with the relevant files.

.. admonition:: Download
   :class: download

   Download the latest release of the Kuiper Linux kernel :doc:`here </wiki-migration/resources/tools-software/linux-software/adi-kuiper_images/release_notes>`.


-  Follow the instructions on this :doc:`page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` to **Image your SD Card** with this downloaded kernel.
-  You need to copy the following three files into the BOOT section of your SD Card, as described on the above :doc:`page </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` under **Configuring the SD Card for FPGA Projects**:
-  Image
-  system.dtb
-  BOOT.bin

.. admonition:: Download
   :class: download

   `Configuration Files for TX <https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_config_files.zip>`_

   
   `Configuration Files for RX <https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rx_config_files.zip>`_


.. important::

   
   -  If you just imaged your SD Card following the steps above, you will already have the latest Image file in the BOOT section.
   -  Be sure to select the appropriate .dtb (device tree file) and BOOT.bin (FPGA configuration file), depending on whether you are using the TX or RX Platform.
   -  **Rename your device tree file to system.dtb**
   


XHIDDENEND

ZCU102 Configuration
--------------------

The ZCU102 board can be configured as follows to allow control of the front end Platform using the :doc:`LIBIIO command line tools </wiki-migration/resources/tools-software/linux-software/libiio/cmd_line>`.

Boot from SD Card
~~~~~~~~~~~~~~~~~

XHIDDENSTART Click to expand XHIDDENSTARTSTOP In order to configure the FPGA to boot from the Linux kernel installed on the SD Card, SW6 [4:1] on the ZCU102 board needs to be set to 1110 (off, off, off, on) as shown below:

.. note::

   You may refer to the **MPSoC Device Configuration** section in the `ZCU102 User Guide <https://docs.xilinx.com/v/u/en-US/ug1182-zcu102-eval-bd>`_ for more information.


|SW6 Configuration to boot from SD Card| XHIDDENEND

USB to UART Bridge
~~~~~~~~~~~~~~~~~~

XHIDDENSTART Click to expand XHIDDENSTARTSTOP The ZCU102 board uses a micro-B cable to connect the USB UART port on the board (J83) to a host PC.

.. note::

   You may refer to the **CP2108 USB UART Interface** section in the `ZCU102 User Guide <https://docs.xilinx.com/v/u/en-US/ug1182-zcu102-eval-bd>`_ for more information.


   |ZCU102 USB UART Port|

.. admonition:: Download
   :class: download

   
   If a driver does not appear for this interface in your PC's Device Manager, it can be downloaded and installed from `here <https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads>`_. You can then use PuTTy (download from `here <https://www.putty.org/>`_) or any other SSH/Telnet Client to control this interface with the board.


XHIDDENEND

Network Configuration
~~~~~~~~~~~~~~~~~~~~~

XHIDDENSTART Click to expand XHIDDENSTARTSTOP The ZCU102 board uses an RJ45 ethernet cable to connect the ethernet port (P12) to a host PC.

.. note::

   You may refer to the **GEM3 Ethernet** section in the `ZCU102 User Guide <https://docs.xilinx.com/v/u/en-US/ug1182-zcu102-eval-bd>`_ for more information.


|ZCU102 Ethernet Port| The ethernet interface can then be used to control the ZCU102 board with higher level user applications based on Python or MATLAB.

Modifications to the network configurations can be made following the guidance detailed on the :doc:`Network Configuration </wiki-migration/resources/tools-software/linux-software/network-config>` wiki page.

XHIDDENEND

User Interfaces
---------------

Higher level applications can be used to configure the Platform, instead of the LIBIIO command-line terminal interface, using the ethernet port to communicate with the ZCU102 board.

Python Control
~~~~~~~~~~~~~~

ADI's pyadi-iio library enables configuration and control of many IIO components using Python. Details on getting started with this library can be found :doc:`here </wiki-migration/resources/tools-software/linux-software/pyadi-iio>`.

MATLAB Control
~~~~~~~~~~~~~~

ADI has also developed an RF Microwave Toolbox which enables users to configure and control IIO components using MATLAB. Details on getting started with this toolbox can be found :doc:`here </wiki-migration/resources/tools-software/rf-microwave-toolbox>`.

.. |SW6 Configuration to boot from SD Card| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/zcu102_sw6_sdcard.jpg
.. |ZCU102 USB UART Port| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/zcu102_usb_uart_port.jpg
.. |ZCU102 Ethernet Port| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/zcu102_ethernet_port.jpg
   :width: 400px
