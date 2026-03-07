Adding DC Offsets to AWG Outputs:
=================================

A variety of electronic test applications require you to add a DC offset to a signal generator’s output. The result is a signal that is an AC waveform superimposed on top of a DC voltage. For example, you can use a sine wave added on top of a DC power supply voltage for testing a circuit’s immunity to noise that appears on its power rails, i.e. power supply rejection ratio (PSRR). In the case of testing transistor based amplifiers, you can bias the circuit with a DC voltage that has an AC component riding on top of it. Even a repetitive series of unipolar pulses (used for driving a FET gate signal for DC/DC converters) are can be considered as a pulse train with a DC offset (perhaps equal to ½ the pulse amplitude). All of these applications need a DC plus AC signal, all with different voltage, current, and waveform bandwidth requirements.

Various methods can be employed to generate a waveform on top of a DC voltage. A function generator by itself often can produce a waveform with a DC offset. If you cannot set the DC offset high enough, adding a DC power supply in series with the function generator helps. When you need larger currents, you can use a DC power supply with external analog adjustment terminals that you can drive with a function generator. Or you can use a current mode transformer driven by a signal generator to couple an AC waveform onto the output of a DC power supply.

Using the AWG by Itself
-----------------------

Most arbitrary waveform generators can produce a DC offset along with their output waveforms, as shown in figure 1. The digital to analog converter (DAC) in an arbitrary waveform generator can be programed to produce an output signal with a combined DC offset plus waveform signal voltage in the full scale range of the DAC which is 0 to +5V for the ADLM1000 and -5 to +5V for the ADALM2000. Therefore, you can set the arbitrary waveform generators to produce a small waveform with a DC offset as large as for example 4.995 V. While this is the most convenient way to produce a signal riding on top of a DC offset, your application may require even higher DC offsets. If you need to generate a signal with a larger DC offset than is available from your signal source, you need to employ a different technique.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_1.png
   :align: center
   :width: 400px

.. container:: centeralign

   Figure 1, Producing DC+AC using only a function generator.


Measurement Tip
~~~~~~~~~~~~~~~

Many arbitrary waveform generators, including the ADALM2000 but not the ADALM1000, have a 50Ω output impedance. There is a 50Ω resistor inside the generator that is in series with the output. This design approach, used in high frequency generators, helps minimize signal reflections when the output is connected to a coax cable with a characteristic impedance of 50Ω and is terminated with a 50Ω load. The 50Ω output impedance and 50Ω load form a 2-to-1 voltage divider. Therefore, the actual internal generator voltage is twice the value seen at the load. Note: if the load resistance is infinite (an open circuit), the resulting output voltage is the full value you set. And if the load resistance, R\ :sub:`L`, is any value other than 50 Ω, the actual output voltage, V\ :sub:`OUT`, is: V\ :sub:`OUT` = V\ :sub:`SET` [R\ :sub:`L` / (50 + R\ :sub:`L`)]. See figure 2. Note: this attenuation affects both the AC amplitude and DC offset.

If you set a voltage V\ :sub:`SET` with R\ :sub:`L` = 50Ω: V\ :sub:`OUT` = V\ :sub:`SET` [50/(50+50)] = V\ :sub:`SET`/2

If you set a voltage V\ :sub:`SET`\ t with R\ :sub:`L` = ∞ Ω: V\ :sub:`OUT`\ t= V\ :sub:`SET` [∞/(50+∞)] = V\ :sub:`SET`

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_2.png
   :align: center
   :width: 300px

.. container:: centeralign

   Figure 2, Effect of function generator 50Ω output impedance on output voltage.


Using a Signal Generator in Series with a Power Supply
------------------------------------------------------

If the need is to produce a test signal riding on top of a DC offset, but requires a DC offset larger than the AWG can deliver, place a DC power supply in series with the function generator output, as shown in figure 3. This technique offers you the function generator’s full bandwidth capabilities in addition to having flexibility in the DC level provided by the power supply. However, this technique has a few important limitations. One or both the AWG and DC power supply must be fully isolated from earth (USB cable) ground. The AWG outputs, in the case of the ADALM1000 and ADALM2000, are not internally isolated (floating) from earth (USB cable) ground. This means that if you put a DC power supply in series with the AWG output, the DC power supply must be isolated. The :adi:`LTM8067` isolated μModule (Power Module) DC/DC Converter break-out board is provided in the ADALP2000 Analog Parts Kit. It can take a 3.1 V to 32V input (likely from a wall plug power adapter “wall wart”). A trim pot on the breakout board allows the output voltage to be adjusted from 3V to 15V. Because the output voltage pins are fully isolated the voltage can be either positive or negative depending on which pin is connected to the AWG output. The output current can be as much as 440 mA depending on the input and output voltage setting.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, Producing DC+AC using an AWG in series with an isolated DC power supply.


A limitation of using this technique is that the current available to the load is limited to the output current of the AWG generator, since the load current must flow through both the power supply and AWG output. Also, the ADALM2000 generator has a 50Ω output impedance, meaning any load current flows through this resistance. This resistance forms a voltage divider with the load impedance, so be sure to adjust the DC power supply output voltage accordingly.

.. _measurement-tip-1:

Measurement Tip
~~~~~~~~~~~~~~~

Some bench function/arbitrary waveform generators let you enter a value for the expected load resistance, R\ :sub:`L`, in the range of 1 ohm to 10 k ohms, or infinite. The default value is 50 ohms. If you change the value for this parameter, the function generator automatically adjusts the internal voltage it produces to take into consideration the voltage divider formed by the internal 50Ω resistor and your load resistance such that V\ :sub:`OUT` is equal to the entered voltage setting. This adjustment applies to both the DC offset and AC portion of the function generator output signal.

Using a Power Supply controlled by a Function Generator
-------------------------------------------------------

Another way to produce a signal with a large DC offset is using a power supply that allows access to an external analog programming node or input. A voltage applied to this input is summed by the power supply with its internal voltage reference and produces a proportional voltage on the power supply output terminals. Therefore, you can connect a signal generator output to the analog voltage summing input and modulate the power supply output voltage with the generator signal. See figure 4 which shows an AWG channel driving the SET input of an LT3080 linear voltage regulator. The value of R\ :sub:`POT` sets the DC output offset. This technique provides a lot of flexibility in the DC offset voltage and in the amount of current available to the load (both of which are determined by the power supply ratings).

However, the performance of most DC power supplies can impose significant bandwidth limitations. While most AWG generators produce waveforms in the KHz or even MHz range, the output voltage of most DC power supplies has a bandwidth of only a few Hz depending on the output decoupling capacitors. So, when this technique is used, the signal on the power supply’s output (consisting of the DC offset plus a waveform) has a bandwidth of only a few Hz.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4: Producing DC + AC using an AWG to drive the analog programming input of a Linear DC regulator.


There are many small (low cost) power supply modules available based on DC-DC converters that are adjustable using on board potentiometers such as the three examples shown in figure 5. Because the output setting feedback resistor divider is adjustable the error amplifier summing junction is thus also accessible as we can see in the typical Buck-Boost converter module schematic shown in figure 6. A jumper wire can be readily soldered to the end of the trim pot at the FB (feedback input) pin of the controller IC. Then by selecting an appropriate resistor the signal from an AWG can be injected or summed with the DC feedback from the output. The AWG signal seen at the output will of course be inverted.

A Buck-Boost module is the most versatile choice in that the output can be either higher or lower than the input voltage where in the case of a Buck converter the output can only be lower than the input voltage and for a Boost converter the output can only be higher than the input voltage.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Example adjustable Buck, Buck-Boost and Boost Modules.


.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_6.png
   :align: center
   :width: 650px

.. container:: centeralign

   Figure 6, Producing DC + AC using an AWG to drive the Feedback summing junction of a Buck-Boost Module.


Just about any regulated power supply that has an external, accessible feedback network can be used like this. Just remember the output filtering network of most DC power supplies has a bandwidth of only a few Hz depending on the size of the output decoupling capacitors. So, when you use this technique, the signal on the power supply’s output (consisting of the DC offset plus a waveform) might have a bandwidth of only a few Hz. Also the response to a high going step will likely be much faster than a low going step in that most supplies are only designed to source current. For a low going step the output capacitors will only discharge through the load.

Using a Current Transformer Driven by a Function Generator
----------------------------------------------------------

To get the full output voltage and current benefits of a power supply combined with the higher signal bandwidth available from the AWG generator, a current mode transformer can be used, driven by the AWG generator output, to inject an AC signal in series with the output of a DC power supply. See the configuration shown in figure 7.

There are some limitations to this technique. First, select a current transformer that can support the needed bandwidth. Also ensure that the transformer can support the maximum DC current you expect to flow through it to the load. The transformer winding resistance will cause the average DC voltage seen at the load to be lower than the DC output of the power supply. Note that the inherent galvanic primary to secondary isolation of the transformer windings allows the DC power supply voltage to be very high with respect to the common ground of the AWG.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/awg-dc-offset-fig_7.png
   :align: center
   :width: 550px

.. container:: centeralign

   Figure 7, Producing DC + AC using a DC power supply in series with a current transformer driven by an AWG.


Summary
-------

A variety of lab testing applications require adding a DC offset to an AC signal generator output. There are several different ways to accomplish this. Each method has advantages and disadvantages affecting the range of output voltage, output current, output bandwidth, and the ease of implementation. Ultimately, the method you choose depends on your specific requirements, the equipment at your disposal, and the time you can commit to designing a solution.

Active Learning Module arbitrary waveform generators can produce DC offsets across their entire output voltage range, even with small amplitude waveforms.
