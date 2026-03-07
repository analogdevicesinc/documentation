Fractional Delay
================

| :doc:`Click here to return to the Basic DSP page </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp>`
| ---------------------------------------------------------------------------------------------------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


| The Fractional Delay cell provides a variable delay to a single audio input. The input is delayed by the amount reflected in the percentage text box and allows for fractional delays (fractions of a sample period via linear interpolation). The top drop-down menu labeled Max represents the largest amount of delay that could be applied to the input signal and sets the data delay buffer size. If fractional sample delay time is not required, the sample based :doc:`Delay </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/delay>` cell is recommend to conserve DSP cycles. |

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

|fracdelay.png| At run-time the delay amount can be adjusted between 0% and 100% of the "Max" delay value . If you select a new **Max** value in the drop-down menu, the program must be regenerated using "Link Compile Download".

This algorithm can be grown in order to support multiple input/output pairs. Each input and output have the same delay amount applied. Note, for each input/output pair selected, the amount of data memory reserved will be: *Number of Input/Output pairs \* Max Delay*

| The maximum delay available for a particular delay block depends on the total available system data RAM, which is specified in the DSP processor data sheet. Setting the Max control's value, allocates memory on the DSP, reserving that memory for use by this particular block only, and reducing the available memory for all other delay blocks in the design. This is a compiler directive and modifies the assembly code, so any time you change the*\* Max*\* setting you must recompile and download the program. The maximum delay value range is limited to the remaining unallocated memory of the RAM.

Delay Amount
------------

| The fractional delay setting is a percentage of the maximum delay. For example, if the **Max** delay is set to 480 (10ms at 48kHz sampling rate)

-  A delay setting of 100.0 (100%) is (1.0 \* 480) or 480 samples
-  A delay of 10.05 (10.05%) is (0.1005 \* 480) or 48.24 samples

| If more precise control over the fractional delay amount is required, the fractional version of the :doc:`Multi-Tap Voltage Controlled Delay </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/multitapvoltagecontrolleddelay>` cell can be used, and the delay percentage is defined via an external input pin.
| To update the delay percentage via an external micro-controller (MCU), the valid delay percentage value is a fixed point number between 0.0 and 1.0 (0% to 100%).

.. |fracdelay.png| image:: https://wiki.analog.com/_media/fracdelay.png
