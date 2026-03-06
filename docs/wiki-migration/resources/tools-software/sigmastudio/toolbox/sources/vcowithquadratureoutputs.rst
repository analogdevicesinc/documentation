VCO with Quadrature Outputs
===========================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+---+---+
| The voltage-controlled oscillator block, typically used for modulation applications, takes a control input signal (green pin) and outputs a sine tone at a particular frequency on the first blue pin, and a cosine signal (90 degree phase shifted copy of the signal) on the second blue pin. | |vco_q002.jpg| |
+---+---+

| 
| The input value may be from zero to one (5.23 format), and the VCO linearly interpolates its derived value into an output frequency from 0 Hz (0.0 input) to fs/2 (1.0 input). Fs is the sampling frequency.
| If the input applied is greater than 1, the derived output value will fold back to frequencies below fs/2.
| To change the source's Sampling Rate, Right-click in the block and select Set Sampling Rate, which will open the Sampling Rate window (default is 44.1 kHz).
| This cell can be found in the Voltage Controlled subfolder in the Sources section of the toolbox.
| |image1|

.. |vco_q002.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/vco_q002.jpg
.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/vco_quad_039.jpg
