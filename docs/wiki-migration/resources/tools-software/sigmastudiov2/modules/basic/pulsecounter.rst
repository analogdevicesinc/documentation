:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Pulse Counter
=============

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/pulsecounter.png
   :alt: pulsecounter.png

Description
-----------

| The Pulse Counter block, counts the number of inputs received. There is a start/stop pin to initiate and pause the count, and also a reset pin to set the count back to zero. Any non-zero input on the pulse input pin, is considered a pulse and will be counted when the count is enabled.
| The pulse counter is to count the number of pulses in specified amount of time. The time is dictated by the signal on StartStop input pin. When the StartStop pin is high, counter starts counting pulses, otherwise the last count value is output. The Reset pin clears the count value and start from zero when StartStop pin is high.

Targets Supported
-----------------

============= ========== ================ ============= ================
Name          ADSP-214xx ADSP-215xx/SC5xx ADAU145x/146x ADSP-218xx/SC8xx
============= ========== ================ ============= ================
Pulse Counter B/S        B/S              S             B
============= ========== ================ ============= ================

Pins
----

Input
~~~~~

========= ======= ========================
Name      Type    Description
========= ======= ========================
StartStop Control Starts/Pause the counter
Reset     Control Resets the counter value
PulseIn   Control Input to the counter
========= ======= ========================

Output
~~~~~~

=========== ======= ===================================================
Name        Type    Description
=========== ======= ===================================================
CountResult Control Outputs the count of non zero inputs to the counter
=========== ======= ===================================================

| 
