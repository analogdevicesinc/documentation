ADC digital filters
===================

The ADALM2000 hardware design includes two gain range settings for the analog input voltage divider:

-  High gain mode: for signals from -2.5 V to +2.5V ( 0.5V/Div setting or lower )
-  Low gain mode: for signals from -25 V to 25 V ( 1.0V/Div setting or higher )

As in any voltage divider, parasitic capacitance introduces a low pass frequency response for signals passing through the divider and needs to compensated. This is generally done by adding adjustable capacitance to the divider network. Hardware frequency compensation calibration of the ADALM2000 is performed by adjusting the 4 trimmer capacitors so that a test square waveform looks as flat top as possible. During board production the trim capacitors are adjusted in the high gain mode. However, even for a this very accurate calibration, when switched to low gain mode the frequency compensation may not be as good. To solve this mismatch issue between gain ranges two digital filters have been included in the Scopy software with adjustable gain and time constant parameters.

The filters can be enabled or disabled in Scopy from the Preferences tab and when enabled, their configurable parameters are found in the :doc:`Scopy Oscilloscope </wiki-migration/university/tools/m2k/scopy/oscilloscope>` instrument under the corresponding channel settings. Each filter has its own pair of parameters: gain and time constant. These parameters depend on the residual frequency response of the hardware divider network after the trim capacitors have been adjusted.


|image1|

.. container:: centeralign

   Figure 1. Scopy preferences menu where ADC filters can be activated


   |image2|

.. container:: centeralign

   Figure 2. ADC digital filters parameters


There are two cascaded single pole recursive filters that can be independently enabled. These types of filters can be used to process digital signals just as you would use RC networks to frequency compensate analog signals. This includes: DC removal, high-frequency noise suppression, wave shaping, smoothing, etc.

|

.. tip::

   **Exponential compensation**

   | The software frequency compensation technique used in Scopy is often called Exponential compensation which adds one or more exponentially decaying terms to a step in the signal. With 2 available stages, Scopy can correct for multiple spurious inductances and capacitances in the internal or external input divider circuit (such as a 10X probe). **Exponential compensation works best for overshoots and undershoots smaller than about 10% of the step height.** In this case, a sum of exponential terms is an accurate generic model for such defects.


The digital filters provide a solution for the hardware calibration mismatch issue between low gain and high gain modes. The setting of these compensation parameters can be determined by following these steps. The Signal Generator outputs of the ADALM2000 should be connected to the Oscilloscope inputs. Oscilloscope +1 to Signal Generator CH 1 and Oscilloscope 2+ to Signal Generator CH 2 with 1- and 2- tied to GND. The Signal Generator channels should be set for Square wave shape and the amplitude set to +2.4 V with 0 offset. Set the Frequency to 4 KHz ( generally a good place to start but other frequencies might work better ). Adjust the Scope time scale to show two cycles of the waveform. With the vertical scale set to 0.5 V/Div observe the shape of the waveform. If the hardware trim was done properly the top and bottom of the wave should be flat. Now switch to 1.0 V/Div setting. The waveform might now be either under or over compensated. If it is under compensated the gain correction parameter should be a positive number. If it is over compensated the gain correction parameter should be a negative number. The value of the gain parameter can be estimated by the ratio of the size of the exponential portion of the waveform to the settled wave amplitude ( P-P step ) which is 4.8 V in this case. The Time Constant parameter can be estimated from the 63% settled time point in the waveform in microSeconds. Once these estimated values are entered and the filter is enabled further fine tuning of the values can be done to make the wave as square topped as possible.

Calibration using the hardware trimmers
---------------------------------------

The boards are calibrated in the factory during production test but sometimes the trimmers, highlighted in Figure 3, might need be adjusted by the user as well.


|image3|

.. container:: centeralign

   Figure 3. M2k calibration trimmers highlighted


It is necessary to connect the AWG signal generator output channels to the oscilloscope input channels in a loopback configuration as described above in the section on the software filter adjustments driving the scope 1+ and 2+ inputs or the scope 1- and 2- inputs for the corresponding trim capacitors. Generate a square wave with 2.4 V amplitude and 4kHz frequency then analyze the oscilloscope window, in high gain mode (vertical range setting should be 0.5 V/Div or less). The waveform should look as square, flat top and bottom as possible.



|image4|

.. container:: centeralign

   Figure 4. Waveform before high gain hardware calibration


If the waveform does not have the desired square shape, then you should adjust the trimmers of the corresponding channel until the waveform looks like the example in Figure 5.



|image5|

.. container:: centeralign

   Figure 5. Waveform after high gain hardware calibration


The inputs are now calibrated but you may notice a difference in response if you switch from high gain mode to low gain mode ( 1V/Div or higher). The ADC digital filters were implemented to compensated for this range mismatch issue.



|image6|

.. container:: centeralign

   Figure 6. Waveform after high gain hardware calibration, but visualized in low gain mode


Compensation using the digital filters
--------------------------------------

The slight overshoot that appear in low gain mode after the board is calibrated in high gain mode can be removed using the digital filters. For better results, we can enable both filters with corresponding parameters, so the wave will be perfectly square. If we zoom in on the signal presented in Figure 7 we can notice the 50 mV overshoot.


|image7|

.. container:: centeralign

   Figure 7. 50 mV Overshoot of the signal


This can be removed if we apply a digital filter with the following parameters: TC=60 and gain=-0.025 The filtered signal will appear as in Figure 8.



|image8|

.. container:: centeralign

   Figure 8.Initial signal (green) and filtered signal(orange)


It is noticed an improvement in the shape of the signal, but we can obtain an even better result using the second filter cascaded. With Filter 2 enabled and its parameters set to TC=9 and gain=0.047 the response is visibly improved, as shown in Figure 9.



|image9|

.. container:: centeralign

   Figure 9.Initial signal (green),Filter 1 signal(cyan), cascaded filters signal(orange)


In Figure 10 you can see the same signal previously presented in Figure 6 but with the digital filters enabled. Is visible that the slight overshoot has disappeared. Now you can change between high and low gain modes and have an almost perfect square signal in both cases.



|image10|

.. container:: centeralign

   Figure 10.Filtered signal


Further you can find some examples on how to determine the suitable filter parameters depending on the signal characteristics.

Examples for determining Gain and TC
------------------------------------

There are two possible cases: The signal may be under compensated (undershoot), or it can be over compensated (overshoot). In the case of undershoot it is necessary to apply a high pass response to cancel the under compensation and in case of overshoot a low pass response. For both cases we can used the same digital filter because the filter function has a high-pass response if gain parameter is positive and a low-pass response if gain parameter is negative.

:math:`gain=\delta/Vpp`

:math:`\delta=value at which the signal settles-initial value of the signal`

:math:`Vpp=peak to peak amplitude of the signal`

:math:`TC=number of microSeconds it takes the signal to rise from initial point to 63.2% \times \delta`

Undershoot
~~~~~~~~~~

To find 𝛿, place one horizontal cursor at the initial point of the signal and the other one at the point where the signal settles. In the case presented in Figure 6 the peak to peak value of the signal is 5 V.

:math:`\delta=2.491-2.141=0.35 V`

:math:`\displaystyle gain=0.\frac{35}{5}=0.07`


|image11|

.. container:: centeralign

   Figure 11. Cursors placement to find delta


To find TC place one vertical cursor at the initial point and the other one at the point where signal is equal with its initial value plus 63.2% of 𝛿.

:math:`63.2% \times \delta=0.632 \times 0.35=0.221`

In this example TC is 15 micro seconds.


|image12|

.. container:: centeralign

   Figure 12. Cursors placement to find TC


To see the difference between the initial signal and the digital filtered signal, take a snapshot and align it to the initial signal then enable Filter 1 with the parameters TC=15 and gain=0.07, as in Figure 13.



|image13|

.. container:: centeralign

   Figure 13. Initial signal(green) and filtered signal(orange)


Overshoot
~~~~~~~~~

The steps to find gain and TC in this case are similar to the previous case, the difference is sign of the gain as the initial value of the signal is higher than the value at which it settles.

:math:`\delta=2.49-2.74=-0.25 V`

:math:`\displaystyle gain=-0.\frac{25}{5}=-0.05`


|image14|

.. container:: centeralign

   Figure 14. Cursors placement to find delta


:math:`63.2% \times \delta=0.632 \times (-0.25)=-0.158`

In this example TC is 31 micro seconds.


|image15|

.. container:: centeralign

   Figure 15. Cursors placement to find TC


Take a shapshot of the initial filter and enable Filter 1 with the parameters TC=31 and gain=-0.05, as in Figure 16.



|image16|

.. container:: centeralign

   Figure 16. Initial signal(green) and filtered signal (orange)


.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/scopy_preferences.png
   :width: 900px
.. |image2| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/filter_settings.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/m2k_trimmers_highlighted.jpg
   :width: 800px
.. |image4| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/waweform_before_adjustment.png
   :width: 900px
.. |image5| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/waveform_after_adjustment.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/waveform_adjusted_lowgain.png
   :width: 900px
.. |image7| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/slight_overshoot.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/one_filter.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/two_filters.png
   :width: 900px
.. |image10| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/final_filtered_signal.png
   :width: 900px
.. |image11| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/delta_undershoot.png
   :width: 900px
.. |image12| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/tc_undershoot.png
   :width: 900px
.. |image13| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/filtered_undershoot.png
   :width: 900px
.. |image14| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/delta_overshoot.png
   :width: 900px
.. |image15| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/tc_overshoot.png
   :width: 900px
.. |image16| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/filtered_overshoot.png
   :width: 900px
