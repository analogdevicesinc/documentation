Transmitter Signal Chain Overview and Theory of Operation
=========================================================

Link to higher level page: :doc:`Satcom Reference Design </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`

The overall TX block diagram is shown below. The wiki sections below will walk through the design elements of each sub-circuit.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_overall_chain_v3.jpg
   :align: center
   :width: 600px

Digital to Analog Converter (DAC) + DSP
---------------------------------------

The :adi:`AD9082` (“MxFE”) is an ideal digitizer for this wideband RF front end due to its high level of integration, performance, and RF sampling rate. The MxFE’s high instantaneous and analog input bandwidth enable RF sampling up to 8GHz, providing architectural and frequency planning flexibility at the system level. It also has highly configurable, on-chip DSP capabilities (DDC/DUC channelizers, NCOs, and programmable FIR filters) as well as four DAC channels and two ADCs for use in this multi-channel system.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_dac.jpg
   :align: center
   :width: 600px

The :adi:`ADF4371` integrated PLL/VCO is an ideal choice for generating the MxFE sample clock. The ADF4371 can generate a clean, low-jitter clock from 62.5MHz up to 32GHz, and its differential outputs are capable of directly driving the MxFE clock pins. The ADF4371 is also used to generate clocking for the LO signal. You can read more about the LO signal path :doc:`here </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`.

The :adi:`LTC6953` clock distributor is used to ensure proper clock synchronization between all of the :adi:`ADF4371`'s throughout this reference design. An external source generates a clock signal, which is then buffered and replicated before being sent to the FPGA, the :adi:`AD9082`, and both the :doc:`TX and RX LO signal paths </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`.

.. tip::

   Although only a single :adi:`LTC6953` is required for 4T4R, With EZSync™ or ParallelSync™, multichip synchronization is realizable, allowing for expandability while maintaining the proper clock signals.


--------------

Up-converter Design
-------------------

By utilizing a high performance :adi:`ADRF5022` silicon switch, the down-converter design allows for two separate signal paths to achieve wideband capability. The high frequency X, Ku and Ka-band signals pas through the :adi:`ADRF5022`'s switch state "2" and are applied to the IF input of the ADMFM2001. Before mixing with an external LO, the signals pass through a cascaded chain inside the SIP involving a lowpass filter, power amplifier, a second lowpass filter, and attenuator. The signals are then applied to the ADMFM2001's internal mixer where they are up converted to an RF by mixing with an external LO. For more information about LO generation for this particular design, :doc:`see this link </wiki-migration/resources/eval/developer-kits/satcom-ref-design/lo-overview>`. The high frequency RF signals are then amplified by :adi:`HMC7950` before further signal conditioning. C, S, L, and UHF band signals bypass the :adi:`ADMFM2001` SIP and are sent to the beamforming section after further RF conditioning.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_up_conversion_section_v3.jpg
   :align: center

--------------

TX Beamforming Network and PA
-----------------------------

The 4T4R beamforming network consists of a modular array of four BFIC tiles, allowing for sixteen elements. The transmit path for multi-beam analog beamforming begins with a Knowles BPF followed by an :adi:`ADAR5000`. The BFP removed unwanted spurs just outside our desired band. The :adi:`ADAR5000` Wilkinson splitter divides each of the four channels into four equal phase constituents, for a total of 16 subchannels for each of the four BFIC tiles. The signals enter the :adi:`ADAR3000S` where their individual amplitude and phase can be manipulated via the variable amplitude and phase blocks (VAPS). After the :adi:`ADAR3000S`, more filtering and amplification is performed before the signal is transmitted via the antenna.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_bf_section_v2.jpg
   :align: center

--------------

Timing and Control
------------------

Automatic gain control (AGC), RF path switching, and beam switching/reconfiguration often have critical timing specs that drive component selection, especially in systems that require fast frequency hopping or wideband tuning. The RF switches, DSAs, and tunable beam states in the transmitter signal chain offer fast switching and settling times, a high degree of configurability, and can be controlled via standard parallel and/or SPI interfaces. The tables below list the control interfaces and minimum configuration and settling time details at the component level for each of the sections of this reference design.

TX Beamforming Network
~~~~~~~~~~~~~~~~~~~~~~

Inside of the :adi:`ADAR3000S`, there are 16 digital step attenuators and 16 time delay units (TDU) combined into Variable Amplitude and Phase (VAP) blocks. Each digital step attenuator provides up to 31.5dB of attenuation with a resolution of 0.5dB. Each TDU can provide up to 54.5 ps of delay in steps of 0.865 ps. Each of the VAPs can tuned in a minimum of 10ns.

The :adi:`ADAR3000S` contains internal RAM which can store up to 64 states for each beam for a total of 256 beam states. For faster access, there is also optional FIFO memory, which stores up to 16 beam states per channel for a total of 64 beam states. The :adi:`ADAR3000S` is conveniently controlled by 4-wire SPI, allowing for control of up to 16 devices on the same serial line.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/tx_satcom_bf_control_requirements_v2.jpg
   :align: center

--------------

TX Performance Simulations and Measurements
-------------------------------------------

Wideband Signal Conditioning Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the TX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the :adi:`ADMFM2001` microwave downconverter containing signal chains each with their own frequency-dependent s-parameter or sys-parameter datasets
-  A standalone model of an :adi:`AD9082` DAC containing frequency-dependent sys-parameter datasets
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_genesys_simulation_v3.jpg
   :align: center

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node 8" which is the end of the signal chain, before the beamforming section.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_system_level_cascade_no_bf_v2.jpg
   :align: center

Beamforming Front End Only
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the TX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the :adi:`ADMFM2001` microwave downconverter containing signal chains each with their own frequency-dependent s-parameter or sys-parameter datasets
-  A standalone model of an :adi:`AD9082` DAC containing frequency-dependent sys-parameter datasets
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_genesys_schematic_bf_only_v1.jpg
   :align: center

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

.. _noise-power-spectral-simulation-1:

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _two-tone-test-spectral-simulation-1:

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _system-cascade-1:

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node xx" which is the end of the signal chain, before the beamforming section.

Wideband Signal Conditioning and Beamforming Combined
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simulations were created using Keysight SystemVue/Genesys. All components in the TX signal chain were modeled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The signal chain below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the :adi:`ADMFM2001` microwave downconverter containing signal chains each with their own frequency-dependent s-parameter or sys-parameter datasets
-  A standalone model of an :adi:`AD9082` DAC containing frequency-dependent sys-parameter datasets
-  Frequency-dependent component interconnect modeling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 30mil Rogers 4350 PCB stackup

::

   * 

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_genesys_schematic_combined_v1.jpg
   :align: center

The Genesys workspace incorporates various system level cascade analyses that takes advantage of MATLAB equation-based frequency planning. Three different analyses are shown below:

-  Noise power Spectral Simulation
-  Two-Tone Test Spectral Simulation
-  System Cascade highlighting gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR)

.. _noise-power-spectral-simulation-2:

Noise Power Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|image1| |image2|

.. _two-tone-test-spectral-simulation-2:

Two-Tone Test Spectral Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _system-cascade-2:

System Cascade
^^^^^^^^^^^^^^

As mentioned above, the system cascade simulation measures gain (CGAIN), noise figure (CNF), third order output intercept (EOIP3), output 1dB compression point (EOP1DB), minimum detectable signal (MDS), and carrier to noise distortion ratio (CNDR). The x-axis shows all of the individual components cascaded together and the nodes in between. The variables are shown on two separate y axes for scaling purposes. The markers are placed on "Node 2" which is the end of the signal chain, before the signal is sent to antenna.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_system_level_cascade_combined_v1.jpg
   :align: center

:doc:`Home </wiki-migration/resources/eval/developer-kits/satcom-ref-design>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_input_signal_combined_v1.jpg
   :width: 425px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/space-based-satcom-ref-design/satcom_tx_output_signal_combined_v1.jpg
   :width: 425px
