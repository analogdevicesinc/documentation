Voltage Controlled Pulse
========================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

The Pulse block generates a pulse train with the values 0 and 1. There are two inputs to this cell: Frequency and Duty Cycle.

Frequency is an 8.24 number between 0 and 0.5. An input of 0 will create DC, and 0.5 will create Fs/2. For example, at Fs = 48 kHz, a frequency input of 0.1 will create a 4.8 kHz pulse train.

Duty cycle is an 8.24 number between 0 and 1, corresponding to 0% and 100%. A duty cycle of 0.6 will create a pulse train which has value 1 60% of the time.

Note that since the Pulse block runs at a discrete sampling rate, exact frequency generation is not always possible. A mechanism called "Round Coefficients" approximates the requested frequency more closely by following some short pulses with longer pulses at the closest possible frequencies.

The "Round Coefficients" feature is enabled/disabled with a small circle on the window. When the circle is BLUE, coefficients are rounded. When the circle is ORANGE, the rounding feature is disabled.


|image1|

Input Pins
==========

+--------------+------------------------------------------+------------------------------------------------------------------+
| Name         | Format [int/dec/float] - [control/audio] | Function Description                                             |
+==============+==========================================+==================================================================+
| Pin 0: Input | decimal- Control                         | Control signal to the module to vary the frequency of the pulse  |
+--------------+------------------------------------------+------------------------------------------------------------------+
| Pin 1: Input | decimal- Control                         | control signal to the module to vary the duty cycle of the pulse |
+--------------+------------------------------------------+------------------------------------------------------------------+

Output Pins
===========

+---------------+------------------------------------------+-------------------------------------+
| Name          | Format [int/dec/float] - [control/audio] | Function Description                |
+===============+==========================================+=====================================+
| Pin 0: Output | decimal - audio                          | Output pulse signal from the module |
+---------------+------------------------------------------+-------------------------------------+

GUI Controls
============

+------------------+---------------+-------+------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range | Function Description                                                                                       |
+==================+===============+=======+============================================================================================================+
| isRounded        | 0             | 0 -1  | To select Round or un round the coefficients(which will control first cycle no of samples of TOFF of pulse |
+------------------+---------------+-------+------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
=========================

+------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+
| GUI Control Name | Compiler Name                                                                          | Function Description                                     |
+==================+========================================================================================+==========================================================+
| isRounded        | <fc #008000>PulseAlg_withInputPinS300</fc><fc #ff0000>1</fc><fc #000080>isRounded</fc> | To round/unround the no of samples T-OFF period of Pulse |
+------------------+----------------------------------------------------------------------------------------+----------------------------------------------------------+

| 
| Here,

-  <fc #008000> Green</fc> - Algorithm Name
-  <fc #ff0000> Red</fc> - Instance Number (Changes for each instance)
-  <fc #000080> Blue</fc> - Parameter Name

Supported IC's
==============

ADAU145x and ADAU146x processors are supported.

Example
=======

The schematic below generates a 4.8 kHz pulse with 50% duty cycle.


|image2|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pulse.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/pulse_sigmastudio_project.png
