Motor Control Hardware
======================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.



Hardware solutions
------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-fmcmotcon1-ebz_top.jpg
   :alt: AD-FMCMOTCON1-EBZ
   :align: right
   :width: 300px

-  :doc:`AD-FMCMOTCON1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/controller_board>` - Controller board.

   -  Compatible with all Xilinx FPGA platforms with FMC LPC or HPC connectors

      -  2 x Gbit Ethernet PHYs for high speed industrial communication
      -  Hall + Differential Hall + Encoder + Resolver interfaces
      -  Current and voltage measurement using isolated ADCs
      -  Xilinx XADC interface
      -  Fully isolated control and feedback signals

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-drvlv1-ebz_top.jpg
   :alt: AD-DRVLV1-EBZ
   :align: right
   :width: 300px

-  :doc:`AD-DRVLV1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/lv_board>` - Low voltage drive board.

   -  Connects to the Controller board and has a power stage that can drive drive Brushed DC / BLDC / PMSM / Stepper motors up to 48V and 18A.
   -  Integrated over current protection
   -  Current measurement using isolated ADCs
   -  Bus voltage, phase currents and total current analog feedback signals
   -  PGAs to maximize the current measurement input range
   -  BEMF zero cross detection for sensorless control of PMSM or BLDC motors

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz.png
   :alt: AD-DYNO1-EBZ
   :align: right
   :width: 300px

-  :doc:`AD-DYNO1-EBZ </wiki-migration/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno>` - Dynamometer Drive System.

   -  Two BLDC motors connected in a dyno setup
   -  Electronically adjustable load – the load value is set using the onboard buttons + LCD
   -  Programmable step and ramp load changes
   -  Measurement and display of load motor phase currents
   -  Measurement and display of load motor speed
   -  External control using Analog Discovery

Where to Buy
------------

.. container:: round box

   `ZYNQ Intelligent Drives Kit <http://www.em.avnet.com/en-us/design/drc/Pages/Zynq-Intelligent-Drives-Kit.aspx>`__


Downloads
---------

.. admonition:: Download
   :class: download

   **AD-FMCMOTCON1-EBZ**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_schematics.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_bom.pdf>`__
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-fmcmotcon1-ebz_layout.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.5 or higher).
   
   **AD-DRVLV1-EBZ**
   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_schematics.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_bom.pdf>`__
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/ad-drvlv1-ebz_layout.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.5 or higher).
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#quickstart
   :alt: Quick Start Guides#.:\|Overview#reference_hdl|HDL
