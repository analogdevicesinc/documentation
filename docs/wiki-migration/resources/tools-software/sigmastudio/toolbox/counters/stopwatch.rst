Stopwatch
=========

| :doc:`Click here to return to the Counters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters>`
| ----------------------------------------------------------------------------------------------------

|stopwatchpic1.png| The stopwatch block allows for a stop, start, and reset counting mechanism. When one needs to know how long something takes (i.e. how many samples have passed), you signal the start and stop of an event, and a stopwatch measures the time between the signaling of the start and stop. Stopwatches also allow for the count to be reset to zero to measure additional time intervals.

The stopwatch allows external signals to control the start and stop of the counter. The output of the stopwatch block is the total sample count, in 28.0 data format, for the active period. When active, the output value and count are incremented for every sample period.

| **Inputs:**
| |stopwatchpic2.png|

-  The top input pin is the START pin. While the STOP pin signal is zero (see below), an input value greater than zero triggers the counter to start, a zero value will stop the counter.
-  The bottom input pin is the STOP pin. An input value greater than zero will stop the counter (regardless of the value of the start pin).

**Reset button:**

The **Reset** button resets the value of the counter and output to zero. If the count is active (e.g. START = 1 and STOP = 0) the counter remains active and continues counting from zero. If the count is inactive (e.g. START = 0 or STOP = 1) the reset button clears the count and the output will remain at 0. The RESET button is controlled via a parameter coefficient.

--------------

| Below are graphs showing values for START, STOP, and the resulting output values. The vertical red lines on the count output denote when the RESET button is pressed.
| |stopwatchpic3.png|

--------------

To better understand the counter output, imagine that for every sample that passes when the count is active, you are incrementing by 2^-23. This is the smallest amount possible to increment by (since our data is in 5.23 format the LSB is 2^-23). However the format of the count output is in 28.0 thus the maximum value that can be achieved by the count output is 2^28 – 1 = 268435455. If the count reaches this value it will no longer be incremented and will not wrap around, but just maintain this max value. This maximum value in samples can be converted to a meaningful time value in seconds by knowing the sampling frequency of the block.

| **For example @ fs = 48000 Hz:**
| 268435455 samples \* 1 s / 48000 samples = 5592.4053 s = 93.02 minutes

In this example, the stopwatch can count up to a maximum of 93.02 minutes.

--------------

**Example:**

| Below is a sample schematic showing the basic operation of the Stopwatch. The DC input blocks along with a mono switch, allow for the start and stop pins to be toggled from 0 to 1. This controls the beginning and end of the count. The reset button on the stopwatch controls a coefficient parameter that clears the value of the counter.
| |stopwatchpic4.png|

.. |stopwatchpic1.png| image:: https://wiki.analog.com/_media/stopwatchpic1.png
.. |stopwatchpic2.png| image:: https://wiki.analog.com/_media/stopwatchpic2.png
.. |stopwatchpic3.png| image:: https://wiki.analog.com/_media/stopwatchpic3.png
.. |stopwatchpic4.png| image:: https://wiki.analog.com/_media/stopwatchpic4.png
