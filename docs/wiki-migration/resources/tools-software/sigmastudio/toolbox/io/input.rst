Input
=====

| :doc:`Click here to return to the IO page </wiki-migration/resources/tools-software/sigmastudio/toolbox/io>`
| The Input block receives input from the hardware's input pins and makes it available in the schematic design.
| |inputpic1.png|

**To enable/disable an input:**

| Check the block for the input channel(s) you with to enable. Un-check the box disable an input channel. The pin will turn blue when an input is enabled and grey when disabled. The default block has two pins enabled, for stereo connection.
| |inputpic2.png|

If you have multiple DSP processors in your design, specify which DSP is associated with the input block by right-clicking and selecting Add Algorithm > IC # > DSP Type.

-  Every enabled input must be connected to an output, else there will be errors on compilation.
-  Only a single input block can be associated with a processor. You will receive an error if you attempt to add multiple inputs to a schematic.
-  To change the Input's Sampling Rate, Right-click the block name and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz):

| 
| |inputpic3.png|

Relationship Between Hardware Inputs and Input Cell Channels
------------------------------------------------------------

For SigmaDSP products that only have digital audio inputs, the routing is quite simple. Each checkbox on the input cell corresponds to one input channel. Because TDM modes can be used, the exact mapping between a hardware pin and corresponding input channels will change based on the register configuration.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/screenhunter_01_nov._29_11.20.jpg
   :alt: screenhunter_01_nov._29_11.20.jpg
   :align: center

For SigmaDSP products that contain both analog and digital inputs, the analog inputs are represented on the top portion of the input cell and the digital inputs occupy the remaining positions on the input cell. For example, on the ADAU170x and ADAU1761 devices, which have two ADC input channels, the left ADC corresponds to input channel 0, the right ADC corresponds to input channel 1, and the digital I2S/TDM channels correspond to channels 2 through 9 on the input cell.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/screenhunter_02_nov._29_11.21.jpg
   :alt: screenhunter_02_nov._29_11.21.jpg
   :align: center

ADAU1701 Serial Input Port Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the ADAU1701 (and ADAU1702, ADAU1401, ADAU1401A), which have 2 analog channels and up to 8 digital channels, the input channels are routed as follows:

+--------------------------+--------------------------+-----------------------------------+
| Hardware Input, I2S mode | Hardware Input, TDM mode | Channel Assignment in Input Block |
+==========================+==========================+===================================+
| Left ADC                 | Left ADC                 | 0                                 |
+--------------------------+--------------------------+-----------------------------------+
| Right ADC                | Right ADC                | 1                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN0, 1st slot      | SDATA_IN0, 1st slot      | 2                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN0, 2nd slot      | SDATA_IN0, 2nd slot      | 3                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN1, 1st slot      | SDATA_IN0, 3rd slot      | 4                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN1, 2nd slot      | SDATA_IN0, 4th slot      | 5                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN2, 1st slot      | SDATA_IN0, 5th slot      | 6                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN2, 2nd slot      | SDATA_IN0, 6th slot      | 7                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN3, 1st slot      | SDATA_IN0, 7th slot      | 8                                 |
+--------------------------+--------------------------+-----------------------------------+
| SDATA_IN3, 2nd slot      | SDATA_IN0, 8th slot      | 9                                 |
+--------------------------+--------------------------+-----------------------------------+

ADAU1761 Serial Input Port Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the ADAU1761, the routing is dependent on the channel settings of the serial port.

I2S (2 channel) Routing
^^^^^^^^^^^^^^^^^^^^^^^

============================ =================================
Hardware Input               Channel Assignment in Input Block
============================ =================================
Left ADC                     0
Right ADC                    1
First channel in I2S stream  2
Second channel in I2S stream 3
============================ =================================

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_input_routing_001.jpg
   :align: center

TDM4 (4 channel) Routing
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------+-----------------------------------+
| Hardware Input                          | Channel Assignment in Input Block |
+=========================================+===================================+
| Left ADC                                | 0                                 |
+-----------------------------------------+-----------------------------------+
| Right ADC                               | 1                                 |
+-----------------------------------------+-----------------------------------+
| First channel in I2S or TDM stream      | 2                                 |
+-----------------------------------------+-----------------------------------+
| **Third** channel in I2S or TDM stream  | 3                                 |
+-----------------------------------------+-----------------------------------+
| **Second** channel in I2S or TDM stream | 4                                 |
+-----------------------------------------+-----------------------------------+
| Fourth channel in I2S or TDM stream     | 5                                 |
+-----------------------------------------+-----------------------------------+

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_input_routing_002.jpg
   :align: center

TDM8 (8 channel) Routing
^^^^^^^^^^^^^^^^^^^^^^^^

+------------------------------------------+-----------------------------------+
| Hardware Input                           | Channel Assignment in Input Block |
+==========================================+===================================+
| Left ADC                                 | 0                                 |
+------------------------------------------+-----------------------------------+
| Right ADC                                | 1                                 |
+------------------------------------------+-----------------------------------+
| First channel in I2S or TDM stream       | 2                                 |
+------------------------------------------+-----------------------------------+
| **Fifth** channel in I2S or TDM stream   | 3                                 |
+------------------------------------------+-----------------------------------+
| **Second** channel in I2S or TDM stream  | 4                                 |
+------------------------------------------+-----------------------------------+
| **Sixth** channel in I2S or TDM stream   | 5                                 |
+------------------------------------------+-----------------------------------+
| **Third** channel in I2S or TDM stream   | 6                                 |
+------------------------------------------+-----------------------------------+
| **Seventh** channel in I2S or TDM stream | 7                                 |
+------------------------------------------+-----------------------------------+
| **Fourth** channel in I2S or TDM stream  | 8                                 |
+------------------------------------------+-----------------------------------+
| Eighth channel in I2S or TDM stream      | 9                                 |
+------------------------------------------+-----------------------------------+

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/io/adau1761_input_routing_003.jpg
   :align: center

.. |inputpic1.png| image:: https://wiki.analog.com/_media/inputpic1.png
.. |inputpic2.png| image:: https://wiki.analog.com/_media/inputpic2.png
.. |inputpic3.png| image:: https://wiki.analog.com/_media/inputpic3.png
