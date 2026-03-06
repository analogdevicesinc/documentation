Basic DSP Examples
==================

:doc:`Click here to return to the Tutorials section. </wiki-migration/resources/tools-software/sigmastudio/tutorials>`

Example 1
---------

This schematic uses the DC Input block, Adders, and an AB in/Out Condition block to compare the level of two input VCO sources that have a dc value added to them. The output of the Condition block is split with a T Connection and sent to Output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample1.jpg
   :alt: basicdspexample1.jpg

For the current configuration, the condition will evaluate false, and signal B will be sent to the output. If you click the Condition icon in the AB In/Out Condition block so that it shows greater than (>), then recompile, the condition will evaluate true and the A signal will output.

Example 2
---------

This schematic shows how the output from the Delay block is split at a T Connection, to be sent to Output and also fed into the Feedback block and then back into the 2nd input of the Multiple Control Mixer.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample2.jpg
   :alt: basicdspexample2.jpg

Example 3
---------

This schematic shows how the Linear Gain block can be used to apply plain boost, how the Divide block can be used to divide one value with another, and how the DSP Readback block reads back the value from the DSP.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample3.jpg
   :alt: basicdspexample3.jpg

Example 4
---------

This schematic uses DC Input Entry, Tone (lookup/sine), Signal Invert, Value Hold and Output blocks. Here the Value Hold retains the incoming signal at the green pin as the Control input by the dc-input block at the red pin is inverted.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample4.jpg
   :alt: basicdspexample4.jpg

Example 5
---------

This schematic uses a DC Input block, Tone (lookup/sine), T Connection, Voltage-Controlled Delay, and Output blocks, and explains how it all works with the voltage-controlled delay algorithm. The dc input gives the samples of delay to the input signal when the delay is within the range of the maximum allowed and the output is undefined if it exceeds the maximum allowed or is set to zero. Here the voltage-controlled delay is set for a maximum delay of 5623 samples, which corresponds to 0.1275 milliseconds. The dc input is set for the maximum value of 3013.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample5.jpg
   :alt: basicdspexample5.jpg

The graph below shows the delay as offset between the lowest, -1 point on the input and the same on the output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/tutorials/basicdspexample5-2.jpg
   :alt: basicdspexample5-2.jpg
