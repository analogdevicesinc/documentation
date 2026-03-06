Chime Generator
===============

`Click here to return to the Source page <https://wiki.analog.com/resources/tools-software/sigmastudio/toolbox/source>`__

The Chime Generator module used to a chime sound with programmable, wave type, frequency, attack, decay, On time, Off time, number of pulse repetitions and time delay between the pulse. There are two control inputs pins one for On/Off and one for selecting the current GUI control. There are two output pins one for chime running status and one for chime output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/sources/chimegenerator_215xx.jpg
   :align: center
   :width: 400px

**Input Pins:**

**pin0:On/Off Control Input:** The DC or Switch module can be connected to the On/Off control input which is used to enable/disable the Chime Generator. There is slew applied when ever change in enable/disable, also the correct sequence complete before stop.

**pin1:Configuration Index:** The DC module can be connected to the control index control input which is used to select the current Chime Generator GUI control when control grown.

**Output Pins:**

**pin2:Chime Running Status:** The Chime running status control output which is used to get the Chime Generator running status.

**pin3:Chime Output:** The Chime output for the selected GUI control.

**GUI Controls:**

**Wave Type:** The wave type can be chosen as Sine/Square using this control. We can change the wave type in run time and there is a slew will be applied when change from one wave type to other.

**Frequency :** The frequency control used to set the Sine/Square frequency in Hz for the Chime.

**Attack:** The attack control used to set the attack duration in msec for every sequence of the Chime start.

**Attack Type:** The attack type supported is linear.

**Decay:** The decay control used to set the decay duration in msec for every sequence of the Chime end.

**Decay Type:** The attack type supported is linear.

**On Time:** Chime pulse On duration in msec.

**Off Time:** Chime pulse On duration in msec.

**NPulses:** Number of Chime pulses to be generated for each sequence.

**Tdwell:** The Chime generation delay in msec for each sequence.
