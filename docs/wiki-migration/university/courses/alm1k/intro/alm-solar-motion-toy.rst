Activity: Investigating A Solar Powered Motion Toy
==================================================

Objective:
----------

The objective of this activity is to investigate interesting bits of electronics hidden in everyday items. This activity requires some amount of soldering and mechanical construction.

Background:
-----------

Solar powered novelty items such as the dancing hula girl and other solar ornaments have become very inexpensive and common place. Looking from the outside, it consists of a small solar panel to harvest power from ambient light and some sort of electro-mechanical “motor” or pusher that makes her wiggle back and forth. A typical example, is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig1.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 1, Typical solar dancing hula girl


Inside the toy are mechanical levers connecting the upper and middle body parts to a small permanent magnet hanging just above a coil of very fine copper wire. The coil is offset slightly such that the magnet hangs directly over one side of the coil.

The complete circuit is shown in figure 2. There are a total of four electrical components. A small solar panel, a 470 uF 10 V electrolytic capacitor, an air core (300 Ω internal series resistance) inductor / pulse coil and a small circuit board with a black blob on it (see video listed below under **Going Further** for more details).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Solar powered motion toy circuit.


Under the epoxy blob is the integrated circuit chip. It sends correctly timed pulses to the coil and magnet combination. The integrated circuit is more or less just a low frequency oscillator which runs at approximately 1 Hz driving an open drain NMOS switch (output on pin 3 in figure 2) which periodically connects the coil to the – (negative) terminal. The circuit pulses the coil pushing the small magnet making it swing. When everything is in sync the hula girl dances. The 470 uF capacitor serves to store up the current from the solar panel and provide a slug a current when the coil is pulsed.

The small solar panel is made by Putian Weite Electronics Co. ,Ltd. From the company web site the device used is a low light, amorphous silicon type solar cell, shown in figure 3. VIMUN SC-3012-2A, 29.44mm×11.6mm×1.1mm, 4 cells. The following specifications were listed, 2.0 V open circuit, 9.0 uA short circuit, 1.5 V output, at 200Lux.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig3.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 3, Small Solar panel.


To better test the components the toy will need to be de-constructed into its constituent parts. Soldering cut up male pin jumper wires to the solar panel and circuit board, as shown in figure 4, makes connecting them to a solderless breadboard easier. It is recommended that you color code the jumper wires, especially on the small PC board, as shown. Green is used for the negative (ground), orange for the positive and white for the coil connection (output). The very fine wires from the coil of course are very difficult to solder to. To provide a solid surface to solder the fine wires of the coil to, a small scrap of copper clad circuit board can be glued to the plastic base. Solder the coil wires to that before adding the jumper wires. The polarity of the coil connections is important. If they get swapped the current pulses will push the swinging magnet in the wrong direction. The coil is glued to the plastic base and is not easily removed without damaging it, so it is left as is.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-toy-de-con.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 4, De-constructed parts.


So that’s all there is inside the dancing hula girl, but what else can we do with these parts to learn about electronics?

Materials:
~~~~~~~~~~

| 1 – Solar toy (disassembled)
| ADALM1000 module
| Solderless breadboard
| 4 – Male to male jumper wires, different colors

Measuring Circuit Operation:
----------------------------

The first thing to do is take some measurements of the overall circuit under different conditions without the swinging magnet. Below is a table of the results powering the circuit in figure 2 from the DC output of AWG channel A of the M1k and the solar panel illuminated by a 60 W incandescent bulb.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig5.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 5, Supply voltage test circuit.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-tab1.png
   :align: center
   :width: 600px

Table 1.

It seems that the magnitude of the power supply voltage has a minimal effect on the oscillator frequency and pulse width. When using the solar panel the voltage across the capacitor sags to about 1 V when the coil is pulsed and then slowly re-charges to 1.4 V from the solar panel.

To further investigate the oscillator, reassemble the mechanical parts with the permanent magnet suspended over the coil but the electronics outside the case to observe the switching waveform across the coil as shown in figure 6. Power the circuit with AWG CHA set to DC 1.4V. Set AWG channel B to Hi-Z / Split I/O mode.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solor-toy-external.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 6, Reassembled test circuit.


Below in figure 7 is a screen capture of scope channel CHA, green trace, capturing the supply voltage at pin 1 (figure 5) and channel CHB, orange trace, capturing the voltage on the coil at pin 3 (figure 5).

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Coil waveform with magnet.


We first notice that the frequency is now more like 2.3 Hz. So clearly the swinging magnet is changing how the circuit functions. If you stop the magnet from swinging the frequency slows to the 0.8 Hz measured before. The next thing about the waveform in figure 7 we notice is that the coil voltage goes above the supply voltage for a short time. It is greater than the supply for about the same amount of time as the pulse is low, when the coil is energized. The coil voltage then swings back below the supply voltage before the next cycle starts. This extra voltage is induced in the coil by the magnet swinging over the coil. This induced voltage on pin 3 and the circuit’s sensitivity to the voltage with respect to the supply is acting as a feedback signal locking the oscillator to the natural frequency of the mechanical system and the swinging magnet.

In figure 8 we have a long persistence screen shot. Now we can see that the on period of the oscillator, when the coil is energized, remains constant but the off period changes over time due to possible noise on the signal when crossing the supply voltage and to stay in sync with the magnet as it swings.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Waveform persistence screen shot.


Other Things to investigate:
----------------------------

The circuit board is simply an oscillator and could be used for other purposes.

.. _materials-1:

Materials:
~~~~~~~~~~

| 1 – Red LED
| 1 - 100Ω resistor
| 1 – 10 kΩ resistor
| 1 – 10 uF capacitor
| 1 – 3.3 kΩ resistor

The IC on the circuit board makes a good LED flasher as well. Connect the LED and a series current limit resistor in place of the coil as shown in figure 9.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig9.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 9, Used as LED flasher


Measure the oscillator frequency and pulse width. You would think that the oscillator would operate at the same frequency independent of the load but using the circuit in figure 9 at 3 V and a red LED with a 100 Ω series resistor the frequency is 5.46 Hz with a pulse width of 17.5 mSec. With the LED load the voltage swing seen at pin 3 is from nearly 0 V (WRT pin 2) when the LED is on and about 1.2 V when off. This happens because the LED stops conducting when the voltage from pin 1 to pin 3 is less than the turn on voltage of the LED (about 1.8 V). For the coil load the voltage swings the full amount from 0 V to the supply voltage (about 3 V). This difference obviously has an effect on the oscillator frequency.

Further testing as shown in figure 10, using a just a 1 KΩ resistor as the load and AWG channels B (CHB) a variable power supply for the top of the resistor shows that the oscillator runs at this faster frequency until the variable supply (and thus the peak swing) was just a few 10s of mV less than the voltage on pin 1 (CHA voltage). The frequency and wave shape quickly transitions to the slower mode as the voltage reaches the supply value and beyond. Clearly the internal circuitry is sensing the output swing on pin 3 and does not fully reset unless the voltage reaches the supply.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig10.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 10, Testing effect of the voltage on pin 3.


To further test this external frequency locking, the test setup is reconfigured as shown in figure 11 to allow the injection of an external sinewave. The test is done with the magnet and mechanical parts removed. The injected signal is a 1.0 V p-p sine wave at 2.5 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig11.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 11, Injecting an external signal.


Figure 12 is a screen shot of the output waveform (orange trace) frequency and phase locked to the external injected 2.5 Hz sinewave (green trace). The period of the output pulse is 400 mSec or 2.5 Hz.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Oscillator locked to 2.5 Hz external signal.


Getting back to alternate uses, another resistor can be added to the LED flasher to make the voltage swing all the way up to the battery voltage as shown in figure 13. This will make the circuit flash at the slower 0.8 Hz rate. The added 10 KΩ resistor across the LED insures that the voltage at pin 3 goes to the battery voltage when off. Using a high value resistor will not add any significant extra current when on.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig13.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 13, Slow LED flasher.


Measuring Solar Panel Characteristics:
--------------------------------------

Also as in the Lab activity on the :doc:`Characteristics of Photovoltaic Solar Cells </wiki-migration/university/courses/alm1k/alm-lab-pv>`, we have one here that can be tested. The solar panel from the example toy generates 1.72 volts open circuit in full sunlight with a short circuit current of 5.6 mA.

Just a single one of these small solar cells does not produce much power but multiple copies could be connected in series / parallel to produce more power.

Since these cells are not much use for providing power but are sensitive to low light conditions, they might be better used as ambient light sensors or as the tracking sensor as part of a control system for example a larger moveable solar array.

Measuring Inductor Characteristics:
-----------------------------------

Use the ALICE Impedance Analyzer to measure the characteristics of the coil. AWG A Mode set to SVMI, set to Sine shape, Min to 1.0, Max 4.0, Freq to 1000. External resistor is 470 Ω. AWG B set to Hi-Z Split I/O mode.

|image1| |image2|

.. container:: centeralign

   Figure 14, Inductor measurements.


The measured values for the coil used in this example were 16.3 mH at 1 KHz with a DC series resistance of 297 ohms. You could verify the DC coil resistance using the ALICE DC Ohmmeter tool as well.

In addition we can learn more about inductors by building various configurations around the coil. Its high internal series resistance will make it difficult to use as part of a high Q resonator, filter or oscillator but given sufficient gain it probably can be made to work.

One experiment is to hold a magnetic compass next to the coil to detect the magnetic field while it is being pulsed. The compass needle should swing back and forth in time with the pulses. You can also drive the coil from a function generator such as ALM1000. Hover the magnet over the coil and you will feel the pulses of force from the magnetic field push on the magnet.

Transformer action can be investigated by driving a 1 mH or 10 mH inductor, like the ones included in the ADALP2000 Analog Parts Kit, with the function generator, such as channel A of the ALM1000, and holding the inductor close to the coil, connected to channel B of the ALM1000 in Hi-Z mode.

**Going Further**

| `Flappy solar ornaments have an interesting history. <https://www.youtube.com/watch?v=MHRxYtVD1IU&t=1s>`__
| `Flappy Flower Solar Ornament Teardown <https://www.youtube.com/watch?v=pwR--SBEM9U>`__
| `Really nice "flip flap" pendulum kicker - with a transistor level schematic <https://odysee.com/@bigclivedotcom:0d/really-nice-flip-flap-pendulum-kicker:5>`__

**Return to Lab Activity table of contents**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig14a.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/alm1k/intro/alm-solar-motion-toy-fig14.png
   :width: 600px
