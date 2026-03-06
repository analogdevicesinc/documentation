X-Band Phased Array Development Platform User Guide
===================================================

Product Details
---------------

The :adi:`X-Band Development Platform <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/x-band-development-platform.html>` contains one :adi:`AD9081-FMCA-EBZ <eval-ad9081>` AD9081 MxFE Evaluation Board, one :doc:`ADXUD1AEBZ </wiki-migration/resources/eval/user-guides/xud1a>` X/C Band Up/Down Converter, and one :doc:`ADAR1000EVAL1Z </wiki-migration/resources/eval/user-guides/stingray>` X/Ku-Band Analog Beamforming Board. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a X Band 32 transmit/32 receive channel hybrid beamforming phased array.

The X-Band Development Platform highlights a complete system solution. It is intended as a testbed for demonstrating hybrid beamforming phased array radar as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms. The system is designed to mate with a `ZCU102 <https://www.xilinx.com/ZCU102>`__ Evaluation Board from Xilinx®, featuring the Zynq® UltraScale+™ ZU9EG FPGA, with provided reference software, HDL code, and MATLAB system-level interfacing.

The system can be used to enable quick time-to-market development programs for applications like:

-  ADEF (Phased-Array, RADAR, EW, SATCOM)
-  Hybrid Beamforming
-  Electronic Test and Measurement

.. image:: https://wiki.analog.com/_media/analogTV>6186691801001
   :alt: analogTV>6186691801001

--------------

Features
--------

ADAR1000EVAL1Z (Stingray) X/Ku Phased Array Proto-typing Board

-  32 Channel Analog Phased Array Prototyping Platform
-  8x ADAR1000 Analog Phased Array Beamforming ICs
-  32x ADTR1107 Transmit/Receive ICs
-  RF In, RF Out Design
-  Individual RFIO for each BFIC
-  10 GHz Lattice Spacing
-  Stand-Alone RF Detector/ADC Combo for Calibration
-  PMOD and SDP Connectors for Programming
-  On-Board Power Regulation from Single 12V Power Adapter (Included)

ADXUD1AEBZ X/C Band Up/Down Converter

-  X Band (RF) to C Band (IF) up/down converter
-  4 TX/RX RF Input/Output via SMA
-  4 TX IF Inputs via SMPM
-  4 RX IF Output via SMPM
-  External LO or Internal PLL Options
-  PMOD Connector for Programming
-  Interposer Board via PMOD to allow SDP and FMC Connectors for Programming
-  On-Board Power Regulation from Single 12V Power Adapter (Included)

AD9081-FMCA-EBZ MxFE Evaluation Board

-  Mates with Xilinx ZCU102 Evaluation Board (Not Included)

   -  On-Board Power Regulation Powered by ZCU102 Evaluation Board via FMC Connector

-  4x RF Receive (Rx) Channels (8x Digital Rx Channels)
-  Total 4x 12-bit 4GSPS ADC
-  8x Digital Down Converters (DDCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
-  8x Programmable Finite Impulse Response Filters (pFIRs)
-  4x RF Transmit (Tx) Channels (8x Digital Tx Channels)
-  Total 4x 16-bit 12GSPS DAC
-  8x Digital Up Converters (DUCs), Each Including Complex Numerically-Controlled Oscillators (NCOs)
-  Flexible Clock Distribution

   -   On-Board Clock Distribution from Single External 100MHz Reference
   -   Support for External Converter Clock

--------------

General Description
===================

This user guide serves as the main source of information for system engineers and software developers using the X-Band Phased Array Development Platform. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a 32-channel transmit/32 receive hybrid beamforming phased array phased array at X-Band (8 GHz to 12 GHz).

The system platform highlights a complete system solution. It is intended as a testbed for demonstrating phased array system level calibrations, hybrid beam forming (analog/digital) algorithms, and other signal processing algorithms. The board is designed to mate with a `ZCU102 <https://www.xilinx.com/ZCU102>`__ Evaluation Board from Xilinx®, which features the Zynq® UltraScale+™ ZU9EG FPGA, with provided reference software and HDL code.


|1000|

.. container:: centeralign

   \ **Figure 1: High Level Block Diagram**\


--------------

User Resources
==============

Hardware
--------

-  :doc:`Hardware </wiki-migration/resources/eval/user-guides/x-band-platform/hardware>`

Software
--------

-  :doc:`Software </wiki-migration/resources/eval/user-guides/x-band-platform/software>`

--------------

Related Documents
=================

Publications
~~~~~~~~~~~~

-  :adi:`Hybrid Beamforming Receiver Dynamic Range Theory to Practice <en/technical-articles/hybrid-beamforming-receiver-dynamic-range.html>`
-  :adi:`Hybrid Beamforming Transmit Calibration with SFDR Optimization <en/resources/technical-articles/hybrid-beamforming-transmit-calibration-with-sfdr-optimization.html>`
-  :adi:`Over-the-Air Pattern Measurements for Hybrid Beamforming Phased Array <en/resources/technical-articles/over-the-air-pattern-measurements-for-hybrid-beamforming-phased-array.html>`

Related Part Pages
~~~~~~~~~~~~~~~~~~

MxFE
^^^^

-  :adi:`AD9081 </en/products/ad9081.html>`
-  :doc:`AD9081/AD9082 Zynq UltraScale+ MPSoC ZCU102 Quick Start Guide </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/quickstart/zynqmp>`
-  :adi:`UG-1578 User Guide </media/en/technical-documentation/user-guides/ad9081-ad9082-ug-1578.pdf>`

ADXUD1AEBZ
^^^^^^^^^^

-  :doc:`ADXUD1AEBZ </wiki-migration/resources/eval/user-guides/xud1a>`

ADAR1000EVAL1Z
^^^^^^^^^^^^^^

-  :doc:`ADAR1000EVAL1Z </wiki-migration/resources/eval/user-guides/stingray>`

FPGA Evaluation Board Hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  `Zynq UltraScale+ FPGA ZCU102 <https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html>`__

--------------

Support
=======

For additional questions or support, please visit the Engineering Zone forum at :ez:`ADEF <adef-system-platforms>`.

--------------

.. |1000| image:: https://wiki.analog.com/_media/resources/eval/user-guides/xbdp-wiki-system-block-diagram.png
