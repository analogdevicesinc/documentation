:doc:`Click here to return to the Sources page </wiki-migration/resources/tools-software/sigmastudiov2/modules/sources>`

Chime Generator
===============

The Chime Generator module produces programmable chime sounds with configurable parameters such as wave type, frequency, attack, decay, on/off timing, pulse repetitions, and dwell delay. It provides two input pins for control and two output pins for monitoring and signal output.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/modules/sources/ChimeGenerator_SSPlus.jpg
   :alt: ChimeGenerator_SSPlus.jpg
   :width: 600px

Input Pins
----------

-  pin0 – On/Off Control Input

   -  Connect a DC or Switch module to enable or disable the Chime Generator.
   -  A slew is applied whenever the state changes.
   -  The sequence completes correctly before stopping.

-  pin1 – Configuration Index

   -  Connect a DC module to select the active GUI control.
   -  Determines which Chime Generator parameter is currently applied.

Output Pins
-----------

-  pin2 – Chime Running Status

   -  Provides the current running status of the Chime Generator.

-  pin3 – Chime Output

   -  Outputs the generated chime signal based on the selected GUI control.

GUI Controls
------------

-  **Wave Type**

   -  Select between Sine or Square.
   -  Wave type can be changed at runtime; a slew is applied during transitions.

-  **Frequency**

   -  Set the chime frequency (Hz).

-  **Attack**

   -  Define the attack duration (ms) for each chime sequence start.
   -  Attack Type: Linear.

-  **Decay**

   -  Define the decay duration (ms) for each chime sequence end.
   -  Decay Type: Linear.

-  **On Time**

   -  Set the pulse ON duration (ms).

-  **Off Time**

   -  Set the pulse OFF duration (ms).

-  **NPulses**

   -  Specify the number of pulses per sequence.

-  **Tdwell**

   -  Set the dwell delay (ms) between sequences.
