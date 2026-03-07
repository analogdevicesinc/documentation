Timer w/ External Reset
=======================

| :doc:`Click here to return to the Counters page </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters>`
| ----------------------------------------------------------------------------------------------------

|timerwresetpic1.png| Time Timer counts for a specified amount of time and then sets a flag upon completion. When you want to prevent an event from occurring until a certain amount of time (samples) have passed, the timer can be used to trigger or delay schematic functionality.

The Timer w/ external reset allows an external signals to control the start and stop of the count. The output of the timer block is a 5.23 format value of zero or one, indicating whether the value of the timer has been reached. While the count value has not been reached the output will be zero, and once the value has been reached, the output will be one.

| **Inputs:**
| |timerwresetpic2.png|

-  The top pin is the START/RESET pin. When the value does not equal zero, the timer will start. When the value is set to zero, the timer is reset.
-  The bottom pin is the TIMER pin. This pin allows an external signal to set the timer's duration in samples, as a 28.0 format integer value.

--------------

| The timer's counter begins incrementing upon the top Start/Reset pin being set greater than zero. The output will be zero until the timer value is reached, designated by the bottom Timer pin. If the START/RESET pin is set to zero before the count is reached, the output remains at zero and the count will not begin again, until the START/RESET pin is set back to one. Below are graphs showing the values of the START/RESET pins and the output according to a TIMER length of 500 samples.
| |timerwresetpic3.png|

--------------

**Example:**

The timer can be used in many situations in which it is important for the output to trigger an on/off or flagged event. Unlike the stopwatch algorithms, the output of this block is solely a 1 or 0 depending on whether the count value has been reached. (The stopwatch algorithms output the actual current count value).

| In this example schematic, DC input blocks along with a mono switch, allow for the START/RESET pin to be set. This pin controls both when the count starts, and also when the value is cleared. A second DC block (NOTE: 28.0 for integer value) sets the length of the timer to 500 samples. The output of the timer in this case is going straight to the hardware output, but this value of 0 or 1 could also be used for logic conditioning.
| |timerwresetpic4.png|

.. |timerwresetpic1.png| image:: https://wiki.analog.com/_media/timerwresetpic1.png
.. |timerwresetpic2.png| image:: https://wiki.analog.com/_media/timerwresetpic2.png
.. |timerwresetpic3.png| image:: https://wiki.analog.com/_media/timerwresetpic3.png
.. |timerwresetpic4.png| image:: https://wiki.analog.com/_media/timerwresetpic4.png
