.. _eval ltc23xx prerequisites:

Prerequisites
===============================================================================

What you need depends on which evaluation path you are following. The main
path uses the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
with Linux; the alternative path uses a demonstration board with a
microcontroller for no-OS evaluation.

.. important::

   This guide focuses on :adi:`LTC2378-20` with the `ZedBoard
   <https://digilent.com/reference/programmable-logic/zedboard/start>`__ for
   Linux (the primary and most supported path) and the :adi:`DC2135A` with the
   :adi:`MAX32666FTHR` for no-OS. The setup applies to all other supported
   devices as they share the same FMC connector and pin-compatible interface.

ZedBoard
-------------------------------------------------------------------------------

Hardware prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. An LTC23xx FMC evaluation board.
#. An FPGA carrier: `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
#. A microSD card for booting Kuiper Linux
#. A Micro-USB cable for the UART console connection
#. An Ethernet cable connected to your local network
#. A signal source for the analog input (SMA connector)

Software prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ZedBoard boots Kuiper Linux from the microSD card. The following
files are required on the SD card boot partition:

- ``BOOT.BIN`` - combines the FSBL, U-Boot, and FPGA bitstream; build the
  ltc project for your device from :git-hdl:`HDL projects <projects/>`
- ``uImage`` - Linux kernel image
- ``devicetree.dtb`` - compiled device tree for the ZedBoard/LTC2378

.. note::

   Pre-built Kuiper Linux images that include the LTC2378 FMC bitstream
   are available as part of the
   :ref:`kuiper` distribution. For custom builds, see:

   :external+hdl:ref:`Build an HDL project <build_hdl>`

For visualizing captured data from the FPGA board, use one of:

#. :ref:`iio-oscilloscope` - a graphical tool for capturing and displaying IIO
   device data
#. :external+scopy:doc:`Scopy <index>` v2.0 or later (must include
   the IIO plugin)

DC2135A
-------------------------------------------------------------------------------

Hardware prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. :adi:`DC2135A` demonstration board (features the LTC2378CMS-20)
#. :adi:`MAX32666FTHR` microcontroller platform
#. USB cable to connect the :adi:`MAX32666FTHR` to the host PC
#. External ±16V power supply for the :adi:`DC2135A` analog circuitry
#. A low-noise signal source for the analog input (J4 SMA connector)
#. Jumper wires for the SPI connections between :adi:`DC2135A` and :adi:`MAX32666FTHR`

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms or microcontroller
   boards for sale or loan; obtaining them is the normal part of
   development or evaluation.

Software prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :external+no-OS:doc:`build_guide` set up on the host PC
- The ltc project for your device from :git-no-os:`no-OS projects <projects/>`
- Maxim/ADI toolchain for the :adi:`MAX32666FTHR` target
