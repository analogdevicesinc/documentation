:doc:`Link to parent page </wiki-migration/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end>`

Transmitter Front End Overview & Theory Of Operation
====================================================

| The 2-24GHz transmitter block diagram is shown below. The following wiki sections will go into more detail on the theory of operation of the individual, functional blocks of the signal chain.
| |image1|

| 

IF Input Stage
--------------

| The DAC output first feeds into the IF input section (block diagram below) of the front end with 4.8GHz low-pass filtering to reject the DAC image spurious. The IF input frequency is 4-5GHz and within the 1st Nyquist of the DAC sampling at 12GSPS. After the image LPF comes an ADRF5730 digital step attenuator for fine resolution level control, an LNA, and an additional LPF for additional suppression of DAC output spurious.
| |image2|

| 
| ===== Frequency Conversion Stage & Frequency Plan ===== The transmit signal chain uses two separate frequency conversion paths to enable continuous, 2-24GHz frequency coverage. The two signal paths are selectable via :adi:`ADRF5020` RF switches. For the 6.5-24GHz RF output frequency band, the 4-5GHz IF input is fed into an :adi:`HMC8191` wideband I/Q mixer with a tunable LO source, upconverting the entire band to the desired RF output frequency.

For the 2-7GHz RF output band, a dual-frequency conversion heterodyne signal path is used with the IF input first being upconverted to a high, 11-16GHz IF through the :adi:`HMC8191` with tunable LO, and then downconverted to the 2-7GHz RF output through an :adi:`HMC773A` mixer with a fixed 18GHz LO. Cascaded low and high-pass filters provide 11-16GHz IF filtering and an :adi:`HMC882A` tunable low pass filter mitigates mixer output spurious for the final 2-7GHz RF output band. The figure below shows the frequency conversion section of the signal chain and the frequency operation ranges for each individual path.

| 
| |image3|
| The figure below provides an additional frequency plan visualization showing the individual frequency conversion steps for each frequency band.
| |image4|
| The following table summarizes the possible frequency conversion paths:
| |image5|
| ===== RF Output Stage ===== The RF output stage, shown in the figure below, is comprised of a wideband :adi:`ADL9006` driver amp, an :adi:`ADMV8818` tunable bandpass filter, and finally an :adi:`HMC994APM5E` PA. The :adi:`ADMV8818` tunable filter operates across a 2-18GHz frequency range for additional filtering of output spurious, and can be bypassed for operation up to 24GHz.
| |image6|

| 

Timing & Control
----------------

| 
| |image7|

Transmitter Performance Simulations
-----------------------------------

Keysight Systemvue/Genesys was used for detailed signal chain modelling and cascade analysis. Every component in the signal chain was modelled with frequency-dependent sys-parameter or s-parameter datasets to ensure accurate simulation results. The Genesys signal chain model shown below takes into account the following components:

-  Manufacturer-provided, frequency-dependent s-parameter or sys-parameter datasets for every active and passive RF component
-  A standalone model of the ADMV8818 tunable bandpass filter configured to tune a 1GHz wide passband to the RF center frequency during frequency sweeps. The ADMV8818 internal bypass path is engaged above 18GHz.
-  A standalone model of the HMC882A tunable lowpass filter configured to tune its 3dB corner frequency minimize LO feedthrough and spurious
-  Frequency-dependent component interconnect modelling i.e. PCB trace loss approximation for DC-50GHz CPWG traces, 8mil Rogers 4003 PCB stackup

| 
| |image8|

| 
|

.. admonition:: Download
   :class: download

   To request the complete Keysight Genesys/Systemvue simulation workspaces for 2-24Ghz MxFE Front End Rx & Tx signal chains, please send a request to `here <https://support.analog.com/en-US/technical-support/create-case-techsupport/>`__ and include the following info:


   | \* Name
   
   -  Job Title
   -  Company Name & Location
   -  Application/Use Case
   
   |

   |


| The Genesys workspace already has numerous system analysis and Matlab-based frequency sweeps in place, including the following functionality:

-  2-24GHz CW input sweep with Matlab equation-based frequency plan automated to ensure correct signal chain configuration for any given RF output frequency. All LO frequencies, frequency-dependent RF paths, and tunable filter passbands are automatically tune during sweep.
-  Gain levelling implemented using the IF DSAs to normalize cascaded gain to the lowest-gain frequency point for optimal flatness (+/- 2dB).

| 
| **Transmitter Performance (Gain, OIP3, and OP1dB), 2-24GHz, Rough Gain Levelling Implemented**
| As described above, the following plot assumes PCB implementation with low loss traces. This plot shows the Gain, OIP3, and OP1dB performance of the transmitter across frequency:
| |image9|
| **Transmitter Output Spectrum, +12dBm out @ 12.5GHz**
| The following plot shows the spectral output power components of the transmitter at +12dBm input power and 12.5GHz frequency:
| |image10|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/txblockdiagram.png
   :width: 990px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_if_input_section.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/txfreqconversionsection.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/txfreqplan.png
   :width: 500px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_frequency_plan.png
   :width: 900px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_rf_output_section.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_switch_and_atten_ctrl.png
   :width: 800px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_genesys_simulation.png
   :width: 900px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_rf_performance.png
   :width: 950px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/developer-kits/2to24ghz-mxfe-rf-front-end/tx_output_spectrum_12ghz.png
   :width: 950px
