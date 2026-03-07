OneShot Fall, Reset
===================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+
| The One Shot Fall block outputs a trigger signal based upon the falling edge of the input signal. At the first falling edge of the input signal, the output signal will go high. The output signal will remain high until a non-zero input signal is seen on the reset pin. The reset pin clears the output back to zero and will maintain the output at zero while the signal on the reset pin is non-zero. Once the reset pin goes back to zero, the output will go high at the next falling edge of the input signal. | |oneshotfallresetpic1.png| |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------+

Input Pins
----------

+--------------+------------------------------------+-----------------------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                                      |
+==============+====================================+===========================================================+
| Pin 0: Input | any - any                          | Input signal that is monitored for the first falling edge |
+--------------+------------------------------------+-----------------------------------------------------------+
| Pin 1: Reset | any - control                      | Resets the output trigger signal back to zero             |
+--------------+------------------------------------+-----------------------------------------------------------+

Output Pins
-----------

+----------------+------------------------------------+------------------------------------------------------------+
| Name           | Format [int/dec] - [control/audio] | Function Description                                       |
+================+====================================+============================================================+
| Pin 0: Trigger | any - control                      | Output flag signal set to "1" in the selected bit position |
+----------------+------------------------------------+------------------------------------------------------------+

GUI Controls
------------

+------------------------+---------------+--------------+---------------------------------------------------------------------------------------------+
| GUI Control Name       | Default Value | Range        | Function Description                                                                        |
+========================+===============+==============+=============================================================================================+
| Output Bit Designation | 28            | [28.0 Bit26] | Sets bit position of the output "1" flag. 28.0 is the default values which represents 1LSB. |
+------------------------+---------------+--------------+---------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name       | Compiler Name          | Function Description                                                                                                         |
+========================+========================+==============================================================================================================================+
| Output Bit Designation | OneShotFallAlg1output1 | Actual value written to DSP from the representation of the drop-down menu to select the bit position of the output "1" flag. |
+------------------------+------------------------+------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

| The following graph shows the output response based on a given input signal and reset signal through the OneShotFallReset block. In the graphs the input signal is only toggling between "1" and "0" however this algorithm will respond to any changes in level of the input signal, thus the first falling edge of the input signal will trigger the output to go high.
| |oneshotfallresetpic2.png|
| The format of the "1" output value of the is designated by the drop-down menu. The following table shows the "1" Output that corresponds to the drop-down menu selection.
| |oneshotfallpic3.png|

Example
-------

| The following image shows the OneShotFallReset block being used with a LFO :doc:`triangle source </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/trianglewave>`, reset :doc:`switch </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/onoffswitch>`, and :doc:`GPIO output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeoutput>`. When the LFO is turned on, the output will go high on the first drop of the triangle waveform. The output can be reset when the switch is turned on.
| |oneshotfallresetpic4.png|

Algorithm Details
-----------------

+----------------------------+--------------------------------------------------+
| Toolbox Path               | Basic DSP - Logic - Toggle - OneShot Fall, reset |
+----------------------------+--------------------------------------------------+
| Cores Supported            | AD1940                                           |
|                            | ADAU170x                                         |
|                            | ADAU144x                                         |
|                            | ADAU176x                                         |
|                            | ADAU178x                                         |
+----------------------------+--------------------------------------------------+
| "Grow Algorithm" Supported | no                                               |
+----------------------------+--------------------------------------------------+
| "Add Algorithm" Supported  | no                                               |
+----------------------------+--------------------------------------------------+
| Subroutine/Loop Based      | no                                               |
+----------------------------+--------------------------------------------------+
| Program RAM                | 9                                                |
+----------------------------+--------------------------------------------------+
| Data RAM                   | 4                                                |
+----------------------------+--------------------------------------------------+
| Parameter RAM              | 1                                                |
+----------------------------+--------------------------------------------------+

.. |oneshotfallresetpic1.png| image:: https://wiki.analog.com/_media/oneshotfallresetpic1.png
.. |oneshotfallresetpic2.png| image:: https://wiki.analog.com/_media/oneshotfallresetpic2.png
.. |oneshotfallpic3.png| image:: https://wiki.analog.com/_media/oneshotfallpic3.png
.. |oneshotfallresetpic4.png| image:: https://wiki.analog.com/_media/oneshotfallresetpic4.png
