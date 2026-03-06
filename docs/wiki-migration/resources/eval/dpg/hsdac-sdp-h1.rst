SDP-H1 for High-Speed DAC Evaluation
====================================

.. hint::

   The SDP-H1 platform is used to evaluate many types of Analog Devices components and systems. The information on this page applies only to High-Speed DAC evaluation.


The SDP-H1 is a device designed to support the evaluation of Analog Devices' High-Speed Digital-to-Analog Converters (DAC). The device is connected to a PC over USB, and allows a user to download a data vector into the SDP-H1, which is then played out to an attached DAC evaluation board.

**Please note:** *Analog Devices' pattern generators and high-speed DAC evaluation boards are designed and sold solely to support an efficient and thorough means by which to evaluate Analog Devices high speed DACs in a lab environment for a wide range of end applications. Any application or use of the pattern generators and/or high-speed DAC evaluation boards, other than specified above, will not be supported.*

This page describes the hardware of SDP-H1. The device can be driven from many different software applications. For more information on the software, please see the :doc:`High-Speed DAC Software Suite </wiki-migration/resources/eval/dpg/dacsoftwaresuite>` documentation.

For information on other models of DAC pattern generators, please see the :doc:`DPG page </wiki-migration/resources/eval/dpg>`.

Ordering Code
=============

The part number for the SDP-H1 is EVAL-SDP-CH1Z.

To order an SDP-H1, please visit the :adi:`SDP-H1 Ordering Page <en/system-demonstration-platform/controller-boards/evaluation/EVAL-SDP-H1/eb.html#buy>`

Hardware Specifications
=======================

*Please note that not all hardware options and specifications are supported with any particular evaluation board or software package. Specifications are subject to change without notice.*

-  Converter Interfaces

   -  CMOS Interface

      -  32-bits (shared with the P lines of the LVDS bus)
      -  Up to 300Mbps per bit(SDR)
      -  Same connector and pinout as :doc:`DPG3 </wiki-migration/resources/eval/dpg/dpg3>` when paired with the :adi:`DAC FMC Adapter <en/evaluation/AD-DAC-FMC/eb.html>`.

   -  LVDS Interface

      -  32-bits (P lines shared with CMOS interface)
      -  Up to 740Mbps per line (370MHz DDR) when used with evaluation boards with interface widths of 16 lines or less. Up to 370Mbps (185MHz DDR) when used with evaluation boards with interface widths greater than 16lines (up to a maximum of 32 lines).
      -  Same connector and pinout as :doc:`DPG3 </wiki-migration/resources/eval/dpg/dpg3>` when paired with the :adi:`DAC FMC Adapter <en/evaluation/AD-DAC-FMC/eb.html>`.

-  Memory

   -  64MB DDR2 Discrete Memory

-  PC Interface

   -  USB 2.0 "B" connector

-  Specified for operation at 25ºC only

.. note::

   Some PCs with USB 3.0 *SuperSpeed* ports have been unable to communicate reliably with the SDP-H1. On these PCs, the standard USB 2.0 ports (without the |image1| logo) should be used with the SDP-H1.


Connector Pinouts
=================

The SDP-H1 platform utilizes the standard VITA 57.1 "FMC-LPC" connector. See the `VITA FMC page <http://www.vita.com/fmc>`__ for more information.

Firmware Update
===============

The firmware of the SDP-H1 is updated automatically every time the platform is used. No user interaction is required.

Support
=======

Please contact `DPG Support <https://wiki.analog.com/mailto/dpg.support@analog.com>`__ with any additional questions regarding the DPG or DAC Software Suite.

Please contact `ACE Support <https://wiki.analog.com/mailto/ace.support@analog.com>`__ if you are using :doc:`DPG Lite </wiki-migration/resources/tools-software/ace/dpg-lite>` with :doc:`ACE </wiki-migration/resources/tools-software/ace>`.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/dpg/500px-usb_3.0_icon.png
   :width: 50px
