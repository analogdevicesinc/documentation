How to Optimize AD936x’s AGC Settings?
======================================

Pre-requisites
--------------

To build and run the demo:

-  Create a :doc:`standard ADI SD card </wiki-migration/resources/tools-software/linux-software/zynq_images>`
-  Build the BOOT.BIN for the design from MATLAB using the provided :git-MathWorks_tools:`hdlworkflow <targeting_models/tuneAGC-ad9361/hdlworkflow.m>` script
-  Copy the provided :git-MathWorks_tools:`targeting_models/tuneAGC-ad9361/reg/devicetree.dts` onto the BOOT partition of the SD card.
-  Now the ADRV9361-Z7035 can be booted from the built SD card.
-  Copy the ``reg`` folder to the SD-card and run the makefile. Next, run the object file generated.
-  Run the :git-MathWorks_tools:`unittests <targeting_models/tuneAGC-ad9361/tuneAGCad9361Tests.m>` or :git-MathWorks_tools:`targeting_models/tuneAGC-ad9361/run_testbench.m` example from MATLAB.

This article is a synopsis of the insights gained from an AGC optimization study we conducted for AD936x. First, the observations gathered by utilizing Simulink’s “RF Blockset Models for Analog Devices RF Transceivers” are summarized, followed by the conclusions drawn when this analysis was extended from a behavioral simulation-based study to one using a physical AD936x. The main purpose of this exercise is to demonstrate how to optimize the relevant parameters such that the feature-rich AGC on AD936x can be utilized better to achieve gain control of the waveforms. Importantly, this document is intended as a recipe such that the guidelines can be adapted accordingly when they are applied for any arbitrary waveform received using AD936x. Another useful point that this analysis highlights is the effectiveness of the Simulink models in gaining some preliminary insights into understanding a key feature of AD936x in a behavioral simulation setting, before validating them using the physical device itself.

In order to ensure that the AGC is not tuned during the data payload portion of a waveform which might affect the performance of equalization and demodulation phases, the recommended way is to let the AD936x’s AGC determine the optimal gain during the preamble phase in fast attack mode and subsequently, lock the AGC during the data payload phase to the optimal gain index determined previously. Consequently, this document will focus exclusively on fast attack mode since it is the preferred mode when the goal is to configure AD936x to respond quickly to rapid gain fluctuations. Similarly, we constrain the discussion to waveforms that contain a preamble followed by data payload, since our approach relies on determining the optimal gain without affecting the downstream receiver processing.

To this end, test waveforms using two standards, IEEE 802.11a and ADSB were used. The overall study we conducted considered performance metrics such as bit error rate (BER), packet error rate (PER), error vector magnitude (EVM) and AGC lock time (the time taken for the AGC state machine to go from State #1 to State #5). But, for the purpose of conciseness in illustrating the guidelines, the primary focus will be on minimizing AGC lock time, since the performance metrics chosen might be different depending on the application. The Simulink model displaying the use of AD9361 receiver that together with a test data source and a configurable AGC mode based on WLAN packet detection is shown in Figure 1. |image1| ``Figure 1: Simulink’s RF Blockset Model of AD9361 Rx, where the AGC is Enabled at the End of a WLAN Packet in the Proposed AGC Optimization Methodology``

Identifying the Relevant Settings using Simulink Models
-------------------------------------------------------

The evolution of the AGC in fast attack mode, which is detailed in Figure 2, operates over six main states to correctly manage signals with very dynamic characteristics. In fast attack mode, the AGC has numerous configurable parameters to control the transitions between these states, making it both flexible but complex to tune. However, using Figure 2 we can first group the parameters into five classes to simplify analysis. Of these, the first three classes correspond to events that trigger state transitions. The five classes are:

-  Peak overload settings
-  Peak underload settings
-  Energy lost settings
-  Power measurement settings in State #2
-  Miscellaneous timing settings

|image2| ``Figure 2: Fast Attack AGC High Level State Diagram``

1. Peak Overload Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

From Figure 2, we see that peak overloads lead to the following state transitions:

-  The self-transition of State #1 to itself
-  State #2 ---- → State #1
-  State #3 ---- → State #4

From Table 20 in :adi:`AD9361 Reference Manual, UG-570 <en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html>` which is shown in Figure 3 and the discussion related to it, we see that Large LMT Overload Threshold, Large ADC Overload threshold, Small ADC Overload threshold and Peak Overload Wait Time are a some of the settings that affect 1.1. These settings determine whether a strong signal is detected independent of all other AGC settings. Consequently, a subproblem within the overall optimization study is to set these four parameters optimally such that for a given waveform in a certain channel environment with a particular gain variation profile, as few cycles are spent as possible in reducing the gain for a strong signal. That is, while significantly strong signals certainly require gain adjustment via 1.1, the state machine should be configured such that in a large number of cases, gain changes are made primarily in State #2. |image3| ``Figure 3: Table 20 from AD9361 Reference Manual, UG-570``

Furthermore, it must be noted that in our study, the goal was to determine the optimal gain via fast attack within 8 µs, which happens to be the preamble duration for both IEEE 802.11a and ADSB. The sample rate chosen was 40 MSPS and 12.5 MSPS respectively. The sample rate of 12.5 MSPS was selected such that the AGC tuning methodology can be understood in reference to the existing Simulink models available on the Analog Devices Github repository [2]. Within the 8 µs window, around 4-5 µs are required to perform preamble detection. So, in practical terms, we have only around 3 µs to drive the state machine to lock, if the AGC is enabled using a packet detector. Consequently, Peak Overload Wait Time which is clocked at ClkRF rate (the clock used at the input to the Rx FIR filter) is within an order-of-magnitude of the targeted AGC lock time. Therefore, in such scenarios, optimally setting these thresholds is extremely important since a misconfiguration will force the state machine to endlessly remain in State #1, constantly trying to reduce the gain and never finding the optimal gain within the targeted lock time. To further improve the probability of meeting this targeted lock time, we used the end of a packet to enable the AGC such that the AGC is able to monitor the subsequent packet from the beginning of its preamble.

In our Simulink-based optimization study, test data was passed through the AD936x receiver model for different combinations of the four previously mentioned settings, which were generated using a nested for-loop. As an example, considering 4 values of Large LMT Overload Threshold, 5 values of Large ADC Overload threshold, 7 values of Small ADC Overload threshold and 7 values of Peak Overload Wait Time, one might collect AGC lock time statistics for 980 combinations to determine the optimal combination (or combinations) that achieves target lock time.

|image4| ``Figure 4: An Illustrative Example Showing Combinations of the Tuning Settings Tested to Handle Peak Overload Events``

Additionally, ADC Overrange Sample Size, which controls the number of samples to use in the sum-of-squares calculation of ADC thresholds, is dependent on the ADC overload threshold values and is not an independently tunable setting. It must also be noted that, the step size values used to reduce gain are also important since they influence how quickly gain is reduced in the event of a peak overload. However, since the goal is to drive the state machine out of State #1 and into the subsequent states as quickly as possible in order to determine the optimal gain and meet the target AGC lock time, it is recommended that they are tuned over the higher end of the allowable range. Moreover, relative to 1.1, 1.2 and 1.3 can be considered as additional checks that handle strong signals after the AGC has exited State #1. The conditions that lead to these transitions are the same as 1.1.

We can summarize the settings used to handle peak overload events as follows:

-  Large LMT Overload threshold – Tuned
-  Large ADC Overload threshold – Tuned
-  Small ADC Overload threshold – Tuned
-  ADC Overrange Sample Size – Tuned, but not an independent degree-of-freedom
-  Peak Overload Wait Time – Tuned
-  Step Size Decrement to handle Case #2, Table 20 from [1] – Tuned, over the higher end of the allowable range
-  Step Size Decrement to handle Case #3, Table 20 from [1] – Tuned, over the higher end of the allowable range
-  Final Overrange Count – Tuned

2. Peak Underload Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

From Figure 2, we see that peak underloads or low power events lead to the following state transitions:

-  State #2 ←--- → State #2a
-  State #3 ---- → State #2a

Both these transitions depend on Enable Incr Gain bit, Low Power Threshold, Dec Power Measurement Duration, Increment Gain Step LPF/LMT and Increment Time. Of these settings, the smallest value that Dec Power Measurement Duration can assume is 16 (see eq. (17) from [1]) with a step-size of 16. For reasons that are elaborated in a following subsection, we observed that it is preferable to set Dec Power Measurement Duration to a small value. However, due to the fact that Increment Gain Step LPF/LMT is a 3-bit unsigned number [3], we observed that a maximum gain increment of 7 indices can be insufficient to drive the state machine out of State #2a within a short amount of time.

For example, suppose that Dec Power Measurement Duration is set to 32 and for particularly low power IEEE 802.11a packets, 2 or 3 gain increments by 7 indices are required to drive the state machine out of State #2a. Since ClkRF = 1/40e6 = 0.025 µs, each increment by 7 indices requires 16 ClkRF = 0.4 µs and therefore, a total of 0.8 or 1.2 µs in total. As we mentioned previously, since the total time available to achieve gain lock is 8 µs, of which AGC Attack Delay consumes 1 µs (mode details in a following subsection), this state transition consumes a significant amount of time leaving little room to perform gain adjustment in State #2 and eventually reach State #5. Consequently, in our studies, we set Enable Incr Gain bit to 0, thereby eliminating transitions 2.1 and 2.2 altogether. Any gain change that needs to be made for a low power signal can be made in State #2 relative to the AGC Lock Level, as discussed next. Additionally, although Dec Power Measurement Duration is not used in the context of handling low power events, it is tuned when measuring power in State #2, as discussed in a following subsection. We can summarize the settings used to handle low power events as follows:

-  Enable Incr Gain bit - 0
-  Low Power Threshold – Not used
-  Dec Power Measurement Duration – Not used
-  Increment Gain Step LPF/LMT – Not used
-  Increment Time – Not used

3. Energy Lost Settings
~~~~~~~~~~~~~~~~~~~~~~~

As shown in Figure 2, we see that the state machine exits the lock state either when overloads are detected or when energy is lost. Here, we focus on the latter case since the conditions and settings that result in gain unlocking due to peak overloads is similar to that of State #1. The settings that come into play in this scenario are Stronger Signal Threshold, Gain Lock Exit Count and Power Meas in State #5. When the AGC is allowed to unlock at the end of the burst, rather than using an external trigger to change the mode from fast attack to manual, we set Stronger Signal Threshold to a fixed value. This value was subjectively determined as half the difference between the AGC Lock Level (the target power level to achieve using optimal gain control) and the noise power level. In our studies, this rule proved to be a good metric to differentiate between valid signal power versus noise power for triggering a state transition.

On the other hand, Gain Lock Exit Count is dependent on the packet structure inherent to the wireless standard used. As an example, for WLAN signals, setting Gain Lock Exit Count to a value larger than the expected interframe space will fail to trigger a gain unlock and a move to State #1. In summary, the settings used to handle energy lost events are set as follows:

-  Stronger Signal Threshold – Fixed
-  Gain Lock Exit Count – Application dependent
-  Power Meas in State #5 – Tuned

4. Power Measurement Settings in State #2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From [1], we see that the AGC then adjusts the gain to match the average signal power to the AGC Lock Level setting. However, there is a maximum amount that it can increase, set by AGCLL Max Increase. As we mentioned previously, we recommend that low-power conditions be handled vis State #2 rather than via state transitions 2.1 and 2.2. Consequently, AGCLL Max Increase must be set as high as possible in order to be able to boost the gain level of low power signals.

Additionally, in State #2, AGC matches the average signal power to the AGC Lock Level set by the user. It is closely tied to the peak-to-average power (PAPR) level of the received waveform. Typically, most commonly used waveforms regardless of the application have a PAPR in the range 1-15 dB. However, when one collects statistics of the complementary cumulative distribution function, Pr[Peak Power (dB)>Average Power(dB)] as a function of Peak Power (dB), the probability of an above average peak value is revealed. Therefore, the AGC Lock Level needs to be set such that the appearance of an above average peak has as little effect as tolerable by the application under consideration. As an example, if the AGC Lock Level is set to -11 dB and the PAPR of the received waveform is 14 dB with a probability of 1e-3, a compression of 3 dB is to be expected every 1000 samples. However, if the AGC Lock Level is set too low, the bitgrowth experienced by the signal in the decimator chain and as a consequence, its SNR might suffer due to insufficient dynamic range of the signal at the output of the ADC. Therefore, it is recommended that the effects of this trade-off are considered by testing a few values of AGC Lock Level on either side of the average signal power level.

We can summarize the power measurement settings in State #2 as follows:

-  AGCLL Max Increase – Tuned, over the higher end of the allowable range
-  Dec Power Measurement Duration – Tuned, over the lower end of the allowable range
-  AGC Lock Level – Tuned, application dependent

5. Miscellaneous Timing Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From [1], we see that when AD936x enters the Rx state, the AGC first waits for a time in µs set by the AGC Attack Delay. This delay allows the receive path to settle before the AGC begins determining the optimum gain index. When the targeted AGC lock time is in µs, as in our study, it is reasonable to set the AGC Attack Delay as low as possible.

Similarly, the AGC enters State #2 only after no peak overloads are detected for a time period given by Energy Detect Count. Since this counter is clocked at ClkRF rate, this setting is a function of the sample rate used, the PAPR probability of the signal and the LMT/ADC overload thresholds. Assuming that the LMT/ADC thresholds are set such that State #1 only handles the extremely large peak overloads while delegating most of the gain changes to State #2, Energy Detect Count can be set tuned over the lower end of the allowable range.

On the other hand, upon entering State #2, the AGC waits for a time equal to Settling Delay minus Energy Detect Count. By appropriately configuring Energy Detect Count to represent the time window within which peak overloads are typically expected, no additional time needs to be spent in entering State #2. So, it is recommended that Settling Delay be set to Energy Detect Count. In summary, the miscellaneous timing settings can be set as follows:

-  AGC Attack Delay – Tuned, over the lower end of the allowable range.
-  Energy Detect Count – Tuned
-  Settling Delay – Fixed, set equal to Energy Detect Count

Results and Summary
-------------------

In this section, we summarize our analysis using Monte-Carlo simulation results. In the case of WLAN, the test data contained around 1500 packets each experiencing a random gain value. For ADSB, our test data contained a random (uniformly selected between 10 and 15 per second) number of Mode-S messages in a data record of length 1s. The test data also contained numerous legacy and spurious signals that are modulated using PPM. |image5| ``Figure 5: Histogram of AGC Lock Time for WLAN Test Signals`` |image6| ``Figure 6: Histogram of AGC Lock Time for ADSB Test Signals.``

The difference in the observed AGC lock time upon optimizing the AGC settings as opposed to using unoptimized AGC settings can be observed from Figure 5 and Figure 6. It must be noted that unlike WLAN, wherein the packetized structure of the transmission was exploited, in the case of ADSB, the Mode-S messages are interspersed with legacy or spurious signals. Consequently, in the latter case, we relied on a preamble correlator. This is the reason why we observe that the minimum lock time is greater than 6 µs, which is the time window used for in the correlator. Additionally, we conducted tests using a free-running AGC wherein, the state-machine is free to adjust the gain depending on the various overloads and low-power conditions that the signal encounters, with no external control. However, for these tests, lock time is not an appropriate metric since the AGC performs gain adjustments regardless of whether the preamble or the data payload portion of the signal is being processed. |image7| ``Figure 7: Bar-Graph of PER for WLAN Test Signals`` |image8| ``Figure 8: Bar-Graph of EVM for WLAN Test Signals``

Similarly, the importance of optimized AGC settings and constraining the AGC to determine the optimal gain only during the preamble can be further reinforced by observing the PER for WLAN. We notice that despite using optimized settings, if the AGC is run in fast attack mode, the PER performance is as bad as using unoptimized settings. Finally, we look at the EVM performance for WLAN in Figure 8. Since Mode-S messages only contain a Manchester encoding type modulation, to compute EVM in this case, we computed the difference between the sum of the sample points before and after the symbol transition. This is compared with a reference constellation of Manchester-encoded symbols to determine EVM. The results are shown in the table below. Therefore, we recommend that it is important to lock the optimal gain determined during preamble and use it for the remainder of the packet.

``Table 1: Mode-S EVM Performance``

====================== ====================== =======
Optimized AGC Settings Free-running FAGC Mode EVM (%)
====================== ====================== =======
Yes                    Yes                    10.1
No                     No                     8.2
Yes                    No                     3.2
====================== ====================== =======

In summary, the overall theme in optimizing the AGC settings to determine the optimal gain is to ensure that the settings that handle peak overloads and peak underloads delegate gain adjustment to State #2 as quickly as possible. This is because, the state transitions that are triggered by these events might require multiple clock cycles clocked at the sample rate used. As this quantity might be of the same or within an order-of-magnitude of the targeted AGC lock time, it is imperative that the AGC is driven from State #1 to State #5 using the most direct path possible most of the time.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig2.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig3.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig4.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig6.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig7.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig8.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/agc_fig9.png
   :width: 600px
