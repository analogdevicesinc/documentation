Hardware
========

Functional Overview
-------------------

The system consists of a transmit path, receive path, clock management and
power supply.

Transmit Path
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Description
   * - :adi:`AD9162`
     - High performance, 16-bit DAC that supports data rates to 6 GSPS.
       The DAC core is based on a quad-switch architecture coupled with a
       2x interpolator filter that enables an effective DAC update rate of
       up to 12 GSPS.
   * - :adi:`ADL5240`
     - Digitally controlled variable gain amplifier (VGA) operating from
       100 MHz to 4000 MHz. Integrates a 20 dB gain amplifier with a 6-bit
       digital step attenuator with 31.5 dB control range in 0.5 dB steps.

Receive Path
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Description
   * - :adi:`AD9625`
     - 12-bit monolithic sampling ADC that operates at conversion rates of
       up to 2.6 GSPS. Designed for sampling wide bandwidth analog signals
       up to the second Nyquist zone.
   * - :adi:`HMC1119`
     - Broadband, highly accurate, 7-bit digital attenuator, operating from
       0.1 GHz to 6.0 GHz with 31.5 dB attenuation control range in
       0.25 dB steps.

Clock Management
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Description
   * - :adi:`ADF4355`
     - Fractional-N or integer-N PLL frequency synthesizer. A series of
       frequency dividers permits operation from 54 MHz to 6800 MHz with an
       integrated VCO with fundamental output from 3400 MHz to 6800 MHz.
   * - :adi:`HMC361`
     - Low noise Divide-by-2 static divider operating from DC to 10 GHz
       input frequency. Low additive SSB phase noise of -148 dBc/Hz at
       100 kHz offset.

Power Supply
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1

   * - Component
     - Description
   * - :adi:`ADM7170`
     - 6.5 V, 500 mA, ultralow noise, high PSRR, fast transient response
       CMOS LDO
   * - :adi:`ADM7150`
     - 800 mA, ultra low noise/high PSRR LDO
   * - :adi:`ADM7154`
     - 600 mA, ultralow noise, high PSRR, RF linear regulator
   * - :adi:`ADP1740`
     - 2 A, low VIN dropout, linear regulator
   * - :adi:`ADP1761`
     - 1 A, low VIN, low noise, CMOS linear regulator
   * - :adi:`ADP2370`
     - High voltage, 1.2 MHz/600 kHz, 800 mA, low quiescent current buck
       regulator
   * - :adi:`ADP5073`
     - 1.2 A, DC-to-DC inverting regulator
   * - :adi:`ADP2165`
     - 5.5 V, 5 A, high efficiency, step-down DC-to-DC regulator with
       output tracking
   * - :adi:`AD7291`
     - 8-channel, I2C, 12-bit SAR ADC with temperature sensor (power level
       monitoring)

Board Specifications
--------------------

The AD-FMCOMMS11-EBZ is a 12 layer board measuring 110 mm x 69 mm (not
including SMA connectors). The mounting holes align with the ZC706 carrier
board.

Configuration Options
---------------------

Several solder links on the board allow optional clock reference
configuration for the clock management unit, ADC and DAC.

.. list-table::
   :header-rows: 1

   * - Location
     - Device Controlled
     - Settings
     - Action
   * - JP1/JP2
     - Differential clock reference for ADF4355
     - A and COM
     - Internal clock reference
   * - JP1/JP2
     - Differential clock reference for ADF4355
     - B and COM
     - External clock reference
   * - JP22/JP5
     - Differential clock reference for DAC
     - A and COM
     - ADF4355 clock reference
   * - JP22/JP5
     - Differential clock reference for DAC
     - B and COM
     - External clock reference
   * - JP3/JP4
     - Differential clock reference for ADC
     - A and COM
     - External clock reference
   * - JP3/JP4
     - Differential clock reference for ADC
     - B and COM
     - HMC361 clock reference

Additionally, several GPO and GPIO pins are brought to connector J2 on the
bottom of the PCB. These pins allow configuration of the PA, LNA and SPDT
switch on the board.

Supported Carriers
------------------

.. list-table::
   :header-rows: 1

   * - Board
     - HDL
     - Linux
   * - :xilinx:`ZC706 <products/boards-and-kits/ek-z7-zc706-g.html>`
     - Yes
     - Yes
