Growable Single Volume Control
==============================

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+---+---+
| The Growable Single Vol Ctrl (or "Growable Single Volume Control") algorithm applies gain to an input signal. The gain is updated using an RC-type slew curve. The number of input channels is scalable - each input is routed to a corresponding output pin. The same gain is applied to all input channels simultaneously. | |growablesinglevolumecontrol1.jpg| |
+---+---+

Input Pins
----------

+--------------------+------------------------------------+-------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description    |
+====================+====================================+=========================+
| Pin 0: Audio Input | decimal - audio                    | Audio Input - Channel 0 |
+--------------------+------------------------------------+-------------------------+

Output Pins
-----------

+---------------------+------------------------------------+--------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description     |
+=====================+====================================+==========================+
| Pin 0: Audio Output | decimal - audio                    | Audio Output - Channel 0 |
+---------------------+------------------------------------+--------------------------+

GUI Controls
------------

+--------------------+---------------+-------------+-----------------------------------------------+
| GUI Control Name   | Default Value | Range       | Function Description                          |
+====================+===============+=============+===============================================+
| Volume Slider (dB) | 0             | -144 to +24 | Controls the target level for the output gain |
+--------------------+---------------+-------------+-----------------------------------------------+

DSP Parameter Information
-------------------------

+-----------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name      | Compiler Name                 | Function Description                                                                                                                                                                     |
+=======================+===============================+==========================================================================================================================================================================================+
| Volume Control Slider | GainS200AlgGrowDP1gain_target | Target value for the output gain.                                                                                                                                                        |
+-----------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| N/A                   | GainS200AlgGrowDP1alpha       | Rate at which the output gain slews to the target value. The alpha and 1-alpha values are stored in consecutive memory locations. Note: This parameter is stored in non-modulo data RAM. |
+-----------------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Algorithm Description
---------------------

| The Growable Single Volume Control applies gain to any number of input signals. It is implemented using a slew curve approximating an RC curve. The same instantaneous gain value is applied to all input signals simultaneously.
| This plot shows the response of an input signal when the gain is changed from zero (linear) to one (full scale, linear):
| |growablesinglevolumecontrol2.jpg|
| This plot shows the response of an input signal when the gain is changed from one (full scale, linear) to zero (linear):
| |growablesinglevolumecontrol3.jpg|

Example
-------

| This example shows 4 digital audio channels being processed by a Growable Single Volume Control cell. When the slider is moved, the gain of all 4 channels will be uniformly changed, following an RC slew curve.
| |growablesinglevolumecontrol4.jpg|

Algorithm Details
-----------------

+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Toolbox Path               | Volume Controls - Adjustable Gain - Single/Multiple Controls - Clickless SW Slew - Growable Single Vol Ctrl |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Cores Supported            | ADAU144x                                                                                                    |
|                            | ADAU1761                                                                                                    |
|                            | ADAU1781                                                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| "Grow Algorithm" Supported | yes - see Algorithm Growth Information                                                                      |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| "Add Algorithm" Supported  | yes - see Algorithm Addition Information                                                                    |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Subroutine/Loop Based      | no                                                                                                          |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Program RAM                | 7\*                                                                                                         |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Data RAM                   | 3\*                                                                                                         |
+----------------------------+-------------------------------------------------------------------------------------------------------------+
| Parameter RAM              | 3\*                                                                                                         |
+----------------------------+-------------------------------------------------------------------------------------------------------------+

\*Numbers are based on one instance of the algorithm with no additional "add" or "grow"

Algorithm Growth Information
----------------------------

+--------------------------+-------------------------------------------------------------------------------------------------------+
| Description              | An extra channel is added. The application of gain to each channel is done with the same calculation. |
+--------------------------+-------------------------------------------------------------------------------------------------------+
| Program RAM Repetition   | 2 per growth                                                                                          |
+--------------------------+-------------------------------------------------------------------------------------------------------+
| Data RAM Repetition      | 1 per growth                                                                                          |
+--------------------------+-------------------------------------------------------------------------------------------------------+
| Parameter RAM Repetition | none                                                                                                  |
+--------------------------+-------------------------------------------------------------------------------------------------------+

Algorithm Addition Information
------------------------------

+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Description              | An extra channel is added. The gain calculation is done separately for each channel, so the program, data, and parameter RAM requirements double. |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Program RAM Repetition   | 7 per add                                                                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Data RAM Repetition      | 3 per add                                                                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter RAM Repetition | 3 per add                                                                                                                                         |
+--------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. |growablesinglevolumecontrol1.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/growablesinglevolumecontrol1.jpg
.. |growablesinglevolumecontrol2.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/growablesinglevolumecontrol2.jpg
.. |growablesinglevolumecontrol3.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/growablesinglevolumecontrol3.jpg
.. |growablesinglevolumecontrol4.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/growablesinglevolumecontrol4.jpg
