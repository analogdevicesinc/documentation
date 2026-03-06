LO Generation and Distribution
==============================

Overview
--------

The mixers (:adi:`HMC8108` and :adi:`HMC1056` on both the Rx and Tx side of the Marlin system require a local oscillator (LO) signal to mix with the input signals to generate output RF (Tx) or IF (Rx) signals ranging between 9.1-10.1 GHz. To do this, an LO is required that can handle X-Band outputs at the desired power level. The HMC8108 specifies an input power level between -10 and 0 dBm, whereas the HMC1056 datasheet indicates that although a typical input LO of +10 dBm is desired, conversion gain varies in the range of -10 to -7 dB for an RF frequency range of 9-10 GHz with an input LO power between 8-12 dBm. It is important to note that in the Marlin application, an LO signal is required at each of the 16 Rx channels along with 1 Tx channel, making it 17 total LO channels per tile. It would be difficult to achieve an individual LO signal for each channel, as that would not only cause pinout issues, but would also increase the power consumption per channel in an application that is specifically designed to minimize power. Therefore, a solution incorporating one LO signal going through splitter and amplifier stages has been implemented in the Marlin platform.

LO Generation: ADF5356
----------------------

The :adi:`ADF5356` is a microwave wideband synthesizer with an integrated VCO. This chip, when used with an external loop filter and external reference signal, allows implementation of fractional-N or integer N phase locked loop frequency synthesizers. The integrated voltage controlled oscillator (VCO) has a fundamental output frequency ranging between 3.4GHz - 6.8GHz.

In the case of the Marlin platform, the 10MHz reference signal is sent by the backplane LTC6953. Since the internal VCO core only outputs up to 6.8GHz, the internal RF N divider and RF doubler are utilized to get the desired output frequency of 9-10GHz. After going through the math while assuming about a 5 MHz channel spacing, it is determined that both the reference signal doubler and divider are unnecessary and can be disabled. The output stage RF doubler can be enabled by setting the prescaler value to 8/9 with register 0 in the controls. Below is a labeling of the internals of the ADF5356 for reference.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_adf5356.png
   :width: 600px

**Figure 1: ADF5356 signal path and settings**

The RF output power between 6.8GHz and 13.6GHz RF_outB is 0 to 2 dBm. This signal will incur insertion loss while passing through the series of splitters prior to hitting the mixers. Therefore, some amplification prior to running the signals through the splitters is necessary.

LO Distribution
---------------

Since the LO signal is needed among 17 channels as mentioned previously, splitters are necessary. The Marlin platform uses the `SEPS-8-153+ <https://www.minicircuits.com/pdfs/SEPS-8-153+.pdf>`__ 8-way splitter and the `EP2C+ <https://www.minicircuits.com/pdfs/EP2C+.pdf>`__ 2-way splitter modules. The signal is first sent to one 2-way splitter, out of which one output is sent straight to the HMC1056 on the Tx side. The other output of the first 2-way splitter is sent to another 2-way splitter, which outputs to two 8-way splitters. Each output of these 8-way splitters is sent to each one of the 16 HMC8108 modules in each RxFE signal chain. The LO signal incurs loss at each of the splitter stages on the way to the HMC8108 chips, and therefore amplification is needed prior to that. The diagram below highlights the power level of the LO signal at each stage of amplificaton, splitting, and attenuation. The end result is a +1dBm drive power to the HMC8108 (Rx) and +10dBm drive power to the HMC1056 (Tx), which both fall within the recommended ranges in the part datasheets.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_losplitpowerlevels.png
   :width: 600px

**Figure 2: Power Levels of LO Signal at each stage of distribution**
