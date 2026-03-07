Voltage Controlled Oscillator Reset Phase
=========================================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| The voltage-controlled oscillator block (reset phase), typically used for modulation applications, takes a control input signal (second red pin) and outputs a sine tone at a particular frequency on the blue pin. It also has a control pin that resets the phase of the output signal. | |vco_004.jpg| |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------+

| 
| The input value may be from zero to one (5.23 format), and the VCO linearly interpolates its derived value into an output frequency from 0 Hz (0.0 input) to fs/2 (1.0 input). Fs is the sampling frequency.
| If the input applied is greater than 1, the derived output value will fold back to frequencies below fs/2.
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).

.. |vco_004.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/vco_004.jpg
