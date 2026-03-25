.. _adaq8092 user-guide:

User Guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADAQ8092` uModule soldered to the :adi:`EVAL-ADAQ8092-FMCZ
<EVAL-ADAQ8092>` does not require an external supply to power up the board. It
uses the +12 V supply from the carrier board (such as ZedBoard) and activates
the on-board LDOs to provide the 3.3 V and 1.8 V supplies needed by the board.

On the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__,
configure the BOOT switches (JP7-JP11) and the MIO0 jumper (JP6) for the
desired boot mode, and set VADJ to **2.5 V** as required by the HDL project.
Refer to the :ref:`adaq8092 quickstart zed` guide for the specific jumper
positions for SD card and JTAG boot modes.

.. _adaq8092 analog-inputs:

Analog Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/analog_input_circuitry.png
   :align: center
   :width: 600

   Analog Input Circuitry of EVAL-ADAQ8092-FMCZ

The :adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>` allows the user to use either a
single-ended or differential source. For single-ended input, the user can either
use the on-board balun to drive the part differentially, or bypass it to drive
the part in single-ended mode. The input configuration is selected using jumper
settings and 0 Ohm resistor placement.

**Factory default settings (single-ended input)**

======= ==== ==============
Channel Link Location
======= ==== ==============
1       JP1  Pin 2 to Pin 3
\       JP3  Pin 2 to Pin 1
\       JP4  Pin 2 to Pin 3
2       JP2  Pin 2 to Pin 3
\       JP5  Pin 2 to Pin 1
\       JP6  Pin 2 to Pin 3
======= ==== ==============

.. note::

   With the factory default settings, the board is ready for a single-ended
   source. If using a differential source instead, install 49.9 Ohm resistors
   at R1 (Channel 1) and R3 (Channel 2) to properly balance the inputs.

**Differentially driven using the balun**

======= ==== ==============
Channel Link Location
======= ==== ==============
1       JP1  Pin 2 to Pin 1
\       JP3  Pin 2 to Pin 3
\       JP4  Pin 2 to Pin 1
2       JP2  Pin 2 to Pin 1
\       JP5  Pin 2 to Pin 3
\       JP6  Pin 2 to Pin 1
======= ==== ==============

.. note::

   When using this configuration, resistor values must also be changed to
   properly balance the impedance and maintain a gain of approximately 5.
   For Channel 1: R8 and R9 = 200 Ohm, R14 and R16 = 18.2 Ohm.
   For Channel 2: R10 and R11 = 200 Ohm, R15 and R17 = 18.2 Ohm.

Encode circuitry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/encode_circuitry.png
   :align: center
   :width: 600

   Encode Circuitry of EVAL-ADAQ8092-FMCZ

The board supports both single-ended and differential encode modes. The default
configuration uses the single-ended encode mode, which requires a CMOS level
signal. The board also provides an option to install an oscillator at Y1 as a
built-in clock source for single-ended encode mode.

When using a sinusoidal, PECL, or LVDS signal, the differential encode mode is
recommended.

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/power_circuitry.png
   :align: center
   :width: 600

   Power Circuitry of EVAL-ADAQ8092-FMCZ

The :adi:`EVAL-ADAQ8092-FMCZ <EVAL-ADAQ8092>` uses the +12 V supply from the
carrier board at pin C35 of the FMC connector. The power distribution chain is:

- **LTC4359** (U2): reverse input protection
- **LTM8074** (U4): step-down regulator, configured for 5 V output
- **LTC1673-1.8** (U3): provides VDD and OVDD supplies (1.8 V)
- **LTC1763-3.3** (VR1): provides VCC supply (3.3 V)

The VADJ voltage provided from the carrier through the FMC connector must be
set to **2.5 V**. The VADJ value can be checked in the HDL project at
:external+hdl:ref:`adaq8092_fmc`.

External supplies can also be used if some of the built-in power circuitry
requires rework.

Schematic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evaluation board schematic can be found at:

- :adi:`EVAL-ADAQ8092-FMCZ Schematic <media/en/technical-documentation/eval-board-schematic/eval-adaq8092-schematic.pdf>`
