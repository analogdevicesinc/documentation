.. _eval-ad9213-dual user-guide:

User guide
===============================================================================

Hardware guide
-------------------------------------------------------------------------------

Evaluation board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./images/ad9213_dual_ebz_layout.jpeg
   :alt: AD9213-DUAL-EBZ evaluation board layout diagram
   :align: center
   :width: 600

   AD9213-DUAL-EBZ Layout

Scalable clocking architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`EVAL-AD9213-DUAL-EBZ` implements a clocking architecture designed for
multi-channel scalability. The
:adi:`ADF4377` ultra-low jitter PLL with
integrated VCO generates the sample clock, while the
:adi:`LTC6955` low jitter fanout clock buffer and
the :adi:`LTC6952` JESD204B clock generation and
distribution IC distribute clocks across both
:adi:`AD9213` converters. This architecture
supports multi-chip synchronization (MCS) at 10 GSPS and enables the
interleaved 20 GSPS operating mode.

.. figure:: ./images/ad9213_dual_ebz_scalable_architecture_diagram.jpeg
   :alt: Scalable clocking architecture diagram for the AD9213-DUAL-EBZ
   :align: center
   :width: 600

   AD9213-DUAL-EBZ Scalable Clocking Architecture

Power distribution network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ./images/ad9213_dual_ebz_power_distribution_network_diagram.jpeg
   :alt: Power distribution network diagram for the AD9213-DUAL-EBZ
   :align: center
   :width: 600

   AD9213-DUAL-EBZ Power Distribution Network

Downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 60 40
   :header-rows: 1

   * - Description
     - Download
   * - Schematic
     - :download:`02_049155d_top.pdf <./files/02_049155d_top.pdf>`
   * - Layout
     - :download:`08_049155c.zip <./files/08_049155c.zip>`
   * - BOM
     - :download:`05-049155-01-d.zip <./files/05-049155-01-d.zip>`

Software guide
-------------------------------------------------------------------------------

The :adi:`EVAL-AD9213-DUAL-EBZ` is supported through the Linux IIO subsystem
when used with the Intel Stratix 10 SX SoC Development Kit. The FPGA is
programmed via the Quartus Prime Programmer and the system boots from an
SD card containing the ADI Linux image.

Once booted, the following IIO-based tools can be used to interact with and
capture data from the device:

- :ref:`iio-oscilloscope`
- :adi:`VisualAnalog <en/resources/interactive-design-tools/visualanalog.html>`

.. esd-warning::
