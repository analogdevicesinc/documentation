AD936X Quick Start Guides
=========================

AD-FMCOMMS2/3/4/5-EBZ
---------------------

The Quick Start Guides provide a simple step by step instruction on how to do an initial system setup for the AD-FMCOMMS2/3/4/5-EBZ boards on various FPGA development boards. They will discuss how to program the bitstream, run a no-OS program or boot a Linux distribution.

Supported Carriers
~~~~~~~~~~~~~~~~~~

The AD-FMCOMMS2/3/4/5-EBZ is, by definition a "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carriers we support are:

+-------------------------------------------------------------------------------+----------+--------------+---------+
| Board                                                                         | FMCOMMS5 | FMCOMMS2/3/4 | Arradio |
+===============================================================================+==========+==============+=========+
| `AC701 <https://www.xilinx.com/AC701>`_                                       |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `KC705 <https://www.xilinx.com/KC705>`_                                       |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `KCU105 <https://www.xilinx.com/KCU105>`_                                     |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `VC707 <https://www.xilinx.com/VC707>`_                                       |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `ZC702 <https://www.xilinx.com/ZC702>`_                                       | √        | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                                       | √        | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                     | √        | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `Zed Board <http://zedboard.org/product/zedboard>`_                           |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `MITX045 <http://zedboard.org/product/mini-itx-board>`_                       |          | √            |         |
+-------------------------------------------------------------------------------+----------+--------------+---------+
| `SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_  |          |              | √       |
+-------------------------------------------------------------------------------+----------+--------------+---------+

Supported Environments
~~~~~~~~~~~~~~~~~~~~~~

The supported OS are:

+----------------------------------------------------------+-----+----------------+----------------+
| Board                                                    | HDL | Linux Software | No-OS Software |
+==========================================================+=====+================+================+
| `AC701 <https://www.xilinx.com/AC701>`_                  | √   |                | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `KC705 <https://www.xilinx.com/KC705>`_                  | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `KCU105 <https://www.xilinx.com/KCU105>`_                | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `VC707 <https://www.xilinx.com/VC707>`_                  | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `ZC702 <https://www.xilinx.com/ZC702>`_                  | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `ZC706 <https://www.xilinx.com/ZC706>`_                  | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `Zed Board <http://zedboard.org/product/zedboard>`_      | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+
| `MITX045 <http://zedboard.org/product/mini-itx-board>`_  | √   | √              | √              |
+----------------------------------------------------------+-----+----------------+----------------+

Hardware Setup
~~~~~~~~~~~~~~

In most carriers, the AD-FMCOMMS2/3/4-EBZ board connects to the LPC connector (unless otherwise noted). The AD-FMCOMMS5-EBZ board is a dual FMC connector, and requires either FMC connectors (which can be either LPC + LPC). The carrier setup requires power, UART (115200), ethernet (Linux), HDMI (if available) and/or JTAG (no-OS) connections. A few typical setups are shown below.

ZC702 + FMCOMMS2
^^^^^^^^^^^^^^^^

Early versions of the ZC702 carriers need to work around `AR# 51438, PG signal does not assert by default <https://www.xilinx.com/support/answers/51438.html>`_ errata.

ZC706 + FMCOMMS2
^^^^^^^^^^^^^^^^

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/cf_ad9361_setup.jpg
   :width: 800px

SoCkit + ARRADIO
~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/sockit_arradio.jpg
   :width: 800px

Jumper Configuration
^^^^^^^^^^^^^^^^^^^^

======= ========= ========= ======== ======== ========
\       CLOCKSEL0 CLOCKSEL1 BOOTSEL0 BOOTSEL1 BOOTSEL2
======= ========= ========= ======== ======== ========
**POS** 2-3       2-3       2-3      2-3      1-2
======= ========= ========= ======== ======== ========

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/sockit_clksel_bootsel.jpg
   :width: 350px

+--------------+


| JP2          |

+==============+

| 1.8V or 2.5V |

+--------------+

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/sockit_jp2.jpg
   :width: 200px

======= ===== ===== ===== ===== ===== =========
\       MSEL0 MSEL1 MSEL2 MSEL3 MSEL4 CODEC_SEL
======= ===== ===== ===== ===== ===== =========
**POS** 0     1     0     1     0     0
======= ===== ===== ===== ===== ===== =========

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms2-ebz/sockit_sw6.jpg
   :width: 200px

ADRV936X System-On-Module
-------------------------

The ADRV936X SOMs have three selectable switches. Two are used for selecting the boot source, and one for selecting the SD card source. The selection will be based on your carrier and how you want to boot the device.

For switch S3 and S4

========= == ==
BOOT Mode S3 S4
========= == ==
JTAG      0  0
QSPI      0  1
SD Card   1  1
========= == ==

For switch S1:

============== ==
SD Card Source S1
============== ==
Onboard        0
Carrier        1
============== ==

For our standard evaluation system most users boot from the SD cards placed either on the SOM or carrier board. For the **ADRV1CRR-BOB** carrier or carriers without SD card slots be sure to set S1 to 0.

Networking
----------

By default, all SD cards for the prototyping platform (not TES) are configured for DHCP networking over their Ethernet interfaces. If you want to change the networking interfaces to use static addresses, which is required for directly connected Ethernet cables without DHCP servers in the loop, a :git-linux_image_ADI-scripts:`helper script <enable_static_ip.sh>` is provided.

To update the IP address of the board you must be logged into the board over UART or JTAG or Ethernet.

From the development board or SOM itself run the following with the desired IP address:

::

   enable_static_ip.sh <ip address> eth0

This will fix the IP address of the desired Ethernet adapter and prevent the onboard network manager from changing it.
