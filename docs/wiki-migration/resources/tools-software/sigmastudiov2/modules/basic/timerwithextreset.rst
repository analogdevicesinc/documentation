:doc:`Click here to return to the Basic page </wiki-migration/resources/tools-software/sigmastudiov2/modules/basic>`

Timer With External Reset
=========================

| 
| |timerwext.png|

Description
-----------

| The timer block starts increment the counter value, when the control signal to Start/Reset pin is non zero and resets the counter value to zero, when the control signal to Start/Reset pin is zero. The timer continues the counter increment until it reaches the Specified value in timer input pin and its sets the flag to one upon completion. The output of the timer block is 0 or 1, indicating whether the value of timer is reached.
| The timer's counter begins incrementing upon the top Start/Reset pin being set greater than zero. The output will be zero until the timer value is reached, designated by the bottom Timer pin. If the START/RESET pin is set to zero before the count is reached, the output remains at zero and the count will not begin again, until the START/RESET pin is set back to one
| ===== Targets Supported =====

+-------------------+------------+------------------+---------------+------------------+
| Name              | ADSP-214xx | ADSP-215xx/SC5xx | ADAU145x/146x | ADSP-218xx/SC8xx |
+===================+============+==================+===============+==================+
| TimerWithExtReset | B/S        | B/S              | S             | B                |
+-------------------+------------+------------------+---------------+------------------+

| 
| ===== Pins =====

Input
~~~~~

========== ===== ==================================
Name       Type  Description
========== ===== ==================================
StartReset Audio Starts or Resets the timer counter
CountValue Audio Sets the timer duration
========== ===== ==================================

Output
~~~~~~

========= ===== =============================================
Name      Type  Description
========= ===== =============================================
TimerFlag Audio Indicates the counter reached the timer value
========= ===== =============================================

.. |timerwext.png| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/basic/timerwext.png
