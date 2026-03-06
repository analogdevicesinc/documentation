ADALM1000 Low Capacitance FET Input Buffers
===========================================

In the High-Z mode the two analog input channels of the ADALM1000 provide a 1 mega ohm input resistance but in parallel there is nearly 400 pF of capacitance as we learned in this document on the :doc:`ALM1000 analog inputs </wiki-migration/university/tools/m1k/analog-inputs>`. While working on this example lab activity on a :doc:`CMOS output transconductance amplifier </wiki-migration/university/courses/alm1k/alm-lab-ota>` (OTA) it was found that the ALM1000 analog input was unable to probe the output of the second stage, at the drains of PMOS M\ :sub:`4` and NMOS M\ :sub:`5` in `figure 2 <https://wiki.analog.com/_detail/university/courses/alm1k/alm-ota-lab_f3.png>`__ of the Lab, without the amplifier becoming very unstable. Note the screen shot of the scope display when channel B is connected to this node. The channel A green curve is the input of the amplifier which is configured with an inverting gain of 6.8. The channel B orange curve shows the oscillation.

.. image:: https://wiki.analog.com/_media/university/tools/ota_hi-z-node-un-buffered.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Oscillation with channel 2 connected to second stage


Figure 2 is the schematic for one channel of an N-JFET input buffer source follower. The design in its most simple form uses one N channel JFET, Q\ :sub:`1`, and an NPN current mirror, Q\ :sub:`2` and Q\ :sub:`3`, as the current to drive the source of Q\ :sub:`1`.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-fet-probe_f2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, FET source follower input buffer


N-channel JFETs are depletion mode devices and when used as source followers can provide nearly zero input to output voltage offset if biased at the proper I\ :sub:`D` current. The choice of N-JFET to use could be from a number of possibilities as long as the source load current is adjusted to be equal to the I\ :sub:`D` value where V\ :sub:`GS` is equal to zero. The combination of the fixed and adjustable resistors are used to set the drain current and thus the input to output voltage offset. Devices 2SK117, 2SK193 and 2N4338 were used in prototyping the circuit. The magic I\ :sub:`D` current for the 2SK117 was around 2 mA and for the 2SK193 also 2 mA. The 2N4338 zero V\ :sub:`GS` I\ :sub:`D` was much lower at around 280 uA. Another perhaps more widely available FET would be the Fairchild J112 and J113 devices with zero-gate voltage drain currents of 5 mA and 2 mA.

The gate input capacitance for the 2N4338 and 2SK193 are both listed as 5 pF with the gate capacitance for the 2SK117 somewhat higher at 13 pF. Any of these values are much smaller than the nearly 400 pF of the ALM1000 input structure.

The FET buffer can be powered directly from the fixed +5 V supply on the ALM1000 analog connector which will limit the allowed range of analog input voltages to be somewhat less than the 0 to +5 V supported by the analog inputs because of the headroom needed by the source follower and the current source. Two NMOS transistors such as 2N7000 could be used in place of the NPN (2N3904) devices in the current mirror. MOS current sources should have slightly lower headroom requirements than the BJT current source. To provide the extra supply voltage provision is made to insert 1.5 V batteries below ground and above the 5 V supply. In the prototype mock-up L1131 button batteries were used. Current draw is very low for the buffers and the batteries could last for up to 100 hours of use.

Now with the very high input resistance and very low input capacitance of the FET buffer we can observe the sensitive internal node of the OTA without disturbing the frequency stability of the amplifier. As we can now see in the scope screen shot in figure 3. Again the green curve is the input signal. The dark orange curve is the output of the amplifier and the lighter orange curve is the output of the second stage of the amplifier. We can now see this node as we should, quickly jumping as the NPN and PNP halves of the push-pull output stage turn on and off.

.. image:: https://wiki.analog.com/_media/university/tools/ota_hi-z-node-fet-buffer.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3. No Oscillation with FET buffer connected to second stage


A second important benefit of the significantly lower capacitance is the ability to use just resistors for input attenuators rather than needing frequency response compensating capacitors as in this note on the :doc:`ALM1000 analog inputs </wiki-migration/university/tools/m1k/analog-inputs>`. To confirm this two 510 KΩ resistors as a 2X attenuator was used as shown in figure 4:

.. image:: https://wiki.analog.com/_media/university/tools/m1k-fet-probe_f4.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 4 Resistor only input voltage divider


Figure 5 is a screen shot showing channel A generating a 2 KHz 0 to 5 V square wave, green trace, and the attenuated and buffered signal on channel B, orange trace. Note the vertical scale of channel B goes from -2.5 V to +7.5 V. We see that the insertion of the 510 KΩ resistor in series with the gate of the FET without a frequency compensation capacitor has not affected the rise/fall time of the signal enough to be visible within the bandwidth of the ALM1000.

.. image:: https://wiki.analog.com/_media/university/tools/fet-buffer-input-divider.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, FET buffer with input resistor attenuator


Figure 6 is a rendering of what the top of the 0.8" X 2.0" PCB with two FET buffers will look like. Design files for this board are included in the zip file attached to this blog.

.. image:: https://wiki.analog.com/_media/university/tools/m1000_fet_probe_pcb.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 6, FET probe PCB top layer


On the top left the 6/8 pins of the ANALOG1 connector pass through to the 1X8 pin second analog connector (ANALOG2). The buffer outputs at the source of the FET can be connected to either the CHA/B pin or the optional input only AIN/BIN pins through jumpers JPA and JPB. The 5 pin PROBE header connector contains the channel A and B FET inputs along with two ground pins. The center pin is connected to the fixed +2.5 V power supply to provide a mid swing reference for any external resistor divider that might be used ahead of the buffer to allow larger input voltage ranges as in figure 4. On the right side of the board are places for the two offset adjustment resistors.

The plus and minus button batteries can be inserted into the two 2X2 0.1" header sockets using the technique shown in figure 7. The spacing between diagonal pins in the 2X2 header is just about right to fit the thickness of the battery. Shorting jumpers can be inserted to operate from just the fixed +5 V supply.

.. image:: https://wiki.analog.com/_media/university/tools/coin_cell_holder.png
   :align: center
   :width: 175px

.. container:: centeralign

   Figure 7 Easy way to connect a 1.5 V or 3 V button battery to PCB.


An integrated option is to use the AD8541 CMOS single supply rail-to-rail input/output single opamp from the Analog Parts Kit ( or AD8542 dual ) as a unity gain follower. The CMOS input of the AD8541 offers very low input bias current and low capacitance.

.. image:: https://wiki.analog.com/_media/university/tools/m1k-fet-probe_f8.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 8, AD8542 CMOS buffer schematic


The AD854X datasheet does not specify the input capacitance but test results were very similar to what was seen using the N-JFET followers. The rail-to-rail input and output capabilities of these op-amps means they can operate directly from the fixed +5 V power supply without needing the extra external 1.5 V batteries on the positive and negative supplies as with the N-JFET followers. Figure 9 is a rendering of the top of this buffer circuit.

.. image:: https://wiki.analog.com/_media/university/tools/m1000_cmos_buffer_pcb.png
   :align: center
   :width: 350px

.. container:: centeralign

   Figure 9, AD8542 CMOS buffer PCB


In conclusion we now have ways to effectively buffer the adverse effects of the large input capacitance of the ALM1000 analog inputs.

`Design file archive: <https://wiki.analog.com/_media/university/tools/wiki-m1k_fet_probes.zip>`__
