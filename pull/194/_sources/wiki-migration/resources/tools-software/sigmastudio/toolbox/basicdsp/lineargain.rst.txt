Linear Gain
===========

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ------------------------------------------------------------------------------------------------------

|lineargainpic1.png| The Linear Gain block scales the signal by the value specified in the text field.

-  Drag it into the workspace.
-  Right-click the block and select **Add Algorithm > IC N >**

   -  **Gain (slew)**

      -  **Gain (no slew)**

-  (Slew instructions mean better quality but at the expense of memory.)
-  Enter the desired scale factor into the text field.

For a sample design using this block, see the :doc:`Basic DSP </wiki-migration/resources/tools-software/sigmastudio/tutorials/basicdspexamples>` example.

The value you specify is in 5.23 format (5 bits for the integer, 23 for the decimal). The accepted values for this block are therefore in the range: -16 to 15.999.

This is the multiplication factor so therefore a value of "1" will not change the gain at all. The value of "0" will multiply by zero so it will mute the audio. The value of 2 will double the signal level (Add 6dB) Values less than 1 but greater than zero, 0<X<1 will reduce the gain of the signal. A negative value will invert the polarity of the audio and apply the gain factor. So -2 will add two dB and invert the polarity. A value of -0.5 will lower the signal by 6dB and invert the polarity. The value of -1 will only invert the polarity.

You can choose a slew or no-slew algorithm. Using slew RAM gradually ramps the signal from original to target value, while using no-slew RAM jumps the signal immediately.

For more information on target/slew ram, see :doc:`Target Slew RAM </wiki-migration/resources/tools-software/sigmastudio/sigmadsparchitecture/ad1940/targetslewram>` in the :doc:`Basic Sigma DSP Architecture </wiki-migration/resources/tools-software/sigmastudio/sigmadsparchitecture>` book section of this wiki.

.. |lineargainpic1.png| image:: https://wiki.analog.com/_media/lineargainpic1.png
