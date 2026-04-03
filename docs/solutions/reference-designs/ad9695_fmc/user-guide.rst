.. _ad9695 user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connector layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/9695_connections.png
   :width: 600
   :alt: AD9695-1300EBZ connector layout

   AD9695-1300EBZ Connector Layout

.. tip::

   For more information on Sysref (J200), see the :adi:`JESD204B Survival Guide
   <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`.

Jumper configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/9695_pins.png
   :width: 600
   :alt: Jumper connections on AD9695-1300EBZ

   Jumper Connections on AD9695-1300EBZ

Before using the evaluation board, configure the jumpers as follows:

- Jump **P307**, **P308**, **P309**, **P311**, **P304**, **P305**, **P312**,
  and **P602** (SPI Enable).
- Do **not** jump **P100** (Power Down/Standby) and **P1**.
- Jump **P401** towards the inside of the board to power the board via FMC.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AD9695-1300EBZ is powered through the FMC connector (via jumper P401) from
the FPGA carrier board. No separate power supply is required for the evaluation
board itself.

The supply domains and their nominal voltages are:

.. list-table::
   :header-rows: 1

   * - Domain
     - Jumper
     - Test Point
     - Approx. Voltage
   * - AVDD_0P9
     - P307
     - TP303
     - 0.95 V
   * - AVDD_1P8
     - P308
     - TP304
     - 1.80 V
   * - AVDD_BUF
     - P309
     - TP305
     - 2.50 V
   * - DRVDD_0P9
     - P304
     - TP301
     - 0.95 V
   * - AVDD_1P8_PLL
     - P311
     - TP306
     - 1.80 V
   * - DVDD_0P9
     - P305
     - TP302
     - 0.95 V
   * - AVDD_1P8_SPI
     - P312
     - TP307
     - 1.80 V

.. warning::

   Removing jumpers or the board while powered via FMC may damage the board
   and/or chip. Always power down before making changes.

Analog inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect a clean, low-jitter signal source to **J101** (Channel A) or **J104**
(Channel B) via coaxial cable. It is recommended to use a narrow-band
band-pass filter with 50 Ω terminations.

For the ADC sample clock, connect the **channel 9** output of the
:adi:`AD-SYNCHRONA14-EBZ <AD-SYNCHRONA14-EBZ>` to connector **P202**
(1300 MHz, 50 Ω coaxial cable, 10 dBm).

Schematic, PCB Layout, Bill of Materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design and integration files (schematic, PCB layout, BOM) are available from
the :adi:`AD9695 product page <AD9695>` under the Design Resources tab.

Helpful documents:

- :adi:`AD9695 Data Sheet <AD9695>`
- :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and
  Evaluation*

Software guide
-------------------------------------------------------------------------------

The AD9695-1300EBZ is supported through the :ref:`libiio` library on ADI
Kuiper Linux, which runs on the FPGA carrier board (ZCU102). Applications that
interface via libiio include:

- :ref:`iio-oscilloscope` — graphical waveform and spectrum analyzer
- :external+pyadi-iio:doc:`index` — Python interface

For a step-by-step walkthrough, see the :ref:`ad9695 quickstart zcu102`
guide.
