Rotary Volume
=============

| :doc:`Click here to return to the GPIO Conditioning page </wiki-migration/resources/tools-software/sigmastudio/toolbox/gpioconditioning>`

+---+---+
| The Rotary Volume block controls the volume level of an input audio signal, using the GPIO rotary encoder inputs. This block has the functionality of the Rotary Encoder, Up/Down Control, Index lookup Table, and SW External Volume control blocks all in one algorithm control. The user has the flexibility to define a custom volume curve that will be scrolled through by the rotary encoder. | |rotaryvolpic1.png| |
+---+---+

Input Pins
----------

+--------------------------+-----------------------------+----------------------------------------------------------------------------------+
| Name                     | Format                      | Function Description                                                             |
|                          | [int/dec] - [control/audio] |                                                                                  |
+==========================+=============================+==================================================================================+
| Pin 0: Rotary Input Up   | int - control               | Control signal from GPIO rotary encoder that increments the volume               |
+--------------------------+-----------------------------+----------------------------------------------------------------------------------+
| Pin 1: Rotary Input Down | int - control               | Control signal from GPIO rotary encoder that decrements the volume               |
+--------------------------+-----------------------------+----------------------------------------------------------------------------------+
| Pin 2: Interface Read    | n/a                         | Interface Read register to load previous constant volume data value to algorithm |
+--------------------------+-----------------------------+----------------------------------------------------------------------------------+
| Pin 3: Input Audio       | decimal - audio             | Audio Input to the volume control                                                |
+--------------------------+-----------------------------+----------------------------------------------------------------------------------+

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
| Debounce            | 20            | [0, 1000]    | Sample counter for the Debounce time on the Rotary Encoder                                                                                                                                                                                                                                                                               |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Points | 33 pts        | [2, 800]     | Sets the table size: the  number of points used in the volume table curve.                                                                                                                                                                                                                                                               |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume Table Values | 1             | [-16, 15.99] | The table points are the actual gain values for the volume curve in linear representation. Although the range supports the full values of [-16, 15.99] the table values should generally be between [0, 1] for proper gain adjustments. The user has full control in this table to add a linear, logarithmic of custom gain volume curve |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SW Slew Rate        | 12            | [1, 23]      | Controls the slew ramp speed for the volume transition between consecutive volume gain points                                                                                                                                                                                                                                            |
+---------------------+---------------+--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

DSP Parameter Information
-------------------------

+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| GUI Control Name    | Compiler Name         | Function Description                                                                      |
+=====================+=======================+===========================================================================================+
| Debounce            | RotaryVolAlg1countmax | The integer number is directly written to the DSP.                                        |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| Volume Table Values | RotaryVolAlg1table_p0 | All the points in the table are written to the DSP in their linear gain format.           |
|                     | ...                   |                                                                                           |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| SW Slew Rate        | RotaryVolAlg1step     | The value for the slew rate written to the DSP follows the formula: ``2^(-SW Slew Rate)`` |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

The Rotary Volume control allows a GPIO inputs from a rotary encoder to control a custom volume curve. The volume curve can be any linear, logarithmic, or custom curve designed with any number of points. When the encoder is turned the volume will increase or decrease according to the volume curve in the table. The transition between points in the table has a smooth transition and the rate is determined by the Slew rate parameter. The Debounce time is used to smooth the actual physical input of the GPIO rotary encoder.

Example
-------

| The following image shows how two GPIO inputs are used to control the volume algorithm in the Rotary Volume block. The Rotary Volume algorithm has been grown in order to support stereo audio. A mux switch allows comparison between the direct signal from the Inputs, and the volume adjusted signal, routed to the Outputs. The Interface Read and Write blocks allow the last volume level to be saved and recalled.
| |rotaryvolpic2.png|

Algorithm Details
-----------------

+----------------------------+------------------------------------------------------------------+
| Toolbox Path               | GPIO Conditioning - Volume Control - Rotary - Rotary Volume      |
+----------------------------+------------------------------------------------------------------+
| Cores Supported            | ADAU170x                                                         |
|                            | ADAU144x                                                         |
|                            | ADAU176x                                                         |
|                            | ADAU178x                                                         |
+----------------------------+------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                           |
+----------------------------+------------------------------------------------------------------+
| "Add Algorithm" Supported  | no                                                               |
+----------------------------+------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                               |
+----------------------------+------------------------------------------------------------------+
| Program RAM                | 88\*                                                             |
+----------------------------+------------------------------------------------------------------+
| Data RAM                   | 41\*                                                             |
+----------------------------+------------------------------------------------------------------+
| Parameter RAM              | 36\* - Based on 33 points in table: each point = 1 Parameter RAM |
+----------------------------+------------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| Description              | When the Rotary Volume algorithm is grown, an extra pair of input/output pins are added to the control. All the same processing occurs in terms of the rotary encoder volume processing, but the growth allows for new pairs of input/output audio signals, in order to apply the gain adjustment. | |rotaryvolpic3.png| |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| Program RAM Repetition   | 2 per growth                                                                                                                                                                                                                                                                                       |                     |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| Data RAM Repetition      | 9 per growth                                                                                                                                                                                                                                                                                       |                     |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
| Parameter RAM Repetition | none                                                                                                                                                                                                                                                                                               |                     |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+

.. |rotaryvolpic1.png| image:: https://wiki.analog.com/_media/rotaryvolpic1.png
.. |rotaryvolpic2.png| image:: https://wiki.analog.com/_media/rotaryvolpic2.png
.. |rotaryvolpic3.png| image:: https://wiki.analog.com/_media/rotaryvolpic3.png
