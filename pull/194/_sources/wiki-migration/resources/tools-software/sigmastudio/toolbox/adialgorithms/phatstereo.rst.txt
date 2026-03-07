phatstereo
==========

| :doc:`Click here to return to the ADI Algorithms page </wiki-migration/resources/tools-software/sigmastudio/toolbox/adialgorithms>`
| |phatpic1.png| Phat-Stereo is a spreading algorithm that uses stereo cross-coupling to simulate surround sound in stereo speakers and other 2-channel situations. The ear is most responsive to interaural phase shifts below 2 kHz, so this increase in phase shift results in a widening of the stereo image.

A 3D enhancement, it yields an enriched surround field both for headphones and for stereo speakers.

| 
| Two parameters control the block:

**Cut Freq (Hz)** - Controls the cutoff frequency of the first-order lowpass filter. Determines the frequency range of the added out-of-phase signals. For best results, the range should be 500 Hz to 2 kHz.

**Level** - Controls the output level of the filter; -80dB would basically be a passthrough with no signal modification.

.. |phatpic1.png| image:: https://wiki.analog.com/_media/phatpic1.png
