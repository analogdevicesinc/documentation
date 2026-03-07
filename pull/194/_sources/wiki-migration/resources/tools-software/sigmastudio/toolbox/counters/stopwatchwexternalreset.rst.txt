Stopwatch w/ External Reset
===========================

| :doc:`Click here to return to the Counters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters>`
| |stopwatchwextpic1.png| The stopwatch block allows for a stop, start, and reset counting mechanism. When one needs to know how long something takes (i.e. how many samples have passed), you signal the start and stop of an event, and a stopwatch measures the time between the signaling of the start and stop. Stopwatches also allow for the count to be reset to zero to measure additional time intervals.

Note: This block differs from the Stopwatch block because it can be reset by an external input signal. The regular Stopwatch can only be reset by writing to its reset parameter coefficient.

The stopwatch allows external signals to control the start and stop of the counter. The output of the stopwatch block is the total sample count, in 28.0 data format, for the active period. When active, the output value and count are incremented for every sample period.

| **Inputs:**
| |stopwatchwextpic2.png|

-  The top input pin is the START pin. While the STOP pin signal is zero (see below), an input value greater than zero triggers the counter to start, a zero value will stop the counter.
-  The middle input pin is the STOP pin. An input value greater than zero will stop the counter (regardless of the value of the start pin).
-  The bottom (orange) pin is the RESET control pin. When the reset signal is one, it will reset the value of the counter and output to zero. If the count is active (e.g. START = 1 and STOP = 0) the count will reset to zero continue to increment from zero. If the count is inactive (e.g. START = 0 or STOP = 1) the reset signal clears the count and the output remains at 0.

--------------

| Below are graphs showing values of the START, STOP, RESET, and the resulting output values.
| |stopwatchwextpic3.png|

--------------

| To better understand the counter output, imagine that for every sample that passes when the count is active, you are incrementing by 2^-23. This is the smallest amount possible to increment by (since our data is in 5.23 format the LSB is 2^-23). However the format of the count output is in 28.0 thus the maximum value that can be achieved by the count output is 2^28 – 1 = 268435455. If the count reaches this value it will no longer be incremented and will not wrap around, but just maintain this max value. This maximum value in samples can be converted to a meaningful time value in seconds by knowing the sampling frequency of the block.
| **For example @ fs = 48000 Hz:**
| 268435455 samples \* 1 s / 48000 samples = 5592.4053 s = 93.02 minutes

In this example, the stopwatch can count up to a maximum of 93.02 minutes.

--------------

**Example:**

| The stopwatch can be used in many different situations. Below is a sample schematic showing the basic operation of the Stopwatch w/ External Reset. The DC input blocks along with a mono switch, allow for the start, stop, and reset pins to be toggled from 0 to 1. This controls the beginning, end, and clearing of the count. The main difference between the Stopwatch and Stopwatch w/ external reset is how the clearing of the count output is handled. In this case an external data signal can be used to control the reset function of the count. With the stopwatch a coefficient parameter (controlled by a button in SigmaStudio) allows the count to be cleared.
| |stopwatchwextpic4.png|

.. |stopwatchwextpic1.png| image:: https://wiki.analog.com/_media/stopwatchwextpic1.png
.. |stopwatchwextpic2.png| image:: https://wiki.analog.com/_media/stopwatchwextpic2.png
.. |stopwatchwextpic3.png| image:: https://wiki.analog.com/_media/stopwatchwextpic3.png
.. |stopwatchwextpic4.png| image:: https://wiki.analog.com/_media/stopwatchwextpic4.png
