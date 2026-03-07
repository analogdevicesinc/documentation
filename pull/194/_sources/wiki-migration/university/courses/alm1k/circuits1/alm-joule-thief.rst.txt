Activity: DC-DC Boost Converter, For ADALM1000
==============================================

Objective:
----------

The object of this activity is to explore an inductor based circuit which can produce an output voltage which is higher than the supplied voltage. This class of circuits is referred to as DC to DC converters or boost regulators. In this activity the voltage from a 1.5 V supply (alkaline battery) will be boosted to a voltage high enough to drive two LEDs in series.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the ALM1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the ALM1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H.

Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I, CB-I for the current waveforms.

The circuits used in this Lab activity while generally low current can potentially produce voltages beyond the 0 to 5 V analog input range of the ALM1000. :doc:`Input voltage divider </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>` and AC coupling techniques as discussed in the document on ALM1000 analog inputs would be required to measure these voltages. Refer to the document to construct and use input voltage dividers as necessary when preforming these experiments with the ALM1000.

Background Basics:
------------------

When the current flowing in an inductor is quickly interrupted a large voltage spike is observed across the inductor. This large voltage spike can in fact be useful in some cases. One example is the DC to DC boost converter, which is a circuit that can create a larger DC voltage from a smaller one with very high efficiency. The basic idea is to combine an inductive spike generator (L\ :sub:`1` and Q\ :sub:`1`) with a rectifier circuit (D\ :sub:`1` and C\ :sub:`1`) to convert the repetitive voltage spikes into a DC or constant voltage as depicted in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Simple DC-DC booster circuit


When the transistor is turned on, current flows from the 1.5 V source into the inductor, energy is stored in the magnetic field. When the transistor is abruptly turned off the stored energy has to flow back out of the inductor and the voltage at the collector spikes up higher than the 1.5 V supply. When that happens the diode D\ :sub:`1` is forward biased and current will flow from the inductor to charge up the storage capacitor C\ :sub:`1`. When the collector voltage subsequently drops below the voltage on the capacitor, the diode is reverse biased and the output voltage remains constant. Just as in the chapter on AC power supplies, the output capacitor must be sized appropriately to minimize the ripple relating to the current flowing in the load, the two LEDs in this example. We show a small capacitor here and hence the circuit will not be able to source a large output current.

There are many underlying fundamental concepts that could be explored before doing this lab activity to help better understand the operation of what, on the surface at least, looks like a fairly simple circuit. Here are some of the other lab activities that can be performed in support of this lab:

-   :doc:`Parallel LC Resonance and energy storage </wiki-migration/university/courses/alm1k/circuits1/alm-cir-lc-resonator>`
-   :doc:`Multi-winding Transformers </wiki-migration/university/courses/alm1k/alm-lab-transformers>`
-   :doc:`PN Diode I/V curves </wiki-migration/university/courses/alm1k/alm-lab-2>`
-   :doc:`Diode Rectifiers </wiki-migration/university/courses/alm1k/circuits1/alm-cir-diode-rectifier>`
-   :doc:`BJT Device I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4>`
-   :doc:`BJT Transistor as a switch </wiki-migration/university/courses/alm1k/alm-lab-4s>`

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard and jumper wire kit

**For 1.5 V Battery substitute (figure 2):**

| 1 - 2N3904 small signal NPN transistor
| 1 – 47 Ω resistor (yellow purple black)
| 1 – 10 KΩ potentiometer
| 1 – 47 uF capacitor
| 1 – 0.1 uF capacitor (104)

**For DC to DC boost converter (figure 3):**

| 1 - 2N3904 small signal NPN transistor
| 1 – 1 KΩ resistor (brown black red)
| 1 - HPH1-1400L (Coilcraft Hexapath inductor)
| 2 – LEDs (any color will do)

**Optional Additional Equipment:**

| 1.5 V AA battery and holder
| Small handheld DMM

Simple "Joule Thief" DC/DC Converter:
-------------------------------------

Construction Directions:
~~~~~~~~~~~~~~~~~~~~~~~~

\**Step 1: \*\*

Note, if you have a 1.5 Volt battery (AA) and a battery holder with wires attached, you can skip this step and use the battery as the 1.5 V supply. Otherwise you will need to make the circuit shown in figure 2 to simulate a single cell battery. This circuit makes a 1.5 V power supply using the fixed 2.5 V power supply on the ALM1000. Build the circuit on one end of your solder-less breadboard being sure to leave space for the rest of this lab's circuits. Improved versions of a 1.5 V power supply can be found in Appendix II below.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, 1.5 Volt power supply


Once you have the 1.5 V supply constructed, you will need to adjust the potentiometer, R\ :sub:`POT`, such that the output is set to 1.5 V. Use one or the other of the ALM1000 inputs in Hi-Z mode to measure the voltage. (display the AVG voltage for the channel you choose). An optional DMM could also be used to measure the DC voltage. Note the dashed green box in figure 1 surrounding the ground connections. Later you will be measuring the current in ground for different sections of the circuit. The ground connections in figure 1 will always be connected directly to the ground of the ALM1000. The other sections of ground will, at various times, be either connected to the main ground or the CH-A connector pin on the ALM1000. So as you construct the circuit keep these “ground” connections separate, i.e. don't use one of the common power bus strips for all the “grounds”.

Temporarily connect one of your LEDs (Red, Green, or Yellow) from the 1.5 V output to ground. Be careful to note the polarity of the diode so it will be forward biased. Does it light up? Probably not very bright if at all since 1.5 V is generally not enough to turn on an LED. We need a way to boost the 1.5 V to a higher voltage to light a single LED let alone two LEDs connected in series. Disconnect the 1.5 V (or 2.5 V supply if using the circuit from figure 2) and remove the LED before moving to the next construction step.

**Step 2:**

Next, on your solderless breadboard construct the DC-DC boost circuit (so called Joule Thief) section as shown in figure 3.

The 6 winding HPH1-1400L inductor, pinout shown below, can be configured for 6 different inductance values depending on how many windings are connected in series. Connecting all 6 windings in series will give 36 times ( N\ :sup:`2` ) the inductance of a single winding (0.2 mH for the HPH1-1400L) or about 7 mH. 5 windings = 25 X 0.2 or about 5 mH, 4 windings = 16 X 0.2 or about 3.2 mH. See Appendix III at the end of this document for more information. For this circuit we need 2 sets of three windings connected in series. Note the winding polarity dots. It is very important that the winding polarity be connected as shown.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-hph1-1400l.png
   :align: center
   :width: 350px

The two ground connections in figure 3 for the emitter of transistor Q\ :sub:`1` and the LEDs will sometimes be connected directly to the ground of the ALM1000. At other times, they will either be connected to the main ground or the CH-A connector pin on the ALM1000 depending which branch current is being measured. So as you construct the circuit keep the ground connections so that it will be easy to separate them from the main ground connection bus i.e. use a jumper wire to the common power bus strips.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig3.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 3, DC to DC boost converter


Measurement Procedure:
~~~~~~~~~~~~~~~~~~~~~~

Start with the three sections of ground all connected to the main ALM1000 ground. With CH-B in Hi-Z mode you will be using it to observe various voltage waveforms around the circuit. The circuit is a free-running oscillator so you will need to enable triggering on the CB-V signal.

Using CH-B in Hi-Z mode observe and save the voltage waveforms seen at the following circuit nodes. First, the 1.5 V input source. Second, the “boosted” output, V\ :sub:`OUT`\ at the collector of Q\ :sub:`1` (also the top of LED\ :sub:`1`). Third measure the voltage seen at the left end of resistor R\ :sub:`1`, pin 6 of the inductor. Fourth, measure the voltage at the base of transistor Q\ :sub:`1`. By also using CH-A in Hi-Z mode two of the four circuit nodes can be observed at the same time. In the example below while using CH-B to view the boosted output waveform we are also using CH-A to observe the base voltage.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/base_voltage_free_run.png
   :align: center
   :width: 650px

.. container:: centeralign

   Boosted output voltage and Q\ :sub:`1` base voltage waveforms example


While the program is paused use the left mouse button to place two time markers as shown. The two time markers show the time for one cycle from when the transistor turns off, falling edge of base waveform, to the rising edge of the positive spike of the output. This is about 0.16 mSec or a frequency of 6316 Hz as shown in the CB Freq display.

You may want to save snap-shots of the voltage traces or save the VBuffB array to another temporary data array to be plotted later when you are making the current measurements.

Measuring Currents:
~~~~~~~~~~~~~~~~~~~

Now that we have measured all the interesting voltage waveforms associated with the circuit we need to measure the relevant current waveforms as well.

If we set the Channel A voltage to a DC value we can use it as an AC (and DC) ammeter with one end connected to the set DC voltage. The DC voltage we set could be a supply voltage or it could be 0V and we would then be measuring the current flowing into or out of ground.

The first current we will measure is the current flowing in the inductor from the 1.5 V source. Set AWG CH-A to SVMI mode and Shape to DC with a Max value of 1.5 V, to match the 1.5 V from the 1.5 V AA battery, if you are using that. Because the shape is set to DC the Min and frequency values are ignored. Disconnect the top end of the inductor, pins 1 and 12, from the 1.5V supply and connect it to CH-A. Under the curves menu be sure to select the CA-I trace to be displayed.

Hit the run button and you should see the same boosted output waveform on the CB-V trace, the constant 1.5V DC voltage on the CA-V trace and the inductor current on the CA-I trace. Adjust the CA-I vertical scale as needed to fit the peak amplitude of the current on the screen.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/supply_current_free_run.png
   :align: center
   :width: 650px

.. container:: centeralign

   Waveform display of the boosted output, 1.5 V input and supply current


Note the time when transistor Q\ :sub:`1` is on and when Q\ :sub:`1` is off and the current in the inductor. Take a snap-shot of the CA-I current trace for future reference (or save the IBuffA array into another array so it can be plotted later).

Disconnect the inductor pins from CH-A and reconnect them to the 1.5V supply (battery). Now we want to measure the currents in the two ground branches. First, disconnect the emitter of Q\ :sub:`1` from the main ground bus and connect it to CH-A. Set the CH-A Max value to 0 (the same voltage as ground).

Hit the run button and you should again see the same boosted output waveform on the CB-V trace, the constant 0V DC voltage on the CA-V trace and the Q\ :sub:`1` emitter current on the CA-I trace. Adjust the CA-I vertical scale as needed to fit the peak amplitude of the current on the screen. Note the polarity (direction) of the current. Display the saved inductor current trace and compare the two. What part of the inductor current flows in Q\ :sub:`1` and where in time does it flow? Save the CA-I trace of the emitter current. (or save the IBuffA array into another array variable).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/emitter_current_free_run.png
   :align: center
   :width: 650px

.. container:: centeralign

   Waveform display of the boosted output, 1.5 V input and emitter current


Now we will measure the current in the LED load. Disconnect the emitter of Q\ :sub:`1` from CH-A and reconnect it to the main ground bus. Disconnect the ground end of the LEDs from the main ground bus and connect it to CH-A.

Hit the run button and you should again see the same boosted output waveform on the CB-V trace, the constant 0V DC voltage on the CA-V trace and the LED load current on the CA-I trace. Adjust the CA-I vertical scale as needed to fit the peak amplitude of the current on the screen. Note the polarity (direction) of the current. Display the saved inductor current trace and compare the two. What part of the inductor current flows in LED load and where in time does it flow? Save the CA-I trace of the LED current. (or save the IBuffA array into another array variable).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/led_current_free_run.png
   :align: center
   :width: 650px

.. container:: centeralign

   Waveform display of the boosted output, 1.5 V input and LED current


Conservation of current says that the sum of the current in Q\ :sub:`1` and the LEDs should be the same as the current in the primary section of the inductor. Use the Math plotting function to plot the sum of the saved emitter and LED data buffers. Compare this to the measured inductor current waveform.

What is the maximum peak and average voltage of the “boosted” output? What is the p-p seen on the waveform? What is the maximum peak and average current in the inductor, the transistor and the LEDs and what is the p-p value seen in the currents? Record the values in your lab report.

How does this circuit work?
---------------------------

To better investigate how the circuit operates we next need to break (open) the feedback loop and stop the circuit from oscillating. We can then inject a test signal at the base of the transistor as shown in figure 4. Add the modifications shown in figure 4 to your circuit.

The voltage waveform on the secondary side of the transformer might go outside the 0 to +5 V range of the ALM1000 input. To observe the voltage waveform we can AC couple the signal and use a :doc:`DC restoration circuit </wiki-migration/university/courses/electronics/text/chapter-7>`, using a diode and adjustable DC voltage from a voltage divider, to set the DC level of the AC coupled waveform to an appropriate value for the ALM1000 input range.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig4.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 4, Configured to measure Q\ :sub:`1` base current


Start with a switching frequency of 2 kHz which is supplied by AWG Channel A, CA-V. Set the Min value to 0 and the Max value to 1.5 (enough to turn on Q\ :sub:`1`). Set the mode to SVMI and the shape to square. Set the duty cycle to 40%.

First with the CHB input connected to the boosted output you should see something like the next screen shot.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/base_current.png
   :align: center
   :width: 650px

.. container:: centeralign

   Measuring the base current of Q\ :sub:`1`\


We see that the base current, light blue trace, peaks as the transistor first turns on and then levels off. The collector voltage at first goes very close to ground and stays below 0.5 V for some time. As it approaches 0.5 V it then rises fairly rapidly to nearly the 1.5 V battery voltage. When the transistor turns off we see a negative spike in the base current similar but opposite to the positive spike in the base current when the transistor turned on.

We need to also observe the collector current while this is happening. First take a snap-shot of the traces for reference and display the saved RB-V trace. Disconnect the 1.5V battery from pin 12 of the inductor. Connect the CHB AWG output to pin 12. Set CHB to SVMI mode, Shape DC, Max value to 1.5 V. Turn on the CB-I trace (all four traces should be selected at this point). Hit the Run button. You should now see something like the next screen shot.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/collector_current.png
   :align: center
   :width: 650px

.. container:: centeralign

   Measuring the collector current of Q\ :sub:`1`\


Now we can see that the collector current (yellow trace), which is also the current in the inductor, ramps up to some value and levels off at about the same time that the collector voltage (dark orange) rises above 1.0 V. The inductor current ramps back down to zero when the transistor is turned off. To better understand the relationship between the base current and collector current as the collector emitter voltage changes in might be helpful to preform the Beta vs collector voltage section of the :doc:`BJT Device I/V curves </wiki-migration/university/courses/alm1k/alm-lab-4>` lab activity at this point.

In the meantime it is possible to calculate the β and plot it during the time the transistor is turned on. Under the Math drop down menu click on Enter Formula. Enter the following to calculate β:

IBuffB[t]/IBuffA[t]

Under the Math drop down menu click on Math Axis and change it to I-B to use the yellow axis for the Math trace. Under the Math drop down menu click on Formula to display the Math trace. You should now see something like the following.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/calculated_beta.png
   :align: center
   :width: 650px

.. container:: centeralign

   Calculating Q\ :sub:`1` Beta (magenta curve)


You might want to change the duty cycle of AWG A so that it spends more time with the transistor turned on. The calculated β, I\ :sub:`C`/I\ :sub:`B`, when the transistor is off is rather meaningless. With the transistor off both I\ :sub:`C` and I\ :sub:`B` should be zero.

**Find Minimum Cycle Time**

With pin 12 connected back to the 1.5 V battery and Channel B in Hi_Z mode and connected to the output voltage, if we adjust the width of the CH-A pulse such that it is just wide enough to turn on Q\ :sub:`1` long enough for it to come out of saturation and the current in the inductor to stop increasing we have a display something like this.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/base_current_min_width.png
   :align: center
   :width: 650px

.. container:: centeralign

   Measuring minimum cycle time


Now we can measure the minimum amount of time for one cycle of the circuit. While the program is paused use the left mouse button to place two time markers as shown. The two time markers show the time from when the transistor is turned on to when the positive spike of the output returns to the battery voltage of 1.5 V. This is about 0.157 mSec or a frequency of 6370 Hz. Compare this result to the frequency you measured earlier. Explain why they should be the same?

**The Feedback Signal**

Now we want to examine the feedback signal. Put the CHA duty cycle back to 40%.

Now move the CHB input to pin 6 of the transformer. Notice the following about the waveform. It looks like an inverted version of the boosted output waveform, note the winding polarity dots. Also note that it too has the flat (constant) portions of the signal centered at the 1.5 V battery voltage. Because of the larger negative going spike the waveform goes below 0V (ground). We can shift the signal up so we can see the negative peak by moving the CHB input to the other end of the AC coupling cap (end of diode D\ :sub:`1`).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/base_feedback_signal.png
   :align: center
   :width: 650px

.. container:: centeralign

   Feedback signal waveform goes below ground


Adjust the voltage divider pot until the signal is more centered in the display area. To correct the grid labels for CHB first adjust the channel offset value to 1.0 and the CHB position control to 1.5.

|image1| |image2|

Adjust the voltage divider pot until the flat portion of the signal is centered on the 1.5 V battery voltage on the display grid. Like the next screen shot. Now we can see that the negative peak is at about -1.0 volts. The peak-to-peak voltage swing on pin 12 should be the same as the peak-to-peak voltage swing on pin 7 (collector of Q\ :sub:`1`) because the winding ratio is 3:3 (or 1:1).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/base_feedback_signal_ls.png
   :align: center
   :width: 650px

.. container:: centeralign

   Feedback signal level shifted to show negative peak


As additional investigation.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following modifications to the basic circuit are submitted for additional investigation in to how to make DC-DC boost circuits.

New Materials for figure 5:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1 – 470 Ω resistor (yellow purple brown)
| 1 – 5 KΩ potentiometer

Changing the value of resistor R\ :sub:`1` changes the oscillation frequency. Add a 5 KΩ potentiometer in series with a 470Ω resistor in place of R\ :sub:`1`, as shown in figure 5. Observe V\ :sub:`OUT` while adjusting the potentiometer. Why does changing the base resistor change the frequency?

Changing the 1.5 V supply voltage also changes the frequency. If you are using the circuit from figure 1 to generate the input supply voltage try adjusting the voltage. If you have been using a fixed 1.5 V battery substitute CHA set to DC mode as the input supply and try adjusting its voltage. How does the frequency change as the voltage is increased or decreased and why? The number of windings used in the primary and secondary of L\ :sub:`1` also changes the oscillation frequency. Experiment with using different combinations of the 6 windings in the HPH1-1400L. In the previous schematics there were 3 windings in series for both the primary and secondary or a 3:3 ratio. Try 2:4 and 4:2 combinations or others and see how the oscillation frequency and the circuit waveforms change for the different ratios.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig5.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 5, Adding a variable resistor to adjust the frequency.


Materials for figure 6:
~~~~~~~~~~~~~~~~~~~~~~~

| 1 - 2N3904 small signal NPN transistor
| 1 - 2N3906 small signal PNP transistor
| 1 – 1 KΩ resistor (brown black red)
| 1 – 4.7 KΩ resistor (yellow purple red)
| 1 – 47 KΩ resistor (yellow purple orange)
| 1 – 5 KΩ potentiometer
| 1 – 4.7 nF capacitor (472)
| 1 - HPH1-1400L (Coilcraft Hexapath inductor)
| 2 – LEDs (any color will do)

The second coupled winding of L\ :sub:`1` provides the necessary inversion in the feedback signal to cause the circuit to oscillate. An alternative to the two winding inductor is to include a common emitter inverter stage instead. In figure 6 we see that a PNP common emitter inverting stage, Q\ :sub:`2`, has been used. The output signal at the collector of Q\ :sub:`1` is AC coupled to the base of Q\ :sub:`2` by C\ :sub:`1` and the series combination of R\ :sub:`2` and the potentiometer. The RC time constant of this feedback network sets the oscillation frequency. Adjusting the potentiometer changes the frequency.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, Using PNP stage and capacitor feedback


Materials for figure 7:
~~~~~~~~~~~~~~~~~~~~~~~

| 2 - 2N3904 small signal NPN transistors
| 1 – 470 Ω resistor (yellow purple brown)
| 1 – 4.7 KΩ resistor (yellow purple red)
| 1 – 10 KΩ resistor (brown black orange)
| 1 – 5 KΩ potentiometer
| 1 – 10 nF capacitor (103)
| 1 - HPH1-1400L (Coilcraft Hexapath inductor)
| 2 – LEDs (any color will do)

Similarly, an NPN common emitter inverting stage can be used as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-fig7.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 7, Using NPN stage and capacitor feedback


Sampling effects.
-----------------

In digital sampling systems like the ADALM1000 a continuous analog input signal is sampled at discrete time intervals, t\ :sub:`s`\ =1/f\ :sub:`s`, which must be carefully chosen to ensure an accurate representation of the original analog signal. In the case of the ALM1000 samples are taken every 10 uSec or 100,000 samples per second. It becomes very clear exactly when the samples are taken if we change the traces to be displayed as zero-order hold rather than connecting the sample points with straight lines. Under the Options drop down menu select the Z-O-Hold option. The following screen shot example shows the waveform on the output (CH-B) and pin 6 of the inductor (CH-A) in zero-order hold mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/zero-order-hold-free_run.png
   :align: center
   :width: 650px

.. container:: centeralign

   Zero-Order Hold display


Now we can more easily see how many samples are taken for each cycle of the circuit. For some cycles there are 15 samples and for some cycles there are 16 samples. There is never the same exact number of samples per cycle because the oscillator frequency is not an exact fraction of the 100 KHz of the ALM1000 nor is it locked or synchronized with it. It is also important to point out that the channel B samples are taken 5 uSec (half of the sample time) after the channel A samples.

It is clear that the more samples taken per cycle (a faster sampling rate), the more detailed the digital representation, but if fewer samples are taken per cycle (a lower sampling rate), a point is reached where information about the signal is actually lost, :adi:`Sampled Data System Design <media/en/training-seminars/tutorials/MT-002.pdf>`.

The analog voltage signals can be any value between the samples. To fill in the details between these samples we would normally need to sample faster. However, in the case of repeating waveforms like this we can observe that a slightly different set of points along the cycle are sampled each cycle. Note for example in the above screen shot the positive and negative peaks of the traces have slightly different values each cycle. We can use this to our advantage to fill in the details of the waveform if we can figure out how to assemble one representative cycle from the captured samples of many cycles. This technique of resorting the samples is called equivalent time sampling or ETS. For the most recent details on using this software feature always refer to the latest version of the :doc:`Equivalent Time Sampling Users Guide </wiki-migration/university/tools/m1k/alice/advanced-equivalent-time-sampling-guide>`. Appendix I explains how this is done in the ALICE desktop software. We can use the ETS feature by opening the ETS control screen like this.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/ets_controls_1.png
   :align: center
   :width: 200px

.. container:: centeralign

   ETS controls.


We know the input frequency is 6348 Hz so we need to pick a Divide Factor and Freq Multiplier that gives us a frequency as close to 6348 Hz as possible. In this case a Divide Factor of 47 and a Freq Multiplier of 3 gives us a frequency of 6383 Hz. The traces with the ETS enabled and still displayed in Z-O-Hold mode are shown next.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/zero-order-hold-free_run_ets.png
   :align: center
   :width: 650px

.. container:: centeralign

   ETS Zero-Order Hold display


The signal frequency has now been shifted down to about 1700 Hz and there are now about 57 samples per cycle vs the 16 samples per cycle before. We are now able to see much more detail in the waveforms. The equivalent sample rate is now (6348/1700)x100KSPS or about 364 KSPS. If we use the frequency adjustment ability shown in figure 5 we could fine tune the oscillator frequency and get even higher equivalent sample rates and get very detailed trace displays like this example.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/supply_current_free_run_ets.png
   :align: center
   :width: 650px

.. container:: centeralign

   Output voltage and supply current waveforms using Equivalent Time Sampling


In this example we have down converted the input frequency from the 6.3 KHz to 423 Hz for an equivalent sample rate of (6348/423)x100KSP or about 1.5 MSPS.

Appendix I: Using Equivalent Time Sampling with the ADALM1000
-------------------------------------------------------------

The ALICE 1.3 desktop software suite for ADALM1000 includes an option that implements a form of equivalent time sampling or ETS. For the most recent details on using this software feature always refer to the latest version of the :doc:`Equivalent Time Sampling Users Guide </wiki-migration/university/tools/m1k/alice/advanced-equivalent-time-sampling-guide>`.

**Periodic waveforms**

The key to understanding how this "magic" works is to realize that many of the kinds of signals that an oscilloscope user might like to measure are periodic. That is, they have a fixed pattern or shape that repeats periodically. Indeed it is almost impossible to see any other type of signal with an ordinary (non-sampling) analog oscilloscope. A digital oscilloscope like ALM1000 can of course capture and store any non-periodic waveform at the base real time sample rate. Often the analog signal chain and the ADC used in a scope like the ALM1000 have more usable bandwidth than some fraction of the sample rate.

**Sub-sampled waveform capture**

If you display a buffer of raw data captured from a signal with a higher frequency than even one tenth the sample rate (10 samples per cycle), you will still see a waveform; just not much detail. If the sampling frequency is not exactly an integer fraction (or multiple) of the input frequency each sample represents a unique point somewhere along the repeating waveform. For example if we look at the following figure we see a case where the sample frequency is slightly slower than the input frequency, by a factor of 19/20. So from the top graph we see that 20 unique points are obtained from 20 different cycles of the input signal. If these sample points are then assembled in the proper order we get the graph on the bottom.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/ets_example.png
   :align: center
   :width: 600px

**Sub-sampling with a ratio of 19/20.**

In this simple example the points are just plotted in the order they are taken. If, on the other hand, the ratio of the input frequency and the sample rate were the other way around, 20/19, then each sample would come earlier in each cycle and it would look like time was going backward if the points were plotted in the same order. To make time increase the order of the points would need to be reversed. This sub-sampling has the same effect as a down conversion mixer shifting the input to a lower frequency, even DC for certain ratios like 1, or 2 or 3 etc.

This technique assumes that either the sample rate or the input frequency or both are adjustable such that a known ratio can be calculated. In the case of the ALM1000 we have only the fixed sample rate of 100 KSPS to work with.

Fortunately it is possible to use a different approach. Instead of trying to set the exact ratio, the fixed 100 KSPS sampling rate is used and if we know the frequency of the input signal an actual ratio is then calculated. With this known ratio it is very easy to find out which sample within the record has what delay (or its position) within the input waveform period.

**The ETS controls in ALICE.**

To control all this ALICE has an ETS window. The real time sample rate of 100000 is shown at the top as a reminder. Next is a check box to turn on and off ETS. Next you enter the Divide factor, in this case 4 was used. From the divide factor entered ALICE picks an offset and record length to best display the input signal. The base or minimum frequency is shown, in this case 1/4 of the sample rate or 25,000 Hz. This is the frequency that will be shifted to DC. The user can then enter the frequency multiplier. Multiply factors from 1 to 75 are allowed in the program. The multiplied value is displayed. This does not really change anything in how ALICE displays the signal. It is handy to use this value when setting the frequency of the input source.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/ets_controls_2.png
   :align: center
   :width: 200px

.. container:: centeralign

   ETS controls


As was pointed out earlier if the input frequency is above or below the Base frequency (the frequency that will be shifted to DC) the order of the samples will be either forward or reversed in time. These controls allow the user to pick which way to order the data.

There is a major complication in the case of the ALM1000 and how the A and B channels are sampled. The A channel samples first every 10 uSec (100KSPS) and channel B samples second, 5 uSec later, between the channel A samples. This is not so big a deal in real time sample mode and ALICE handles this when drawing the traces. But in ETS mode this 5 uSec difference causes the channel B data to shift all over with respect to channel A depending on the frequency of the input and to what frequency it is down shifted to. Think of this 5 uSec difference with respect to the equivalent time sampling rate which might be many MHz.

To adjust for this difference there is a place to enter a shift factor for channel B. This shift factor is in sample points. The best way to adjust this is to connect both channels to the same signal and adjust the value until the two waveforms are on top of each other. A positive number shifts the trace to the right and a negative one shifts it to the left. Either might be necessary depending on the Forward or Reverse data order. Then move channel B to the other signal you wish to observe.

Appendix II: Improved 1.5V sources
----------------------------------

Materials in addition to figure 2:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 1 - 2N3906 small signal PNP transistor
| 1 – 470 Ω resistor (yellow purple brown)

The output impedance (load regulation) of the simple emitter follower in figure 1 can be improved through the addition of feedback. Shown in figure A1 is a follower circuit where the single NPN (Q\ :sub:`1` is a 2N3904) transistor is replaced with a NPN/PNP compound transistor (Q\ :sub:`2` is a 2N3906). The load regulation of a single transistor follower is a function of how much the V\ :sub:`BE` changes as the emitter current changes. In the case of the compound transistor configuration a small increase in the current of Q\ :sub:`1` is amplified and causes a much larger current to flow in PNP transistor Q\ :sub:`2`.

There is also the added benefit that the base current of Q\ :sub:`1` is now much smaller and its effect on the voltage divider of potentiometer R\ :sub:`POT` is much smaller.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-figa1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A1, Improved follower


Even better load regulation can be achieved by using an op-amp to provide high gain. As shown in figure A2, the output of the op-amp drives the base of transistor Q\ :sub:`1` to whatever bias voltage is needed to maintain the emitter voltage (negative input of the op-amp) equal to the voltage set at the positive input of the op-amp by the voltage divider. The circuit can essentially source current up to the maximum current limit of the transistor or the +5V power supply with very little change in the +1.5V output.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/alm-joule-thief-figa2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure A2, Precision follower


Appendix III: Formulas used to calculate electrical characteristics of multi-winding coupled inductors or transformers:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manufacturer datasheets list certain electrical characteristics for the devices. Probably the most important for our purposes is the winding inductance. For power conversion applications the DC resistance (DCR), the maximum rms current (I\ :sub:`rms`), and saturation current I\ :sub:`sat` are also specified.

\**Connecting windings in series: \*\*

For higher inductance, multiple windings (W\ :sub:`N`) can be connected in series. As the inductance increases, energy storage and I\ :sub:`rms` remain the same, but DCR increases and I\ :sub:`sat` decreases.

Inductance = Inductance\ :sub:`table` × (W\ :sub:`N`)\ :sup:`2`

Note: this Wn\ :sup:`2` factor is only valid when the coupling factor between windings is exactly ( or very nearly ) one. A more general formula is L\ :sub:`T` = L\ :sub:`1` + L\ :sub:`2` + 2M

| DCR = DCR\ :sub:`table` × W\ :sub:`N`
| I\ :sub:`sat` = (I\ :sub:`sattable` × 6) ÷ W\ :sub:`N` (connected in series)
| I\ :sub:`rms` = I\ :sub:`rmstable`

Where Inductance\ :sub:`table`, DCR\ :sub:`table`, I\ :sub:`sattable`\ and I\ :sub:`rmstable`\ come from the manufacturer's datasheet.

\**Connecting windings in parallel: \*\*

To increase current ratings, multiple windings (W\ :sub:`N`) can be connected in parallel. DCR decreases, current ratings increase, and inductance remains the same.

| Inductance = Inductance\ :sub:`table`
| DCR = 1 ÷ [W\ :sub:`N` × (1 ÷ DCR\ :sub:`table`)]
| I\ :sub:`sat` = (I\ :sub:`sattable` × 6) ÷ W\ :sub:`N` ( connected in parallel )
| I\ :sub:`rms` = I\ :sub:`rmstable` × W\ :sub:`N`

`Data Sheet <http://www.coilcraft.com/pdfs/doc157_SigXfrmApp.pdf>`_

**Resources:**

-  LTSpice files: :git-education_tools:`m1k/ltspice/simple_joule_thief_ltspice`
-  Fritzing files: :git-education_tools:`simple_joule_thief_bb <m1k/fritzing/simple_joule_thief-bb>`

**For Further Reading:**

| `Boost Converter <https://en.wikipedia.org/wiki/Boost_converter>`_
| `Joule Thief <https://en.wikipedia.org/wiki/Joule_thief>`_
| `Compound Transistor <https://en.wikipedia.org/wiki/Sziklai_pair>`_

**Return to ALM Lab Activity** :doc:`Table of Contents </wiki-migration/university/labs/circuits>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/chb-offset-adj.png
   :width: 150px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/alm1k/circuits1/chb-pos-adj.png
   :width: 150px
