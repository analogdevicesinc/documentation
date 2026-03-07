DC Power Profiling
==================

**Power Consumption Profiling and Battery Life Analysis Techniques**

In other documents the voltage and current measurement features of the :adi:`ADALM1000 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADALM1000.html>` (SMU) have been discussed. In this document techniques to measure DC voltage and current consumption or power of a device or system using the Active Learning Modules are discussed.

Background:
-----------

Energy savings and power efficiency are top priorities for developers’ of an ever-growing number of embedded systems applications. These constraints can be due to government initiatives or regulations, requirements to increase battery life, or simply a need to lower the electricity bill. In battery-operated systems, energy efficiency often plays the most important role. In cases where developers are satisfied with their system’s battery life, increasing the energy efficiency means the design can use a smaller and lighter battery, which could lower the overall cost. There are also situations where the operating life must be extended to the absolute maximum, such as products where the battery cannot be replaced or replacement involves very high costs.

Having a low-power microcontroller (MCU) by itself does not mean a design will have low energy consumption. The trick is to optimize the system software not just in terms of functionality, but also with respect to energy efficiency. Having full control of the hardware surrounding the MCU and optimizing the overall software and peripheral usage are crucial factors for reducing system energy consumption. Software is not usually seen as an energy drain, yet every clock cycle consumes energy. Minimizing the number of clock cycles becomes a key challenge to reduce overall system consumption.

Hardware instruments that can measure voltage and current over an extended time frame enable designers to visualize the energy consumption of individual devices, multiple devices within a larger system, or a network of interacting devices to analyze and improve the power performance of these systems.

Generally, data logging is the capture of data for a specific duration of time. The data is then analyzed to determine the performance of a circuit board, module, or a product. The duration of time can last for seconds, minutes or even hours.

The M1k precision Source Measure Unit (SMU) channels can be used to capture high dynamic range voltage and current measurements over extended time. The M1k's SMU channels can directly measure DC voltages from 0 to 5 V (higher voltages possible by using :doc:`external attenuators </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`) and DC currents from -200mA to +200mA.

Because of the 100 KSPS sampling rate it can actually measure time varying currents as well. But the current to be measured has to be flowing into or out of the SMU channel. This limits the range of voltages that the current must be "referenced" to, 0 to +5V.

Setting Up The Hardware
-----------------------

Simple Use Case:
~~~~~~~~~~~~~~~~

For testing devices that use supply voltages less than or equal to +5 V and currents up to +200 mA, the simplest way to connect the M1k SMU channel to a device under test (DUT) is shown in figure 1.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-1.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 1, Powering DUT directly from SMU channel.


The DUT voltage and current are measured directly and the DUT power is simply calculated from the measured voltage and current. Because the M1k has two SMU channels two devices or partitions of a larger system can be tested at the same time.

Summing in an Offset Current
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The M1k SMU channels operate in two quadrants, positive voltage (0 to 5) and positive and negative current (-200mA to +200mA). When the SMU channels are used to power a system or device under test, generally only the positive half of the current range is required (one quadrant). This effectively wastes half of the available current measurement range. If a constant DC current is summed with the output of an SMU channel (set to SVMI mode) the net current range supplied to the device under test can be effectively offset to be mainly (or Just) in the positive quadrant. The result being, the range of current available is now 0 to as much as +400 mA.

The offset current could be supplied by the second SMU channel as shown in figure 2. A series resistor is used to isolate the two SMU channels. SMU channel A is used as the voltage source, as in figure 1, in SVMI mode and SMU channel B is set in SIMV mode as the offsetting current source. In the example shown the 6.2 Ω power resistor from the :doc:`ADALP2000 </wiki-migration/university/tools/adalp2000/parts-index>` parts kit is used but any low value resistor greater than 2 Ω could be substituted. The output voltage of Channel B cannot go above the 5 V limit which forces the maximum usable voltage from Channel A to be 5 V minus the voltage drop across the series resistor. In this example the voltage drop would be up to 200mA times 6.2 Ω, or 1.24 V. The channel A output voltage would ideally need to be no higher than 5.0 – 1.24 = 3.76. Practically speaking the maximum usable voltage might be closer to 3.3 or 3.5 V. This is still a very useful supply voltage range in that many micro-controllers operate at 3.3V or even lower.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-2.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 2, Offset current summed from CHB.


The current from CHA can be both positive when the DUT current is greater than the constant DC offset current from CHB and negative when the DUT current is less than the constant DC offset current from CHB.

If a 1.5 V AA battery, B\ :sub:`1`, for example is substituted for resistor R\ :sub:`1` as shown in figure 3 the voltage seen at the output of SMU Channel B will be 1.5 V lower (more negative) than the DUT voltage which is set by SMU Channel A. Now SMU Channel A can be set all the way up to the maximum +5.0 V. However, the lowest voltage that SMU Channel A can be set to now has to be greater than the battery voltage or +1.5V in this case. Other battery voltages can be used as long as the voltage seen at the output of SMU Channel B remains within the permitted 0 to +5 V.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-3.png
   :align: center
   :width: 500px

.. container:: centeralign

   Figure 3, External Battery Offsets CHB voltage.


Offset current from external powered source:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As an alternative, an externally powered current source such as the :adi:`LT3092` from the ADALP2000 kit could be used as in figure 4. Fixed resistors R\ :sub:`1` and R\ :sub:`2` along with variable resistor R\ :sub:`pot` adjust the DC current supplied. The external power supply voltage needs to be high enough to accommodate the DUT voltage plus the minimum voltage headroom of the LT3092 current source. Given there is 1 V across R\ :sub:`1` plus the 1.2 V minimum headroom of the LT3092, the external power supply voltage will need to be at least 2.2 V greater than the DUT voltage or 7.2 V for V\ :sub:`DUT` equal to 5 V.

With the externally powered current source it is possible to potentially drive the CHA output pin above the +5 V limit when the SMU channel is off or in the Hi-Z mode. To limit the current that would otherwise flow in the output protection diodes on the M1k board, clamp PNP transistor Q\ :sub:`1` is added to the output as shown. If the voltage on CHA where to go more than 0.6 V above +5 V the transistor will turn on shunting the current to ground. The resistor in the collector shares some of the power dissipation with Q\ :sub:`1`. Q\ :sub:`1` can be any PNP transistor capable of handling the possible 200 mA current.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-4.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 4, External offset current from LT3092.


LT3080 variant
^^^^^^^^^^^^^^

The :adi:`LT3080` linear regulator can be used in a similar current source configuration with a slightly different pinout as in figure 5. Please refer to the LT3080 datasheet page 21 for more detail on use as a two terminal current source.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-5.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 5, Variant that uses LT3080.


Case for DUT powered by battery voltage greater than 5 V:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suppose the use case is to profile a DUT powered from a 9V battery, B\ :sub:`1`, as in figure 6. With SMU channel A set in the SVMI Split I/O mode and with the voltage source set to 0 V and with output pin CHA connected to the negative battery terminal it can measure the DUT current. The 9 V battery voltage is too high to measure directly with the AIN input. Voltage divider R\ :sub:`1` and R\ :sub:`2` in parallel with the internal 1 MΩ resistor forms a ratio of 2.47. This allows the AIN input to measure voltages up to 2.47 X 5.0 or 12.35 V which is more than enough to measure the 9 V battery (other resistor divider values can of course be used, more on using voltage divider can be found here: :doc:`Measuring voltages beyond 0 to 5V with the ADALM1000 (M1K) </wiki-migration/university/courses/alm1k/circuits1/alm-measure-outside-0-5-range>`).

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-6.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 6, Measuring DUT with supply voltage greater than +5 V.


It is also of course possible to combine the offset current technique here as well.

Special Power Profiler Software:
--------------------------------

The ALICE desktop software can of course be used to capture the test voltage and current measurements vs time but it is not ideally suited to this application. The Data Logger tool is closer but lacks the ability to display the current or power over time. The Power Profiler tool adds this functionality. Python source code can be found `here <https://raw.githubusercontent.com/analogdevicesinc/alice/Version-1.3/power-profiler-1.3.pyw>`_.

Once the program is running the main time trace display and controls, as shown in figure 7, should appear. Be sure that the ALM1000 is plugged into the USB port before starting the program. When first started the chart will be blank.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-7.png
   :align: center
   :width: 700px

.. container:: centeralign

   Figure 7 Power Profiler software tool.


The majority of the area is taken up by the graph or chart. Below that are various control buttons and entry slots. Starting on the left there are controls for each SMU channel. One trace can be displayed for each channel, either voltage, current, power or off. Traces can be drawn on a single grid or on 2 separate grids. On the chart, there are 10 equally spaced vertical grids drawn on the single grid or 5 equally spaced vertical grids drawn on each of the two grids. Next to that are controls to set the vertical range (scale per division) and position (offset) for each channel.

The Run button starts the recording and the Stop button will pause the recording. The Reset button clears the chart. The Exit button closes the program. With the Save Screen button you can save the chart area to an encapsulated postscript file.

Normally the program records data continuously until the Stop button is clicked. Clicking on the Run For box and entering a number of samples will halt the recording after running for the set number of samples. Entering a number of seconds greater than zero for the Delay will take data samples at that rate, otherwise the sample rate (from 50 sps to 300 sps) can be selected with the spinbox. The actual average number of samples per second (Sps) is displayed. Finally there is a control to turn on/off logging to a file.

The SMU channel controls are shown in figure 8. These are essentially the same as in the Meter-Source and Data Logger tools.

.. image:: https://wiki.analog.com/_media/university/courses/tutorials/alm-power-profile-fig-8.png
   :align: center
   :width: 600px

.. container:: centeralign

   Figure 8, SMU Channel DC controls.


There are buttons to Save and Load the channel configuration.

**For Further Reading**
