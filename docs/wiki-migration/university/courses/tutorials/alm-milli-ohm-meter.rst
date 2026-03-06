Measuring very small resistances, A Milliohm-meter
==================================================

Objective
---------

The objective of this document is to present techniques to measure very small resistances, below 1 Ω, accurately using the AD8210 current shunt monitor IC.

Background
----------

The lowest resistance range on a typical three and a half digit digital multi-meter (DMM) is 200 ohms with a resolution of 0.1 ohms. More expensive high end dedicated bench milliohm meters will support lower ranges and 4 wire measurements.

Why would you need a milliohm meter? To test and debug cables, connectors, PC board traces and other kinds of low resistance cases. To measure the series resistance of power inductors that can be a few tenths of an Ohm. For accurate measurements of components like switches and relay contacts you will need to resolve resistance values of 1 ohm or less with resolution in the milliohms. Contact resistance due to oxidation or corrosion build-up will require a substantial current to break through any film built up on the contacts.

The Kelvin Measurement technique
--------------------------------

A “4-wire” or `Kelvin measurement technique <https://en.wikipedia.org/wiki/Four-terminal_sensing>`__ for low resistance is illustrated in figure 1. This technique eliminates the effects of test equipment lead and probe resistance. A current of known value from the current source is forced to flow through the test resistance R\ :sub:`DUT`. A voltmeter is used to measure (sense) the drop across the resistor INSIDE the current forcing connections. The four wires connected to the resistance to be tested are noted as F+ and F – for the force connections and S+ and S- for the sense connections. Ohms law can then be used to calculate just the resistance seen between S+ and S-. Voltage drops in the current loop due to any resistance in the F+ and F- force test leads is not seen by the volt meter. Any resistance in the S+ and S- sense test leads is unimportant given the assumed very high input impedance of the voltmeter compared to R\ :sub:`DUT`.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, “4-wire” or Kelvin measurement technique


Because the voltage drop across the unidentified resistance is measured at the probe tips, the resistance of the test leads carrying the constant current is not included. The resistance under test can be found by dividing the voltage drop between the sense probes by the test current.

The test current for a typical DMM on the 200 ohm range is typically between 1 mA and 2 mA. For lower ohm ranges like 20 ohms or even 2 ohms the test current would need to increase to 20 mA and 200 mA. Specialty milliohm meters generally use test currents in the area of 100 mA to 200 mA and can sometimes be as high as 1A.

Applying the technique
----------------------

By combining a few components from the ADAPL2000 analog parts kit a milliohm meter can be constructed that can make 4 wire measurements of very small resistances.

A key component of this milliohm meter is the AD8210 current shunt monitor IC. This circuit is most often used to measure an unknown current flowing through a known low value shunt resistor. The small differential voltage drop across the shunt is amplified by a fixed gain of 20 and referenced to a DC output reference level, often ground. The block diagram from the AD8210 datasheet is shown here in figure 2.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig2.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 2, AD8210 data sheet block diagram


| The output voltage of the AD8210 is given by:
| :math:`V_OUT = I_SHUNT \times R_SHUNT \times 20`

| Rearranging for the measured current:
| :math:`I_SHUNT = V_OUT /(R_SHUNT \times 20)`

| We can also flip this equation around to measure resistance:
| :math:`R_DUT = V_OUT /(I_TEST \times 20)`

Using the ADALM1000
~~~~~~~~~~~~~~~~~~~

The programmable current source(s) in the ADALM1000 can supply anything from -200 mA to +200 mA. This makes it ideal for use as the driving source for a milliohm meter. The 0 to 5 V input range of the ADALM1000 is also well suited as the sense volt meter. The 16 bit ADC has enough dynamic range to measure very small voltages but it is not a differential input which makes it unsuitable for 4 wire measurements. To fix that shortcoming we can use the AD8210 as a differential to single-ended converter circuit.

The practical range of test currents from the source in the M1k is 5 mA to 150 mA (or slightly higher). The input Voltage measurement range of one of the M1k inputs is 0 to 5 V. AD8210 has a voltage gain of 20. Assuming that the AD8210 is powered by the fixed +5V supply and the 5 volt input span of the M1k, which translates to a maximum differential voltage at the inputs of the AD8210 of 5/20 or 250 mV. For a test current of 150 mA that gives a maximum resistance of 250 mV/150 mA or 1.667 ohms. If we assume 1 mV resolution for the M1k 0-5 V input range or 0.05 mV resolution at the test resistance gives an approximate resistance resolution of 0.3 mOhms at 150 mA. The largest resistance that can be practically measured is around 50 ohms using a test current of 5 mA. To use the AD8210 with the M1k the following connections are made as shown in figure 3. Resistor R\ :sub:`1` is inserted in series with the channel A current source because the driver is not stable driving loads much smaller than 10 Ω. The actual value of R\ :sub:`1` does not matter and does not figure into the measurements (the 6.2 Ω power resistor from the kit for example). There is an upper limit to the value of R\ :sub:`1` based on the maximum voltage available on channel A. For a 150 mA maximum test current the voltage drop across 10 Ω is 1.5 V. This added to the +2.5 V at F- results in a possible output voltage on channel A of 2.5 +1.5 + 0.25 = 4.25 V which is within the available output voltage range.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig3.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 3, ADALM1000 Connections


The AD8210 will likely have some small output offset. With channel A set to Hi-Z mode i.e. not sourcing any current, the average voltage seen on channel B (in Split I/O Hi-Z mode) will be the offset. This can be nulled out in the ALICE software by using the channel B offset entry. With the offset adjusted to zero we can now make measurements.

To make the measurement, the channel A source is set to SIMV mode and DC. The value for the desired test current, say +150 mA is entered in the channel A Max value.

| The measured resistance can be calculated using the following formula entered as the channel A User measurement formula:
| DCV2/(20*DCI1/1000)

The value returned in the DCV2 variable is the channel B average voltage and the value returned in DCI1 is the average channel A current (in mA). The factor of 20 is the fixed gain of the AD8210 and the factor of 1000 converts mAmps to Amps.

Making the "4 Wire" connections
-------------------------------

In figure 4 we see the ADALM100 connected to a small solder-less breadboard that contains the AD8210. Four mini-grabber clips are used to connect to the test resistor, in this case a 1 Ohm power resistor. The red and black grabbers are the F+ and F- wires respectively and the blue and green grabbers are the S+ and S- wires respectively. Note that the sense connections are right next to the body of the resistor and the force connections are at the ends of the leads.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, DUT Connection example


Figure 5 is a close-up screen shot of the ALICE desktop scope measurements display. The calculated resistance (Ohms) is 0.9989 Ohms for this particular 1 Ohm 5% resistor. The channel A test current display shows the 150 mA current and the channel B voltage (AD8210 output) is also displayed.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig5.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 5, Screen close-up of measured value


Also shown in figure 4 are some other low value resistors and two 4 pin Vishay (VPR221S) calibration resistors (four terminal precision 2 Ω 0.05% calibration resistors). Notice that two of the calibration resistors have four leads such that the Kelvin connection is made inside the package for the highest possible accuracy. Figure 6 is a close-up screen shot of the ALICE desktop scope measurements for a 50 mOhm resistor. The measured value is 49.5 mOhms.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig6.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 6, Screen close-up of 50 mOhm measurement


Using the ADALM2000
~~~~~~~~~~~~~~~~~~~

The ADALM2000 can also be used with this 4 wire technique but lacks some of the capabilities of the ADALM1000 such as the high current drive capability and current measurement capability. The analog inputs of the M2k are differential however; the 12 bit ADC in the M2k does not have enough dynamic range to measure very small voltages directly so again the AD8210 amplifier is needed. The ADALM2000 connections are shown in figure 7.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig7.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 7, ADALM2000 Connections


To accurately measure the test current I\ :sub:`TEST`, we need to accurately know the resistance of R\ :sub:`1` (actual value to be measured using a bench DMM). The voltage drop across R\ :sub:`1` can be accurately measured using the channel 1 differential inputs 1+ and 1- using a four wire connection method. With this voltage and the known value of R\ :sub:`1` we can calculate the actual value of I\ :sub:`TEST`.

The W1 and W2 voltage sources of the M2k can be connected in parallel due to the internal 50 Ω series resistors. This effectively doubles the maximum available test current. If each source supplies 50 mA of current the voltage drop across the internal 50 Ω series resistor will be 2.5 V leaving a maximum of 2.5 volts that can be dropped across the combination of R\ :sub:`1` and R\ :sub:`DUT`. If for example, R\ :sub:`1` is 10 Ω and I\ :sub:`TEST` is less than or equal to 100 mA (50 mA from W1 plus 50 mA from W2) then there will be up to 1 volt dropped across R\ :sub:`1`. Allowing for 0.25 V drop across R\ :sub:`DUT`, R\ :sub:`1` could be up to 20 Ω and still deliver a total of 100 mA from the up to +5 V internal output range of W1 and W2.

Making the Kelvin connections
-----------------------------

Using things like the mini-grabbers is OK for the wire leads on some components but another option for making the Kelvin connections is to use special test probes and clips. These special purpose test leads can be rather expensive, often hundred dollars or more. Some look like normal test probes but with two pointy bits rather than a single probe point as in figure 8.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig8.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 8, Kelvin test probes


For hobbyists, Adafruit offers these Kelvin spring clips https://www.adafruit.com/product/3313 for $2.50 each with no wires attached. Each side of the plastic clip is electrically insulated. These clips can also be ordered through `Digikey <https://www.digikey.com/product-detail/en/adafruit-industries-llc/3313/1528-2279-ND/7310912>`__.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig9.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 9, Two wire Kelvin test clip


The SMD test lead tweezers shown in figure 10 can also be used in some cases to make the force/sense Kelvin connection right at a component lead.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig10.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 10, SMD test lead tweezers


A more robust construction
==========================

Using a solder-less breadboard to connect to the AD8210 can be a little flakey resulting in the offset shifting when the wires are wiggled. To try to minimize the variability, a soldered proto board can be used to connect the AD8210 to the M1k and provide a place to connect the 4 force and sense wires / test probes. One approach to minimize the variability, a small adapter board for the BOB mounted AD8210 from the ADALP2000 kit can be constructed on a small proto-board as shown in figure 11. The square pins of the AD8210 BOB do not fit into a standard DIP IC socket so using female pin headers might be required. Not perfect but better than a solder-less breadboard.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig11.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 11, Hand soldered adapter board.


Further testing of the configuration suggested above has shown that offset and linearity of the AD8210 when the output is near ground is not very good. Connecting pin 7 (V\ :sub:`REF1`) to 2.5 volts as shown in figure 12 will reference the "zero" current point at 2.5V/2 or 1.25 V. This takes away from the total range (by about 1/4) but gives much better accuracy. One or two hundred mV above ground at the AD8210 output is enough shift but this is the simplest way to shift the output away from ground.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig12.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 12, AD8210 connections to center Vout at 1.25 V (2.5/2)


Going even further a small 1" by 1" plug in :doc:`accessory PC board </wiki-migration/university/tools/adalm1000/accessory-boards-index>` has been designed to mount the SMD AD8210 and connect it to the M1k and provide a place to connect the 4 force and sense wires / test probes.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig13.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 13, SMD break-out PC board


In figure 13 the Milliohm meter board is shown connected to a 4 pin Vishay (VPR221S) 2 ohm 0.05% calibration resistor.

Specialized Milli-Ohm software for M1k
--------------------------------------

Using the full blown ALICE desktop scope display is overkill for the milliohm meter. A standalone tool much like the other DC tools offered in the ALICE software package is available. It is included in the release package of the ALICE tools for Windows. A screen shot of the standalone tool is shown in figure 14. It includes an example schematic at the bottom as a reminder for how to connect the AD8210. Included are controls to manually and auto zero the channel B offset voltage and channel A offset current.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig14.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 14, Milliohm meter software tool


The AD8210 will likely have some small output offset. As the software runs, with the auto zero boxes checked, first the channel A current is set to 0, i.e. not sourcing any current, the average measured channel A current and channel B voltage will be the automatically entered in the offset entry locations. Then channel A is set to the test current and the unknown resistance is measured and displayed on the top line.

When the Auto Zero boxes are not checked you can manually enter the values. The second line reports the measured channel A current and channel B voltage. If the CA Test I is set to 0 these will be the offsets. If the Test current is set too high for the resistance being measured such that the channel B voltage goes above 4.8 V the line displaying the voltage (and current) turns red.

The gain accuracy of the AD8210 in the datasheet is specified to be +/- 0.5% Max and the calibration accuracy of the M1k is likely in the same range. The software has entry places to adjust the gain as well. In the screen shot of figure the current and voltage gains (really only need to change one) are adjusted such that the reading is exactly 2.000 ohms for one of the Vishay calibration resistors. The total adjustment was 0.8% which is within the range that we might expect. A second 2.000 ohm calibration resistor was then checked with the adjusted values with identical results.

It should also be noted that the board used in this case had pin 7 connected to +2.5 V so the channel B offset (zero current value) was around 1.3 V.

Alternate way to auto zero
~~~~~~~~~~~~~~~~~~~~~~~~~~

Also since the current source in the M1k is bipolar it should be possible in a test version of the software to alternate between both positive and negative test current and null out the offset that way. In figure 15 we show pin 7 connected to the +5 V supply. Now the "zero" current output of the AD8210 will be at +5V/2 or +2.5 V. Because we have half the voltage range at the output of the AD8210 we have to also reduce the magnitude of the test current by half.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig15.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 15, M1k Connections for bipolar auto-zero


A screen shot of a test version of the software that implements this bipolar test current technique is shown in figure 16. In this case there are no check boxes to enable auto zero or places to enter the offsets. We still need places to enter the test current and adjust the gain. The reminder schematic at the bottom is changed to show how pin 7 should be connected for this version of the software.

A second copy of the PCB was configured for this technique. The screen shot shows the results for the same 2 ohm calibration resistor. For this board the total gain adjustment needed was slightly different (1.3%).

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig16.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 16, Bipolar test current software version


Using the Milliohm Board as high current Ammeter
------------------------------------------------

A side benefit of this AD8210 break-out board is that with a known external shunt resistor it can be used as a high current Ammeter. In figure 17 a hand wired shunt using a 0.12 ohm power resistor and two screw terminals is shown. The exact value of the shunt can of course be measured using the Milliohm meter software, after calibrating it against the Vishay resistor.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig17.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 17, External shunt resistor connection example as Ammeter


One Final Thing
---------------

Here is another example of test leads for the Milliohm meter. Shown in figure 18 two wire shielded mini-grabber cables are used for F+ / S+ and F- / S-.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/milli-ohm-meter-fig18.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 18, Another set of test leads


**Additional resource links:**

| `Two wire vs four wire resistance measurements <https://www.edn.com/design/test-and-measurement/4411117/Two-wire-vs--four-wire-resistance-measurements>`__
| `Four wire sensing can make or break your measurements <http://www.electronicdesign.com/blog/four-wire-sensing-can-make-or-break-your-measurements>`__
| `Optimize high current sensing accuracy <http://www.analog.com/en/analog-dialogue/articles/optimize-high-current-sensing-accuracy.html>`__
| `Measuring low resistance 4 wire on the cheap <http://www.instructables.com/id/Measuring-low-resistance-4-wire-on-the-cheap/>`__
