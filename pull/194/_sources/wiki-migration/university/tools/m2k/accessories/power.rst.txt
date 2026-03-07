ADALM2000 Power Booster Board
=============================

The AD-M2KPWR-EBZ is an ADALM2000 add-on board which increases the output current capability up to 700mA. This board can be also used as a standalone benchtop power supply with positive and negative outputs.

|image1| |image2|

Figure 1. AD-M2KPWR-EBZ Top view and bottom view

Features
--------

-  ADALM2000 compatible
-  USB Type-C powered (no Power Delivery included)
-  Provides two outputs with increased current sourcing capabilities

Description
-----------

The AD-M2KPWR-EBZ is a USB Type C powered board capable to increase the output current of ADALM2000’s power supplies.

**Inputs**:

-  USB type C : 4 – 18 V (validated with RPI USB-C power supply - not provided in the kit), 15W (power supply permitting)
-  External (screw terminal connector): 4–18V; 20W (power supply permitting)

**Outputs**: (2 control modes)

-  Two variable power supplies that track M2K user supplies:
-  0V to 5V (400mA in USB power mode)
-  -5V to 0V (400mA in USB power mode)
-  Two independent variable power supplies, adjusted by potentiometers
-  1.5V to 15V (up to 700mA if powered with 18V)

-  -15V to -1.5V (up to 700mA if powered with 18V)

Applications
~~~~~~~~~~~~

-  General-purpose electronic systems
-  Educational applications
-  Automated test equipment

Package contents
----------------

-  AD-M2KPWR-EBZ
-  Standoffs and screws

.. image:: https://wiki.analog.com/_media/university/tools/m2k/accessories/ad-m2kpwr-ebz-angle-web.png
   :width: 600px

Figure 2. AD-M2KPWR-EBZ Isometric view - Package contents

Getting started
---------------

AD-M2KPWR-EBZ must be supplied either from a 5.1V 3A USB Type C power adapter or from a lab supply using the screw terminal connector. Make sure that the jumper on the P2 connector is on the position corresponding to the chosen supply:

.. container:: centeralign

   \ |image3|\


.. container:: centeralign

   Figure 3. AD-M2KPWR-EBZ supply select jumper


================== ===================================
P2                 Selected supply method
================== ===================================
Jumper 1-2 shorted Vext - for external lab supply
Jumper 2-3 shorted Vusb - for USB Type C power adapter
================== ===================================

.. container:: centeralign

   Figure 4.AD-M2KPWR-EBZ connected to ADALM2000 and USB Type C supply


M2K and POT modes
~~~~~~~~~~~~~~~~~

In M2K mode the board is plugged into ADALM2000. After that, the programable user supplies of ADALM2000 can be used as usual, but they will source more current. The jumper on the connector P7 must be in M2K- position and the jumper on the connector P6 must be in M2K+ position.

.. container:: centeralign


   ..

|image4|

.. container:: centeralign

   Figure 5. AD-M2KPWR-EBZ POT/M2K mode setup jumpers


================== =============================== =============
P6                 Output voltage                  
================== =============================== =============
Jumper 1-2 shorted Positive supply adjusted by R20 ( 1.5 -> 15V)
Jumper 2-3 shorted Positive supply of M2K          ( 0V-> 5V)
================== =============================== =============

================== =============================== =================
P7                 Output voltage                  
================== =============================== =================
Jumper 1-2 shorted Negative supply adjusted by R19 ( -15V -> -1.5V )
Jumper 2-3 shorted Negative supply of M2K          ( -5V -> 0V)
================== =============================== =================

In POT mode the board can be used as a standalone benchtop power supply. The output voltage is adjusted with potentiometers R19 and R20. The output voltage will be available at the same pins: V+ and V-.

Gain
~~~~

The board can be adjusted such as the output voltage is double or triple than the value set from the M2K. This feature is only available in M2K mode, and it is activated by soldering or desoldering the solderjumpers on the bottom of the board according to the table. You can find the table with the soldering instructions on the bottom of the board.

Schematics and CAD Files
~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   ::
   
      *[[https://wiki.analog.com/_media/university/tools/m2k/accessories/02-065173-01-b.pdf|Rev B Schematics]]
      *[[https://wiki.analog.com/_media/university/tools/m2k/accessories/09-065173-01b.zip|Rev B Gerbers]]
      *[[https://wiki.analog.com/_media/university/tools/m2k/accessories/20-065173-01b.zip|Rev B Cadence Project]]
   


.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/accessories/ad-m2kpwr-ebz-top-web.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/accessories/ad-m2kpwr-ebz-bottom-web.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/accessories/m2kpwr_supply_jumper.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/accessories/m2kpwr_pot_control.png
   :width: 600px
