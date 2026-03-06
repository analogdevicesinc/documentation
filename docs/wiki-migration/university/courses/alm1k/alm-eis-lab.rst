Activity: Electrochemical Impedance Spectroscopy - ADALM1000
============================================================

Objective:
----------

This activity will explore measurement techniques and use of Electrochemical Impedance Spectroscopy with Li-ion rechargeable batteries.

Background:
-----------

Electrochemical Impedance Spectroscopy or EIS is a safe perturbation technique used to examine processes occurring inside electrochemical systems. An EIS system measures the impedance of a battery cell over a range of frequencies. The measured data can determine the state of health (SOH) and state of charge (SOC) of a battery. A wide dynamic range source measurement unit (SMU) such as the ADALM1000 (M1k) can be configured to excite and measure current, voltage, and the impedance response of a battery. For more detailed background on EIS see the first few pages of this reference design :adi:`CN0510 <media/en/reference-design-documentation/reference-designs/CN0510.pdf>`. The remainder of this document will cover how the measurements can be performed using the M1k hardware / software.

Definitions of Terms
~~~~~~~~~~~~~~~~~~~~

We should define some of the terminology surrounding batteries:

A Primary battery such as a common 1.5 V Alkaline AA cell is not rechargeable. A Secondary battery is rechargeable. Examples are, the lead-acid battery used in a car, Nickel-Cadmium (Ni-Cd), Nickel Metal-Hydride (Ni-MH) and Li-ion cells used in portable electronic devices.

A cell is an electrochemical device capable of supplying the energy that results from an internal chemical reaction to an external electric circuit. A battery is composed of one or more cells, either parallel or series connected to obtain a required current/voltage capability (batteries comprised of series connected cells are by far the most common).

ESR (Equivalent Series Resistance) is the internal resistance present in any cell that limits the amount of peak current it can deliver. The Amp-hour capacity of a battery (or cell) is its most important figure of merit: it is defined as the amount of current that a battery can deliver for 1 hour before the battery voltage reaches the end-of-life point. The "c" rate is a current that is numerically equal to the A-hr rating of the cell. Charge and discharge currents are typically expressed in fractions or multiples of the c rate.

The MPV (mid-point voltage) is the nominal voltage of the cell, and is the voltage that is measured when the battery has discharged 50% of its total energy. The measured cell voltage at the end of its operating life is called the EODV, which stands for End of Discharge Voltage (some manufacturers refer to this as EOL or End of Life voltage).

The gravimetric energy density of a battery is a measure of how much energy a battery contains in comparison to its weight. The volumetric energy density of a battery is a measure of how much energy a battery contains in comparison to its volume.

A constant-voltage charger is a circuit that recharges a battery by sourcing only enough current to force the battery voltage to a fixed value. A constant-current charger is a circuit that charges a battery by sourcing a fixed current into the battery, regardless of battery voltage. Li-ion battery chargers generally use some form of controlled (constant) current charging.

Electrical model of a battery.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We know that an ideal voltage source will produce a constant output voltage independent of the current supplied to the load, i.e. whatever current is needed to maintain the voltage at a constant value. However, real world voltage sources can only supply current up to some limit. The power supplies built into the M1k lab hardware, for example, use active circuitry to maintain the output voltage at a constant value but only for load currents less than 200 mA. A relatively modest current because the board is powered from the computer USB port. Bench top laboratory supplies, powered from the wall outlet, can supply much more, often many amps. Similarly, batteries store a finite amount of energy and have a limited current capability depending on the size of the battery. As the current increases the output voltage will begin to drop as the chemical reaction in the battery tries to maintain the current. In most cases this drop in output voltage with increasing load current can be accurately modeled by including a resistor, typically a few ohms at the most, in series with an ideal voltage source, as shown in figure 1. This is the “internal” resistance or impedance of the battery, Z\ :sub:`int`. This simple model isn’t perfect, because as the battery discharges its voltage will drop even without significant loading. But the internal impedance model does capture the characteristics at a given state of battery charge. Since this simple model is the same as a Thevenin equivalent, we can characterize it in the same way, by measuring the open-circuit voltage and short-circuit current. We do not want to damage the battery, so a current limiting resistor (which also allows us to measure the current) is added in series with the battery as shown in figure 2. When the output is “short-circuited”, this resistor limits the maximum current that will flow.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig1.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 1, Equivalent circuit for a real world voltage source (battery).


Measuring a Battery:
--------------------

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solder-less breadboard, and jumper wire kit
| 1 - Li-ion rechargeable battery (3.7 V 18350 cell or similar suggested)
| 1 - 10 Ω resistor (R\ :sub:`L`)

Directions:
~~~~~~~~~~~

In the kit supplied for this Lab you should have a rechargeable battery (typically a Li-ion 18350 cell). Battery packs like the one shown in figure 1 generally are supplied with wires and a two pin connector already attached. Add an external 10 Ω resistance in series with the battery as shown in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, Characterizing the battery equivalent circuit.


Hardware setup:
~~~~~~~~~~~~~~~

Setup Channel A AWG generator for a 4.1 volt Max and with Min of 3.6 volt (0.5 V p-p) with a triangle shape and a frequency of 100 Hz. Current will flow out of the battery (discharge) and into CHA when the voltage is less than the open circuit battery voltage and will flow into the battery (charge) from CHA when the voltage is greater than the open circuit battery voltage.

Procedure:
~~~~~~~~~~

Measure the open-circuit voltage (when current, as measured by CA-I, through the 10 ohm resistor is zero) and the incremental change in voltage across the battery (BIN) vs. the change in current (CA-I) and determine the Thevenin equivalent resistance. This is a DC test. The complex AC impedance will be measured in the next section of this activity.

Questions:
----------

| 1. Based on your estimate of the internal resistance, what is the maximum current that the battery could supply? What is the maximum power it could deliver to a load?
| 2. Measure the internal resistance at different states of charge i.e. when the battery is fully charged, at 50% charge and when it is at the EODV voltage. How does the internal resistance compare at the different amount of charge in the battery? Can you predict the remaining life in a battery based on its internal resistance?
| 3. Now place a 470 Ω resistor across the terminals of the battery, and record the voltage. In your lab report, discuss whether your measurement is reasonably well predicted by the internal resistance model for the batteries.

Measuring AC Impedance vs. Frequency:
-------------------------------------

We can use the same hardware measurement configuration from figure 2 to measure the AC complex impedance vs frequency. Set AWG A to a sine shape. The time domain screen shot shown in figure 3 shows the time response for CHA voltage, green trace, CHA current, cyan trace, and the battery voltage (BIN) orange trace. The current is negative indicating that the battery is being discharged. Also note that the voltage and current waveforms are nearly exactly in phase with each other.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, Time domain waveforms.


| Using the measured p-p voltage at the battery and the p-p current, we can calculate the incremental resistance from the following formula:
| :math:`R = \Delta V/\Delta I`

:math:`6.2mV/49.2mA = 126 m \Omega`

Open the ALICE impedance analyzer tool. Set the number of FFT samples to the maximum 65536. We need the large number of FFT samples because we will be measuring the impedance at very low frequencies.

We need to enter 10 as the Ext reference resistor value. We already know that the impedance will be very small based on the time waveform data so the Ohms/div is set to 0.02. With the same AWG A settings we get the Impedance analyzer results at 100 Hz shown in figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, Impedance Analyzer results at 100 Hz.


The results of interest are the real and imaginary impedance, R series and X series. The real part is 0.123 Ω which agrees very closely with the time domain measurement value. The Impedance Magnitude is the more appropriate value to compare to the time technique and comes in at 0.125. The imaginary impedance is -0.019 which means it is capacitive however the calculated Series Capacitance and Dissipation factor reported are meaningless for a battery.

We can manually change the AWG A frequency to get impedance values at different frequencies. About the lowest frequency the software can measure is 1.6 Hz (100000 Samples / second divided by the 65536 FFT size). Try a few different test frequencies.

Sweeping the Frequency:
~~~~~~~~~~~~~~~~~~~~~~~

We can use the ALICE Bode plotting tool in conjunction with the Impedance Analyzer to measure the real and imaginary impedance as the test frequency is swept automatically. Under the Impedance Analyzer screen Options drop down menu click on Sweep-on.

Open the Bode Plot tool. Click on Lin-F for a linear frequency sweep. Set the Start frequency to 1 Hz and the Stop frequency to 5000 Hz. Under the Curves drop down menu select CB-dBV, Series R and Series X. Select CHA as the Sweep Gen source. Set number of sweep steps to 400 and single sweep. Click on the green Run button on the Impedance Analyzer screen to start the frequency sweep. Figures 5 and 6 show the Impedance Analyzer and Bode Plot results respectively.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Impedance Analyzer sweep 1 to 5000 Hz.


.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Bode Frequency sweep 1 to 5000 Hz.


Information from EIS is most frequently represented by a Nyquist plot, but can also be shown using a Bode plot. In a Nyquist plot, the negative imaginary component of impedance (y-axis) is plotted against the real component of impedance (x-axis). Different regions of the Nyquist plot correspond to various chemical and physical processes occurring in the battery (see Figure 2 in :adi:`CN0510 <media/en/reference-design-documentation/reference-designs/CN0510.pdf>`).

ALICE does not provide a graphing configuration to display X vs R. The simplest thing to do is export the impedance sweep data by clicking on the File drop down menu on the Impedance Analyzer screen and clicking on Save Data. A file selector menu will pop up and you can edit the file name and hit Save to make the CSV data file.

The CSV file consists of five columns of data, Frequency, Series R, Series X, Series Z, Series Angle. Open the file in Excel and select the Series R and Series X columns (B and C) and insert a Scatter plot of these two columns as shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, Excel scatter plot of Series X vs Series R.


If we compare this graph to Figure 2 in CN0510 we see that we need to multiply the Series X column of values by -1. Make a new column in Excel multiplying the Series X column by -1, and make a new scatter plot of Series R and the negated Series X data.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, Excel scatter plot of Negative Series X vs Series R.


Now our data plot looks more like Figure 2 in CN0510 just not over as wide a frequency range.

A second graphing method is to use the pyplot general purpose graphing library that comes built in ALICE. We can write a simple python script to generate the negative Series X vs Series R plot as shown here.

::

   SR = numpy.array(NSweepSeriesR) * 1000.0 # convert ohms to miliohms
   SX = numpy.array(NSweepSeriesX) * -1000.0 # convert ohms to negative miliohms

   plt.figure()
   plt.grid()
   plt.plot(SR, SX, 'g', label='Impedance')
   plt.title('Battery Impedance')
   plt.xlabel('Real mOhms')
   plt.ylabel('-Imaginary mOhms')
   plt.legend(loc='best')
   plt.tight_layout()
   plt.show(block=False)

Copy the script into a text file and run the script by clicking on Run Script under the File drop down menu on the Impedance Analyzer screen. You should get a graph something like figure 9.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-eis-lab-fig9.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 9, pyplot graph of Negative Series X vs Series R.


**For further reading:**

| `Rechargeable Battery <http://en.wikipedia.org/wiki/Rechargeable_battery>`__
| `Battery Specifications <http://web.mit.edu/evt/summary_battery_specifications.pdf>`__
| `Considerations In Designing Single Supply, Low-Power Systems Part II: Battery Powered Systems <http://www.analog.com/en/analog-dialogue/articles/designing-single-supply-low-power-battery.html>`__
| `CN0510 User Guide <:doc:`/wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0510`>`__
| :adi:`CN0510 Reference Design <media/en/reference-design-documentation/reference-designs/CN0510.pdf>`

**Return to ALM Lab Activity Table of Contents**
