ADXBAND16EBZ Prototyping Platform User Guide
============================================

Quick Start Guide
-----------------

:doc:`quickbringup_guide#adxband16ebz_quick_start_guide </wiki-migration/resources/eval/user-guides/quickbringup_guide>`

Product Details
---------------

The Triton Quad-Apollo System Development Platform contains four :adi:`AD9084` software defined, direct X-Band Quad-MxFE, as well as associated RF front-ends, clocking, and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a **16 transmit/16 receive channel** direct X-Band sampling phased array at L/S/C/X-Band (0.1 GHz to ~12GHz). The Rx & Tx RF front-end has drop-in configurations that allow for customized frequency ranges up to Ku-Band (12-18GHz), depending on the end user’s application.

The ADXBAND16EBZ System Development Platform highlights a complete system solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms. The system is designed to mate with a `VCU118 <https://www.xilinx.com/VCU118>`__ Evaluation Board from Xilinx®, which features the Virtex® UltraScale+™ XCVU9P FPGA, with provided reference software, HDL code, and MATLAB system-level interfacing.

In addition to the ADXBAND16EBZ Digitizing Card, the kit also contains a 16Tx/16Rx Calibration Board that is used to develop system-level calibration algorithms, or otherwise more easily demonstrate power-up phase determinism in situations pertinent to their own use case. The Calibration Board also allows the user to demonstrate combined-channel dynamic range, spurious, and phase noise improvements and can also be controlled via MATLAB add-on when connected to the PMOD interface of the `VCU118 <https://www.xilinx.com/VCU118>`__.

The system can be used to enable quick time-to-market development programs for applications like:

-  ADEF (Phased-Array, RADAR, EW, SATCOM)
-  Communications Infrastructure (Multiband 5G and mmWave 5G)
-  Electronic Test and Measurement

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_revb_populated_top_shopped.png
   :align: center

Video Demo
----------

`04_adi-ims2023_ringwood_direct_x-band_sampling_540p\_.mp4 <https://wiki.analog.com/_media/resources/eval/user-guides/04_adi-ims2023_ringwood_direct_x-band_sampling_540p_.mp4>`__

--------------

Features
--------

-  Multi-channel, wideband system development platform for the :adi:`AD9084` :adi:`ad9084.html <en/products/ad9084.html>`
-  Mates with Xilinx `VCU118 <https://www.xilinx.com/VCU118>`__ Evaluation Board (Not Included)
-  16x RF Receive (Rx) Channels (32x Digital Rx Channels)

   -  Total 16x 4GSPS to 20GSPS ADC
   -  48x Digital Down Converters (DDCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
   -  16x Programmable Finite Impulse Response Filters (pFIRs)

-  16x RF Transmit (Tx) Channels (32x Digital Tx Channels)

   -  Total 16x 4GSPS to 28GSPS DAC
   -  48x Digital Up Converters (DUCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)

-  Flexible Rx & Tx RF Front-Ends

   -  Rx: Filtering, Amplification, Digital Step Attenuation for Gain Control
   -  Tx: Filtering, Amplification

-  Multiple System Control and Analysis Tools

   -  IIO Oscilloscope GUI
   -  MATLAB Add-Ons & Example Scripts
   -  HDL and Embedded Software Solutions for JESD204B/JESD204C Bring-Up

-  Provided Application-Specific Examples

   -  Multi-Chip Synchronization for Power-Up Phase Determinism
   -  System-Level Amplitude/Phase Alignment Using NCOs
   -  Low-Latency ADC-to-DAC Loopback Bypassing JESD Interface
   -  pFIR Control for Broadband Channel-to-Channel Amplitude/Phase Alignment
   -  Fast-Frequency Hopping

-  On-Board Power Regulation from Single 12V Power Adapter (Included)
-  315-Watt Max Power Consumption
-  Flexible Clock Distribution
-  Single-ended 400MHz (0dBm) Clock Reference input required ADF4382 (4x) Reference Clock Distribution
-  Support for External Converter Clock
-  High channel density in X-Band Lattice Spacing Form Factor
-  SYSREF Distribution for Multi-Chip Synchronization
-  Multiple Frequency Bands (12.8GSPS)
-  8 – 12GHz Rx/ 8 – 12GHz Tx (ADXBAND16EBZ, 4x AD9084)
-  Ethernet & USB Interfaces

--------------

General Description
-------------------

This user guide serves as the main source of information for system engineers and software developers using the ADXBAND16EBZ System Evaluation Board, which contains four :adi:`AD9084` software defined, direct X-Band Sampling Phased Array Development Platform, as well as associated RF front-end, clocking, and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a 16 transmit/16 receive channel direct X-Band sampling phased array at L/S/C/X-Band (0.1 GHz to ~12GHz). The Rx RF front-end has by-pass configurations that allow for customized frequency ranges up to Ku-band, depending on the end user’s application.

The ADXBAND16EBZ System Evaluation Board highlights a complete system solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as implementation of system level calibrations, beam forming algorithms, and other signal processing algorithms. The board is designed to mate with a `VCU118 <https://www.xilinx.com/VCU118>`__ Evaluation Board from Xilinx®, which features the Virtex® UltraScale+™ XCVU9P FPGA, with provided reference software and HDL code.

High-Level Block Diagram
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/block_diagram_hires.png
   :align: center

System Integration
~~~~~~~~~~~~~~~~~~

Below is the full integrated system including the VCU118, ADXBAND16EBZ, and ADXBAND16EBZ-CAL in full operation.

Key Components Locations
~~~~~~~~~~~~~~~~~~~~~~~~

Key components highlighted within the Triton system


|image1|

Calibration Board
~~~~~~~~~~~~~~~~~

ADXBAND16EBZ-CAL Digitizing Card Key Features:

• Provides both individual adjacent channel loopback and combined channel loopback options

• Combined Tx and Rx channels output via SMPM connectors

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_calibration_board.jpg
   :width: 600px

Triton Signal Chain
~~~~~~~~~~~~~~~~~~~

|image2| |image3|

--------------

Multi-Chip Synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~

A 4-step process allows single clock synchronization across dozens of channels using a tree fan-out architecture for bi-directional SYSREF

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_clocktree_revb1-scrubbed_revb.png
   :align: center

--------------

Combined Channel Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combining 16 Tx channels after phase alignment improves Power Magnitude ~23dBm with SFDR improving by ~18dB

Combining 16 Rx channels after phase alignment improves NSD performance ~12dB with SFDR improving by >11dB

|image4| |image5|

Publications
~~~~~~~~~~~~

-  Prior Generation Quad MxFE: :adi:`Power-Up Phase Determinism Using Multichip Synchronization Features in Integrated Wideband DACs and ADCs <en/technical-articles/power-up-phase-determinism-using-multichip-synchronization.html>`
-  :adi:`Integrated Hardened DSP on DAC/ADC ICs Improves Wideband Multichannel Systems <en/technical-articles/integrated-hardened-dsp-on-dac-adc-ics-improves-wideband-multichannel-systems.html>`

Related Part Pages
~~~~~~~~~~~~~~~~~~

AD9084
^^^^^^

-  :adi:`AD9084 </en/products/ad9084.html>`

ADF4382A
^^^^^^^^

-  :adi:`ADF4382A </en/products/ADF4382A.html>`

ADL8102
^^^^^^^

-  :adi:`ADL8102 </en/products/ADL8102.html>`

ADL8100
^^^^^^^

-  :adi:`ADL8100 </en/products/ADL8100.html>`

ADMV8913
^^^^^^^^

-  :adi:`ADMV8913 </en/products/ADMV8913.html>`

ADRF5730
^^^^^^^^

-  :adi:`ADRF5730 </en/products/ADRF5730.html>`

ADF4351
^^^^^^^

-  :adi:`ADF4351 </en/products/ADF4351.html>`

LTC6953
^^^^^^^

-  :adi:`LTC6953 </en/products/LTC6953.html>`

LTC6952
^^^^^^^

-  :adi:`LTC6952 </en/products/LTC6952.html>`

LT8627SP
^^^^^^^^

-  :adi:`LT8627SP </en/products/LT8627SP.html>`

LTM8060
^^^^^^^

-  :adi:`LTM8060 </en/products/LTM8060.html>`

LTM4709
^^^^^^^

-  :adi:`LTM4709 </en/products/LTM4709.html>`

LTM8074
^^^^^^^

-  :adi:`LTM8074 </en/products/LTM8074.html>`

FPGA Evaluation Board Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Xilinx Virtex UltraScale+ FPGA VCU118 <https://www.xilinx.com//products/boards-and-kits/vcu118.html>`__

--------------

Questions
---------

For additional questions or support, please visit the Engineering Zone forum at :ez:`adef`.

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_revb_populated_top_partition.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_bd_generic_adc.png
   :width: 1000px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_bd_generic_dac.png
   :width: 1000px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_sig_tx_performance.png
   :width: 1000px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/triton_rx_sig_performance.png
   :width: 1000px
