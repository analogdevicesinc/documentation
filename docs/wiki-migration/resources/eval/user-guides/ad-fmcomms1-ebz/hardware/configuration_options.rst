AD-FMCOMMS1-EBZ Configuration Options
=====================================

.. important::

   Analog Devices uses six designations to inform our customers where a semiconductor product is in its :adi:`life cycle <en/support/customer-service-resources/sales/product-life-cycle-information.html>`. From emerging innovations to products which have been in production for twenty years, we understand that insight into life cycle status is important. Device life cycles are tracked on their individual product pages on `analog.com <adi>>`__, and should always be consulted before making any design decisions.

   
   This particular articl/edocument/design has been retired or deprecated, which means it is no longer maintained or actively updated, even though the devices themselves may be **Recommended for New Designs** or in **Production**. This page is here for historical/reference purposes only.

 There is one main configuration which needs to be made during use of the `ad-fmcomms1-ebz <https://wiki.analog.com/../../ad-fmcomms1-ebz>`__ - to use or not to use the RF section. When not using the RF section of the board, the analog interface is directly to the ADC inputs and DAC outputs. (The RF section is not powered down, so it still consumes the same amount of power).

The following "jumpers" are solder jumpers - typically three pads, where a solder blob is places across two of the pins. (This is as good as you can do for RF signals, and still have jumpers). Without these connected in either the RF or bypass direction, the inputs and outputs will be floating, and the performance will suffer... :)

.. tip::

   Don't change these very often - as the pads will wear out from the heat, and you will damage the card.


RF Enabled (default configuration)
----------------------------------

This is the default configuration option (the way it is tested and shipped). For performance characteristics when in this configuration, check the `specifications <https://wiki.analog.com/card_specification>`__ section.

Connecting the ADC RF Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will connect the differiantial input (JP1.2, JP2.2, JP3.2, JP7.2) of the AD9643 to either the SMB Header (J13, J11 via JP1.1, JP2.1, JP3.1, JP7.1) or to the output of the AD8366 (via JP1.3, JP2.3, JP3.3, JP7.3). This can be found on page 3 of the schematic.

Close Solder Jumper:


|Settings for RF Section enabled|

====== ===== ======= =====
JUMPER A (1) COM (2) B (3)
====== ===== ======= =====
JP1          X---X   
JP2    X---X         
JP3    X---X         
JP7          X---X   
====== ===== ======= =====

| 

Connecting the DAC RF Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will connect the jumpers found on page 8 of the schematic.

Close Solder Jumpers:


|image1|

====== ===== ======= =====
JUMPER A (1) COM (2) B (3)
====== ===== ======= =====
JP4    X---X         
JP5    X---X         
JP6    X---X         
JP17   X---X         
====== ===== ======= =====

| 
| -----

RF Disabled
-----------

Like mentioned above - don't do this very often (or better yet, at all) - the boards are not designed to take excess heat on these pads, and they will lift off, and destroy the functionality of the board.

The performance of the card in this configuration is shown below.

Note: that the ADC configuration does **NOT** go down to DC, due to:

-  Transformers which provide common mode adjustment.
-  Filters, which provide AC-coupling

Bypassing the ADC RF Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Close Solder Jumper:


|Settings for RF Section bypassed|

====== ===== ======= =====
JUMPER A (1) COM (2) B (3)
====== ===== ======= =====
JP1    X---X         
JP2          X---X   
JP3          X---X   
JP7    X---X         
====== ===== ======= =====

| 

Bypassing the DAC RF Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Close Solder Jumpers:


|image2|

====== ===== ======= =====
JUMPER A (1) COM (2) B (3)
====== ===== ======= =====
JP4          X---X   
JP5          X---X   
JP6          X---X   
JP17         X---X   
====== ===== ======= =====

| 

Pi Attenuators
--------------

The physical configuration of the resistors normally sets the name of the attenuator circuit, with the “pi attenuator” above being so named because in its unbalanced form it resembles the shape of the Greek letter “p” (Pi) which has two vertical bars connected at the top by a third bar forming the restiveness shape.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad-fmcomms1-ebz/hardware/pi.png
   :alt: Pi Attenuators
   :align: center
   :width: 300px

In the FMComms1 design, the input and output impedance are always equal, that is Z\ :sub:`IN` = Z\ :sub:`OUT`. In this case, it is placed in series between the signal source and the load to provide the required amount of attenuation. Various on line calculators are avalible to help determine the values of the resistors.

-  `Chemandy Electronics <http://chemandy.com/calculators/pi-attenuator-calculator.htm>`__

There are a three pi attenuators in the design:

-  Receive chain:

   -  between the *RF IN* and the balun (R62, R63, R64, page 2 of the schematic)

-  Transmit chain:

   -  between the ADL5375 modulator and the ADL5620 Amplifier (R95, R96, R97, page 10 of the schematic)
   -  between the ADL5620 Amplifier and the *RF OUT* connector (R26, R27, R29, page 10 of the schematic)

The default build of these attenuators is 0dB attenuation. (2 resistors are *Do Not Insert* and the remaining is a 0 ohm.)

.. |Settings for RF Section enabled| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/adc2.png
   :width: 200px
.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/dac1.png
   :width: 130px
.. |Settings for RF Section bypassed| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/adc1.png
   :width: 200px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/fmc/dac2.png
   :width: 130px
