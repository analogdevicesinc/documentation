:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

Receiver Front End Overview & Theory Of Operation
=================================================

The 2-24GHz Receiver block diagram is shown below. The following wiki sections will go into more detail on the theory of operation of the individual, functional blocks of the signal chain.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rxblockdiagram.png
   :align: center
   :width: 1000px

| 

Rx Input Stage & Modes Of Operation
-----------------------------------

The first stage of the Rx chain is the multi-mode input network (shown below), which can be configured for three different modes for quick performance optimization in a dynamic environment. The desired signal path is selectable via two :adi:`ADRF5020` RF switches, which are capable of sub-100ns switching time and are controllable with GPIOs from the FPGA/ASIC.


|image1|

.. important::

   The maximum survivable input level of the receiver front end is +20dBm. An RF limiter or other protection circuitry may be required depending on the survivability specifications.


The first mode enables an :adi:`ADL9005` wideband LNA closest to the antenna, which provides the best possible NF across frequency and should be used as the default mode of operation. The second mode switches over to the :adi:`ADMV8818` tunable filter configured to its full bypass state, effectively acting as an LNA bypass path. Transitioning from the LNA path to the filter path (in bypass mode) enables quick, front end gain reduction to react to high-power blockers potentially desensitizing the receiver. Finally, the third mode enables the :adi:`ADMV8818` as a tunable pre-selector BPF, which is used here as an alternative to switched filter banks. This sub-octave, pre-selector filter path is used to address 2nd order intermod (IMD2) spurs that can show up when two out-of-band blocker spurs add or subtract to create a spur that falls in band, potentially masking the desired signal. Pre-selector filtering needs to be near the beginning of the signal chain adequately mitigate these interfering signals before they can hit a non-linear component such as an amplifier or mixer. Additionally, the :adi:`ADMV8818` has independently configurable high and low pass filter bands to facilitate variable passband bandwidth- a frequent requirement of preselector filtering in wideband, tunable receiver signal chains. For example, the first band in a 2 to 24 GHz signal chain may only cover 2 to 3 GHz and would need good rejection at 1.5 GHz on the low side (F_high/2) and at 4 GHz on the high side (F_low*2). Whereas a higher band in the signal chain may cover 12 to 18 GHz, with good rejection required at 9 GHz on the low side and at 24 GHz on the high side. These differences mean many more filters are needed to cover lower frequencies bands than high frequency bands. A frequency spectrum example of the pre-selector filtering is shown in the following figure.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/preselectorfiltergraphic.png
   :align: center
   :width: 800px

Following the switchable input network are an :adi:`ADRF5740` digital step attenuator (DSA), LNA, and additional :adi:`ADMV8818` tunable BPF. The :adi:`ADRF5740` is one of two DSAs in the signal chain (with the other in the IF section), both of which serve multiple roles including gain levelling/control and NF/linearity optimization. This second :adi:`ADMV8818` in the signal chain primarily acts as an image & IF rejection filter but can also provide some level of IMD2 mitigation if the LNA input path is used instead of the preselector filter path.

The image is a frequency band that, when present at the mixer input, will generate signals equal in amplitude to the desired signals at the mixer output. IF signal rejection is required to knock down spectrum at IF frequencies before the mixer to avoid them from leaking directly across the mixer and showing up as un-wanted spurs. A frequency spectrum example of the unwanted image and IF bands is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/imgfilteringgraphic.png
   :align: center
   :width: 800px

   | 

Downconversion Stage & Frequency Plan
-------------------------------------

After the input network, the signal chain splits into two frequency conversion paths, each designed to translate a different frequency band of the RF input spectrum to an appropriate sampling IF. This architecture and frequency plan enables continuous frequency coverage across the entire 2-24GHz range by avoiding “dead zones” in coverage around the ADC Nyquist boundaries.

RF input frequencies above 6.5GHz (some coverage overlap with low-freq path) feed into an :adi:`HMC8191` wideband I/Q mixer with a tunable LO source, downconverting the entire band to a final IF of 4-5GHz. Input frequencies below 7GHz feed into a more traditional, dual-stage heterodyne signal path- first running through an :adi:`HMC773A` upconverter to a high IF of 11-16GHz, then through the shared-path :adi:`HMC8191` downconverter to a 4-5GHz IF. The lower-frequency path contains an additional amplifier to account for some of the extra conversion loss resulting from the two mixing stages, as well as 11-16GHz IF band-pass filtering to reject both the LO and the RF from leaking across the :adi:`HMC773A` mixer and into the downconverter. The figure below shows the frequency conversion section of the signal chain and the frequency operation ranges for each individual path.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rxfreqconversionsection.png
   :align: center
   :width: 900px

The figure below provides an additional frequency plan visualization showing the individual frequency conversion steps for each frequency band.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rxfreqplan.png
   :align: center
   :width: 600px

The following table summarizes the possible frequency conversion paths:

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rxfrequencyplan.png
   :align: center
   :width: 900px

|

| ===== Spurious Analysis ===== Keysight SystemVue/Genesys was used to simulate different spurious signal rejection tests, namely IF rejection and image rejection tests. The test setup was similar for both tests - Our desired signal was injected at the input to the reciever chain, along with the undesired IF and image components for their respective tests. There are two paths a signal can take at the input of the receiver, one of which is for low noise performance and the other is for high spurious signal rejection performance. The low noise path utilizes an :adi:`ADL9005` amplifier at the input of the chain to optimize noise performance of the front end, whereas the high rejection path implements an :adi:`ADMV8818` bandpass filter to increase attenuation of undesired received signals.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/ifrejectionpaths.png
   :align: center
   :width: 600px

Taking the low noise path, the average IF rejection performance was calculated to be 56.80dBc. The following plot shows the simulated IF rejection performance of the receiver front end in the low noise path:

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/ln_ifrejection.png
   :align: center
   :width: 900px

Taking the high rejection path, the average rejection performance is improved by 58dB, giving an average rejection of 115.0788dBc. The following plot shows the IF rejection of the receiver front end in the high rejection path:

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/hr_ifrejectionplot.png
   :align: center
   :width: 900px

Taking the low noise path, the average image rejection performance was calculated to be 89.04dBc. The following plot shows the simulated image rejection performance of the receiver front end in the low noise path:

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/ln_imagerejection.png
   :align: center
   :width: 900px

Taking the high rejection path, the average image rejection performance improved significantly to 160.7dBc. The following plot shows the simulated image rejection performance of the receiver front end in the high rejection path:

| |image2|
| ===== IF Section ===== The IF section of the receiver front end, shown below, is the final stage before the ADC, performing additional signal conditioning and filtering. Two high-linearity amplifiers provide additional gain while the :adi:`ADRF5730` DSA assists the DSA in the RF section with gain levelling/control and performance optimization in the IF. Anti-aliasing filtering is implemented by cascaded, COTS HPF and LPFs to provide 1GHz of IF bandwidth centered in the 2nd Nyquist band (4-5GHz) of the :adi:`AD9082` sampling at 6GSPS.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/rxifsection.png
   :align: center
   :width: 900px

The plot below shows the simulated frequency response of the IF section of the signal chain with the anti-aliasing filtering providing roughly 30-40dB of OOB (out-of-band) rejection around the sampled IF band. In general, anti-aliasing filtering should target 60dBc of OOB rejection, but satisfying this requirement with readily available COTS filters is somewhat impractical. It is recommended to use a custom anti-aliasing filter implementation if greater rejection is required by the end system.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/if_response.png
   :align: center
   :width: 800px

| 

Timing & Control
----------------

Automatic gain control (AGC), RF path switching, and filter switching/reconfiguration often have critical timing specs that drive component selection, especially in systems that require fast frequency hopping or wideband tuning. The RF switches, DSAs, and tunable filters in the receiver signal chain offer fast switching/settling times, a high degree of configurability, and can be controlled via standard parallel and/or SPI interfaces. The ADMV8818 tunable filters also have the ability to store up to 128 filter states in an internal lookup as well as an internal state machine, allowing faster recall of preset filter configurations. The table below lists the control interfaces and minimum configuration and settling time details at the component level.

| |image3|
| ===== Receiver Performance Simulations ===== Keysight Systemvue/Genesys was used for detailed signal chain modelling and cascade analysis. Every component in the signal chain was modelled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The Genesys signal chain model shown below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the ADMV8818 tunable filter configured to tune a 1GHz wide passband to the RF center frequency during frequency sweeps
-  Frequency-dependent component interconnect modelling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 8mil Rogers 4003 PCB stackup

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/rx_genesys_schematic.png
   :align: center
   :width: 800px

   | 
|

.. admonition:: Download
   :class: download

   To request the Keysight Pathwave simulation files that model the performance of these circuits, please send a request `here <https://support.analog.com/en-US/technical-support/create-case-techsupport/>`__ and include the following info:


   | \* Name
   
   -  Job Title
   -  Company Name
   -  Company Location
   -  Application/Use Case
   
   |

   |


| The Genesys workspace already has numerous system analysis and Matlab-based frequency sweeps in place, including the following functionality:

-  2-24GHz CW input sweep with Matlab equation-based frequency plan automated to ensure correct signal chain configuration for any given RF input frequency. All LO frequencies, frequency-dependent RF paths, and tunable filter passband automatically tune during sweep
-  Gain levelling implemented using the RF & IF DSAs to normalize cascaded gain to the lowest-gain frequency point for optimal flatness (+/- 2dB). Total attenuation is distributed evenly across the two DSAs.

| 
| **Receiver Performance (Gain, IIP3, IP1dB, NF, SFDR), 2-24GHz, LNA Path, Rough Gain Levelling Implemented**
| As described above, the performance shown in the following plot assumes PCB implementation with low loss traces. This plot shows the simulated Gain, IIP3, IP1dB, NF, and SFDR performance across frequency when taking the LNA path at the input of the receiver: |image4|

| **Receiver Performance (Gain, IIP3, IP1dB, NF, SFDR), 2-24GHz, Preselector BPF Path, Rough Gain Levelling Implemented**
| The following plot shows the simulated Gain, IIP3, IP1dB, NF, and SFDR performance across frequency when the Bandpass Filter path is taken at the input of the receiver: |image5|

| **Receiver Performance vs Input Power Level with Gain Control, 10GHz, LNA Path**
| The following plot shows the simulated performance of the receiver, including RF power at the input of the ADC, total noise power, IMD3, and CNDR3, when sweeping RF input power at an RF frequency of 10GHz, with the LNA path selected: |image6|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/rxinputnetwork.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/hr_imagerejection.png
   :width: 900px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/timing_control.png
   :width: 900px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rx_cascade_lna_path_gain_levelling_v2.png
   :width: 800px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rx_cascade_preselector_path_gain_levelling_v2.png
   :width: 800px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/rx_input_blocker_sweep_agc_enabled.png
   :width: 800px
