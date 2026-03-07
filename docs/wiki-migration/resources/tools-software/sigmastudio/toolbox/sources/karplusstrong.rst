Karplus-Strong String Sound Synthesis
=====================================

:doc:`Click here to return to the Sources section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/sources>`

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+
| Karplus-Strong string synthesis is a method of sound synthesis that uses physical modeling to emulate the sound of a hammered of plucked string. A short waveform is looped through a filtered delay line to produce the output signal. | |karplusstrong021.jpg| |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+

An explanation of the basic theory is located on the Wikipedia page https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis.

The slider control is the length of the initial delay line. The minimum value is 70 samples and the maximum is 350 samples.

The "fback Gain" is the feedback gain of the filter. It only accepts a small range of values. It must never exceed 1 so the maximum value you can enter is 0.999899983406067 (0x00, 0x7F, 0xFC, 0xB9). The minimum value is 0.899999976158142 (0x00, 0x73, 0x33, 0x33).

The LPass filter input is the lowpass filter cutoff frequency.

.. |karplusstrong021.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/karplusstrong021.jpg
