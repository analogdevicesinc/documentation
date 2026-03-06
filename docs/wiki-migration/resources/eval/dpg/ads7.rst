ADS7-V1/-V2 for High-Speed DAC Evaluation
=========================================

.. hint::

   The ADS7-V1 and ADS7-V2 platforms are used to evaluate many types of Analog Devices components and systems. The information on this page applies only to High-Speed DAC evaluation. For information on using the ADS7 with High-Speed ADC devices, please check these pages for the :doc:`ADS7-V1 </wiki-migration/resources/eval/ads7-v1>` and :doc:`ADS7-V2 </wiki-migration/resources/eval/ads7-v2>`.


The ADS7-V1 and ADS7-V2 are devices designed to support the evaluation of Analog Devices' High-Speed Digital-to-Analog Converters (DAC). The device is connected to a PC over USB, and allows a user to download a data vector into the ADS7, which is then played out to an attached DAC evaluation board at full speed.

**Please note:** *Analog Devices' pattern generators and high-speed DAC evaluation boards are designed and sold solely to support an efficient and thorough means by which to evaluate Analog Devices high speed DACs in a lab environment for a wide range of end applications. Any application or use of the pattern generators and/or high-speed DAC evaluation boards, other than specified above, will not be supported.*

This page describes the hardware of ADS7-V1 and ADS7-V2. The device can be driven from many different software applications. For more information on the software, please see the :doc:`High-Speed DAC Software Suite </wiki-migration/resources/eval/dpg/dacsoftwaresuite>` documentation.

For information on the DPG3, the predecessor to the ADS7 platforms, please see the :doc:`DPG3 page </wiki-migration/resources/eval/dpg/dpg3>`.

Ordering Code
=============

The part number for the ADS7-V1 is ADS7-V1EBZ. The part number for the ADS7-V2 is ADS7-V2EBZ.

Hardware Differences
====================

The ADS7-V1 has two FMC connectors, while the ADS7-V2 has only one. The two platforms have the same specifications per FMC connector, the ADS7-V1 simply has two of them. Most evaluations will only need the ADS7-V2.

Hardware Specifications
=======================

*Please note that not all hardware options and specifications are supported with any particular evaluation board or software package. Specifications are subject to change without notice.*

-  Converter Interfaces

   -  LVDS Interface (x2 for the ADS7-V1)

      -  32-bits
      -  Up to 1.6Gbps per bit (800MHz DDR)
      -  Same connector and pinout as :doc:`DPG3 </wiki-migration/resources/eval/dpg/dpg3>` when paired with the :adi:`DAC FMC Adapter <en/evaluation/AD-DAC-FMC/eb.html>`.

   -  High-Speed Serial Interface (x2 for the ADS7-V1) *(For JESD204 Converters)*

      -  8 Tx lanes
      -  Up to 13.1Gbps per lane

-  Memory

   -  Dual 2GB DDR3 SO-DIMM
   -  Amount of memory available for pattern download depends on various factors, including PC specifications and converter settings

-  PC Interface

   -  USB 2.0 "B" connector

-  Specified for operation at 25ºC only

.. note::

   Some PCs with early USB 3.0 *SuperSpeed* ports have been unable to communicate reliably with an ADS7. On these PCs, the standard USB 2.0 ports (without the |image1| logo) should be used with the ADS7.


Connector Pinouts
=================

The ADS7 platforms utilize the standard VITA 57.1 "FMC" connector. See the `VITA FMC page <http://www.vita.com/fmc>`__ for more information.

Other Connectors, Buttons, and Switches
=======================================

The other connectors on the board are not enabled. Do not connect anything to these connectors. Buttons and switches on the board should be left in their factory-set position.

Firmware Update
===============

The firmware of the ADS7 can be updated when new features or fixes are available. To update the firmware, click the *Advanced/Debug* button in DPGDownloader. Click the *Update* button in the Firmware section, and select the new firmware file.

On the ADS7-V1, do not interrupt the firmware update process. The unit may become inoperable and will need to be returned to Analog Devices for repair.

The ADS7-V2 has a redundant firmware feature. If a firmware update is interrupted, the unit will revert to the original factory version, and the firmware update can be performed again.

Support
=======

Please contact `DPG Support <https://wiki.analog.com/mailto/dpg.support@analog.com>`__ with any additional questions regarding the ADS7-V1/-V2 or DAC Software Suite.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/500px-usb_3.0_icon.png
   :width: 50px
