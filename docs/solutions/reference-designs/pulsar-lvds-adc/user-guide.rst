.. _pulsar-lvds-adc user-guide:

User guide
==========

The complete user guides for the evaluation boards can be found at:

-  :adi:`UG-745: EVAL-AD7625/EVAL-AD7626 User Guide <media/en/technical-documentation/user-guides/eval-ad7625fmcz_7626fmcz_ug-745.pdf>`
-  :adi:`UG-490: EVAL-AD7960/EVAL-AD7961 User Guide <media/en/technical-documentation/user-guides/ug-490.pdf>`

Additional documentation:

-  :adi:`AD7625 Data Sheet <media/en/technical-documentation/data-sheets/ad7625.pdf>`
-  :adi:`AD7626 Data Sheet <media/en/technical-documentation/data-sheets/ad7626.pdf>`
-  :adi:`AD7960 Data Sheet <media/en/technical-documentation/data-sheets/ad7960.pdf>`
-  :adi:`AD7961 Data Sheet <media/en/technical-documentation/data-sheets/ad7961.pdf>`

Hardware guide
--------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~

The evaluation board connects to the FPGA carrier via the FMC LPC connector.
On the
`ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__,
configure the BOOT switches (JP7-JP11) and the MIO0 jumper (JP6) for the
desired boot mode. Refer to the :ref:`pulsar-lvds-adc quickstart zed` guide
for the specific jumper positions for SD card and JTAG boot modes.

The VADJ voltage provided from the carrier through the FMC connector must be
set to **2.5 V** as specified in the HDL project at
:external+hdl:ref:`pulsar_lvds_adc`.

The HDL project parameter ``RESOLUTION_16_18N`` controls the ADC resolution
mode:

-  ``RESOLUTION_16_18N=0``: 18-bit mode (for AD7960)
-  ``RESOLUTION_16_18N=1``: 16-bit mode (for AD7625, AD7626, AD7961)

Jumper configuration — AD7625/AD7626
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following jumpers on the EVAL-AD7625/EVAL-AD7626 board must be configured:

.. list-table::
   :header-rows: 1

   - - Jumper/Solder link
     - Default Position
     - Description
   - - LK2
     - Inserted
     - REFIN to 1.2 V external reference
   - - LK3
     - Inserted
     - 4.096 V from ADR4540 after AD8031 buffer
   - - LK6
     - B
     - VCM buffer to amplifier VCM
   - - LK9
     - A
     - 7 V supply from ADP7102
   - - LK10
     - A
     - -2.5 V from ADP2300
   - - JP1, JP2
     - B
     - CNV+/CNV- from FPGA
   - - JP6
     - B
     - 7 V to amplifier +VS
   - - JP10
     - B
     - -2.5 V to amplifier -VS
   - - JP11, JP12
     - B
     - ADA4899-1 outputs to ADC inputs
   - - JP13, JP14
     - B
     - ADA4899-1 outputs to ADC inputs

Jumper configuration — AD7960/AD7961
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following jumpers on the EVAL-AD7960/EVAL-AD7961 board must be configured:

.. list-table::
   :header-rows: 1

   - - Jumper/Solder link
     - Default Position
     - Description
   - - LK2, LK3
     - Inserted
     - External amplifier supply options
   - - LK4
     - Inserted
     - +7 V from ADP7102
   - - LK5
     - B
     - -2.5 V from ADP2300
   - - LK6
     - B
     - VCM buffer to amplifier VCM
   - - LK7
     - B
     - +5 V from ADR4550 to REF buffer AD8031
   - - JP1, JP2
     - B
     - VIN+/VIN- to ADC driver inputs
   - - JP3, JP4
     - B
     - ADA4899-1 outputs to AD7960 inputs
   - - JP5
     - A
     - AD7960 VCM to AD8031
   - - JP7
     - A
     - REFIN to 2.048 V external reference
   - - JP8
     - B
     - +7 V to amplifier +VS
   - - JP9
     - B
     - -2.5 V to amplifier -VS

Power supply
~~~~~~~~~~~~

The EVAL-AD7625/EVAL-AD7626 boards derive their power from the FMC connector
and internal voltage regulators. Refer to the UG-745 user guide for the
complete power supply schematic.

The EVAL-AD7960/EVAL-AD7961 boards also derive power from the FMC connector.
The +7 V supply is generated from ADP7102 and -2.5 V from ADP2300. Refer to
the UG-490 user guide for the complete power supply schematic.

The FPGA carrier board (ZedBoard) is powered separately through its own 12 V
power input connector (J20).

Analog inputs
~~~~~~~~~~~~~

The AD7625/AD7626 are 16-bit differential input ADCs. The AD7960 is an 18-bit
differential input ADC and the AD7961 is a 16-bit differential input ADC. All
devices use charge redistribution SAR architecture.

For testing purposes, connect a signal generator to the analog inputs of the
evaluation board using the appropriate SMA connectors or jumper wires. For
optimal performance, use a low noise, low distortion signal source.

Schematic, PCB layout, bill of materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Design and layout files for the evaluation boards can be found on the product
pages:

-  :adi:`EVAL-AD7625 design files <EVAL-AD7625>`
-  :adi:`EVAL-AD7626 design files <EVAL-AD7626>`
-  :adi:`EVAL-AD7960 design files <EVAL-AD7960>`
-  :adi:`EVAL-AD7961 design files <EVAL-AD7961>`

Software guide
--------------

The evaluation boards are supported both with Linux (using the Libiio library)
and with no-OS (bare metal).

Linux
~~~~~

The AD796X IIO ADC Linux driver is available in the
:git-linux:`Analog Devices Linux repository <>`. The Libiio library is
cross-platform (Windows, Linux, Mac) with language bindings for C, C#, Python,
and others. Applications that can be used with it are:

-  :git-iio-oscilloscope:`IIO Oscilloscope <releases+>`
-  :external+scopy:doc:`Scopy <index>`

No-OS
~~~~~

For no-OS (bare metal), the AD796X driver and project source code are available
in the :git-no-OS:`Analog Devices no-OS repository <>`. Refer to the
:ref:`quickstart guide <pulsar-lvds-adc quickstart zed>` for instructions on
building and running the no-OS application.
