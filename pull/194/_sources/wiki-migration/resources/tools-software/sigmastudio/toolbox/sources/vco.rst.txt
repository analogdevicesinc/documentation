Voltage Controlled Oscillator
=============================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

| The Voltage Controlled Oscillator block is typically used for modulation applications. The block has a control input signal (orange pin) which specifies a frequency. The blue pin generates a sine tone at the appropriate frequency. |vco003.jpg|
| The input value may be from zero to one (5.23 format, or on ADAU145x/ADAU146x, 8.24 format).

| The VCO accepts values from 0 Hz (0.0 input) to Fs/2 (1.0 input). Fs is the sampling frequency. The algorithm linearly interpolates the input value into an output frequency.
| Note that if the input is greater than 1, the derived output value will fold back to frequencies below Fs/2.
| === Example Schematic === |image1|

.. |vco003.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/vco003.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/vco_sigmastudio_project.png
