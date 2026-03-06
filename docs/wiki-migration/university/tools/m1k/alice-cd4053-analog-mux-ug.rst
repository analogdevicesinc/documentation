Multichannel analog inputs for the ADALM1000 Using the CD4053
=============================================================

The two analog input channels of the ADALM1000 (M1k) provide a high input impedance and wide dynamic range which is very helpful for many of the measurements that students would be making around their laboratory activities. However, there are only the two analog inputs. Often, there are many more than two signals in the circuit or system under investigation that the students would like to monitor. Or there could be a number of low bandwidth sensors, such as ambient temperature or light levels around a room, that need to be measured or monitored over a long duration of time when gathering experimental data. Any number of external analog multiplexer integrated circuits could be used to expand the number of voltage input channels. The widely available CD4053 triple 2-Channel analog multiplexer IC can be used can be used for this purpose. In addition the PDIP versions of the MAX4619 and MAX4583 are pin compatible with the industry-standard 74HC4053.

The rest of this document provides the connections needed for use with the ALICE desk-top External Analog Mux option (as of May 2021 version release).

Alternating Sweep Modes
-----------------------

The external analog Mux interface in the ALICE desktop uses a technique common in analog CRT oscilloscopes (with a single electron beam) where multiple input channels are switched to the beam deflection circuits on alternating sweeps. This trick requires periodic signals and that each sweep is triggered from or synced to the same input signal. In this case the triggering signal will be channel A which is not multiplexed. This could be either the AWG generator output of channel A or an external signal input to the AIN pin in Split I/O mode. The multiplexer output is connected to the BIN pin and channel B is set to Split I/O mode to allow access to the AWG B output separate from the multiplexed signals.

The analog multiplexer is powered from the fixed +5 V supply on the M1k analog connector which will limit the allowed range of analog input voltages to be within the same 0 to +5 V supported by the M1k analog inputs. External resistor voltage dividers connected between the signal being measured and the Mux switch inputs are of course possible for measuring larger voltage signals.

The first configuration of this multiplexer uses all three of the 2 to 1 multiplexers in the CD4053 to switch up to four different signals into the M1k BIN pin, as shown in figure 1. The green labels indicate connections to the 8 pin analog connector on M1k. The light blue labels indicate connections to the 6 pin digital connector on M1k. The red, orange, purple and yellow labels for the Mux inputs match the colors of the controls in figure 2. Digital outputs PIO 0 and PIO1 are used by the software to select between the four mux channels on alternating sweeps. The PIO 2 digital output controls the Mux Inhibit input. The four Mux input signals along with AIN provides a total of five scope voltage traces. This configuration can be used with or without turning on AWG Sync. When the AWG Sync mode is off the AIN signal waveform can be used as the trigger signal. The CHA or CHB current waveforms can of course also be used as a trigger source.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Analog multiplexer Single Mux Alternate Sweep Configuration


How to set the External Analog Mux control settings for this configuration is shown in figure 2. Four mux channels are being used, any or all of the traces can be enabled. The Dual Mux check box should not be checked (off). The Alternate Sweep radio button should be selected.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Single Mux Alternate Sweep Control Settings


In a second configuration shown in figure 3, two Mux channels in the CD4053 can be used to multiplex two input signals into the AIN for a total of four scope voltage traces. This configuration can only be used in the Sync AWG mode where the scope traces will be triggered at the start of each AWG output sweep.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Dual Mux Alternate Sweep Configuration


How to set the External Analog Mux control settings for this configuration is shown in figure 4. All four mux channels are being used and any or all of the traces can be enabled. The Dual Mux check box should be checked (on) because two (dual) mux channels are being used. The Alternate Sweep radio button should be selected.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4, Dual Mux Alternate Sweep Control Settings


Chopping Modes
--------------

A second Mux interface mode in the ALICE desktop uses another technique common in analog CRT oscilloscopes where two input signal are switched or chopped very quickly to the beam deflection circuits. In the case of the M1k we have a sampling system at 100 KSPS and we can use a square wave from the AWG channel A output to drive the Mux control input at ¼ the system sample rate, or 25 KSPS. Thus each Mux input “gets” two samples. The software ignores the first of the two samples to allow for settling time and uses the second sample as the data. The software also up-samples the 25 KSPS data back to 100 KSPS using a 4X digital interpolation filter. The software automatically configures the channel A AWG settings. Once set these should not be changed while using the Chop Sweep mode.

The connections for this Mux chopping mode are shown in figure 5. Two Mux channels in the CD4053 are used to multiplex two signals into the AIN and BIN inputs for a total of four scope voltage traces sampled at 25 KSPS. The channel A AWG output is used to drive the mux so it is not available for other uses but the channel B AWG output can be used for any purpose. So in this configuration one of the AWG channels is traded off for getting the third and fourth input signals.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Analog multiplexer Chop Sweep Configuration


How to set the External Analog Mux control settings for this configuration is shown in figure 6. Four mux channels are being used, any or all of the traces can be enabled. The Dual Mux check box should be checked (on). The Chop Sweep radio button should be selected.

It is best to use the Chop Sweep mode with the AWG Sync enabled to insure that things stay in proper phase alignment. With the AWG Sync enabled the AWG A chopping square wave output will remain in the proper phase relation to the input samples each time the AWG B waveform settings are changed. Once the AWG B settings are changed and everything is re-synced the AWG Sync can be turned off to run in Continuous mode to speed up the screen refresh rate. If the AWG B settings are changed you need to switch on AWG Sync temporarily to re-sync the chopping signal.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, Mux Chop Sweep Control Settings


It is also important to note that, like in figure 1, the AIN input can used independent of the Mux switch to provide one input voltage measurement at the full 100 KSPS. In the software the standard (non-multiplexed) controls for the CA-V trace are grayed out to remind the user that the controls in the External Analog Mux controls are active. However the green CA-V trace can still be selected with the Dual Mux mode check box not selected (off). The main screen gray CA controls will still function to adjust that trace.

In the Chop Sweep mode any of the four Mux channels can be used as the trigger input signal. Clicking on the Chop Mode Trigger Drop down menu button displays a list of the inputs to select from, as shown in figure 7. Triggering from “None” is also an option. When in the Chop Sweep mode the Trigger input selection Drop down list in the Main Scope Window should be set to none. When entering the Chop Sweep mode the software will set this for you.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-ltc1043-analog-mux-fig7.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 7, Mux Chop Trigger Settings


Building the Mux
----------------

The wiring connections to the CD4053 are relatively simple and can be often built on the Solder-less breadboard along with the rest of the experiment circuitry. However, this might not always be a workable solution so a small `PCB adapter <:doc:`/wiki-migration/university/tools/adalm1000/accessory-boards-index`>`__ has been designed. Figure 8 is a rendering of the top of the PCB.

.. container:: centeralign

   Figure 8, CD4053 multiplexer PCB top


Be Aware when using Chop Sweep Mode
-----------------------------------

**Here is something to be aware of when using the Mux in Chop Sweep mode.**

The Mux switches in conjunction with the 100 pF input capacitance of the BIN pin (and AIN) form a rudimentary Sample and Hold circuit (see figure 1 in the :doc:`Track and Hold Amplifier Lab </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-tha-lab>`). When the first Mux switch is closed the input capacitance is charged up to the voltage on that Mux input. When the first switch is opened and the second switch to the other Mux input is closed the input capacitance is still charged to the first Mux input voltage. If the second Mux input is floating the first input Mux voltage (or most of it) will still be on the input capacitance and appear in the trace of the second Mux channel. Unless the second Mux input is driven by a source with low enough impedance to discharge / recharge the input capacitance to the new voltage.

The Mux switches in conjunction with the 100 pF input capacitance of the BIN pin (and AIN) also form a switched capacitor resistor ( see this lab on :doc:`switched capacitor circuits </wiki-migration/university/courses/alm1k/alm-signals-labs/alm-switched-cap-filter-lab>` ). This switched capacitor resistor appears across the pair of Mux inputs as shown in figure 9. In the case of a switched capacitor resistor we know that the apparent value of the resistance is:

:math:`R = 1 / (C F)`

Where in this case C is the 100 pF M1k BIN input capacitance and F is the 25 KHz chopping frequency. This calculates to the equivalent of a 400 KΩ resistance. So effectively the signal attached to one Mux input is loaded by a 400 KΩ resistor connected to the signal connected to the other Mux input.

.. image:: https://wiki.analog.com/_media/university/tools/m1k/alice-cd4053-analog-mux-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, Basic Switched Capacitor Resistor


Both of these issues can of course be gotten around by adding a high impedance unity gain buffer amplifier (non-inverting op-amps) between the measured signals and the Mux inputs.
