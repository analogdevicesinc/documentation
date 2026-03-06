Activity: Analog to Digital Conversion
======================================

Objective
---------

The purpose of this lab activity is to explore the concepts of analog to digital conversion by building explanatory examples.

Background
~~~~~~~~~~

Analog-to-Digital converters (ADC) translate analog signals, real world signals like temperature, pressure, voltage, current, distance, or light intensity, into a digital representation of that signal. This digital representation can then be processed, manipulated, computed, transmitted or stored.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f1.gif
   :align: center

.. container:: centeralign

   Figure 1. Analog to Digital conversion


An ADC samples an analog waveform at uniform time intervals and assigns a digital value to each sample. The digital value appears on the converter’s output in a binary coded format. The value is obtained by dividing the sampled analog input voltage by the reference voltage and them multiplying by the number of digital codes. The resolution of converter is set by the number of binary bits in the output code.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f3.gif
   :align: center

.. container:: centeralign

   Figure 2. Digital output code


An ADC carries out two processes, sampling and quantization. The ADC represents an analog signal, which has infinite resolution, as a digital code that has finite resolution. The ADC produces 2N digital values where N represents the number of binary output bits. The analog input signal will fall between the quantization levels because the converter has finite resolution resulting in an inherent uncertainty or quantization error. That error determines the maximum dynamic range of the converter.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f4.gif
   :align: center

.. container:: centeralign

   Figure 3. Quantization Process


The sampling process represents a continuous time domain signal with values measured at discrete and uniform time intervals. This process determines the maximum bandwidth of the sampled signal in accordance with the Nyquist Theory. This theory states that the signal frequency must be less than or equal to one half the sampling frequency to prevent aliasing. Aliasing is a condition in which frequency signals outside the desired signal band will, through the sampling process, appear within the bandwidth of interest. However, this aliasing process can be exploited in communications systems design to down-convert a high frequency signal to a lower frequency. This technique is known as under-sampling. A criterion for under-sampling is that the ADC has sufficient input bandwidth and dynamic range to acquire the highest frequency signal of interest.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f5.gif
   :align: center

.. container:: centeralign

   Figure 4. Sampling Process


Sampling and quantization are important concepts because they establish the performance limits of an ideal ADC. In an ideal ADC, the code transitions are exactly 1 least significant bit (LSB) apart. So, for an N-bit ADC, there are 2N codes and 1 LSB = FS/2N, where FS is the full-scale analog input voltage. However, ADC operation in the real world is also affected by non-ideal effects, which produce errors beyond those dictated by converter resolution and sample rate. These errors are reflected in a number of AC and DC performance specifications associated with ADCs.

.. image:: https://wiki.analog.com/_media/university/courses/electronics/text/chptr20-f6.gif
   :align: center

.. container:: centeralign

   Figure 5. Transfer Function for an Ideal ADC


Any analog input in this range gives the same digital output code.

Materials
---------

| ADALM2000 Active Learning Module
| Solder-less breadboard, and jumper wire kit
| 1 OP482 operational amplifiers
| 2 AD654 Voltage-to-Frequency Converter
| 3 1kΩ resistor
| 5 10kΩ resistor
| 1 nF capacitor
| 1 SN74HC08 AND gate
| 1 SN74HC32 OR gate
| 1 SN74HC04 inverter
| 1 1 uF capacitor
| 1 AD7920 12-bit ADC

Flash ADC
---------

.. _background-1:

Background
~~~~~~~~~~

Flash analog-to-digital converters, also known as parallel ADCs, are one of the fastest way to convert an analog signal to a digital signal. Flash ADCs are ideal for applications requiring very large bandwidth, but they consume more power than other ADC architectures and are generally limited to 8-bit resolution. Typical examples include data acquisition, satellite communication, radar processing, sampling oscilloscopes, and high-density disk drives.

Flash ADCs are made by cascading high-speed comparators. For an N-bit converter, the circuit employs 2N-1 comparators. A resistive-divider with 2N resistors provides the reference voltage. Each comparator produces a 1 when its analog input voltage is higher than the reference voltage applied to it. Otherwise, the comparator output is 0. The point where the code changes from ones to zeros is the point at which the input signal becomes smaller than the respective comparator reference-voltage levels.

Consider the circuit presented in Figure 6.

.. container:: centeralign


|image1|

.. container:: centeralign

   Figure 6. Flash ADC - analog side circuit


The circuit represents the analog side of a 2-bit Flash ADC with the architecture known as thermometer code (unary code) encoding. For this type of circuit additional logical circuitry is used to decode the unary code to appropriate digital output code. Using logic AND, OR, and INV gates we can build a priority encoder. It's output is the binary representation of the original number starting from zero of the most significant input bit.

.. container:: centeralign


|image2|

.. container:: centeralign

   Figure 7. Flash ADC - encoded output


As mentioned before, flash ADCs are made using high-speed comparators, but for convenience, we are going to use the OP482 quad op-amp to illustrate the principle. Alternatively, you can build the circuit using four AD8561 comparators.

Hardware Setup
~~~~~~~~~~~~~~

Build the circuit presented in figure 7 on your solderless breadboard. This is a circuit for 2-bit Flash ADC with encoded output.

.. container:: centeralign


|image3|

.. container:: centeralign

   Figure 8. Flash ADC breadboard connections


Procedure
~~~~~~~~~

Supply the circuit to +/-5V from the power supply. Configure AWG1 of the Signal Generator to Rising Ramp Sawtooth with 5V amplitude peak-to-peak, 2.5 V offset and 100Hz frequency. Use AWG2 as 5V constant reference voltage for the ADC.

Configure the Logic Analyzer so that the digital channels DIO0, DIO1, DIO2 form a channel group decoded for Unary code and channels DIO6 and DIO7 form a channel group decoded for parralel output.

A plot with the output signals are presented in Figure 9.

.. container:: centeralign


|image4|

.. container:: centeralign

   Figure 9. Flash ADC - output code


The Unary group channel represents the output thermometer code for the 2-bit Flash ADC with all possible output values, by varying the input analog voltage through the entire available range (0-5V). On the Parallel channel are represented the binary values equivalent to the ADC output states.

Voltage-to-Frequency Converter as ADC
-------------------------------------

.. _background-2:

Background
~~~~~~~~~~

For this particular application AD654 Voltage-to-Frequency converter is used as an analog-to-digital converter.

.. container:: centeralign


|image5|

.. container:: centeralign

   Figure 10. Voltage-to-Frequency Converter as ADC


In order to achieve the conversion, the output of the converter should be connected to a microcomputer that has an interval timer/event counter.

The total number of signal edges (rising or falling) counted during the count period is proportional to the input voltage. For this particular setup a 1 V full-scale input voltage produces a 100 kHz signal. If the count period is 100 ms, then the total count will be 10,000. Scaling from this maximum is then used to determine the input voltage. Thus, a count of 5000 corresponds to an input voltage of 0.5 V.

.. _hardware-setup-1:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for Voltage-to-Frequency Converter as ADC.

.. container:: centeralign


|image6|

.. container:: centeralign

   Figure 11. Voltage-to-Frequency Converter as ADC - breadboard connections


.. _procedure-1:

Procedure
~~~~~~~~~

Supply the circuit to +5V from the power supply. Configure AWG1 of the Signal Generator to 1V constant voltage

Configure the scope such that the output signal is displayed on channel 1 and enable the frequency measurement from the channel 1 Measure tab.

A plot with the output signal is presented in Figure 12.

.. container:: centeralign


|image7|

.. container:: centeralign

   Figure 12. Voltage-to-Frequency Converter as ADC at full scale input voltage


The plot represents the output signal of the Voltage-to-Frequency Converter for a 1V full scale input voltage. Notice that the corresponding output frequency is 100kHz.

Now set the input voltage at 0.5V. A plot with the output signal is presented in Figure 13.

.. container:: centeralign


|image8|

.. container:: centeralign

   Figure 13. Voltage-to-Frequency Converter as ADC at half scale input voltage


The plot represents the output signal of the Voltage-to-Frequency Converter for a 0.5V half scale input voltage. Note that output frequency is now 50kHz.

Successive Approximation Register (SAR) ADC
-------------------------------------------

.. _background-3:

Background
~~~~~~~~~~

The successive approximation ADC converts the continuous analog waveform into a discrete digital representation via a binary search through all possible quantization levels before finally converging upon a digital output for each conversion.

Usually, the SAR ADC circuit consists of four subcircuits:

-  Sample and hold circuit (S/H) to acquire the input voltage (Vin).
-  Analog voltage comparator that compares Vin to the output of the internal DAC and outputs the result of the comparison to the SAR
-  Successive approximation register subcircuit designed to supply an approximate digital code of Vin to the internal DAC
-  Internal reference DAC that supplies the comparator with an analog voltage equal to the digital code output of the SAR.

.. container:: centeralign


|image9|

.. container:: centeralign

   Figure 14. SAR ADC - Typical Architecture


The SAR is initialized so that the most significant bit (MSB) is equal to a digital 1. This code is fed into the DAC, which then supplies the analog equivalent of this digital code (Vref/2) into the comparator circuit for comparison with the sampled input voltage. If this analog voltage exceeds Vin the comparator causes the SAR to reset this bit; otherwise, the bit is left a 1. Then the next bit is set to 1 and the same test is done, continuing this binary search until every bit in the SAR has been tested. The resulting code is the digital approximation of the sampled input voltage and is finally output by the SAR at the end of the conversion (EOC).

.. container:: centeralign


|image10|

.. container:: centeralign

   Figure 15. SAR ADC example (4-bit)


Figure 15 shows an example of a 4-bit conversion. The y-axis represents the DAC output voltage. In the example, the first comparison shows that VIN < VDAC. Thus, bit 3 is set to 0. The DAC is then set to 0100 and the second comparison is performed. As VIN > VDAC, bit 2 remains at 1. The DAC is then set to 0110, and the third comparison is performed. Bit 1 is set to 0, and the DAC is then set to 0101 for the final comparison. Finally, bit 0 remains at 1 because VIN > VDAC.

.. _hardware-setup-2:

Hardware Setup
~~~~~~~~~~~~~~

In order to emphasize the operation principle of the SAR ADC with ADALM2000, we will use for the DAC part the circuit sudied in the :doc:`Resistor Ladder Digital to Analog Converter </wiki-migration/university/courses/electronics/electronics-lab-14>` lab, but for this setup we will use a 4-bit DAC (instead of 8-bit). The output of the DAC will be connected to a comparator, while the SAR will be simulated via a script that performs the binary search based on the comparator's output and generates the proper binary value.

.. container:: centeralign


|image11|

.. container:: centeralign

   Figure 16. SAR ADC schematic


Build the following breadboard circuit for SAR ADC.

.. container:: centeralign


|image12|

.. container:: centeralign

   Figure 17. SAR ADC breadboard connections


Two Precision Rail-to-Rail op-amps from the OP484 integrated circuit were used for the SAR ADC, one is used for the R-2R Ladder DAC, and the other one as comparator between the DAC output and input voltage.

.. _procedure-2:

Procedure
~~~~~~~~~

Supply the circuit to +/-5V from the power supply. Configure the scope so that the comparator output signal is displayed on channel 1 and the DAC output on channel 2.

Group the first 4 digital channels in the Logic Analyzer and set the decoder to parallel.

Download the SAR ADC script from the link in the Resources section.

Run the script using the Scopy interface. (A guide on how to use scripts with Scopy can be found here: :doc:`Scopy - Scripting Guide </wiki-migration/university/tools/m2k/scopy/scripting-guide>` )

Visualize the digital output behavior on the Logic Analyzer. An animated plot example is presented in Figure 18.

.. container:: centeralign


|image13|

.. container:: centeralign

   Figure 18. SAR ADC digital output


The digital code is updated using the successive approximation method based on the feedback received from the comparator output.

Visualize the apporximation behavior of the DAC output in time domain using the Oscilloscope. A plot example is presented in Figure 17.

.. container:: centeralign


|image14|

.. container:: centeralign

   Figure 19. SAR ADC approximation plot


The output value trying to reach the input value (which is set to 2V in the script ) after several approximation steps.

AD7920 12-bit ADC
-----------------

.. _background-4:

Background
~~~~~~~~~~

The :adi:`AD7920 <media/en/technical-documentation/data-sheets/AD7910_7920.pdf>` is a 12-bit high speed, low power, succesive approximation ADC. It can operate with a single power supply in range 2.35V to 5.25V. This ADC can be serial interfaced. The serial clock provides the conversion clock and also controls the transfer of information from the AD7920 during conversion. The conversion process and data acquisition are controlled using /CS and the serial clock, allowing the devices to interface with microprocessors or DSPs. The input signal is sampled on the falling edge of CS and the conversion is initiated at this point. In figure 20 are shown simplified schematics of the ADC during the aqcuisition and the conversion phase.

.. container:: centeralign

   \


   |image15|

.. container:: centeralign

   Figure 20. AD7920 acquisition and conversion phase


The acquisition phase is when the SW2 is closed and SW1 is in position A. With this setup, the comparator is held in a balanced condition, and the sampling capacitor acquires the signal on Vin. For the ADC to start a conversion, SW2 opens and SW1 moves to Position B causing the comparator to become unbalaced. the control logic and charge redistribution DAC are used to add and subtract fixed amounts of charge from the sampling capacitor to bring the comparator back to a balanced condition so the conversion is completed.

.. _hardware-setup-3:

Hardware Setup
~~~~~~~~~~~~~~

Figure 21 shows a typical connection setup for the AD7920. VREF is taken internally from VDD so it should be well decoupled. This provides an analog input range of 0 V to VDD. The conversion result is output in a 16-bit word with four leading zeros followed by the MSB of the 12-bit or 10-bit result.

.. container:: centeralign

   |image16|\


.. container:: centeralign

   Figure 21. AD7920 typical connections


.. container:: centeralign

   |image17|\


.. container:: centeralign

   Figure 22. AD7920 breadboard connections


.. _procedure-3:

Procedure
~~~~~~~~~

Open Scopy and enable the positive power supply to 3V. Configure the channel 1 of the Signal Generator as a Constant with a value in range 0-3V, for example the middle domain value 1.5V. You can monitor the actual value of these voltages on the oscilloscope.

.. container:: centeralign

   \ |image18|\


.. container:: centeralign

   Figure 23. Vin (channel 1) and Vref(channel 2) voltages


In Logic Analyzer configure DIO0, DIO1 and DIO2 as a group channel. Set the group channel as SPI and the cannels to corresponding SPI signals. DIO0 as CS#, DIO1 as CLK and DIO2 as MISO. As the CS# falling edge initiates the data transfer, you should set the trigger of DIO0 to falling edge. Set the DIO1 trigger to low and from trigger settings set Trigger Logic to AND. DIO2 does not need a trigger setting as it is the output signal of the ADC. Enable Logic Analizer and it should be waiting for the trigger signals.

In Patern Generator you should configure the clock signal. Enable DIO1 channel, set it's Pattern as Clock with a 5Mhz frequency and click Run. You can control the CS# from the Digital IO tool. The conversion will start when you toggle DIO0 pin, configured as output pin. If the fallnig edge of CS# and the low state of CLK happen the same time, the conversion is initiated and you shoud see the output sigal as well as MISO hexadecimal data in Logic Analyzer as in figure 24.

|

.. container:: centeralign

   \ |image19|\


.. container:: centeralign

   Figure 24. SPI interface of the AD7920


You can check the result using the formula for ADC transfer function, where the MISO data is the Digital output code, voltage read on Oscilloscope channel 1 is the Analog Input, voltage read on Oscilloscope channel 2 is the Reference Input and N is the number of bits of AD7920.
|

.. container:: centeralign

   :math:`Digital output code = ((Analog input)/ (Reference input)) \times ( (2^N)-1)`


:math:`Vin=((Digital code)_10 / ((2^12)-1)) \times V_ref`

:math:`Vin=((07FB)_10/4095) \times V_ref`

:math:`\displaystyle Vin= (\frac{2043}{4095}) \times 3.04 V`

:math:`Vin=1.5 V`

From the above computation it results that the ADC input voltage is 1.5 V, the same value read on the oscilloscope channel 1.

Extra Activity: Dual-Slope ADC
------------------------------

The Dual-Slope ADC (or a variant) is at the heart of many of the most accurate digital voltmeters. This architecture has a few useful characteristics: only a few precision components are required as most error sources cancel out, it can be configured to reject particular noise frequencies such as 50Hz or 60Hz line noise, and it is insensitive to high-frequency noise.

.. container:: centeralign


|image20|

.. container:: centeralign

   Figure 25. Dual-Slope ADC structure


The converter operates by applying the unknown input voltage to an integrator for a fixed time period (called “runup”), after which a known reference voltage, of opposite polarity to the input, is applied to the integrator (called “rundown”). Thus, the input voltage can be calculated from the reference voltage and the ratio of the rundown to runup times:

:math:`Vin = Vref \times (T_rundown/T_runup)`

.. container:: centeralign


|image21|

.. container:: centeralign

   Figure 25. Dual-Slope ADC Integrator output waveforms


By inspection, the accuracy of the dual-slope converter is not affected by the tolerance of most of the components:

-  The integrator’s resistor and capacitor tolerance will affect the slope of the output, but it will affect both runup and rundown equally.
-  Errors in the timebase used to set the runup time and measure the rundown time will affect both times equally.

The reference voltage does need to be accurate, as it directly affects the measurement. Another error source is dielectric absorption in the integrator capacitor, so polypropylene or polystyrene is ideal, and aluminum electrolytic are not appropriate.

.. container:: centeralign


|image22|

.. container:: centeralign

   Figure 27. Dual-Slope ADC Integrator output waveforms


Figure 27 shows the frequency response of a dual-slope ADC. The input is sampled for a fixed time interval (runup), the voltage at the beginning of runup has as much influence on the result as the voltage at the end of runup. This is sometimes called a “boxcar average”, and it has the effect of rejecting disturbances (noise) that occur at frequencies of 1/T, 2/T, 3/T, etc. An integration time of 200ms corresponds to 10 cycles of 50Hz noise, and 12 cycles of 60Hz noise, so this is often chosen as the runup time as it rejects line noise in any country in the world.

Simulation
~~~~~~~~~~

Open the LTspice file DualSlope.asc

.. container:: centeralign


|image23|

.. container:: centeralign

   Figure 28. Dual-Slope ADC Integrator Schematic


Run the simulation, probing the Vintegrate node:

.. container:: centeralign


|image24|

.. container:: centeralign

   Figure 29. Dual-Slope ADC Integrator Simulation 1


The simulation adds 60Hz line noise to a DC input voltage. Several cases are run by the .step directive – input voltages of 1V, 2V, 3V, 4V 5V, and several different phases of the 60Hz line noise. Because the 200ms runup time is an integer number of 60Hz line cycles, the noise falls into a null in the frequency response and rundown time is unaffected, regardless of phase. Change the frequency to 62.5Hz, which lies at a peak in the frequency response:

.. container:: centeralign


|image25|

.. container:: centeralign

   Figure 30. Dual-Slope ADC Integrator Simulation 2


.. _hardware-setup-4:

Hardware Setup
~~~~~~~~~~~~~~

Build the following breadboard circuit for the dual-slope ADC, and make the indicated connections to the M2K.

.. container:: centeralign


|image26|

.. container:: centeralign

   Figure 31. Dual-Slope ADC Integrator Breadboard Circuit


.. _procedure-4:

Procedure
~~~~~~~~~

Open Scopy. A Scopy initialization file is included to aid in setup,\ :git-education_tools:`m2k/other_resources/dual_slope_adc/Dual_slope_scopy_setup.ini`

Power Supply: Tracking enabled, set to +/-5V

Digitial IO: DIO2 set to OUT, set to 1

Pattern Generator: Group DIO0, DIO1, Pattern: Import (load file :git-education_tools:`m2k/other_resources/dual_slope_adc/dual_slope_pattern.csv` ) Frequency set to 5Hz.

Signal Generator: Channel 1 initally set to constant +2.5V

Oscilloscope: 200ms timebase, Ch1 set to 400mV/division. Falling-edge trigger, 200mV (this triggers the M2K at the start of the integrator’s reset interval.)

.. container:: centeralign


|image27|

.. container:: centeralign

   Figure 32. Dual-Slope ADC Integrator waveform


With the reference tied to the -5V supply and the input voltage set to 2.5V, notice that rundown is 2 divisions (400ms) while runup is 1 division (200ms). Thus:

Vin = 5V \* (200ms / 400ms) = 2.5V

By varying the input voltage we can notice a change in the runup time. An animated plot is presented in Figure 33.

.. container:: centeralign


|image28|

.. container:: centeralign

   Figure 34. Dual-Slope ADC Integrator waveform for different input voltages


Using the formula presented above and different runup time values, can you compute/guess the input voltages applied?

A practical implementation of a dual-slope converter would use a microcontroller to control the integrator and set the runup / measure the rundown times. Most microcontrollers have counter peripherals, making this a fairly easy task.

Further Reading
---------------

.. admonition:: Download
   :class: download

   **Lab Resources:**

   
   -  Fritzing files: :git-education_tools:`m2k/fritzing/adc_lab_bb`
   -  LTSpice files: :git-education_tools:`m2k/ltspice/adc_ltspice`
   -  JavaScript files: :git-education_tools:`m2k/javascript/sar_adc_script`
   


Some additional resources:

-  :adi:`ADC and DAC <media/en/technical-documentation/dsp-book/dsp_book_Ch3.pdf>`
-  :adi:`AD654 Voltage-to-Frequency Converter <en/products/analog-to-digital-converters/integrated-special-purpose-converters/voltage-to-frequency-converters/ad654.html>`
-  :adi:`Exploring Different SAR ADC Analog Input Architectures <en/technical-articles/exploring-different-sar-adc-analog-input-architectures.html>`
-  :adi:`RF Sampling ADCs Offer Advantages in Systems Design <en/technical-articles/rf-sampling-adc-offer-advantages-in-systems-design.html>`

**Return to Lab Activity** :doc:`Table of Contents </wiki-migration/university/courses/electronics/labs>`

.. |image1| image:: https://wiki.analog.com/_media/university/courses/electronics/flash_adc.png
   :width: 350px
.. |image2| image:: https://wiki.analog.com/_media/university/courses/electronics/flash_adc-decoded_output.png
   :width: 750px
.. |image3| image:: https://wiki.analog.com/_media/university/courses/electronics/flash_adc-bb.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/university/courses/electronics/flash_adc_logic_gates_out.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/courses/electronics/voltagetofrequencyconverteradc.png
   :width: 500px
.. |image6| image:: https://wiki.analog.com/_media/university/courses/electronics/vf_adc-bb.png
.. |image7| image:: https://wiki.analog.com/_media/university/courses/electronics/vf_adc-wav1.png
.. |image8| image:: https://wiki.analog.com/_media/university/courses/electronics/vf_adc-wav2.png
.. |image9| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc_architecture.png
.. |image10| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc_example.png
.. |image11| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc.png
   :width: 700px
.. |image12| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc-bb.png
.. |image13| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc-digital.gif
.. |image14| image:: https://wiki.analog.com/_media/university/courses/electronics/sar_adc-wav.png
.. |image15| image:: https://wiki.analog.com/_media/university/courses/electronics/acquisition_conversion_ad792.png
   :width: 800px
.. |image16| image:: https://wiki.analog.com/_media/university/courses/electronics/ad7920_connections.png
   :width: 500px
.. |image17| image:: https://wiki.analog.com/_media/university/courses/electronics/ad7920_connections_bb.png
   :width: 900px
.. |image18| image:: https://wiki.analog.com/_media/university/courses/electronics/vref_vin.png
   :width: 900px
.. |image19| image:: https://wiki.analog.com/_media/university/courses/electronics/adc_out_1_5v.png
   :width: 900px
.. |image20| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-struct.png
   :width: 500px
.. |image21| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-integr_wav.png
   :width: 500px
.. |image22| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-freq_resp.png
   :width: 500px
.. |image23| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-sch.png
.. |image24| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-sim1.png
.. |image25| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-sim2.png
.. |image26| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-bb.png
.. |image27| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-wav.png
.. |image28| image:: https://wiki.analog.com/_media/university/courses/electronics/dual_slope-wav.gif
