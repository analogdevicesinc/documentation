Dynamometer Drive System
========================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.


   
   |Dynamometer Drive System|

Features
--------

::

   *[[http://www.anaheimautomation.com/products/brushless/brushless-motor-item.php?sID=143&pt=i&tID=96&cID=22|Two BLDC motors connected in a dyno setup (BLY171S-24V-4000 and BLY171D-24V-4000)]]\\
   * Electronically adjustable load – the load value is set using the onboard buttons + LCD
   * Programmable step and ramp load changes 
   * Measurement and display of load motor phase currents
   * Measurement and display of load motor speed
   * External control using Analog Discovery

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno_diagram.png
   :width: 800px

+---+
+---+

Key Parts
---------

+------------------------------------------------+-----------------------------------------------------------------------+
| Power                                          |                                                                       |
+================================================+=======================================================================+
| :adi:`ADuM5000`                                | isoPower® integrated isolated dc-to-dc converter                      |
+------------------------------------------------+-----------------------------------------------------------------------+
| :adi:`ADP3335`                                 | HIGH ACCURACY ULTRALOW QUIESCENT CURRENT, 500 mA, ANYCAP® LOW DROPOUT |
+------------------------------------------------+-----------------------------------------------------------------------+
| Isolation                                      |                                                                       |
+------------------------------------------------+-----------------------------------------------------------------------+
| :adi:`ADUM3223`                                | 3 KV RMS ISOLATED PRECISION HALF-BRIDGE DRIVER, 4 A OUTPUT            |
+------------------------------------------------+-----------------------------------------------------------------------+

+---+
+---+

User Guide
----------

The system is equipped with an LCD which displays information about the state of the load such and together with the 3 push buttons placed below it can be used to display and configure different system parameters. The **+/-** buttons are used to navigate through the system's menu and to change different system parameters, while the **Enter** button is used to confirm parameter changes or to enter / exit the menu screens.

+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Menu diagram | Menu description                                                                                                                                                                   |
+==============+====================================================================================================================================================================================+
| |Dyno menu|  | Main menu is displayed at power up.                                                                                                                                                |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | The measurement menu displays RMS phase currents and motor speed. The load can be adjusted by pressing the "+" or "-" buttons. In order to go back to the main menu press "Enter". |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Waveforms menu. Select ramp or step load.                                                                                                                                          |
|              | In order to go back select "..." and press "Enter"                                                                                                                                 |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Step load menu. Select "Step" to start toggling the load.                                                                                                                          |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Press "+" or "-" to toggle between the preset step values.                                                                                                                         |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Set maximum duty cycle.                                                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Set minimum duty cycle.                                                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Ramp load menu. Press "+" or "-" to change ramp period.                                                                                                                            |
|              | In order to go back press "Enter"                                                                                                                                                  |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Settings menu.                                                                                                                                                                     |
|              | In order to go back select "..." and press "Enter"                                                                                                                                 |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | Change duty cycle step.                                                                                                                                                            |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| :::          | About.                                                                                                                                                                             |
+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---+
+---+

Analog Discovery™
-----------------

In order interface the Dyno with the Analog Discovery™ USB Oscilloscope:

-  Slide switch S2 to EXT_CTRL position
-  Insert the Analog Discovery™ in P1 the connector(with the Analog Devices logo facing the user)

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/dyno_discovery_control.JPG
   :alt: Dynamometer Drive System
   :width: 400px

Two software packages are available for interfacing with Analog Discovery™:

::

   *[[http://www.digilentinc.com/Products/Detail.cfm?NavPath=2,66,849&Prod=WAVEFORMS|Digilent® WaveForms™]]\\
   *[[http://www.mathworks.co.uk/help/daq/examples/getting-started-acquiring-data-with-digilent-analog-discovery.html|MathWorks Analog Discovery toolbox ]]\\

The signals available to the Analog Discovery™ are:

=========== ======================== ===============================
Dyno Signal Analog Discovery channel Description
=========== ======================== ===============================
I_A         Scope Channel 1 Positive Phase A motor current (185mv/A)
I_B         Scope Channel 2 Positive Phase B motor current (185mv/A)
PWM1        Digital Channel 0        Phase A PWM (3.3V levels)
PWM2        Digital Channel 2        Phase B PWM (3.3V levels)
PWM3        Digital Channel 2        Phase C PWM (3.3V levels)
=========== ======================== ===============================

+---+
+---+

.. warning::

   The system needs a 5V 500mA power supply. The power connector is a 2.1 X 5.5MM jack with the center pin positive(+)


Downloads
---------

.. admonition:: Download
   :class: download

   **AD-DYNO1-EBZ**

   
   -  `Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz_schematics.pdf>`__
   -  `Bill of Materials <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz_bom.pdf>`__
   -  `Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz_layout.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.5 or higher).
   


.. image:: https://wiki.analog.com/_media/navigation AD-FMCMOTCON1-EBZ#signal_chain
   :alt: Signal Measurement Chain#..:\|Overview#none

.. |Dynamometer Drive System| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/ad-dyno1-ebz.png
   :width: 400px
.. |Dyno menu| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcmotcon1-ebz/hardware/Dyno_Menu.png
   :width: 500px
