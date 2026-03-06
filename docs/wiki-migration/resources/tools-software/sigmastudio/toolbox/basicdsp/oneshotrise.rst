OneShot Rise
============

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ---------------------------------------------------------------------------------------------------------

+---+---+
| The One Shot Rise block outputs a trigger signal based upon the rising edge of the input signal. At the first non-zero rising edge of the input signal, the output signal will go high and remain high. If the input signal starts high, the output signal will start and remain high. | |oneshotrisepic1.png| |
+---+---+

Input Pins
----------

+--------------+------------------------------------+----------------------------------------------------------+
| Name         | Format [int/dec] - [control/audio] | Function Description                                     |
+==============+====================================+==========================================================+
| Pin 0: Input | any - any                          | Input signal that is monitored for the first rising edge |
+--------------+------------------------------------+----------------------------------------------------------+

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

| The following graph shows the output response based on a given input signal through the One Shot Rise block. There are two different case scenarios: Case1: The input signal starts high
| Case2: The input signal starts low
| In the graphs the input signal is only toggling between "1" and "0" however this algorithm will respond to any changes in level of the input signal, thus the first rising edge of the input signal will trigger the output to go high.
| |oneshotrisepic2.png|
| The format of the "1" output value of the is designated by the drop-down menu. The following table shows the "1" Output that corresponds to the drop-down menu selection.
| |oneshotfallpic3.png|

Example
-------

| The following image shows the OneShot Rise block being used. A :doc:`switch </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources/onoffswitch>` source is connected to the input and then the output of the block is driving a :doc:`GPIO output </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/generalpurposeoutput>`. When the switch is clicked "high" the signal sent to the GPIO output will be "high."
| |oneshotrisepic4.png|

Algorithm Details
-----------------

========================== =========================================
Toolbox Path               Basic DSP - Logic - Toggle - OneShot rise
Cores Supported            AD1940
                           ADAU170x
                           ADAU144x
                           ADAU176x
                           ADAU178x
"Grow Algorithm" Supported no
"Add Algorithm" Supported  no
Subroutine/Loop Based      no
Program RAM                5
Data RAM                   4
Parameter RAM              1
========================== =========================================

.. |oneshotrisepic1.png| image:: https://wiki.analog.com/_media/oneshotrisepic1.png
.. |oneshotrisepic2.png| image:: https://wiki.analog.com/_media/oneshotrisepic2.png
.. |oneshotfallpic3.png| image:: https://wiki.analog.com/_media/oneshotfallpic3.png
.. |oneshotrisepic4.png| image:: https://wiki.analog.com/_media/oneshotrisepic4.png
