JESD204B Glossary
=================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/index.html\


Control characters
------------------

======= ===== =====================================================
**/R/** K28.0 Initial lane alignment sequence multi-frame start.
**/A/** K28.3 Lane alignment
**/Q/** K28.4 Initial lane alignment sequence configuration marker.
**/K/** K28.5 Code group synchronization.
**/F/** K28.7 Frame synchronization.
======= ===== =====================================================

Abbreviations
-------------

========= =========================================
**CGS**   Code Group Synchronization
**ILAS**  Initial Lane Alignment Sequence
**LMFC**  Local Multi Frame Clock
**LEMC**  Local Extended Multiblock Clock
**MCDA**  Multiple Converter Device Alignment
**NMCDA** No Multiple Converter Device Alignment
**RBD**   RX Buffer Delay
**EMB**   Extended Multiblock
**EoMB**  End-of-multiblock sequence (00001)
**EoEMB** End of extended multiblock identifier bit
========= =========================================

Link parameters
---------------

====== ===============================================
**L**  Lane Count
**M**  Converter Count
**F**  Octets per Frame per Lane
**S**  Samples per Converter per Frame
**NP** Total Number of Bits per Sample
**N**  Converter Resolution
**K**  Frames per Multiframe
**HD** High Density User Data Format
**E**  Number of multiblocks in an extended multiblock
====== ===============================================

Clocks
------

+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **character clock**  | Clock with which 8b10b characters and octets are generated.                                                                                                                                                         |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **conversion clock** | Clock used by a converter device to perform the A2D or D2A conversion.                                                                                                                                              |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **link clock**       | Link parallel clock feeding the link layer, lane rate / 40 or lane rate / 80 for 204B links, lane rate / 66 for 204C 64b66b links                                                                                   |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **device clock**     | Master clock supplied to the JESD204B device from which all other clock signals must be derived. In context of FPGA is an integer multiple of frame clock, used directly in link, transport and application layers. |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **frame clock**      | Clock rate at which samples are generated/processed. Has the same rate as the conversion clock, except for interpolating DACs or decimating DACs, where it is slower by the interpolation/decimation factor.        |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **line clock**       | Clock for the high-speed serial interface.                                                                                                                                                                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **local clock**      | A clock generated inside a JESD204B device.                                                                                                                                                                         |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **SYSREF clock**     | Slow clock used for cross-device synchronization purposes.                                                                                                                                                          |
+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

All clocks inside a JESD204B system must have a integer relationship.
