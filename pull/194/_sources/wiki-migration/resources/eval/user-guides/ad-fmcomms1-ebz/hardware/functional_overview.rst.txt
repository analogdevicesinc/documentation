AD-FMCOMMS1-EBZ Functional Overview
===================================


.. note::

   See `wiki/common <https://wiki.analog.com/wiki/common#retired>`_
 A functional block diagram of the system is given below. The system consists of four functional partitions - transmit path, receive path, clocking and power supply.

.. image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/ad-fmcomms1-ebz/cf_xcomm_kc705_bd.jpg
   :alt: Block diagram
   :width: 600px

Transmit
--------

| Key components:

+-----------------+--------------------------------------------------------------------------------------------------------+
| :adi:`AD9122`   | Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog Converter with offset, phase and gain compensation. |
+-----------------+--------------------------------------------------------------------------------------------------------+
| :adi:`ADL5375`  | 400 MHz to 6 GHz Broadband Quadrature Modulator.                                                       |
+-----------------+--------------------------------------------------------------------------------------------------------+
| :adi:`ADF4351`  | Wideband Synthesizer with Integrated VCO (35MHz to 4400MHz).                                           |
+-----------------+--------------------------------------------------------------------------------------------------------+
| :adi:`ADL5602`  | 50 MHz to 4.0 GHz RF/IF Gain (20dB) Block.                                                             |
+-----------------+--------------------------------------------------------------------------------------------------------+

In the transmit direction, the system converts complex I and Q signals to a corresponding RF signal. The :adi:`AD9122` DAC interpolates the data and applies a frequency translation to the baseband. The complex baseband shifts the fundamental signal away from DC where LO feed-through and images can be easily filtered and otherwise mitigated. This complex analog output from the DAC feeds an :adi:`ADL5375` quadrature modulator via an appropriate filter and matching stage where it is translated to the specified RF output frequency. This signal is then passed through an image rejection filter to an :adi:`ADL5602` for +20dB gain. The RF output power control is accomplished by adjusting the baseband data, RF outputs up to 4GHz can be synthesized in the transmit direction at power levels up to 7.5dBm.

The reference design generates the signals for AD9122 either from an internal DDS or external memory (via VDMA). The internal DDS consists of four independent signal generators with programmable phase offset and frequency. These four signal generators are paired to create two tones that are interleaved and driven to the DAC.

Receive
-------

| Key components:

+-----------------+--------------------------------------------------------------------------+
| :adi:`ADL5380`  | 400 to 6000 MHz Quadrature Demodulator, 500MHz bandwidth.                |
+-----------------+--------------------------------------------------------------------------+
| :adi:`AD8366`   | DC to 600 MHz, Dual-Digital Variable Gain ( 4.5dB to 20.5dB) Amplifiers. |
+-----------------+--------------------------------------------------------------------------+
| :adi:`AD9643`   | 14-Bit, 250 MSPS, Dual Analog-to-Digital Converter (ADC).                |
+-----------------+--------------------------------------------------------------------------+
| :adi:`ADF4351`  | Wideband Synthesizer with Integrated VCO (35MHz to 4400MHz).             |
+-----------------+--------------------------------------------------------------------------+

In the receive direction, the system converts a RF signal into complex I and Q signals. The RF signal is demodulated by the direct-conversion :adi:`ADL5380` Quadrature demodulator to a suitable complex baseband (DC to 400MHz (-3dB point)).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/adl5380_lowrange_basebandrespose.png
   :alt: RF = 400 MHz to 3 GHz, Normalized IQ Baseband Frequency Response
   :width: 400px

The resulting I and Q baseband signals are filtered and then passed to the :adi:`AD8366` DVGA, which provides up between 4.5 dB to 20.25 dB of gain. An anti-alias filter is used to remove harmonics and other out of band signals before the signal is digitized with the :adi:`AD9643`.

The reference design transfers the received data to DDR via DMA. An optional off-line FFT core may be used to generate a spectrum plot.

Clocking
--------

| Key components:

+-------------------+------------------------------------------------------------------------+
| :adi:`AD9548`     | Quad/Octal Input Network Clock Generator/Synchronizer (1Hz to 750MHz). |
+-------------------+------------------------------------------------------------------------+
| :adi:`AD9523-1`   | Low Jitter Clock Generator (1MHz to 1GHz) with 14 Outputs.             |
+-------------------+------------------------------------------------------------------------+

The system may be clocked either through the on board crystal (50MHz) or from the FPGA (through FMC). The clock path mainly consists of an :adi:`AD9548`, :adi:`AD9523-1` and two :adi:`ADF4351` for the transmit and receive LOs. When using multiple boards with external synchronization, the slave boards must use the clocks from the master board.

The :adi:`AD9548` has it's ``REFA`` inputs (in the schematic ``9548_REF_[PN]`` nets) tied to the FMC connector's ``LA_17_[PN]_CC`` pin. This allows the clock from the FPGA to provide a clock to the AD9548, which then is cleaned up (jitter is removed), and driven out on ``OUT0[PN]`` to the :adi:`AD9523-1` in ``REFB``. The AD9523 then upconverts this signal to ~3GHz, and then divides this back down to any integer dividor of this ~3GHz output.

The default reference design that ADI provides does the following:

-  FPGA generates a fixed clock frequency of 30MHz using Xilinx clock generator.
-  This 30MHz is transmitted to the AD9548.
-  This is cleaned up (from a jitter standpoint) and sent to the AD9523.
-  The AD9523 takes this, and creates:

   -  491.52 MHz for the DAC sample rate
   -  245.76 MHz for the ADC sample rate
   -  122.88 MHz for the reference clocks for the LO PLLs.

These clocks can be changed, but the key thing to remember is that the AD9523 drives both the ADC and DAC. The AD9523 has two clock banks (see figure 1 in the datasheet), Bank 0: 0-3 & 10-13, and Bank 1: 4-9. The outputs on the different banks need to be integer mutliples of eachother. The best thing to do if you are interested in the details of this, is to get the :adi:`Eval board software <EVAL-AD9523-1>`, and play with the different settings (you don't need a demo board connected to run the software).

Clock Sync
~~~~~~~~~~

It is possible to synchronize multiple boards on the same FPGA platform to the same master clock.

Power
-----

| Key components:

+-----------------+----------------------------------+
| :adi:`ADP2323`  | Dual 3A, 20V step-down switcher. |
+-----------------+----------------------------------+
| :adi:`ADP7104`  | High accuracy, 500mA LDO         |
+-----------------+----------------------------------+
| :adi:`ADP151`   | Ultra low noise, 150/200 mA LDO  |
+-----------------+----------------------------------+
| :adi:`ADP1740`  | Low VIN, 2A LDO                  |
+-----------------+----------------------------------+

The board receives all the power from the FPGA board through FMC.

Optional add-on boards
~~~~~~~~~~~~~~~~~~~~~~

While the board does have the power (+7dBm) to transmit across the room for learning purposes, if you want to drive things at a higher power level, the transmit path may be followed by an optional off board :adi:`ADL5605` 700 MHz to 1000 MHz, 1 W RF Driver Amplifier, or :adi:`ADL5606`, 1800 MHz to 2700 MHz, 1 W RF Driver Amplifier amplifier to drive the antenna for ISM based communication standards.

To increase receive sensitivity, the receive path may be driven by an optional off board :adi:`ADL5523`, which is a 400 MHz to 4000 MHz Low Noise GaAs pHEMT Amplifier. This provides high gain and low noise figure for single-down conversion IF sampling receiver architectures as well as direct-down conversion receivers.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/block_diagram.png
   :align: center
   :width: 600px

.. image:: https://wiki.analog.com/_media/navigation AD-FMCOMMS1-EBZ#none#./
   :alt: AD-FMCOMMS1-EBZ#Card Specification
