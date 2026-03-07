Receiver Signal Chain Overview and Theory of Operation
======================================================

Link to higher level page: :doc:`Satcom Reference Design </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`

The overall RX block diagram is shown below. The wiki sections below will walk through the design elements of each sub-circuit.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_v2.jpg
   :align: center
   :width: 600px

RX Beamforming Network
----------------------

The 4T4R beamforming network consists of a modular array of four BFIC tiles, allowing for sixteen elements. The multi-beam analog beamforming begins with an :adi:`ADL8142` LNA. The signal then passes through a Ka-band bandpass filter (27.5-30GHz), followed by the :adi:`ADAR3001S` BFIC. After the :adi:`ADAR3001S`, each of the four components of every channel are combined using an :adi:`ADAR5000` Wilkinson combiner.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_beamforming_network_v2.jpg
   :align: center
   :width: 600px

--------------

Down-converter Design and Operation
-----------------------------------

By utilizing high performance silicon switches such as the :adi:`ADRF5024` and :adi:`ADRF5144`, the down-converter design allows for three separate signal paths. High frequency X, Ku and Ka-band signals are applied to the LNA input of the :adi:`ADMFM2000`. After LNA amplification and optional off-chip filtering, the input signal is applied to the :adi:`ADMFM2000`'s internal mixer where it is down converted to an IF by mixing with an external LO. For more information about LO generation for this particular design, `see this link <https://wiki.analog.com/resources/eval/developer-kits/space-based-satcom-ref-design/lo-overview>`_. Midrange C-band signals bypass the internal LNA and mixer but still use the :adi:`ADMFM2000`'s internal filtering and VGA. S-band and lower signals bypass the :adi:`ADMFM2000` SIP and are sampled by the :adi:`AD9082` ADC after further IF conditioning.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_downconversion_v2.jpg
   :align: center
   :width: 600px

Frequency Plan
~~~~~~~~~~~~~~

The following table shows the frequency conversion paths for this design.


|image1|

The image below shows a graphical representation of the frequency plan. The x-axis represents the operational frequency of the reference design while the y-axis represents the different frequency bands ranging from L to Ka. Markers are shown for RF frequency, IF frequency, sampling frequency (Fs), image frequency, and alias frequency.

The horizontal lines represent the bandwidth of RF, IF, and aliasing frequency for each frequency band. The solid vertical lines show Fs and Fs/2, which are used to determine at what frequencies aliasing will occur. For frequencies higher than the 8GHz usable analog bandwidth of the :adi:`AD9082`, down conversion from an RF to IF is required. For the lower frequencies (C-band and below), an IF is not required so only the RF is plotted.

Shown below, the sampling frequency is lowered to 5GHz from 6GHz to avoid the signal folding onto itself over the boundary separating the second and third Nyquist zone.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_freq_plan_chart.jpg
   :align: center
   :width: 1000px

Spurious performance
~~~~~~~~~~~~~~~~~~~~

--------------

IF Section
----------

The IF section is the final segment before the :adi:`AD9082` ADC. Similar to the :doc:`down-converter section </wiki-migration/resources/eval/developer-kits/satcom-ref-design/rx-overview>`, there are three pathways for signal conditioning ahead of the ADC. An :adi:`HMC8413` wideband GaAs LNA provides moderate gain before the signal is filtered. The high frequencies such as Ka, Ku, X-band are conditioned in switch path 1 of an :adi:`ADRF5040` silicon switch. Signals from S-band and lower are conditioned in switch path 2 while signals from C-band are filtered in switch path 3.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/sactom_rx_if_section_v2.jpg
   :align: center
   :width: 600px

--------------

Analog to Digital Converter (ADC) + DSP
---------------------------------------

The :adi:`AD9082` (“MxFE”) is an ideal digitizer for this wideband RF front end due to its high level of integration, performance, and RF sampling rate. The MxFE’s high instantaneous and analog input bandwidth enable RF sampling up to 8GHz, providing architectural and frequency planning flexibility at the system level. It also has highly configurable, on-chip DSP capabilities (DDC/DUC channelizers, NCOs, and programmable FIR filters) as well as four DAC channels and two ADCs for use in this multi-channel system.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_adc_dsp_fpga.jpg
   :align: center
   :width: 600px

The :adi:`ADF4371` integrated PLL/VCO is an ideal choice for generating the MxFE sample clock. The :adi:`ADF4371` can generate a clean, low-jitter clock from 62.5MHz up to 32GHz, and its differential outputs are capable of directly driving the MxFE clock pins. The :adi:`ADF4371` is also used to generate clocking for the LO signal. You can read more about the LO signal path :doc:`here </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`.

The :adi:`LTC6953` clock distributor is used to ensure proper clock synchronization between all of the :adi:`ADF4371` devices in the reference design. An external source generates a clock signal, which is then buffered and replicated before being sent to the FPGA, the :adi:`AD9082`, and both the :doc:`TX and RX LO signal paths </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`.

.. tip::

   Although only a single :adi:`LTC6953` is required for 4T4R, With EZSync™ or ParallelSync™, multichip synchronization is realizable, allowing for expandability while maintaining the proper clock signals.


The `ADI Frequency Planning Utility tool <http://www.analog.com/en/design-center/interactive-design-tools/frequency-folding-tool.html>`_ was used to determine the optimal :adi:`AD9082` ADC sample rate, IF sampling frequency, and IF bandwidth. A 6GSPS ADC rate allows for maximum instantaneous bandwidth (IBW) and complete avoidance of HD2 aliasing in-band for a 1GHz signal bandwidth centered at 4.5GHz (2nd Nyquist). The figure below illustrates this.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/freqfoldinggraphic.png
   :align: center
   :width: 800px

.. important::

   The receiver and transmitter front ends described in this reference design use a frequency plan designed using the :adi:`AD9082`, specifically with 6GSPS and 12GSPS ADC and DAC sample rates, respectively. However, for the case of C-band operation, both the ADC and DAC sample rates are lowered to avoid the signal overlapping the edge of the 2nd and 3rd Nyquist boundary. The RF components themselves are wideband enough to allow for flexibility in the frequency plan and filtering.


--------------

Timing and Control
------------------

Automatic gain control (AGC), RF path switching, and beam switching/reconfiguration often have critical timing specs that drive component selection, especially in systems that require fast frequency hopping or wideband tuning. The RF switches, DSAs, and tunable beam states in the receiver signal chain offer fast switching and settling times, a high degree of configurability, and can be controlled via standard parallel and/or SPI interfaces. The tables below list the control interfaces and minimum configuration and settling time details at the component level for each of the sections of this reference design.

.. _rx-beamforming-network-1:

RX Beamforming Network
~~~~~~~~~~~~~~~~~~~~~~

Inside of the :adi:`ADAR3001S`, there are 16 digital step attenuators and 16 time delay units (TDU) combined into Variable Amplitude and Phase (VAP) blocks. Each digital step attenuator provides up to 31.5dB of attenuation with a resolution of 0.5dB. Each TDU can provide up to 35.3 ps of delay in steps of 0.56 ps. Each of the VAPs can tuned in a minimum of 10ns.

The :adi:`ADAR3001S` contains internal RAM which can store up to 64 states for each beam for a total of 256 beam states. For faster access, there is also optional FIFO memory, which stores up to 16 beam states per channel for a total of 64 beam states. The :adi:`ADAR3001S` is conveniently controlled by 4-wire SPI, allowing for control of up to 16 devices on the same serial line.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_bf_control_requirements_v2.jpg
   :align: center

Down-conversion and IF Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The downconversion and IF section starts with an :adi:`ADRF5730` 6-bit digital step attenuator capable of up to 31.5dB of attenuation in 0.5dB steps. These DSAs can be controlled either by parallel logic level voltages determined by truth tables or by 3-wire SPI. The internal DSAs of the :adi:`ADMFM2000` work by parallel voltage control inputs. All of the RF switches, including the internal switches of the :adi:`ADMFM2000`, are controlled by parallel digital voltage supplies. In order to achieve full functionality of the switches, they must be kept at either a digital "high" or "low" state, determined by their respective datasheets.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_no_bf_control_requirements_v2.jpg
   :align: center

--------------

RX Performance Simulations and Measurements
-------------------------------------------

Wideband Signal Conditioning Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the RX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the :adi:`ADMFM2000` microwave downconverter containing signal chains each with their own frequency-dependent s-parameter or sys-parameter datasets
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_only_no_bf_genesys_v2.jpg
   :align: center

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The noise power spectral simulation shown below uses 76 individual carrier tones with a total combined input power of -11 dBm spanning from 30GHz to 31GHz for a total bandwidth of 1000MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -150dBm are ignored. After passing through the necessary system path, the IF frequency, shown on the second plot, becomes 4500MHz which can be directly sampled by the :adi:`AD9082`.

|image2| |image3|

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The two tone spectral simulation shown below uses 2 individual carrier tones with a total combined input power of -11 dBm centered around 30.5GHz to 31GHz and a delta of 50MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -150dBm are ignored.

|image4| |image5|

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node 10" which comes directly after the digital equalizer.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/system_level_cascade_no_bf_v2.jpg
   :align: center
   :width: 600px

Beamforming Front End Only
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the RX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_bf_only_genesys_v2.jpg
   :align: center
   :width: 650px

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

.. important::

   Simulations below use the :adi:`ADAR3001` definition for channel gain. Channel gain is the power ratio between a single RF output and single RF input, with all other inputs terminated with 50Ω, DSA code = 0, and TDU code = 0. In a real scenario, coherent gain would be used and is the power ratio between a single RF output and single RF input, with the other three inputs driven. All inputs would have similar amplitude and would be phased such that they combine coherently. For :adi:`ADAR3001` coherent gain (dB) = channel gain (dB) + 12 (dB). For :adi:`ADAR5000` coherent gain (dB) = channel gain (dB) + 6 (dB).


.. _noise-power-spectral-simulation-1:

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The noise power spectral simulation shown below uses 76 individual carrier tones with a total combined input power of -40 dBm spanning from 30GHz to 31GHz for a total bandwidth of 1000MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -200dBm are ignored. After passing through the analog beamforming front end, the signal is ready for further conditioning by the wideband receiver section.

|image6| |image7|

.. _two-tone-test-spectral-simulation-1:

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The two tone spectral simulation shown below uses 2 individual carrier tones each with an input power of -40 dBm centered around 30.5GHz to 31GHz and a delta of 50MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -200dBm are ignored.

|image8| |image9|

.. _system-cascade-1:

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node 10" which comes directly after the digital equalizer.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_system_level_cascade_bf_only.jpg
   :align: center
   :width: 600px

Wideband Signal Conditioning and Beamforming Combined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the RX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the :adi:`ADMFM2000` microwave downconverter containing signal chains each with their own frequency-dependent s-parameter or sys-parameter datasets
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_combined_genesys_v2.jpg
   :align: center

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

.. important::

   Simulations below use the :adi:`ADAR3001` definition for channel gain. Channel gain is the power ratio between a single RF output and single RF input, with all other inputs terminated with 50Ω, DSA code = 0, and TDU code = 0. In a real scenario, coherent gain would be used and is the power ratio between a single RF output and single RF input, with the other three inputs driven. All inputs would have similar amplitude and would be phased such that they combine coherently. For :adi:`ADAR3001` coherent gain (dB) = channel gain (dB) + 12 (dB). For :adi:`ADAR5000` coherent gain (dB) = channel gain (dB) + 6 (dB).


.. _noise-power-spectral-simulation-2:

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The noise power spectral simulation shown below uses 76 individual carrier tones with a total combined input power of -40 dBm spanning from 30GHz to 31GHz for a total bandwidth of 1000MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -200dBm are ignored. After passing through the necessary system path, the IF frequency, shown on the second plot, becomes 4500MHz which can be directly sampled by the :adi:`AD9082`.

|image10| |image11|

.. _two-tone-test-spectral-simulation-2:

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The two tone spectral simulation shown below uses 2 individual carrier tones with a total combined input power of -11 dBm centered around 30.5GHz to 31GHz and a delta of 50MHz. Harmonics calculated up to the third order and thermal noise are included. Tones below -150dBm are ignored.

|image12| |image13|

.. _system-cascade-2:

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third input third order intercept (EIIP3), input 1dB compression point (EIP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node 10" which comes directly after the digital equalizer.


|image14|

:doc:`Home </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`

--------------

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_freq_plan.jpg
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/input_signal_no_bf_v2.jpg
   :width: 425px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/output_signal_no_bf_v2.jpg
   :width: 425px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/two_tone_test_input_no_bf_v2.jpg
   :width: 425px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/two_tone_test_output_no_bf_v2.jpg
   :width: 425px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_input_signal_bf_only_v1.jpg
   :width: 425px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_output_signal_bf_only_v1.jpg
   :width: 425px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_two_tone_test_input_bf_only_v1.jpg
   :width: 425px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_two_tone_test_output_bf_only_v1.jpg
   :width: 425px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_input_signal_combined_v1.jpg
   :width: 425px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_output_signal_combined_v1.jpg
   :width: 425px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_two_tone_test_input_combined_v1.jpg
   :width: 425px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_two_tone_test_output_combined_v1.jpg
   :width: 425px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_rx_system_level_cascade_combined_v1.jpg
   :width: 600px
