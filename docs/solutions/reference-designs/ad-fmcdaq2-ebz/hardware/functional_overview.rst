.. _ad-fmcdaq2-ebz functional_overview:

AD-FMCDAQ2-EBZ (Rev E) Functional Overview
============================================

A functional block diagram of the system is given below. The
system consists of four functional partitions - transmit path, receive path,
clocking and power supply.

.. figure:: 220307_fmcdaq2_block_diagram.jpg
   :alt: AD-FMCDAQ2-EBZ Block Diagram

   AD-FMCDAQ2-EBZ Block Diagram

Transmit
--------

Key component:

.. list-table::
   :header-rows: 0
   :widths: 30 70

   * - :adi:`AD9144`
     - Quad, 16-Bit, 2800 MSPS, TxDAC+ Digital-to-Analog JESD204B Converter
       with offset, phase and gain compensation.

The reference design generates the signals for AD9144 either from an internal
DDS or external memory (via DMA). The internal DDS consists of four independent
signal generators with programmable phase offset and frequency. These four
signal generators are paired to create two tones that are interleaved and driven
to the DAC.

Receive
-------

Key component:

.. list-table::
   :header-rows: 0
   :widths: 30 70

   * - :adi:`AD9680`
     - 14-Bit, 1000 MSPS, Dual Analog-to-Digital JESD204B Converter (ADC).

The reference design transfers the received data to DDR via DMA. An optional
off-line FFT core may be used to generate a spectrum plot.

Clocking
--------

Key component:

.. list-table::
   :header-rows: 0
   :widths: 30 70

   * - :adi:`AD9523-1`
     - Low Jitter Clock Generator (1 MHz to 1 GHz) with 14 Outputs.

The system is clocked through an on board crystal (125 MHz). The clock path
mainly consists the :adi:`AD9523-1` which upconverts this
signal to ~3 GHz, and then divides this back down to any integer divider of this
~3 GHz output.

The default reference design that ADI provides does the following:

- Crystal generates a fixed clock frequency of 125 MHz.
- This clock is sent to the AD9523-1.
- The AD9523 takes this, and creates:

  - 1000 MHz for the DAC sample rate
  - 1000 MHz for the ADC sample rate
  - 500 MHz for the reference clocks to FPGA

These clocks can be changed, but the key thing to remember is that the AD9523-1
drives both the ADC and DAC. The AD9523-1 has two clock banks (see figure 1 in
the datasheet), Bank 0: 0-3 & 10-13, and Bank 1: 4-9. The outputs on the
different banks need to be integer multiples of each other. The best thing to do
if you are interested in the details of this, is to get the :adi:`Eval board
software`, and play with the different settings (you
don't need a demo board connected to run the software).

Power
-----

The system-level power tree .ltp3 file simulated in
`LTpowerPlanner <https://www.analog.com/en/design-center/ltpowercad.html>`__ is
given below.

Key components:

.. list-table::
   :header-rows: 0
   :widths: 30 70

   * - :adi:`ADP2384`
     - 4A, 20V step-down switcher.
   * - :adi:`ADP7104`
     - High accuracy, 500 mA LDO
   * - :adi:`ADP150`
     - Ultra low noise, 150/200 mA LDO
   * - :adi:`ADP1740`
     - Low VIN, 2A LDO
   * - :adi:`ADP1741`
     - Low VIN, 2A LDO
   * - :adi:`ADP1755`
     - Low VIN, 1.2A LDO

The board receives all the power from the FPGA board through FMC.

The monitoring function of board's DC voltages is accomplished using
:adi:`AD7291` SAR ADC. The block diagram of the ADC and the
corresponding monitored voltages is shown below.

.. figure:: 220307_fmcdaq2_monitoring_adc.jpg
   :alt: AD7291 Monitoring ADC

   AD7291 Monitoring ADC

**VADJ** pin from FMC connector is used for supplying the translators VCCA
voltage. Supported voltage values of this pin are: 1.2V/1.5V/1.8V/2.5V/3.3V.

For differential to single-ended conversion and for minimizing 2nd harmonic
distortion in transmitting and receiving, a double-balun configuration is used
for TX and RX as front-end interface. More topology detail and information about
the front-end design insights are presented in the following articles:

1. `"Wideband A/D Converter Front-End Design Considerations: When to Use a
   Double Transformer Configuration" by Rob Reeder and Ramya
   Ramachandran <https://www.analog.com/en/analog-dialogue/articles/wideband-a-d-converter-front-end-design-considerations.html>`__
2. `"Ask The Application Engineer -- 36: Wideband A/D Converter Front-End
   Design Considerations II: Amplifier-or Transformer Drive for the ADC?" by
   Rob Reeder and Jim
   Caserta <https://www.analog.com/en/analog-dialogue/articles/wideband-adc-design-considerations-2.html>`__
3. `"Transformer-Coupled Front-End for Wideband A/D Converters" by Rob
   Reeder <https://www.analog.com/en/analog-dialogue/articles/transformer-coupled-front-end-a-d-converters.html>`__
