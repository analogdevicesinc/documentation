Counters
========

| :doc:`Click here to return to the Toolbox page </wiki-migration/resources/tools-software/sigmastudio/toolbox>`
| --------------------------------------------------------------------------------------------

Counters, timers and stopwatches help achieve time based conditional event triggering. In many applications it is important to be able to track time that has passed in order to trigger events, or turn flags on and off, or find out how long it takes to finish a task. It is also useful to trigger the start and stop of counting based on external signals.

Some typical applications include counting time during which a product is inactive in order to power-down the device after a certain time threshold of inactivity is met. Other more generic examples include sequencing of events depending on time that has passed. Thus counters can be used to pause the signal flow; a certain amount of time can be specified to wait for, and then the output will trigger the next event to occur.

In some applications is useful to enter an actual value that sets the counter, whereas in other situations, the signal flow should determine when the counting begins, ends and is reset. SigmaStudio offers a wide range of timing algorithms that allow for flexible control of the counting method.

The toolbox's Counter library includes the following blocks:

-  :doc:`Pulse Counter </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/pulsecounter>`
-  :doc:`Counter </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/counter>`
-  :doc:`Stop Watch </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/stopwatch>`
-  :doc:`Timer - W/ External Reset </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/timerwexternalreset>`
-  :doc:`Stop Watch W/ External Reset </wiki-migration/resources/tools-software/sigmastudio/toolbox/counters/stopwatchwexternalreset>`
