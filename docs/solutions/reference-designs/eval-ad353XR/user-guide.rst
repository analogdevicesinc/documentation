.. _eval-ad353xr user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. todo::

   Add detailed hardware configuration steps once hardware is available.
   Include jumper/link settings from the user guides (UG-2276 / UG-2320)
   and confirm with hardware owner.

The :adi:`EVAL-AD3530R` and :adi:`EVAL-AD3531R` evaluation boards expose an
SPI interface and GPIO signals that connect to the FPGA carrier. The tables
below list the signal mapping for each supported carrier.

Carrier-specific setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**CoraZ7s**

Place a jumper on JP2, shorting the two pins together. Select the JP3
connection depending on the power supply source (USB or external).

.. todo::

   Add photo of CoraZ7s hardware configuration.

**DE10-Nano**

Adjust the switch to FPGA configuration mode.

.. todo::

   Add photo of DE10-Nano switch configuration.

**ZedBoard**

Set jumpers MIO[6:2] to ``01100``. VADJ must be set to **2.5 V**.
The ZedBoard FMC connector is low pin count.

.. todo::

   Add photo of ZedBoard jumper configuration.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board operates from a single **2.7 V to 5.5 V** supply.
Power can be provided via the USB-C connector, the terminal block, or
through the SDP-K1 controller board.

Schematic, PCB layout, bill of materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design support files for the evaluation boards are available on the
respective product pages:

- :adi:`EVAL-AD3530R`
- :adi:`EVAL-AD3531R`

Software guide
-------------------------------------------------------------------------------

The evaluation board is controlled via the Linux IIO subsystem using
the SPI engine Linux driver:

- :dokuwiki:`SPI Engine Linux driver
  <resources/tools-software/linux-drivers/spi-engine>`

Once the system has booted, IIO-based tools can be used to interact with
the device:

- :doc:`IIO Oscilloscope </software/iio-oscilloscope/index>`

.. todo::

   Add devicetree and Linux driver configuration details once confirmed
   with the hardware owner. Include example IIO sysfs commands for setting
   DAC output voltages on each channel.
