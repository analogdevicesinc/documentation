Sine Tone
=========

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+---+---+
| The Tone (Lookup/Sine) block generates a tone from a lookup table, keeping the level constant regardless of frequency. Set the tone frequency in text field or use the arrows; the checkbox turns the tone on and off. | |image2| |
+---+---+

To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

GUI Control
-----------

+------------------+---------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Default Value | Range                   | Function Description                                                                                                             |
+==================+===============+=========================+==================================================================================================================================+
| on/off           | off           | on/off                  | Turns the output of the cell on or off. When the output is off, the output pin will output a constant value of 0 in 5.23 format. |
+------------------+---------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Frequency        | 500.01        | 0.01 to 0.5*Sample Rate | The sets the frequency of the sine tone that is output from the cell.                                                            |
+------------------+---------------+-------------------------+----------------------------------------------------------------------------------------------------------------------------------+

DSP parameter Information
-------------------------

+------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| GUI Control Name | Compiler Name               | Function Description                                                                                                                     |
+==================+=============================+==========================================================================================================================================+
| N/A              | sin_lookupAlg19401mask      | This value is an internal parameter and should be set according to its value as output by the SigmaStudio compiler.                      |
+------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Frequency        | sin_lookupAlg19401increment | This sets the frequency of the sine tone. Its value is stored as a fixed point 5.23 number, equal to Frequency / (Sample Rate \* 0.5).   |
+------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| on/off           | sin_lookupAlg19401ison      | This value controls if the signal will be output or not. 'On' is represented by a 1 in 5.23 format, whereas 'Off' is represented by a 0. |
+------------------+-----------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sinewave014.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/sinewave014.jpg
