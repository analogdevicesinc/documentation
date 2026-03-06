Limiter (ADAU1772)
==================

| :doc:`Click here to return to the Dynamics Processors page </wiki-migration/resources/tools-software/sigmastudio/toolbox/dynamicsprocessors>`
| ----------------------------------------------------------------------------------------------------------------

+---+---+
| The limiter in the ADAU1772 compares the input signal against the setting of the threshold to make adjustments to the output gain. When the input signal level is greater than or equal to the threshold level, the output gain is set to the 'Min Gain' gain setting. When the input signal level is less than the threshold setting, the output gain is set to the 'Max Gain' gain setting. The rate of gain change between the Min and Max settings is determined by the 'Attack' and 'Decay' parameters. | |limiter1.png| |
+---+---+

| 
|

.. important::

   An external detect version of the limiter also exists in the Toolbox library. This cell has a separate input to be compared against the threshold giving the ability to 'sidechain' or use a separate 'key input' to the compressor.


.. important::

   In order to use the limiter on the ADAU1772 the 'Limiter Enable' bit must set high.

   | Core Enable register; address 0x000B; bit [1].
   
   | In SigmaStudio this switch can be found in the Chip Control tab of the Hardware Configuration section of the project.
   | |limiteren.png|


Input Pins
----------

+--------------------+------------------------------------+-----------------------------+
| Name               | Format [int/dec] - [control/audio] | Function Description        |
+====================+====================================+=============================+
| Pin 0: Audio Input | dec - audio                        | Audio signal to be limited. |
+--------------------+------------------------------------+-----------------------------+

Output Pins
-----------

+---------------------+------------------------------------+------------------------------+
| Name                | Format [int/dec] - [control/audio] | Function Description         |
+=====================+====================================+==============================+
| Pin 0: Audio Output | dec - audio                        | Limited audio output signal. |
+---------------------+------------------------------------+------------------------------+

GUI Controls
------------

+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range             | Function Description                                                                                                                                             |
+==================+===============+===================+==================================================================================================================================================================+
| Threshold        | 0 dB          | +12 dB to -138 dB | Controls the value that the input level is compared to. When the input level is greater than or equal to this value, the output gain will ramp to the 'Min Gain' |
+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Min Gain         | 0 dB          | +12 dB to -138 dB | This value is the lowest possible output gain setting                                                                                                            |
+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Max Gain         | 0 dB          | +12 dB to -138 dB | This value is the highest possible output gain setting                                                                                                           |
+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Attack           | 0             | 0 to 16777215     | This value dictates the ramp slope from Max Gain to Min Gain. The display shows this value in ms.                                                                |
+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decay            | 0             | 0 to 16777215     | This value dictates the ramp slope from Min Gain to Max Gain. The display shows this value in ms.                                                                |
+------------------+---------------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |limiter1.png| image:: https://wiki.analog.com/_media/limiter1.png
.. |limiteren.png| image:: https://wiki.analog.com/_media/limiteren.png
   :width: 500px
