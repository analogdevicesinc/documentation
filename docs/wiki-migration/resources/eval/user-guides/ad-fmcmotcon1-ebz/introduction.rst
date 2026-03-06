ADI FMC Motor Drive System Introduction
=======================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



**The ADI FMC motor drive solution solution consist of the following products**

-  :doc:`AD-FMCMOTCON1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_board>` - Controller board. Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors.
-  :doc:`AD-DRVLV1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>` - Low voltage drive board. Connects to the Controller board and has a power stage that can drive drive Brushed DC / BLDC / PMSM / Stepper motors up to 48V and 18A.
-  :doc:`AD-DYNO1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno>` - Dynamometer drive system. Acts as an electronically adjustable load with two BLDC motors connected in a dyno setup.

=================== =============== ==============
AD-FMCMOTCON1-EBZ   AD-DRVLV1-EBZ   AD-DYNO1-EBZ
=================== =============== ==============
|AD-FMCMOTCON1-EBZ| |AD-DRVLV1-EBZ| |AD-DYNO1-EBZ|
=================== =============== ==============

**Purpose**

-  Provide an efficient drive system for different types of electric motors
-  Address power and isolation challenges encountered in motor control applications
-  Provide accurate measurement of motor feedback signals
-  Achieve flexible control with FPGA/SoC interface
-  High speed industrial Ethernet interface

**Added Value**

-  Complete control solution showing how to integrate hardware for

   -  Power

      -  Isolation
      -  Measurement
      -  Control

-  Increased control flexibility due to FPGA interfacing capabilities
-  Increased versatility to be able to control different types of motors
-  Example reference designs showing how to use the control solution with Xilinx FPGAs and Simulink from Mathworks

Where to Buy
------------

.. container:: round box

   `ZYNQ Intelligent Drives Kit <http://www.em.avnet.com/en-us/design/drc/Pages/Zynq-Intelligent-Drives-Kit.aspx>`__


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#none#./
   :alt: Overview#quickstart|Quick Start Guides

.. |AD-FMCMOTCON1-EBZ| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-fmcmotcon1-ebz_top.jpg
   :width: 200px
.. |AD-DRVLV1-EBZ| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-drvlv1-ebz_top.jpg
   :width: 200px
.. |AD-DYNO1-EBZ| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz.png
   :width: 200px
