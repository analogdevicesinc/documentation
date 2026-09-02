.. _ad5766 user-guide:

User Guide
===============================================================================

The complete user guide of the evaluation board can be found at
:download:`EVAL-AD5766SD2Z/EVAL-AD5767SD2Z User Guide <https://www.analog.com/media/en/technical-documentation/user-guides/eval-ad5766sd2z-5767sd2z-ug-1070.pdf>`.

Hardware guide
-------------------------------------------------------------------------------

.. _ad5766 configuration:

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   - - Jumper
     - A
     - B
     - C / No Link
   - - LK1
     - EXT_3.3V
     - EXT_AVCC
     - --f
   - - LK2
     - EXT_3.3V
     - EXT_VLOGIC
     - --
   - - LK3
     - EXT_3.3V
     - EXT_AVCC
     - --
   - - LK4
     - EXT_AVDD
     - INT_AVDD
     - --
   - - LK5
     - EXT_AVSS
     - INT_AVSS
     - --
   - - LK6
     - Sequenced
     - Simultaneous
     - Manual
   - - LK7
     - ADR4525BRZ
     - EXT_VREF
     - --
   - - LK8
     - EXT_AVCC
     - DEMO_SUPPLY
     - EXT_3.3V
   - - LK9
     - 1.2MHz Switching Frequency
     - 2.4MHz Switching Frequency
     - External Clock
   - - LK10
     - Slow Slew
     - Normal Slew
     - Fast Slew
   - - LK11
     - Ground
     - --
     - --
   - - LK12
     - Ground
     - --
     - --

This table has been made for the Rev. A of the evaluation board.

For the Rev. B the following changes have been made:

- LK6, LK9, LK10 no longer the have the C position, instead those configurations
  are obtained by not connecting the jumpers at all.

- LK11 and LK12 are used to bypass the output filters.

- LK8 no longer has 3 positions, it can only be linked or not and connects the
  EN1 and EN2 pins to EXT_3.3V.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD5766/67-SD2Z<EVAL-AD5766>` evaluation board is powered through
the FMC connector. The  VADJ should be set to 2.5V.

The board supports two methods for supplying the DAC parameters (VLOGIC, VACC,
VADD, VASS, etc.):

- a single external 3.3V supply (EXT_3.3V).
- individually powered supply rails.

Refer to the :ref:`configuration table <ad5766 configuration>` for setup
instructions.

The board presents the following connectors for power supply / interface:

.. list-table::
   :header-rows: 1

   - - Connector
     - Scope
   - - J9
     - AVSS and AVDD
   - - J10
     - PMOD SPI
   - - J11
     - AVCC
   - - J12
     - 3.3V Supply
   - - J13
     - VLOGIC

Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output of the DAC can be monitored in 2 ways:

- Through one of the 16 dedicated channel outputs (VOUT1-VOUT16).
- Through the MUX_OUT connection.

.. Schematic, PCB Layout, Bill of Materials
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - :download:`Schematics<resources/ad5766_schematics.zip>`
   - :download:`PCB Layout<resources/ad5766_layouts.zip>`
   - :download:`Bill of Materials<resources/ad5766_bom.xlsx>`

Software guide
-------------------------------------------------------------------------------

The evaluation board is supported both with Linux (using the Libiio library)
and with no-OS (bare metal). The Libiio library is cross-platform (Windows,
Linux, Mac) with language bindings for C, C#, Python, and others. Applications
that can be used with it are:

-  :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
-  :external+scopy:doc:`Scopy <index>`

Python support is available through the
:external+pyadi-iio:doc:`pyadi-iio <index>` library.

Additional resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :adi:`AD5766 / AD5767 datasheet <media/en/technical-documentation/data-sheets/ad5766-5767.pdf>`
- :adi:`AN-928: Understanding High Speed DAC Testing and Evaluation  <media/en/technical-documentation/application-notes/AN-928.pdf>`
