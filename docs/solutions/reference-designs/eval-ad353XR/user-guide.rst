.. _eval-ad353xr user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD3530R` and :adi:`EVAL-AD3531R` evaluation boards expose an
SPI interface and GPIO signals that connect to the FPGA carrier. The tables
below list the signal mapping for each supported carrier.

Carrier-specific setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**CoraZ7s**

Place a jumper on JP2, shorting the two pins together. Select the JP3
connection depending on the power supply source (USB or external).

.. figure:: images/full_set_up_cora.jpeg
   :alt: Full setup - CoraZ7s with EVAL-AD3530R connected
   :width: 700

   CoraZ7s with EVAL-AD3530R

**DE10-Nano**

Adjust the FPGA configuration mode switch (SW10) to the SD card boot
position.

.. figure:: images/de10_nano_setup.jpeg
   :alt: DE10-Nano with EVAL-AD3530R connected via GPIO header
   :width: 700

   DE10-Nano with EVAL-AD3530R

**ZedBoard**

Set jumpers MIO[6:2] to ``01100``. VADJ must be set to **2.5 V**.
The ZedBoard FMC connector is low pin count.

.. figure:: images/zed_board_setup.jpeg
   :alt: ZedBoard with connections
   :width: 700

   ZedBoard with connections

.. figure:: images/ad353xr_setup.jpeg
   :alt: EVAL-AD3530R evaluation board on ZedBoard setup
   :width: 700

   EVAL-AD3530R evaluation board

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

Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD3530R/AD3531R is supported by the Linux IIO subsystem via the
``ad3530r`` driver.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - File
     - Link
   * - Driver
     - :git-linux:`drivers/iio/dac/ad3530r.c <64ec98ac2413d592e484d4cb206fbca93c419693:drivers/iio/dac/ad3530r.c>`
   * - DT bindings
     - :git-linux:`Documentation/devicetree/bindings/iio/dac/adi,ad3530r.yaml <main:Documentation/devicetree/bindings/iio/dac/adi,ad3530r.yaml>`

Once the system has booted, IIO-based tools can be used to interact with
the device:

- :ref:`iio-oscilloscope`
