Activity: Successive Approximation Register (SAR) ADC
=====================================================

Objective:
----------

The objective of this lab activity is to explore the concepts of analog to digital conversion by building an example of a Successive Approximation Register (SAR) ADC partially implemented in both hardware and software.

Notes:
------

As in all the ALM labs we use the following terminology when referring to the connections to the M1000 connector and configuring the hardware. The green shaded rectangles indicate connections to the M1000 analog I/O connector. The analog I/O channel pins are referred to as CA and CB. When configured to force voltage / measure current –V is added as in CA-V or when configured to force current / measure voltage –I is added as in CA-I. When a channel is configured in the high impedance mode to only measure voltage –H is added as CA-H. Scope traces are similarly referred to by channel and voltage / current. Such as CA-V, CB-V for the voltage waveforms and CA-I , CB-I for the current waveforms.

Background:
-----------

The successive approximation ADC (SAR) converts the input analog waveform into a discrete digital representation via a binary search technique through all possible quantization levels before finally converging on a digital output representation for the current input. Typically, the SAR ADC consists of four sub blocks (figure 1):

-  Sample and hold circuit (S/H) to acquire the input voltage (Vin).
-  Analog voltage comparator that compares Vin to the output of the internal DAC and outputs the result of the comparison to the SAR
-  Successive approximation register block designed to supply an approximate digital code of Vin to the internal DAC
-  Internal reference DAC that supplies the comparator with an analog voltage equal to the digital code output of the SAR.

.. container:: centeralign


   ..

|image1|

.. container:: centeralign

   Figure 1. SAR ADC - Typical Architecture


At the start of a conversion, the contents of the SAR is initialized so that the most significant bit (MSB) is set to a digital 1 (on) and all the remaining bits are set to a digital 0 (off). This code is fed into the DAC, which then supplies the analog equivalent of this digital code (mid-sacle) into the comparator circuit for comparison with the sampled input voltage. If this analog voltage exceeds Vin the comparator causes the SAR to reset (reject) this bit; otherwise, the bit is left a 1 (retained). Then the next most significant bit is set to 1 and the same test is done, continuing this binary search algorithm until every bit in the SAR (DAC) has been tested. The resulting code is the digital approximation of the sampled input voltage and is finally output by the SAR at the end of the conversion (EOC).

.. container:: centeralign


   ..

|image2|

.. container:: centeralign

   Figure 2. SAR ADC example (4-bit)


Figure 2 shows an example of a 4-bit conversion. The y-axis represents the DAC output voltage. In the example, the first comparison shows that V\ :sub:`IN` < V\ :sub:`DAC`. Thus, bit 3 is set to 0. The DAC is then set to 0100 and the second comparison is performed. As V\ :sub:`IN` > V\ :sub:`DAC`, bit 2 remains at 1. The DAC is then set to 0110, and the third comparison is performed. Bit 1 is set to 0, and the DAC is then set to 0101 for the final comparison. Finally, bit 0 remains at 1 because V\ :sub:`IN` > V\ :sub:`DAC`.

Materials:
~~~~~~~~~~

| ADALM1000 hardware module
| Solderless Breadboard
| AD8541 CMOS rail-rail op-amp (or 1/2 AD8542 dual op-amp)
| AD5626 12 bit serial DAC
| 10 KΩ Potentiometer
| 220 Ω resistor
| 470 Ω resistor

Hardware Setup:
~~~~~~~~~~~~~~~

In order to demonstrate the operation principle of the SAR ADC with ADALM1000, we will use the AD5626 12 serial DAC from the ADALP2000 parts kit. The output of the DAC will be connected to a comparator, the CMOS rail-rail I/O AD8541 op-amp works well for this. The Successive Approximation algorithm will be simulated via a Python script that performs the binary search based on the comparator's output (connected to one of the digital I/O pins) and generates the proper binary value which will be shifted serially to the AD5626 using 3 of the digital I/O pins.

On your solderless breadboard connect the AD8541 and AD5626 as shown in figure 3. Potentiometer, R\ :sub:`1` provides an adjustable analog input voltage from the +5 V supply to the input of the ADC circuit. The AD5625 DAC will produce a 0 to 4.095 volt output swing when powered from the fixed +5 V power supply. The AD8541 is also powered from the +5 V supply to accommodate this swing range. The digital input, while compatible with 5 volt logic levels really requires only 0 to 3.3 V logic levels. Resistor divider R\ :sub:`2` and R\ :sub:`3` reduces the 5 V swing at the AD8541 output to a swing less than 0 to 3.3 V.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig3.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 3. SAR ADC connections


Procedure:
~~~~~~~~~~

The libsmu Python layer for controlling the ADALM1000 contains a function to configure and control the digital input / output pins. The digital pins can be configured as either static inputs or outputs. We can output a series of pulses on three of the pins to serially load different values into the AD5626 DAC and then read back the state of the AD8541 comparator on the fourth pin.

The routine to send serial data to the DAC looks like this:

::

   def ShiftOut(DValue):
       global PIO_0, PIO_1, PIO_2, PIO_3
       # PIO 0 is strobe 
       # PIO 1 is sdata    
       # PIO 2 is sclk
       # PIO 3 is Comp output
       binstr = bin(DValue)
       binlen = len(binstr)
       datastr = binstr[2:binlen]
       datalen = len(datastr)
       if datalen < 12:
          datastr = str.rjust(datastr , 12 , '0')
          datalen = len(datastr)
      
       i = 1
       while i < datalen+1:
       # sending 0x50 = set to 0, 0x51 = set to 1
           D1code = 0x50 + int(datastr[i-1]) # LSB first for AD5626
           devx.ctrl_transfer(0x40, D1code, PIO_1, 0, 0, 0, 100) # data bit
           devx.ctrl_transfer(0x40, 0x50, PIO_2, 0, 0, 0, 100) # clock to 0
           devx.ctrl_transfer(0x40, 0x51, PIO_2, 0, 0, 0, 100) # clock to 1
           devx.ctrl_transfer(0x40, 0x50, PIO_2, 0, 0, 0, 100) # clock to 0
           i = i + 1
       devx.ctrl_transfer(0x40, 0x51, PIO_0, 0, 0, 0, 100) # strobe to 1
       #
       devx.ctrl_transfer(0x40, 0x50, PIO_0, 0, 0, 0, 100) # strobe to 0

The Successive Approximation algorithm that performs the binary search based on the comparator's output is shown in the next code example.

::

   def SAR():
       global PIO_0, PIO_1, PIO_2, PIO_3
       while (True):       # Main loop
           if (RUNstatus.get() == 1):
               i = 11
               DValue = 2048 # start with just MSB set
               while i > -1:
                   ShiftOut(DValue) # send test value to DAC
                   D3val = devx.ctrl_transfer(0xc0, 0x91, PIO_3, 0, 0, 1, 100) # Read PIO 3
                   if D3val[0] == 0:
                       DValue = DValue - (2**i) # don't keep bit
                   i = i - 1
                   if i > -1:
                       DValue = DValue + (2**(i)) # set next bit to test
               e2.delete(0,"end")
               e2.insert(0,DValue) # display binary result
               Volts = 4.095\*float(DValue)/4096
               VString = ' {0:.3f} '.format(Volts) # format with 3 decimal places
               e1.delete(0,"end")
               e1.insert(0,VString) # display result in volts
       # Update tasks and screens by TKinter
           root.update_idletasks()
           root.update()
           

Download the SAR ADC Python script from this link (`SAR-8541-5626.zip <https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/sar-8541-5626.zip>`_).

Open the SAR-8541-5626.py Python program in your favorite editor. The IDLE that comes with Python is handy because you can run the program directly from there. Run the program. You should see something like figure 4.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig4.png
   :align: center
   :width: 175px

.. container:: centeralign

   Figure 4. SAR ADC demo program


Adjust the Potentiometer up and down and notice how the conversion results change. If you have a DMM, connect it to the wiper of the pot and ground to measure the input voltage as the pot is turned. Move the DMM to the output of the DAC and compare the voltage there to the voltage on the wiper of the pot.

Extra Credit
~~~~~~~~~~~~

As an extra credit exercise, extend the Python program to draw a graph of the DAC value at each step in the search algorithm like what is shown in figure 2.

AD7920 12-bit ADC
-----------------

.. _background-1:

Background
~~~~~~~~~~

The :adi:`AD7920 <media/en/technical-documentation/data-sheets/AD7910_7920.pdf>` is a 12-bit high speed, low power, successive approximation ADC. It can operate with a single power supply in range 2.35V to 5.25V. This ADC can be serial interfaced. The serial clock provides the conversion clock and also controls the transfer of information from the AD7920 during conversion. The conversion process and data acquisition are controlled using /CS and the serial clock, allowing the devices to interface with microprocessors or DSPs. The input signal is sampled on the falling edge of CS and the conversion is initiated at this point. In figure 5 are shown simplified schematics of the ADC during the acquisition and the conversion phase.

.. container:: centeralign

   \


   |image3|

.. container:: centeralign

   Figure 5. AD7920 acquisition and conversion phase


The acquisition phase is when the SW2 is closed and SW1 is in position A. With this setup, the comparator is held in a balanced condition, and the sampling capacitor acquires the signal on Vin. For the ADC to start a conversion, SW2 opens and SW1 moves to Position B causing the comparator to become unbalanced. The control logic and charge redistribution DAC are used to add and subtract fixed amounts of charge from the sampling capacitor to bring the comparator back to a balanced condition as the conversion is completed.

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Figure 6 shows the breadboard connections for the AD7920. VREF is taken internally from VDD so it should be well decoupled. This provides an analog input range of 0 V to VDD. The conversion result is output in a 16-bit word with four leading zeros followed by the MSB of the 12-bit data.

Because of the relatively slow rise/fall times of the ADALM1000 AWG outputs when generating digital square waves, it is necessary to buffer the signals with a 74HC14 Hex inverting Schmitt trigger. Two inverters connected in series sharpens up the edges without introducing an inversion of the signals. Note: non Schmitt trigger gates will not work properly in this circuit.

The SDATA output of the AD7920 returns to a tri-state condition after 16 SCLK cycles or CSB is logic high. A 10 KΩ pull up resistor, R\ :sub:`1`, to the +5 V rail defines the value when in tri-state.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6. AD7920 connections


Lacking a 74HC14 Hex inverting Schmitt trigger, some positive feedback can be added around the two input AND gates in a 74HC08 (from part kit) as shown in figure 6A. A 1 KΩ resistor tied from the output of the gate back to the two shorted together inputs along with a 100 Ω resistor in series with the driving source introduces about 400 mV of hysteresis which is enough to sharpen up the edges. This is not generally standard practice when designing with logic gates, where using actual Schmitt trigger input gates should be done, but in a pinch when you might not have one available, standard input gates such as the 74HC08 (in the parts kit) can be pressed into service.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig6a.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6A. Alternate Schmitt Trigger connections adds hysteresis


Figure 7 shows the AD7920 as mounted on the break out board suppled in the ADALP2000 kit. It is important to note where pin 1 is, square solder pad vs round solder pad. This pinout is up side down as compared to a conventional thru hole 8 pin DIP package. It is IMPORTANT to get the pin connections correct when you wire up your breadboard.

.. container:: centeralign

   |image4|\


.. container:: centeralign

   Figure 7. AD7920 break out board


We can use the AWG outputs to generate the SCLK and CSB inputs. Both AWG CH A and CH B are set as a square wave in SVMI split I/O mode. Their Min, Max and frequency values are set as shown in figure 8.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig8.png
   :align: center
   :width: 250px

.. container:: centeralign

   Figure 8, AWG channels settings.


We can use the scope input channels of the ALM1000 to read the SDATA output waveform. While also monitoring the SCLK and CSB signals generated by the AWG outputs. A typical set of waveforms is shown in figure 8. Green trace is SDATA, dark Orange trace is SCLK and the light Orange trace is CSB.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig9.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 9, SCLK, CSB and SDATA waveforms


Note that, as per the AD7920 datasheet, the first 4 bits of SDATA as read on the falling edge of SCLK are logic 0. The next 12 bits are read on the falling edge of the next 12 SCLK cycles.

You can check the result using the formula for ADC transfer function, where the SDATA data is the Digital output code at pin 2, read on Oscilloscope AIN channel. Optionally the BIN scope channel can be used to measure the Analog Input of the AD7920 at pin 8. The V\ :sub:`REF` is equal to the fixed +5 V supply rail.

.. container:: centeralign

   :math:`Digital output code = ((Analog input)/ (Reference input)) \times ( (2^N)-1)`


:math:`Vin=((Digital code)_10 / ((2^12)-1)) \times V_ref`

:math:`Vin=((07FB)_10/4095) \times V_ref`

:math:`\displaystyle Vin= (\frac{2043}{4095}) \times 3.04 V`

:math:`Vin=1.5 V`

To automate the decoding of the serial data stream on SDATA we can write a Python script that configures the two AWG outputs as was just done in figure 8 and reads the data from the AIN scope input. Download and extract the ad7920-decode.py program from `ad7920-decode.zip <https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/ad7920-decode.zip>`_. Make sure to exit ALICE before running the program (only one program can access the ALM1000 board at a time). You should see a small GUI screen like figure 10. Watch the conversion results, displayed in binary and decimal while you adjust the R\ :sub:`2` pot.

.. image:: https://wiki.analog.com/_media/university/courses/alm1k/alm-signals-labs/alm-sar-adc-fig10.png
   :align: center
   :width: 200px

.. container:: centeralign

   Figure 10, Simple AD7920 decoder GUI.


For extra credit modify the program to display the ADC output results in volts. You could also try to add the ability to use the BIN scope input reading (with BIN connected to pin 8) to also measure the analog voltage at the ADC input and compare these two values.

**For Further Reading:**

| `Successive approximation ADC <https://en.wikipedia.org/wiki/Successive_approximation_ADC>`_
| :adi:`ADC Architectures II: Successive Approximation ADCs <media/en/training-seminars/tutorials/MT-021.pdf>`
| :adi:`ADC and DAC <media/en/technical-documentation/dsp-book/dsp_book_Ch3.pdf>`
| :adi:`Exploring Different SAR ADC Analog Input Architectures <en/technical-articles/exploring-different-sar-adc-analog-input-architectures.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/alm1k/alm-signals-labs-list>`\ **.**

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc_architecture.png
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc_example.png
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/acquisition_conversion_ad792.png
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/adalp2000/bob_ad7920.png
   :width: 300px
