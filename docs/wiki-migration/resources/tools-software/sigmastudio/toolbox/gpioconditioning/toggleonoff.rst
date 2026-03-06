Toggle On/Off
=============

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`

+---+---+
| The Toggle On/Off cell toggles its output when it detects a rising edge on its input. The amplitude of the output signal can be set using the drop-down control in the cell's GUI. | |toggleonoffpic1.png| |
+---+---+

Input Pins
----------

+-----------------------------+------------------------------+-------------------------------------------------------------------------------------+
| Name                        | Format                       | Function Description                                                                |
|                             | [int/dec] - [control/audio]  |                                                                                     |
+=============================+==============================+=====================================================================================+
| Pin 0: Detection input      | integer or decimal - control | Control Signal input that is detected by the toggle on/off cell                     |
+-----------------------------+------------------------------+-------------------------------------------------------------------------------------+
| Pin 1: Interface read input | other - interface register   | Connected to a software interface register - reads the last stored value at startup |
+-----------------------------+------------------------------+-------------------------------------------------------------------------------------+

Output Pins
-----------

+-------------------------------+-----------------------------+-------------------------------------------------------------------------------------------------+
| Name                          | Format                      | Function Description                                                                            |
|                               | [int/dec] - [control/audio] |                                                                                                 |
+===============================+=============================+=================================================================================================+
| Pin 0: Toggle output          | integer - control           | Toggling output. Toggles between zero and one each time a rising edge is detected on the input. |
+-------------------------------+-----------------------------+-------------------------------------------------------------------------------------------------+
| Pin 1: Interface write output | other - interface register  | Connected to a software interface register - writes the last output value                       |
+-------------------------------+-----------------------------+-------------------------------------------------------------------------------------------------+

GUI Controls
------------

+------------------+---------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                                   | Function Description                                                                                                                                                                                                                                                                 |
+==================+===============+=========================================+======================================================================================================================================================================================================================================================================================+
| Drop-down menu   | 28            | 28.0, bits 1 to 22, 5.23, bits 24 to 26 | Controls which bit on the output signals will toggle on/off. For example, if this control is set to 28.0, then bit [0] will toggle on the output signal. If this control is set to 5.23, then bit [23] will toggle on the output signal. All other bits remain at zero at all times. |
+------------------+---------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+----------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Name       | Compiler Name        | Function Description                                                                                                                                                                                                                                               |
+================+======================+====================================================================================================================================================================================================================================================================+
| Drop-down menu | ToggleOneAlg1output1 | Defines the bit that will be toggled on the output. In other words, the output will toggle between zero and this value. As an example, if the drop-down menu is set to "28.0", then the value stored in RAM will be 0X00, 0X00, 0X00, 0X01, or one in 28.0 format. |
+----------------+----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

| The toggle on/off cell detects rising edges on its input and toggles its output each time another rising edge is encountered. In other words, if the output is zero and a rising edge appears on the input, the output will change to one. Conversely, if the output is one and a rising edge appears on the input, the output will change to zero. The graphic below shows this input to output relationship.
| |toggleonoffpic2.png|
| The output of the cell will always toggle between zero and another number. That number is determined by the value in the drop-down menu in the GUI. For example, in the above graphic, only the LSB was toggling, so the output was toggling between zero and one in integer format.

| In the example below, the 23rd bit (in a SigmaDSP with 5.23 decimal representation) is toggling. Therefore, the output toggles between zero and 0.5 in decimal format.
| |toggleonoffpic3.png|
| The input to this cell should only take on two values - for example, a logic switch or a square wave. Signals such as sine waves or noise signals will cause the cell to behave in an unpredictable way.

Example
-------

| This simple example will toggle the 24th bit on the output each time the input switch outputs a rising edge. The output will be a series of zeros and ones in 5.23 format.
| |toggleonoffpic4.png|
| Other cells used in this example: On/Off Switch, Interface Read, Interface Write, Output

Algorithm Details
-----------------

+----------------------------+--------------------------------------------------------------+
| Toolbox Path               | GPIO Conditioning - PushButton - Toggle OnOff - Toggle OnOff |
+----------------------------+--------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                     |
|                            | ADAU1701                                                     |
|                            | ADAU1761                                                     |
|                            | ADAU1781                                                     |
+----------------------------+--------------------------------------------------------------+
| "Grow Algorithm" Supported | no                                                           |
+----------------------------+--------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                           |
+----------------------------+--------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                           |
+----------------------------+--------------------------------------------------------------+
| Program RAM                | 10                                                           |
+----------------------------+--------------------------------------------------------------+
| Data RAM                   | 4                                                            |
+----------------------------+--------------------------------------------------------------+
| Parameter RAM              | 1                                                            |
+----------------------------+--------------------------------------------------------------+

.. |toggleonoffpic1.png| image:: https://wiki.analog.com/_media/toggleonoffpic1.png
.. |toggleonoffpic2.png| image:: https://wiki.analog.com/_media/toggleonoffpic2.png
.. |toggleonoffpic3.png| image:: https://wiki.analog.com/_media/toggleonoffpic3.png
.. |toggleonoffpic4.png| image:: https://wiki.analog.com/_media/toggleonoffpic4.png
