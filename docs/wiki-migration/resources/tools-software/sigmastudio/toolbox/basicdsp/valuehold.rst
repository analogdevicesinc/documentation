Value Hold
==========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| --------------------------------------------------------------------------------------------------------

|valueholdpic1.png| The Value Hold block is used to retain an incoming signal (green pin). The signal is held based on the presence and level of a control signal (red pin).

This block holds the value of the signal on the green input pin, maintaining it on the blue output pin whenever the signal applied to the red pin is 0 (zero), but passing it for all values (positive or negative, 5.23 format) on the red pin.

This module can be used for such applications as applying and holding a value to be either analyzed in real time or read back later.

For a sample design using this block, see the :doc:`Basic DSP example </wiki-migration/resources/tools-software/sigmastudio/tutorials/basicdspexamples>`.

.. |valueholdpic1.png| image:: https://wiki.analog.com/_media/valueholdpic1.png
