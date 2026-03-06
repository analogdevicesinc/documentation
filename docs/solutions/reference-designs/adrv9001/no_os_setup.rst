.. _adrv9001-noos:

ADRV9002 No-OS System Level Design Setup
==========================================

Supported Devices
-----------------

- :adi:`ADRV9002`

Supported Carriers
------------------

- :xilinx:`ZCU102 <products/boards-and-kits/ek-u1-zcu102-g.html>`
- :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
- `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Naming Conventions
------------------

The ADRV9001 is a family designator assigned to the System Development User
Guide (UG-1828 for ADRV9002, ADRV9003, ADRV9004, and upcoming additional
family members). Throughout this document, the ADRV9001 designator may be used
to refer to either ADRV9002, ADRV9003, or ADRV9004.

Project Layout and HDL Generation
----------------------------------

This is how the adrv9001 no-OS project is structured:

.. code-block::

   no-OS/projects/adrv9001
   ├── Makefile
   ├── src
   │   ├── app
   │   │   ├── app_iio.c
   │   │   ├── app_iio.h
   │   │   ├── headless.c
   │   │   ├── ORxGainTable.h
   │   │   ├── RxGainTable.h
   │   │   └── TxAttenTable.h
   │   ├── firmware
   │   │   ├── Navassa_EvaluationFw.h
   │   │   └── Navassa_Stream.h
   │   └── hal
   │       ├── adi_platform.h
   │       ├── adi_platform_types.h
   │       ├── no_os_platform.c
   │       ├── no_os_platform.h
   │       └── parameters.h
   ├── src.mk
   └── system_top.xsa / system_top.hdf

Note the presence of the ``system_top.xsa`` or ``system_top.hdf`` file. In
order to build this no-OS project, you need such a file present in the project
directory. In case you do not have one, either obtain a pre-built file or build
it yourself by following the `Building HDL <https://analogdevicesinc.github.io/hdl/user_guide/build_hdl.html>`__
guide.

See more about the ADRV9002 HDL and options for building with CMOS or LVDS
interface in the :doc:`HDL Reference Design <reference_hdl>`.

The corresponding driver files can be found at:

.. code-block::

   no-OS/drivers/rf-transceiver/navassa/
   ├── adrv9002.c
   ├── adrv9002_conv.c
   ├── adrv9002.h
   ├── common
   ├── devices
   └── third_party

The Navassa API (the transceiver's control API provided by Analog Devices) can
be found under the ``common``, ``devices``, and ``third_party`` directories
within the driver path above.

- :git-no-OS:`No-OS project <projects/adrv9001>`
- :git-no-OS:`No-OS driver <drivers/rf-transceiver/navassa>`

Building
--------

By default, the digital interface is CMOS. In case an LVDS digital interface
is used, this has to be specified in the make command:

.. code-block:: bash

   make LVDS=y

For detailed build instructions, see the
`no-OS Build Guide <https://analogdevicesinc.github.io/no-OS/build_guides/build_guide.html>`__.

Demo Applications
-----------------

The no-OS project includes two demo application types:

- **Headless mode** (``headless.c``) -- configures the ADRV9002 and runs a
  simple loopback test without any host interface.
- **IIOD demo** (``app_iio.c``) -- implements a tinyIIOD server that exposes
  the ADRV9002 channels over USB or network. This allows the
  :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>` application (or
  any IIO client) to connect, configure the device, and stream data.

Make sure to connect your :adi:`EVAL-ADRV9002` board to the correct FMC
connector on the carrier you use:

- :doc:`ZCU102 <quickstart/zynqmp>`
- :doc:`ZC706 <quickstart/zynq>`
- :doc:`ZedBoard <quickstart/zed>`

Here is an example of IIO Oscilloscope connected to a no-OS Navassa IIOD demo
with electrical loopbacks between TX1-RX1 and TX2-RX2.

.. figure:: navassa-tinyiiod.jpg
   :align: center
   :width: 600

   IIO Oscilloscope connected to a no-OS ADRV9002 IIOD demo
