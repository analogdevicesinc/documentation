Mute
====

:doc:`Click here to return to the Volume Controls section. </wiki-migration/resources/tools-software/sigmastudio/toolbox/volumecontrols>`

+---+---+
| When enabled, the Mute block "mutes" the input signal so that their is no output (a 0.0 value DC signal). This is useful when powering up or down and when switching program flow. | |mute.jpg| |
+---+---+

| **To Enable/Disable the mute:** Click the check box; the signal is muted when the box is checked.
| The mute block is available as a Slew or Non-Slew algorithm. The Slew version of the algorithm will smoothly transition the gain to its target value, eliminating any click or pops, but require more system resources.
| **Algorithms:**

-  *No Slew (Standard)* - The default mute algorithm is a "no slew" type algorithm which mutes the signal immediately when enabled, there is no gain ramping, this algorithm requires less resources than the slew algorithms, but it can result in discontinuities (clicks and pops) when toggled in real-time.
-  *HW (RCtype Slew)* - The AD1940 / 1941 include support for mute controls that use a target/slew RAM hardware to slew (smoothly transition) from 0dB gain to muted.
-  *SW (RCtype Slew)* - Slew type algorithm that smoothly transitions from 0dB gain to muted and muted to 0dB gain. This slew algorithm is implemented in software, "SW", and thus requires more instructions than the No Slew algorithm.

| 
| This block supports both Grow Algorithm (adds additional inputs and outputs) and Add Algorithm (adds an independent mute algorithm plus associated inputs and outputs).

Controlling Mute from a Microcontroller
=======================================

The following assumes you have a working microcontroller platform, with SigmaDSP interface code based on :doc:`Interfacing SigmaDSP Processors with a Microcontroller </wiki-migration/resources/tools-software/sigmastudio/tutorials/microcontroller>`.

Within SigmaDSP processors, the Mute function is implemented as a gain. When the checkbox is selected (Mute Enabled), the DSP multiplies the input by 0. This produces a 0 at the output. When the checkbox is unchecked (Mute Disabled), the DSP multiplies the input by 1, allowing the input signal to pass through to the output.

To set the algorithm to Mute, write a 0 to the MuteOnOff address. To unmute the output, write a 1 to the MuteOnOff address.

As usual, adjust the variable name of ``MOD_MUTE1_ALG0_MUTEONOFF_ADDR`` to match your exported files.

Reading Mute Values from the SigmaDSP
-------------------------------------

Mute values are stored in decimal format (8.24 or 5.23), so use the SIGMA_READ_REGISTER_FLOAT function to get the current value.

.. code:: cpp

   double mute_state = SIGMA_READ_REGISTER_FLOAT(MOD_MUTE1_ALG0_MUTEONOFF_ADDR);
   if (mute_state == 1) {
    Serial.println("System is Unmuted");
   }
   else if (mute_state == 0) {
    Serial.println("System is Muted");
   }
   else {
    Serial.println("Mute value is not 0 or 1");
   }

Writing Mute Values to the SigmaDSP
-----------------------------------

To mute the output:

.. code:: cpp

   SIGMA_WRITE_REGISTER_FLOAT(MOD_MUTE1_ALG0_MUTEONOFF_ADDR, 0);

To unmute the output:

.. code:: cpp

   SIGMA_WRITE_REGISTER_FLOAT(MOD_MUTE1_ALG0_MUTEONOFF_ADDR, 1);

.. |mute.jpg| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/toolbox/volumecontrols/mute.jpg
