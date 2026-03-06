ADHV4702-1 DGND Level Modification
==================================

Overview
--------

This design guide is in conjunction with the PCN of ADHV4702-1, which recommends a supply range from GND to positive supply that should be less than or equal to 175V. In this guide, the DGND level modification is discussed for applications that need a positive supply voltage of greater than 175V without compromising the set supply range on the datasheet in a positive single supply configuration. A step-by-step guide is shown for selecting and calculating the discrete parts with the help of the simulation circuit result using :adi:`LTspice <en/design-center/design-tools-and-calculators/ltspice-simulator.html>`.

--------------

Design Guide Document
---------------------

The detailed explanation of the circuit is available here: `ADHV4702-1 DGND Modification <https://wiki.analog.com/_media/resources/technical-guides/adhv4702-1_dgnd_modification.pdf>`__

--------------

Circuit Overview
----------------

.. container:: centeralign

   \ |ADHV4702-1 Schematic|\ *Figure 1. ADHV4702-1 DGND and SD pin modification circuit using external discrete parts*


.. |ADHV4702-1 Schematic| image:: https://wiki.analog.com/_media/resources/technical-guides/adhv4702-1_dgnd_modification.png
   :width: 800px
