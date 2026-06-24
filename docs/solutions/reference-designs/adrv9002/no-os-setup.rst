ADRV9002 No-OS System Level Design Setup
========================================

Supported devices
-----------------

-  :adi:`ADRV9002`

Supported carriers
------------------

-  `ZCU102 <https://www.xilinx.com/ZCU102>`_
-  `ZC706 <https://www.xilinx.com/ZC706>`_
-  `Zed Board <http://zedboard.org/content/overview>`_

Naming conventions
------------------

The ADRV9001 is family designator assigned to the System Development User Guide
(UG-1828 for new ADRV9002, ADRV9003, ADRV9004, and upcoming additional family
members). Thus, throughout this document, ADRV9001 designator may be used to
refer to either ADRV9002, ADRV9003 or ADRV9004.

Project layout and HDL generation
---------------------------------

This is how the adrv9001 no-OS project looks like as a file tree.

::

   no-OS/projects/adrv9001
   ├── Makefile
   ├── src
   │   ├── app
   │   │   ├── app_iio.c
   │   │   ├── app_iio.h
   │   │   ├── headless.c
   │   │   ├── ORxGainTable.h
   │   │   ├── RxGainTable.h
   │   │   └── TxAttenTable.h
   │   ├── firmware
   │   │   ├── Navassa_EvaluationFw.h
   │   │   └── Navassa_Stream.h
   │   └── hal
   │       ├── adi_platform.h
   │       ├── adi_platform_types.h
   │       ├── no_os_platform.c
   │       ├── no_os_platform.h
   │       └── parameters.h
   ├── src.mk
   └── system_top.xsa / system_top.hdf

Note the presence of the system_top.xsa or system_top.hdf file. In order to build this no-OS project, you need such an .xsa or .hdf file present in the project directory, as shown above. In case you don't have one, either obtain a pre-built file or build it yourself by following the `Building HDL <https://wiki.analog.com/resources/fpga/docs/build>`_ guide.

See more about Navassa's HDL and options for building an HDL for CMOS or LVDS interface :doc:`here </solutions/reference-designs/adrv9002/reference_hdl>`.

And this is how the corresponding drivers section looks like as a file tree (the
Navassa API can be found under common, devices and third_party directories):

::

   no-OS/drivers/rf-transceiver/navassa/
   ├── adrv9002.c
   ├── adrv9002_conv.c
   ├── adrv9002.h
   ├── common
   ├── devices
   └── third_party

Building
--------

.. note::

   See `Build <https://wiki.analog.com/resources/no-os/build>`_.

By default, the digital interface is CMOS. In case a LVDS digital interface is
used, this has to be specified in the make command:

::

   make LVDS=y

Demo Applications
-----------------

Make sure to connect your adrv9002 evaluation board to the correct FMC connector
or the carrier you use:

-  :doc:`ZCU102 </solutions/reference-designs/adrv9002/quickstart/zynqmp>`
-  :doc:`ZC706 </solutions/reference-designs/adrv9002/quickstart/zynq>`
-  :doc:`Zed Board </solutions/reference-designs/adrv9002/quickstart/zed>`

.. note::

   See `Dac Dma Example <https://wiki.analog.com/resources/no-os/dac_dma_example>`_.

.. note::

   See `Iiod Demo <https://wiki.analog.com/resources/no-os/iiod_demo>`_.

Here's an example of iio-oscilloscope connected to a NO-OS Navassa IIOD demo
with electrical loopbacks between TX1-RX1 and TX2-RX2.

.. image:: images/navassa-tinyiiod.jpg
   :width: 400
