Introduction
============

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/index.html\


This tutorial will show in a step by step manner how to use the JESD204B Interface Framework to support a high speed data acquisition system using Analog Devices open source repositories.

Prerequisites
-------------

Before going through the tutorial, it's recommended to go through the :doc:`JESD204 Interface Framework </wiki-migration/resources/fpga/peripherals/jesd204>` documentation, :doc:`DAQ2 </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>` project documentation and generic :doc:`HDL project architecture </wiki-migration/resources/fpga/docs/arch>`.

JESD204 Overview
----------------

JESD204B is a high-speed serial link for data converters between converter and logic device (FPGA/ASIC):

-  Up to 12.5 Gbps (raw data)
-  Up to 32 lanes per link
-  Handles data mapping and framing
-  Multi-chip synchronization
-  Deterministic latency

Key Aspects of JESD204 Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  8b/10b Embedded Clock

   -  DC balanced encoding which guarantees significant transition frequency for use with clock and data recovery (CDR) designs
   -  Encoding allows both data and control characters­ – control characters can be used to specify link alignment, maintenance, monitoring, etc
   -  Detection of single bit error events on the link

-  Serial Lane Alignment

   -  Using special training patterns with control characters, lanes can be aligned across a “link”
   -  Trace-to-trace tolerance may be relaxed, relative to synchronous sampling parallel LVDS designs

-  Serial Lane Maintenance/Monitoring

   -  Alignment maintained through the super-frame structure and use of specific “characters” to guarantee alignment
   -  Link quality monitored at receiver on a lane by lane basis
   -  Link established and dropped by the receiver based on error thresholds

-  Device Clock

   -  A clock signal in the system which is a harmonic of the frame rate of the data on the link. In JESD204B systems, the frame clock is no longer the master system reference.

-  SYNC~

   -  A system synchronous, active low signal from the receiver to the transmitter which denotes the state of synchronization
   -  Synchronous to the local multiframe clock (LMFC)
   -  When SYNC~ is low, the receiver and transmitter are synchronizing
   -  SYNC~ and frame clock should have similar compliance in order to ensure proper capture/transmission timing (i.e., LVDS, CMOS, CML)
   -  SYNC~ signals may be combined if multiple DACs/ADCs are involved.

-  Lane 0, … , L-1

   -  Differential lanes on the link (typically high speed CML)
   -  8B/10B code groups are transmitted MSB first/LSB last

-  SYSREF (Optional)

   -  An optional source-synchronous, high slew rate timing resolution signal responsible for resetting device clock dividers (including LMFC) to ensure deterministic latency
   -  One shot, “gapped periodic” or periodic
   -  Distributed to both ADCs/DACs and ASIC/FPGA logic devices in the system
   -  When available, SYSREF is the master timing reference in JESD204B systems since it is responsible for resetting the LMFC references

Deterministic Latency in JESD204B
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Latency can be defined as deterministic when the time from the input of the JESD204x transmitter to the output of the JESD204x receiver is consistently the same number of clock cycles. In parallel implementations, deterministic latency is rather simple – clocks are carried with the data. In serial implementations, multiple clock domains exist, which can cause nondeterminism. JESD204 and JESD204A do not contain provisions for guaranteeing deterministic latency.

JESD204B looks to address the deterministic latency issue by specifying three device subclasses:

-  Device Subclass 0 – no support for deterministic latency
-  Device Subclass 1 – deterministic latency using SYSREF (above 500 MSPS)
-  Device Subclass 2 – deterministic latency using SYNC~ (up to 500 MSPS)

JESD204 Interface Framework Overview
------------------------------------

The JESD204 Interface Framework is a system-level integrated HDL and software framework that handles system-level as well as component-level constraints and dependencies:

-  Valid operating values of a configuration settings
-  Relationship between different configuration settings
-  Constraints are propagated between connected components
-  PLL out frequency constraints will affect converter sample rate constraints and vice versa
-  Diagnostics to detect failure source.

It is an integrated framework covering the whole stack on different facets of system design:

-  Hardware: Reference and rapid prototyping systems
-  HDL: IPs for JESD204 protocol handling
-  Software: Drivers to manage clock-chips, converters and HDL
-  Components have been co-designed for improved interoperability

Key features

-  Automatic interface configuration based on application settings
-  High-level API
-  Dynamic re-configuration
-  Integration with Matlab/Simulink, Python and GNU radio

The JESD204B standard defines multiple layers, each layer being responsible for a particular function. The Analog Devices JESD204B HDL solution follows the standard here and defines 4 layers. Physical layer, link layer, transport layer and application layer. For the first three layers Analog Devices provides standard components that can be linked up to provide a full JESD204B protocol processing chain.

Depending on the FPGA and converter combinations that are being interfaced, different components can be chosen for the physical and transport layer. The FPGA defines which physical layer component should be used and the interfaced converter defines which transport layer component should be used.

The link layer component is selected based on the direction of the JESD204B link, as seen below.

The application layer is user defined and can be used to implement application specific signal processing.

JESD204B TX Chain
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204/tutorial/tx_chain.png
   :align: center

JESD204B RX Chain
~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204/tutorial/rx_chain.png
   :align: center

References
----------

:adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
