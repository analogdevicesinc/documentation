.. _ads7-v1:

ADS7-V1EBZ High Speed Evaluation Board
===============================================================================

.. warning::

   The ADS7-V1EBZ is obsolete and no longer manufactured or supported by
   Analog Devices. All high speed ADC products previously using the ADS7-V1EBZ
   have migrated to the newer :ref:`ADS7-V2EBZ <ads7-v2>` evaluation platform.

Preface
-------------------------------------------------------------------------------

The ADS7-V1EBZ was developed to support the evaluation of Analog Devices
high speed A/D converters, D/A converters and transceivers with JESD204B bit
rates up to 12.5 Gbps. The platform supports specified Analog Devices
evaluation boards only. The ADS7-V1 is not intended to be used as a development
platform, and no support is available for standalone operation.

.. figure:: ../images/ads7-v1ebz.jpg
   :align: center
   :width: 600

   ADS7-V1EBZ Evaluation Board

Features
-------------------------------------------------------------------------------

-  Xilinx Virtex-7 XC7VX690T-FFG1761 FPGA (693,120 logic cells)
-  Two FMC-HPC connectors
-  Ten 13.1 Gbps transceivers per FMC-HPC connector
-  Two DDR3-1866 DIMMs
-  USB 2.0 interface

Using ADS7-V1EBZ for High Speed ADC Evaluation
-------------------------------------------------------------------------------

Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When used with the specified ADC evaluation boards, the ADS7-V1EBZ platform
functions as a high speed data acquisition system. The FPGA on the ADS7-V1 acts
as the data receiver, while the ADC is the data transmitter.

.. figure:: ../images/ad9680_ads7-v1ebz_setup.jpg
   :align: center
   :width: 600

   Typical ADS7-V1EBZ Evaluation Setup

Supported ADC Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a complete list of supported ADC evaluation boards, refer to the
:adi:`High Speed ADC Evaluation Boards <hsadcevalboard>` product page.
