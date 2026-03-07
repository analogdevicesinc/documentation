Making AC Mains Voltage and Current Measurements
================================================

In other documents the voltage and current measurement features of the ADALM1000 (SMU) have been discussed. In this document techniques to safely measure AC Mains Line voltage and current using the Active Learning Modules are discussed.

`ADALM1000.html <https://wiki.analog.com/_media/https///www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADALM1000.html>`_

Background:
-----------

The M1k's SMU channels can measure DC currents from -200mA to +200mA. Because of the 100 KSPS sampling rate it can actually measure AC currents as well. But the current to be measured has to be flowing into or out of the SMU channel. This limits the range of voltages that the current must be "referenced" to, 0 to +5V. To measure current over a wider range of voltages a current shunt monitor IC like the AD8210 from the ADALP2000 Analog Parts kit can be used.

`ad8541.html <https://wiki.analog.com/_media/https///www.analog.com/en/products/ad8541.html>`_ `EVAL-ADALP2000.html <https://wiki.analog.com/_media/https///www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADALP2000.html>`_

The M1k SMU channels use this same chip to measure the current. The operating input common-mode voltage range of the AD8210 is −2 V to +65 V with respect to the ground pin of the IC. A larger voltage range but still not enough to safely measure the current of a household appliance or lighting fixture operating from 120 V AC. So what can we use to do that? Enter the Voltage Step-Down Transformer to measure the line voltage and the Current Sense Transformer to measure the line current.

Measuring the Mains Voltage Waveform
------------------------------------

The Step-Down Voltage Transformer Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To display the AC line voltage waveform a voltage step-down transformer is used to both galvalically isolate and reduce (step down) the voltage before measuring it with the M1k channel B input. The 120 V RMS line voltage must be scaled down to fit within the 0 to 5 volt range of the M1k. The transformer chosen for this example has a rated secondary voltage of 9 V RMS at 250 mA load. The unloaded p-p secondary voltage is about 35 V (+/- 16.5 V peak). This will need to be further reduced using a resistor voltage divider with a ratio of more than 10 and also offset to be centered around 2.5 V as shown in figure 1. The overall total reduction in the voltage should be at least 100:1.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Step-Down Transformer and Resistor Divider


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 2, AC-AC Step-Down Wall Adapter Transformer


Calibration Steps
^^^^^^^^^^^^^^^^^

The step down ratio for the combined transformer and resistor divider is measured by connecting the channel A and B AWG outputs of the M1k to the primary side of the transformer. The two AWG channels are configured as 60 Hz complementary sinewaves from 0 to 5 V to produce a differential 10 V peak to peak voltage at the primary. The secondary of the transformer is connected through the 220K / 22K resistor voltage divider to BIN (Split I/O mode) and the 2.5 V mid rail. The channel B gain and offset scale factors are then adjusted such that the CHB voltage waveform is also 10 V p-p, figure 3. At the same time we can measure the phase difference (shift) from the input to the output of the combined signal path, figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Measured Test Voltage Input / Output waveforms


Knowing this measurement phase shift (error) will be important later on when calculating real and imaginary power and power factor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Measured Test Voltage Input / Output phase


With the step-down transformer plugged into an AC outlet we can now measure the AC line voltage waveform. The pure 60 Hz sinewave from the AWG goes through the transformer with little distortion as we saw in figure 3, however, the actual 60 Hz AC line waveform shows considerable distortion as shown in figure 5. The waveform peaks are measured at + / - 175 V and the RMS voltage is 124.7 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Measured Mains AC Voltage waveform


The 1:1 Current Mode Transformer Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An alternate method to measure the AC line voltage is by first converting the voltage to a small current using a high value resistor load. In this example we are using 5 mA RMS as the nominal target current. Two series connected 12 KΩ resistors are used to spread both the heat (power) and voltage between the two. There is about 1/3 W in each so ½ W or greater resistors should be used. The 5 mA current is then sent through a small 1:1 transformer. A common mode choke, often used in power line filtering for switch mode power supplies, is a good choice. Two typical examples are show below in figure 6. The schematic is shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-6.png
   :align: center
   :width: 450px

.. container:: centeralign

   Figure 6, Example Common Mode Choke 1:1 Transformers


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Voltage to Current Transformer Method


To insulate the high voltage connections and for safety reasons the transformer and resistors are mounted in the plastic case from another (dead / used) plug adapter as in figure 8. The cover can then be glued back on preventing anyone from accidentally touching the Mains AC high voltage. Using an old plug adapter case like this also conveniently provides a way to connect to an AC outlet socket.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-8.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 8, Transformer and resistors mounted in plug adapter case.


.. _calibration-steps-1:

Calibration Steps
^^^^^^^^^^^^^^^^^

The first step is to measure the actual values of the resistors using an accurate DMM. The ratio of the primary to secondary current should be ideally 1:1 but in any real transformer it will be less than 1. The calibration test setup is shown in figure 9. A known 60 Hz sinewave current of about 5 mA RMS is sourced by the channel B SMU in SIMV mode. The secondary current is measured by the channel A SMU in SVMI mode set to the same 2.5 V DC voltage as the fixed 2.5 V supply. The total resistance and the current transformer ratio will be used to convert the measured current waveform data into voltage.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, Current Input / Output Ratio Test


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-10.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 10, Measured Test Current Input / Output waveforms


Knowing this measurement phase shift (error) will be important later on when calculating real and imaginary power and power factor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Measured Test Current Input / Output magnitude and phase


To compare the voltage transformer method and the current transformer method measuring the AC line voltage waveforms the two are shown in figure 12. The RMS current is measured at 4.96 mA which is consistent with the 24 KΩ resistors used.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, Voltage and Current Transformer Waveforms Compared.


Using the Math plotting function we can convert the current transformer waveform back into a voltage by multiplying by the effective (calibrated) voltage to current resistance (~24 KΩ) and plot it on the same vertical scale as the voltage transformer waveform as shown in figure 13.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 13, Voltage and Calculated Voltage Waveforms Compared.


Electronic Burden, I to V converter
-----------------------------------

The M2k does not have the current measurement capability as in the M1k SMU. The solution is to build an op-amp I to V conversion circuit. The single supply rail-rail AD8542 Dual CMOS op-amp is used as an I to V converter as shown in figure 14. The virtual ground at the summing junction, pin 2, presents a very low impedance load on the secondary. The 350 Ω feedback resistor converts the current into a voltage that is measured by the M2k scope channel at pin 1.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-14.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 14, Op-amp I to V converter circuit for M2k


Measuring the Mains Current Waveform
------------------------------------

The Current Sense Transformer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current sense transformer is a transformer that is optimized or designed to produce an alternating current in the secondary winding which is proportional to the current being "sensed" or measured in the primary winding. Like any transformer, current transformers galvanically isolate the measuring of currents in high voltage circuits to a much lower voltage and provide a convenient way of safely monitoring the actual electrical current flowing in a high voltage AC power line. In our case this could be the SMU of the M1k.

The principal of operation of a basic current transformer is slightly different from that of an ordinary voltage transformer. Unlike a power transformer used to step up or down voltages, the current transformer often consists of only one or a few turns as the primary winding. This primary winding can be of either a single flat turn, a coil of heavy duty wire wrapped around the core or just a wire inserted through a central hole like that shown in the photo of a clamp-on current probe transformer, (model LCTC-0250) figure 15. With this current "probe" the jaws open so that it can be clamped around the conductor carrying the current to be measured without having to disconnect the conductor. Current probes such as this are designed for use in 50/60 Hz Mains power applications. The LCTC-0250 probe has a current measuring range up to 100 Amps and a built-in current to voltage (burden) resistor so the output voltage is specified as 15mV/A.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-15.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 15, Clamp-on Current Transformer, model LCTC-0250


Many manufacturers offer a range of current sense inductors that are a toroidal coil with a hole in the center that the user passes a wire (or loops of wire) through to sense the AC current, figure 16. Depending on the particular model and the specification these types of current transformers are designed for use in switch mode power supply control systems and operate over a frequency range from 20 kHz to 200 kHz. The PE-51718 center tapped 100 turn 20 mH version is shown. The size, excluding the leads, is 20mm tall x 11mm wide x 10mm deep which is small enough to fit on a solder-less breadboard.

The nice thing about using a coil like this as a sense transformer is that you can choose any number of turns you want for the secondary. Up to when the center hole is filled based on the gauge of the wire used.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-16.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 16, Pulse Engineering Center tapped 100:1 20 mH example


A current transformer with a built-in primary winding from CoilCraft is shown in figure 17. Since it is totally encapsulated, we can't tell how it is constructed. The design frequency range for this 200:1, 80 mH example is from 1 KHz to 1 MHz.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-17.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 17, CoilCraft 200:1 80 mH example CS4200V-01


In figure 18 we have a surface mount current sense transformer from Würth Elektronik. In this example the primary winding is simply the wide metal strap that goes up and around the central secondary winding. The manufacturer specifies the inductance for this 200:1, 20 mH example at 10 KHz so it probably is also not designed for lower frequency power line applications.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-18.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 18, Würth Elektronik 200:1 20 mH example from MID-SNS Family


Frequency Response Testing
--------------------------

To test these current transformers an M1k was used and the test circuit shown in figure 19. A 4 V peak-peak sine wave signal is generated by the channel A AWG. The signal is then AC coupled through a large capacitor to the 10 ohm load resistor which converts the voltage into a 400 mA peak to peak current. The current is sensed by the primary winding which is connected to ground. On the secondary side the 100 ohm burden resistor is connected across the coil winding and the resulting voltage is measured by channel B in Hi-Z mode. The other end of the coil is referenced to the fixed 2.5 V rail to center it in channel B's input range.

For the clamp-on probe and the PE coil one of the longer wire jumpers from the Analog Parts kit is inserted through the center hole to use as the primary.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-19.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 19, Frequency Bandwidth test circuit using M1k


The input frequency is swept from 20 Hz to 1 KHz in all the following tests. The first bode plot is for the LCTC clamp probe with a single wire through the clamp. Remember that the clamp has a built-in burden so the 100 ohm external resistor was not included for this test case. The magnitude response is very flat, within a dB down to 20 Hz as shown in figure 20.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-20.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 20, LCTC current probe bode plot


Next up is the PE-51718. As can be seen in the response shown in figure 21, below 1 KHz it is not at all flat which is to be expected given the 20 KHz minimum frequency specification. The lighter set of curves are for one wire as primary and the darker set is for 4 turns as the primary.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-21.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 21, PE-51718 bode plot


Next the CoilCraft CS4200V-01 and Würth Elektronik 750316796 examples are tested in figure 22. Both are 200:1 turns ratio. The darker curves are for the 80 mH CoilCraft device and the lighter curves are for the 20 mH Würth device. As expected the higher inductance of the CoilCraft device gives the better low frequency response. The CoilCraft device meets and exceeds its 1 KHz minimum frequency specification and the Würth device is probably only flat above a few KHz using this value of burden resistor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-22.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 22, CoilCraft CS4200V-01 and Würth Elektronik 750316796 bode plot


.. _electronic-burden-i-to-v-converter-1:

Electronic Burden, I to V converter
-----------------------------------

One way to improve the frequency response of any current transformer is to replace the resistive burden with an electronic solution, i.e. an op-amp I to V conversion circuit. Again, the single supply rail-rail AD8542 CMOS op-amp can be used as an I to V converter as shown in figure 23. The virtual ground at the summing junction, pin 2, presents a very low impedance load on the secondary. The 1K feedback resistor converts the current into a voltage that is measured by channel B at pin 6.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-23.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 23, Op-amp I to V converter circuit


To test the frequency response using the op-amp the CoilCraft CS4200V-01 (dark trace) and Würth 750316796 (light trace) are again compared in figure 24. Note the vertical scale is now 3 dB/div. There is a huge improvement in the flatness of the response compared to figure 8 with less than a dB of roll off at 60 Hz. The CoilCraft response is now about as flat as the LCTC current probe in figure 18.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-24.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 24, CoilCraft CS4200V-01 and Würth 750316796 op-amp I to V bode plot


Also note that the M1k SMU channel set to SVMI is equivalent to the op-amp I/V converter circuit of figure 23 as we saw back in figures 7 and 9.

Making real world measurements
------------------------------

As a real world test example the model LCTC-0250 clamp-on current sensor from figure 1 and the M1k are used to measure the current waveform of an LED Holiday light string. The LCTC-0250 probe has a built-in current to voltage (burden) resistor so the output voltage is specified as 15mV/A. The string consists of 35 white LEDs in series. About a foot of the wire was untwisted and one leg was wrapped about 5 times around the clamp. The sensitivity will now be about 75 mV/A (5 \* 15 mV/A).

The probe is connected directly to the input of an M1k without any additional amplification or filtering. As shown in figure 25 the current is simple 1/2 wave rectification and the peak current is between 35 and 45 mA. It is hard to measure exactly with the noise and the signal is too small to trigger on properly and apply trace averaging.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-25.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 25, Current waveform without any signal processing


By applying some mathematical digital filtering we are able to clean up the noise and make the "signal" big enough (by 10X) to trigger on and use trace averaging. A simple 20 tap box car digital filter with an overall gain of 10 is applied to the captured waveform trace and trace averaging is used (set to average 8). The waveform is nice and clean now and the p-p current is 42 mA.

|image1|]

.. container:: centeralign

   Figure 26, filtered current waveform


Additional Real World Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To measure lights with a standard screw in Edison base, a socket was connected to a plug and a few feet of zip cord. About a foot of the wire was un-zipped and one leg was wrapped 6 times around the LCTC-0250 clamp. The sensitivity will be about 90 mV/A (6 \* 15 mV/A). Six different light bulbs were measured. In all the following waveform screens shots the channel A user measurement formula was used to display the calculated peak-to-peak current (in Amps) and the channel B user measurement formula was used to display the calculated (true) RMS current (in Amps). Ignore the channel B voltage trace. It is only there to enable the channel B user measurement display.

As a first experiment an incandescent light bulb was measured. The spec for this bulb is, 390 lumens and 40 W. The packaging for these bulbs says "Double Life" so the light output is probably lower than from other similar 40 W bulbs.

The measured RMS current is 0.33 A. Assuming 120 V RMS Mains voltage results in an RMS power of 39.6 W. The measured power consumption is almost exactly what it should be. As the filament in an incandescent lamp is almost purely resistive the current wave form, shown in figure 27, is a relatively clean sinewave. The vertical voltage scale is 20 mV/div (20/90 or 0.222 A/div).

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-27.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 27, Current waveform for 40 W Incandescent lamp


A second incandescent bulb is tested next with 770 lumens and 60 W. The measured RMS current is 0.498 A. Again assuming 120 V RMS mains voltage results in an RMS power of 59.7 W. The measured power consumption is almost exactly what it should be. Again, the purely resistive current wave form, as shown in figure 28, is the same clean sinewave.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-28.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 28, Current waveform for 60 W Incandescent lamp


We can now assume that the test setup is probably giving accurate results. Next a compact florescent lamp, CFL, that is marketed as a replacement for a 40 W incandescent lamp is measured. The specs listed are 700 lumens, 11 W and 140 mA. The 11 W and 140 mA seem inconsistent? The measured RMS current is 0.130 A. Assuming 120 V RMS mains voltage results in an RMS power of 15.6 W. The measured power is 4.6 W or 42% higher than the specification. The electronic ballast used in the CLF results in the rather nasty looking current waveform shown in figure 29. It draws current on the positive and negative halves of the AC voltage but has a huge crest factor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-29.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 29, Current waveform for first CFL lamp


Next another CFL is measured that is marketed as a replacement for a 60 W incandescent lamp. The specs listed are 15 W and 230 mA. The 15 W and 230 mA also seem inconsistent? The measured RMS current is 0.175 A. Assuming 120 V RMS mains voltage results in an RMS power of 21 W. The measured power is 6 W or 40% higher than the specification. The current waveforms are consistent between the two CLF examples if we compare figures 29 and 30. The higher power lamp having larger peak and RMS currents of course.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-30.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 30, Current waveform for second CFL lamp


Next an LED lamp marketed as a replacement for a 60 W incandescent lamp is measured. The specs listed are 800 lumens, 9 W and 90 mA. The measured RMS current is 0.077 A. Assuming 120 V RMS mains voltage results in an RMS power of 9.24 W. The measured power is much closer to the listed value and only 2.5% higher. As we see in the much smoother current waveform in figure 31, it draws current on the positive and negative halves of the AC voltage with none of the nasty spikes of the CFL. Note that the vertical scale at 10 mV/div is half that in the previous waveform screen shots.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-31.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 31, Current waveform for LED lamp


As another LED lamp example, a 40 degree LED flood light, is measured. The specs listed are 840 lumens, 12 W and 130 mA. The measured RMS current is 0.108 A. Assuming 120 V RMS mains voltage results in an RMS power of 12.96 W. The measured power is much closer to the listed value and only 8% higher. As we see from the current waveform in figure 32, it draws current on the positive and negative halves of the AC voltage but with very square looking pulses at what might be two distinct levels as compared to the more rounded waveform in figure 29. Also none of the nasty spikes of the electronic ballast in a CFL are present. Note that the vertical scale is 10 mV/div as in the previous waveform screen shot.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-32.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 32, Current waveform for LED flood light


The lower crest factor of the LED waveforms probably accounts for the measured power being closed to the listed power. The CFL manufacturers did not probably use high bandwidth hardware like the M1k to measure the true RMS current of their lamps and missed the high crest factor of the current drawn. It is probably important to note at this point that the measurement results shown so far do not take into account any phase difference between the voltage and current waveforms (power factor).

.. _measuring-the-mains-voltage-waveform-1:

Measuring the Mains Voltage Waveform
------------------------------------

We will now add the display of the AC Mains voltage waveform using the voltage step-down transformer technique. To check out the setup for proper phase between voltage and current the 40 W incandescent bulb is used. Figure 31 shows that the two waveforms are in phase as they should be for a resistive load. Note that the RMS voltage for the AC line measures at 117.75 Volts which seems right on the money.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-33.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 33, Current and voltage waveforms for 40 W Incandescent lamp


Now, in figure 34 the relative phase between current and voltage for the second CFL bulb is measured.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-34.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 34, Current and voltage waveforms for second CFL


We leave it up to the reader to interpret what that means. Things like the instantaneous point by point power can be calculated from the two waveforms and then the RMS value of that calculated for example.

Conclusion
----------

For making Mains AC power measurements of line voltage and current, the voltage step-down transformer and current sense transformer can safely isolate the high line voltages from the measurement circuitry. This is a very important safety consideration. The wide dynamic range and relatively high sample rate / bandwidth of the 16 bit ADC in the M1k allows the use of high current (100 Amps) probes like the LCTC to measure currents a low as a few 10's of mA directly without any signal processing.

**For Further Reading**

| `Pulse Transformers <https://www.digikey.com/product-detail/en/pulse-electronics-power/PE-51718NL/553-1547-ND/2265979>`_
| `Galvanic isolation <https://en.wikipedia.org/wiki/Galvanic_isolation>`_

Appendix: Other Off the Shelf Hardware
--------------------------------------

The Seeed Technology Co., Ltd Clamp on current sensor, Product Number 101990065, can be ordered through `Digikey <https://www.digikey.com/en/products/detail/seeed-technology-co.,-ltd/101990065/5487441?utm_adgroup=Current%20Sense%20Transformers&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_Product_Transformers_NEW&utm_term=&utm_content=Current%20Sense%20Transformers&gclid=Cj0KCQjw4eaJBhDMARIsANhrQABKphIVg7nvrS4ynla7G3dFTqRBslLfLdBfj9IYXsSy_-uZlkuHkk8aAmh-EALw_wcB>`_. It has a rated input of 0-60A, rated output of 0-1 V and a turns ratio N=1:1800.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/seeed-current-clamp.png
   :align: center
   :width: 300px

.. container:: centeralign

   Clamp on Current Sensor


The `Clamp on current sensor from SparkFun <https://www.sparkfun.com/products/11005>`_ has a turns ratio Np:Ns=1:2000 and input /output Current Ratio 30A/15mA.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/sparkfun-current-clamp.png
   :align: center
   :width: 300px

.. container:: centeralign

   ECS1030-L72 Non-Invasive Current Sensor - 30A


This Line voltage sensor module based on the ZMPT1010B current transformer has a built in electronic (op-amp) burden circuit. It has exposed screw terminals for the AC line input connection so it has potential shock hazard issues unless installed in an insulating enclosure.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/zmpt101b-arduino-sensor.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure A2, AC line voltage Sensor Module


Extra stuff
-----------

Due to this type of arrangement, the current transformer is often referred to as a “series transformer” as the primary winding, which never has more than a very few turns, is in series with the conductor supplying current to the load.

The secondary winding will have a large number turns wound on a core of low-loss magnetic material. This core has a large cross-sectional area so that the magnetic flux density created is low using much smaller cross-sectional area wire, depending upon how much the current must be stepped down as it tries to output a constant current, independent of the connected load.

The secondary winding will supply a current into either a short circuit, in the form of an ammeter, or into a resistive load until the voltage induced in the secondary is big enough to saturate the core or cause failure from excessive voltage breakdown.

Unlike a voltage transformer application the goal is to have the primary current of a current sense transformer not dependent on the secondary current but instead is controlled by an external load. The secondary current is usually rated at a standard 1 Ampere or 5 Amperes for larger primary current ratings.

The Primary/Secondary Turns Ratio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Current sense transformers commonly have turns ratios ranging from 1:10 to 1:2000. The higher the turns ratio (r = Nsec/Npri), the higher the resolution of the current measurement. However, care must be taken as too high of a turns ratio will necessitate an increase in distributed capacitance and leakage inductance which may decrease the transformer’s accuracy and capability to operate at higher frequencies (due to self-resonance). However, if the number of turns is too low (lower inductance), the output signal may distort or “droop” (in positively sloped unipolar input signal) which may also cause instability in the control circuit and inaccuracies in measurements.

There are three basic types of current transformers: wound, toroidal and bar.

The secondary load of a current transformer is termed the "burden" to distinguish it from the primary load.

Phase shift
-----------

Ideally we want the primary and secondary currents of a current transformer to be in phase. In practice, this is not possible, but, at normal power frequencies, phase shifts of a few tenths of a degree are achievable, while simpler CTs may have phase shifts up to six degrees. For average and RMS current measurements the phase shift does not factor into as ammeters only display the magnitude of the current. However, for power, energy, and power factor (real power vs reactive power measurements, phase shift produces errors. For power and energy measurements, the errors can be considered to be negligible at unity power factor but become more significant as the power factor approaches zero. At zero power-factor, any indicated power is entirely due to the current transformer's phase error. The introduction of electronic power and energy meters has allowed current phase error to be calibrated out.

.. |image1| image:: https://wiki.analog.com/_media/university/courses/tutorials/ac-mains-tests-fig-26.png
   :width: 600px
