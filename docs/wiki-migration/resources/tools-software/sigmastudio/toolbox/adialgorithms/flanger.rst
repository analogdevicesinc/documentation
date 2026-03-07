Flanger
=======

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`

--------------

Flanging is a classic audio phasing effect which generates a swirling frequency (moving comb filter) effect. Flanging is produced by mixing the input single with a delayed copy of itself where the delay time is continuously varied at a low frequency. The Flanger algorithm supports growing by one to support stereo processing.

| Flanging is typically used for guitar but can be utilized as a special vocal effect.
| |flangerpic1.png|

**Controls:**

-  **Max** Max delay value determines to amount of DSP memory allocated for this block during compilation. The maximum delay depends on the particular DSP’s available data RAM. Changing the Max value requires a recompile and program download.
-  **Delay** Delay adjusts the maximum delay amount up to the Max delay. The delay amount affects the density and spacing of frequency notches in the comb filter response. Higher delay amounts increase the intensity of the flanging effect.
-  **LFO Rate (0.01Hz – 2Hz)** LFO rate sets the frequency of the LFO waveform used to modulate delay time. Perceptually this adjusts the number of times per second the frequency sweeps up and down.
-  **Depth (Wet/Dry Mix) (0% – 100%)** Depth determines the intensity of the flange effect. This adjusts the mixture of the “dry” input signal with the “wet” flanged signal.

**Algorithm:**

| Flanger utilizes an FIR comb filter with a short delay time (typically <15ms). The delay time is continuously modulated by a low-frequency-oscillator creating the characteristic flanging sound when the filter notches sweep up and down the in frequency over time.
| |flangerpic2.png|

| **Example:** The following example shows a stereo Flange effect using a 2 input Flanger and Volume Control.
| |flangerpic3.png|

.. |flangerpic1.png| image:: https://wiki.analog.com/_media/flangerpic1.png
.. |flangerpic2.png| image:: https://wiki.analog.com/_media/flangerpic2.png
.. |flangerpic3.png| image:: https://wiki.analog.com/_media/flangerpic3.png
