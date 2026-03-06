ADRV1CRR-FMC
============

Compatible cards
----------------

ADRV9361-Z7035
~~~~~~~~~~~~~~

The :doc:`ADRV9361-Z7035 </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/hardware>` will work with the FMC Carrier, and all functionality of the carrier is supported.

ADRV9364-Z7020
~~~~~~~~~~~~~~

The :doc:`ADRV9364-Z7020 </wiki-migration/resources/eval/user-guides/adrv936x_rfsom/hardware>` will work with the FMC Carrier, but not all carrier functionality is supported. The things that will work:

-  Ethernet
-  USB
-  PMOD1 and PMOD_MIO
-  PUSH BUTTON 1
-  PUSH BUTTON 2
-  PUSH BUTTON 3
-  LED 0

What cannot be used:

-  HDMI OUT
-  CAMERA
-  PMOD0 (pin 0 and 1 are connected)
-  SPF+
-  LED 1
-  LED 2
-  LED 3
-  SLIDE SWITCHES
-  PUSH BUTTON 0
-  FMC connector

Hardware
~~~~~~~~

ADRV1CRR-FMC Rev. C
^^^^^^^^^^^^^^^^^^^

::

    This is the Rev C schematic and layout files for the ADRV1CRR-FMC carrier.

.. admonition:: Download
   :class: download

   
   -  `Rev C Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/02_039799c_top.pdf>`__
   -  `Rev C BOM <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/05_039799-c.xlsx>`__
   -  `Rev C Gerbers <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/038799c.zip>`__
   -  `Rev C Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/08_039799c.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.6 or higher).
   -  `Letter of Volatility <https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/letter_of_volatility_adrv1-fmc.pdf>`__
   


Trips and Tricks
----------------

External AD9361 reference clock via J1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/pzsdr/carriers/pzsdr_ext_clk.png
   :align: center
   :width: 800px

An external Reference Clock can be supplied via J1. In order the switch the source the :git-linux:`arch/arm/boot/dts/zynq-adrv9361-z7035.dtsi` device tree needs to be modified.

::

       clocks {
           xo_40mhz_fixed_clk: clock@0 {
               #clock-cells = <0>;
               compatible = "fixed-clock";
               **clock-frequency = <40000000>;**
               clock-output-names = "XO_40MHz";
           };

           ad9361_clkin: clock@1 {
               #clock-cells = <0>;
               compatible = "gpio-gate-clock";
               clocks = <&xo_40mhz_fixed_clk>;
               **enable-gpios = <&gpio0 105 1>;** /* Set to 1 for extern AD9361_CLK */
               clock-output-names = "ad9361_ext_refclk";
           };

::

   Option:
       enable-gpios = <&gpio0 105 ACTIVE_LEVEL>;

       ACTIVE_LEVEL:
       0 (active high) use on-board XO
       1 (active low) use external clock via J1

-  Update the clock-frequency property with the exact frequency of the external supplied clock.
-  Set enable-gpios = <&gpio0 105 **1**>
-  Rebuild and install your modified device tree on the target
