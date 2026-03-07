Pushbutton Volume, Mute
=======================

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| The PushButton Volume block can be used with the GPIO push buttons to control the volume of an input audio signal. This block has the functionality of the Push and Hold, Up/Down Control, Index lookup Table, and SW External Volume control all in one block. The user has the flexibility to define a custom volume curve, used for taper, that is indexed through the pushbuttons. | |pushvolmutepic1.png| |
| This block has the same functionality as the PushButton Volume algorithm, only with the added feature of a mute operation on the input signal when both GPIO push buttons are pressed simultaneously. This feature comes at a Program Instruction tradeoff.                                                                                                                            |                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

Input Pins
----------

+------------------------+-----------------------------+---------------------------------------------------------------------------+
| Name                   | Format                      | Function Description                                                      |
|                        | [int/dec] - [control/audio] |                                                                           |
+========================+=============================+===========================================================================+
| Pin 0: PushButton Up   | int - control               | GPIO signal from Pushbutton that increases the volume                     |
+------------------------+-----------------------------+---------------------------------------------------------------------------+
| Pin 1: PushButton Down | int - control               | GPIO signal from Pushbutton that decreases the volume                     |
+------------------------+-----------------------------+---------------------------------------------------------------------------+
| Pin 2: Interface Read  | n/a                         | Interface Read register to load previous constant data value to algorithm |
+------------------------+-----------------------------+---------------------------------------------------------------------------+
| Pin 3: Interface Read  | decimal - audio             | Audio Input to the volume control                                         |
+------------------------+-----------------------------+---------------------------------------------------------------------------+

Output Pins
-----------

+------------------------+-----------------------------+-------------------------------------------------------------------+
| Name                   | Format                      | Function Description                                              |
|                        | [int/dec] - [control/audio] |                                                                   |
+========================+=============================+===================================================================+
| Pin 0: Interface Write | n/a                         | Interface Write register to store constant volume data for recall |
+------------------------+-----------------------------+-------------------------------------------------------------------+
| Pin 1: Output Audio    | decimal - audio             | Volume adjusted audio output                                      |
+------------------------+-----------------------------+-------------------------------------------------------------------+

GUI Controls
------------

+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name    | Default Value | Range        | Function Description                                                                                                                                                                                                                                                                                                                     |
+=====================+===============+==============+==========================================================================================================================================================================================================================================================================================================================================+
| Invert GPIO         | unchecked     | [checked,    | Clicking this button inverts the signal on the inputs for the GPIO push buttons. SigmaDSP GEN2 hardware has register features to invert the signal, however GEN3 hardware does not support this. Checking or un-checking this box requires a re-compilation since program code is added or removed to achieve this function.             |
|                     |               | unchecked]   |                                                                                                                                                                                                                                                                                                                                          |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Hold (ms)           | 500           | [0, 10000]   | Determines how long the current volume level is held before the repeat pulses are generated to increase/decrease the volume while the button is held down.                                                                                                                                                                               |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Repeat (ms)         | 250           | [0, 10000]   | Sets the time interval between repeated pulses during holding.                                                                                                                                                                                                                                                                           |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Points | 33 pts        | [2, 800]     | Sets the table size: the number of points used in the volume table curve.                                                                                                                                                                                                                                                                |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Values | 1             | [-16, 15.99] | The table points are the actual gain values for the volume curve in linear representation. Although the range supports the full values of [-16, 15.99] the table values should generally be between [0, 1] for proper gain adjustments. The user has full control in this table to add a linear, logarithmic of custom gain volume curve |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SW Slew Rate        | 12            | [1, 23]      | Controls the slew ramp speed for the volume transition between consecutive volume gain points                                                                                                                                                                                                                                            |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name    | Compiler Name               | Function Description                                                                                                                    |
+=====================+=============================+=========================================================================================================================================+
| Hold (ms)           | PushButtonVolAlg1holdtime   | The hold time is written to the DSP as the number of samples representing the millisecond time: Samples = ``HoldTime(ms)*10^-3 *Fs``    |
+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Repeat (ms)         | PushButtonVolAlg1repeattime | The release time is written to the DSP as the number of samples representing the millisecond time: Samples = ``HoldTime(ms)*10^-3 *Fs`` |
+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Points | PushButtonVolAlg1maxindex   | The number of points minus 1 is the max index into the table.                                                                           |
+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Values | PushButtonVolAlg1table_p0   | All the points in the table are written to the DSP in their linear gain format.                                                         |
|                     | ...                         |                                                                                                                                         |
+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| SW Slew Rate        | PushButtonVolAlg1step       | The value for the slew rate written to the DSP follows the formula: ``2^(-SW Slew Rate)``                                               |
+---------------------+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Information
---------------------

The PushButton Volume control allows two GPIO inputs from push buttons to control a custom volume curve. The volume curve can be any linear, logarithmic, or custom curve designed with any number of points. When the "Up" pushbutton is pressed the volume will increase, indexing up through table values. When the "Down" pushbutton is pressed the volume will decrease, indexing down through table values. When the limit index is reached on either end, the volume will just be held.

When a pushbutton is held up or down, the algorithm will scroll through the volume gain points at rates determined by the hold and repeat times. The hold time designates how long the pushbutton must be held until a new repeat pulse is triggered. The repeast pulse determines the interval between incrementing or decrementing through the volume points while the button is held.

For the PushButton Volume with Mute, there is the additional functionality that when both push buttons are pressed simultaneously, the output will be muted. Any subsequent signal from the pushbutton will reactive the volume and it will increment or decrement from the last volume value before muting.

Example
-------

| The following image shows how two GPIO inputs are used to control the volume algorithm in the PushButton Volume block. The PushButton Volume algorithm has been grown in order to support stereo audio. A mux switch allows comparison between the direct signal from the Inputs, and the volume adjusted signal, routed to the Outputs. The Interface Read and Write blocks allow the last volume level to be saved and recalled.
| |pushvolmutepic2.png|

Algorithm Details
-----------------

+----------------------------+----------------------------------------------------------------------+
| Toolbox Path               | GPIO Conditioning - Volume Control - Push Button - PushButton Volume |
+----------------------------+----------------------------------------------------------------------+
| Cores Supported            | ADAU170x                                                             |
|                            | ADAU144x                                                             |
|                            | ADAU176x                                                             |
|                            | ADAU178x                                                             |
+----------------------------+----------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                               |
+----------------------------+----------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                   |
+----------------------------+----------------------------------------------------------------------+
| Program RAM                | 102\*                                                                |
+----------------------------+----------------------------------------------------------------------+
| Program RAM (Invert GPIO)  | 106\*                                                                |
+----------------------------+----------------------------------------------------------------------+
| Data RAM                   | 31\*                                                                 |
+----------------------------+----------------------------------------------------------------------+
| Parameter RAM              | 37\* - Based on 33 points in table: each point = 1 Parameter RAM     |
+----------------------------+----------------------------------------------------------------------+

Algorithm Growth Information
----------------------------

+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Description                          | When the PUshButton Volume algorithm is grown, an extra pair of input/output pins are added to the control. All the same processing occurs in terms of the push button volume processing, but the growth allows for new pairs of input/output audio signals, in order to apply the gain adjustment. | |pushvolmutepic3.png| |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Program RAM Repetition               | 2 per growth                                                                                                                                                                                                                                                                                        |                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Program RAM Repetition (Invert GPIO) | 2 per growth                                                                                                                                                                                                                                                                                        |                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Data RAM Repetition                  | 1 per growth                                                                                                                                                                                                                                                                                        |                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
| Parameter RAM Repetition             | none                                                                                                                                                                                                                                                                                                |                       |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

.. |pushvolmutepic1.png| image:: https://wiki.analog.com/_media/pushvolmutepic1.png
.. |pushvolmutepic2.png| image:: https://wiki.analog.com/_media/pushvolmutepic2.png
.. |pushvolmutepic3.png| image:: https://wiki.analog.com/_media/pushvolmutepic3.png
