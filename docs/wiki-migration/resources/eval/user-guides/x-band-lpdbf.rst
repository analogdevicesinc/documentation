Marlin: X-Band Low Power Digital Beamforming Virtual Reference Design User Guide
================================================================================

ADEF Reference Designs - What is Marlin?
----------------------------------------

At Analog Devices, the Aerospace and Defense (ADEF) team provides a plethora of enablement solutions in different levels of development. Marlin is a virtual reference design that contains a full signal chain solution for the desired specifications including a combination of RF front end design, digitizer integration, and power optimization. The design includes both Analog Devices and third-party hardware and is supported by multiple simulations and models for each design aspect. Customers can utilize this wiki along with supporting technical articles to build out this platform and modify it to their specifications. The descriptions below show what type of solutions ADI provides, and where Marlin falls among them.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_adeftypesofplatforms.png
   :width: 600px

Product Details
---------------

The Marlin Platform contains 16 receive channels with the ability to scale up to 128 channels with 1 FPGA, as well as associated RF front-ends, clocking, controls and power circuitry. The target application is phased array radars, electronic warfare, and ground-based SATCOM, specifically a **16 receive/1 transmit channel** direct sampling phased array at X-Band (9 to 10 GHz). The design has been catered towards applications that require low power solutions such as UASs, mobile ground stations and autonomous systems.

The Marlin platform highlights a uniquely scalable low power solution. It is intended as a testbed for demonstrating multi-chip synchronization as well as the implementation of system level calibrations, beamforming algorithms, and other signal processing algorithms. The system is designed to mate with a `ZCU102 <https://www.xilinx.com/ZCU102>`__ Evaluation Board from AMD Xilinx®, which features the Zynq® UltraScale+™ XCZU9EG-2FFVB1156E MPSoC.

The system can be used to enable quick time-to-market development programs for applications like:

-  Phased-Array Radar
-  SATCOM
-  Communications Infrastructure (Multiband 5G and mmWave 5G)
-  Electronic Test and Measurement

Block Diagrams and Beamforming Patterns
---------------------------------------

Shown below is a block diagram with a view of one 16Rx/1Tx Marlin tile. In this setup, the tile is connected via an interposer board to the FPGA.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_tilelevelblockdiagram.png
   :width: 600px

8 of the tiles shown above can be stacked on top of each other and connected to a backplane that interfaces with an FPGA as shown below. The backplane supports multi-tile synchronization while also interfacing all 8 tiles with the FPGA.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_stackedrender.png
   :width: 600px

The 3D directivity pattern generated using the MATLAB Sensor Array Analyzer is shown below. 8 by 16 elements spaced half wavelengths from each other with a rectangular lattice structure were the settings used for array geometry. For the isotropic antenna settings, propagation speed of 3e8 m/s and 10 GHz signal frequency were set. The antenna was back baffled to ensure the response was limited to azimuth angles between -90 and 90 degrees.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_beampattern.png
   :width: 600px

The system G/T value was found to be -4.3 dB, assuming 67% antenna aperture efficiency.

**Figure 2: 3D Directivity Pattern**

Features and Specifications
---------------------------

-  Multi-channel, low bandwidth (<25MHz) prototyping platform based on the :adi:`AD9083` and :adi:`AD9106`
-  Mates with Xilinx `ZCU102 <https://www.xilinx.com/ZCU102>`__ Evaluation Board
-  16x RF Receive (Rx) Channels

   -  Total 16x up to 2GSPS ADC
   -  **718 mW per channel**

-  1x RF Transmit (Tx) Channel

   -  Up to 180MSPS DAC with on-chip DDS
   -  **540 mW per channel**

-  Flexible Rx & Tx RF Front-Ends

   -  Rx: Mixing, Filtering, Gain Adjustment
   -  Tx: On-Chip DDS, Mixing, Filtering, Amplification

-  Scalability options

   -  Single-tile use with adapter straight to FPGA
   -  Multi-tile use through backplane to FPGA

-  On-Board Power Regulation from Single 12V Power Adapter
-  Flexible Clock Distribution

   -  Clock Distribution through backplane for multi-tile use cases demonstrating multi-chip synchronization between boards
   -  Clock Distribution on-tile for single-tile use case
   -  External Reference Clock able to be used for both use cases.

Data Converter Overview
-----------------------

As Marlin is an Rx-heavy platform, an analog-to-digital converter is necessary that can handle 16-channel operation while maintaining low power consumption. The :adi:`AD9083` Analog-to-Digital Converter is ideal for this application, as it is a low power 16-channel continuous time Σ-Δ ADC with the ability to handle 16 channels at 125MHz bandwidth. It includes integrated DSP blocks that help to reduce the overall footprint of the Marlin system front end components and also features several power-down options that allow for power savings when needed. The configurable JESD204B interface reduces PCB complexity for the overall system as well. A key feature of the AD9083 that is applicable to the Marlin platform specifically is the ability to support multi-device synchronization.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_ad9083blockdiagramunlabeled.png
   :width: 600px

For the Tx side, a :adi:`AD9106` Digital-to-Analog Converter is used which supports up to 180 MSPS sample rates while also having low power dissipation (typ. 315.25mW at 180MSPS). This DAC utilizes on-chip direct digital synthesizer (DDS) to generate complex waveforms. SPI ports on the AD9106 allow for easy interfacing between the FPGA and the chip.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02_077511a_ad9106blockdiagramunlabeled.png
   :width: 600px

Receiver Front End Overview and Theory of Operation
---------------------------------------------------

The Marlin receive front-end block diagram is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_rxblockdiagram.png
   :width: 600px

**Figure 1: Full receive front-end block diagram**

The table below contains receiver specific specifications derived from a cascade analysis on ADISimRF.

================= =================
**Attribute**     **Value (units)**
Gain              29
Noise Figure (dB) 3.8
IIP3 (dBm)        0.4
SFDR3 (dB)        67
IP1dB (dBm)       -4.2
================= =================

HMC8108
~~~~~~~

The first step of the RxFE chain is the :adi:`HMC8108`. This is an X-Band low noise converter that contains a low noise amplifier followed by an image reject mixer that is driven by an active LO amplifier. This component takes in a radio frequency input (RFIn) signal of 9-10GHz, which is consistent with the target frequency range of the Marlin platform (X-Band). This signal is mixed with an external local oscillator signal that is in the range of 9.1-10.1GHz, thereby generating a single-ended intermediate frequency (IF) output of 90-110MHz. The gain of this stage is typically 13dB with a noise figure of around 2dB when operating at 90-110MHz IF frequencies. The plot below shows the spurious performance of the HMC8108 with the desired RF and IF center frequencies and bandwidths. This plot was generated using the WhatIF Frequency planner.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_whatif.png
   :width: 600px

**Figure 3: Spurious Performance of IFs at HMC8108 Mixer output**

The HMC8108 is a very low power consuming part for what it does; however, that does come with some external circuitry needed. The biasing sequence (on page 15 of the part datasheet) is used to avoid damage to the transistors that are part of the active amplifier and local oscillator buffer stages. This sequence can either be done utilizing several power supplies on a lab bench, or through a biasing and supply circuitry on-board. The latter option is what we designed for in this platform. The biasing circuitry is centered around the :adi:`LT6017` quad-pack op-amp, which biases the LNA_VG1, LNA_VG2, and BUFF_VG pins on the HMC8108. The biasing circuit can be shown below. The :adi:`LT6015` op-amps are all part of the quad-pack in the LT6017, which is why they are placed separately in the LTSpice schematic for clarity purposes.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_hmc8108biasingcircuit.png
   :width: 600px

**Figure 4: HMC8108 gate biasing circuitry**

The supply circuit utilizes the :adi:`LTC4210-1`, which is a hot swap controller that is used to slowly ramp up the supply voltage of the mixer. This helps to accomplish the first 2 out of 8 steps in the HMC8108 biasing sequence. The schematic for the supply circuit is shown below, as well as a table with some important specifications of the circuit. The Vdd output of the supply circuit corresponds with the Vdd inputs of the gate biasing circuits in Figure 3.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_hmc8108supplycircuit.png
   :width: 600px

**Figure 5: HMC8108 supply circuitry**

======================= =================
**Parameter**           **Value (units)**
In-rush startup current 108 mA
Steady state current    1.435 A
Circuit breaker current 4.2 A
======================= =================

**Table 1: Important current values pertaining to the supply circuitry in Figure 2**

It is important to note that the circuit breaker current is dependent on the size of the sense resistor, which in Figure 5 is R289. The in-rush and steady state currents are dependent on the load capacitances of the gate biasing circuits in Figure 4 in addition to the R-C circuit (R291 and C289) at the bottom right of the supply circuit in Figure 5.

Measurements were taken on the HMC8108 evaluation board (:adi:`EVAL-HMC8108`) to verify image rejection rejection numbers. The two IF outputs of the HMC8108 were connected to the QCV-151 90 degree hybrid (see next section) and the single-ended output of that was connected to a spectral analyzer. The 9-10 GHz RF and LO inputs were sent utilizing external signal generators in this test setup. Below is a graph depicting the image rejection at 90MHz and 105MHz IF across 9-10 GHz RF input frequencies.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_hmc8108imagerejectperf.png
   :width: 600px

**Figure 6: Image Rejection of HMC8108**

QCV-151+
~~~~~~~~

Since the :adi:`HMC8108` has an internal 90-degree hybrid, an external 90-degree hybrid is necessary at the intermediate frequency (IF) output of the mixer to convert back to a single ended signal. The way this is achieved is by feeding the hybrid coupler with the differential signal output of the mixer and grounding the 90-degree phase shifted output. That way, the signal coming out of the 0-degree phase shifted output is used as the single=ended IF signal in the rest of the RxFE signal chain. The `QCV-151+ <https://www.minicircuits.com/pdfs/QCV-151+.pdf>`__ has a very low insertion loss of 0.4 dB and high isolation of 20dB between 90-118 MHz, making it ideal for this platform considering that the IF signal is ranging between 90-105 MHz.

LFCN-105+
~~~~~~~~~

The desired IF range is 90 to 105MHz; therefore, our desired signal should be noise-free around that frequency range. In order to filter out all noise or excess signal above that frequency, we implement the `LFCN-105+ <https://www.minicircuits.com/pdfs/LFCN-105+.pdf>`__ low pass filter. This filter has a 1dB insertion loss from DC-105 MHz and a 25-55 dB insertion loss between 1-5 GHz. This will allow for appropriate filtering of all the unwanted signal above 105 MHz. A possible alternative is to use a bandpass filter so the spurious noise below 37.5MHz that is shown in Figure 3 can also be filtered out. For example, the `RBP-98+ <https://www.mouser.com/datasheet/2/1030/RBP_98_2b-1700954.pdf>`__ has a high insertion loss (44-97 dB) between DC-45 MHz, which is ideal considering the spurs occurred under 37.5 MHz. Additionally, the insertion loss between 75-103 MHz ranges between 1.65-2.29dB, which is only slightly higher than that of the LFCN-105+ around those frequencies. However, a bandpass filter was not chosen due to the much larger board footprint necessary as well as power consumption considerations.

A measured plot of the S parameters for this part is shown below. The target operation band (80-105 MHz) is highlighted on the left and the alias band (1895-1920 MHz) is highlighted on the right.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_lfcn105p_sparams.png
   :width: 600px

**Figure 7: Plot of S parameters of LFCN-105+ from measured data**

LTC6421-20
~~~~~~~~~~

The :adi:`LTC6421-20` is a dual-pack differential amplifier/ADC driver module that operates between DC-140 MHz. This part is able to be configured to take in a single-ended input and output a differential signal using an input termination that is drawn out schematically on page 9 of the part datasheet. This configuration eliminates the need for a balun. Additionally, this part can drive an ADC directly without external output impedance matching. The 3mmx4mm package size of the dual-pack amplifier allows for less necessary footprint and also cuts the necessary amount of ADC driver packs for one tile from 16 (in the case of single pack) to 8. Below is a table that shows the difference in cascade performance with and without the driver amplifier in the RX front end chain.

================= =================== ======================
\                 **with LTC6421-20** **without LTC6421-20**
Gain              29                  9
Noise Figure (dB) 3.8                 16.8
IIP3 (dBm)        0.4                 6
SFDR3 (dB)        67                  62
IP1dB (dBm)       -4.2                -4
================= =================== ======================

**Table 2: Cascade Performance Comparison with and without LTC6421-20 in RxFE chain**

Key RxFE IC: AD9083
~~~~~~~~~~~~~~~~~~~

The :adi:`AD9083` is a 16-channel, 125MHz Bandwidth, JESD204B compatible analog-to-digital converter. Each ADC has a integrated signal processing block that filters out noise and reduce the sample rate. Each tile also contains a cascaded integrator comb (CIC) filter, a quadrature digital downconverter (DDC) with multiple finite input response (FIR) decimation filters as well as up to 3 quadrature DDC channels with averaging decimation filters. In addition to the JESD204B compatibility, what makes this chip ideal for the Marlin platform is the support for multi-device synchronization through the usage of the differential SYSREF, TRIG, and SYNCINB input pins. The estimated power draw of this chip is 0.989W in worst-case, with the ability to trigger flexible power-down options through SPI controls when additional power savings are needed. Below is the internal block diagram of the AD9083 labeled specifically with regards to the Marlin application.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_ad9083blockdiagram.png
   :width: 600px

**Figure 8: AD9083 Internal Block Diagram**

The frequencies of the input signals to the ADCs will range from 80-105 MHz depending on what the output of the HMC8108 intermediate frequencies are. These signals are then sent through the CIC decimator that should be set to 4x decimation. Given that the sample rate of the ADC is 2 GSPS, the output of the CIC filter is a single 16-bit data sample at a rate of 500 MSPS (f_s/N or 2GSPS/4). The CIC filter behaves similar to a second-order moving average filter of length N (N is decimation rate).

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_ad9083cicfilter.png
   :width: 600px

**Figure 9: AD9083 CIC Filter Response for Various Decimation Ratios Normalized to f_s**

Figure 9 shows the response of the CIC filter for different decimation ratios which shows the similar behavior to a second-order moving average filter as mentioned before. When the 4x decimation rate is set and with a fundamental frequency between 80-105 MHz, only around 1 dB of loss is incurred (as opposed to around 5 or 25 dB loss with 8x and 16x decimation ratios). Therefore, relying on further decimation further along in the DSP block is wise to minimize loss.

After the mixer downconverts the IF centered around 92.5MHz to baseband, the signal can either go through the J decimator or can bypass that by going through the averaging and decimation filter prior to the amplification stage. The J decimation options are relatively limited by the input data path (CIC Filter and Mixer). Table 19 of the AD9083 :adi:`datasheet <media/en/technical-documentation/data-sheets/ad9083.pdf>` shows the J decimation options. In this case, the signal goes through the J decimator to further reduce the output data rate by a decimation ratio of 16x. The J decimator provides 81.4% of the available output bandwidth, meaning that the frequency of the output is 25.4 MHz (%*(f_CICout/N) or 0.814*(500MHz/16)). The J decimation filter block diagram below details the breakdown of the various DDC filter configurations possible to obtain the desired decimation ratio at this stage.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_ad9083jfilter.png
   :width: 600px

**Figure 10: AD9083 J Decimation Filter Block Diagram**

The frequency translation by the mixers are enabled by the three identical numerically controlled oscillators (NCOs). These NCOs create a complex exponential frequency that is mixed with the input to translate down to DC where it can be filtered while avoiding aliasing. The 7-bit wide NCO frequency tuning word (FTW) is determined based on the carrier frequency, sampling frequency, and CIC decimation ratio. Further information on this calculation can be found on page 43 of the part datasheet (linked above). The NCO_FTW in this case is found to be 23.

The JEDEC standard JESD204B serial interface is the protocol used to link the AD9083 to a digital processing devices (in this case the ZCU102). The JESD204B link is described according to several parameters related to the converters. It is important to note that the total decimation rate is the culmination of the CIC and J decimation stages which is 64 (4*16). This value helps determine the frequency output of the filter stages, which comes out to 31.25 MHz. Below is a table that outlines the parameters and corresponding values for the digital portion of the AD9083 in the Marlin platform.

==================================================== ===========
**Parameter**                                        **Value**
JESD204B Serial Lane Rate                            320 \* Fout
CIC N                                                4
NCO/Mixer                                            Enabled
J Decimator N                                        16
Lanes per link                                       2
Converters per link                                  32
Octets per Frame                                     32
Samples transmitted per single converter/frame cycle 1
Number of bits per sample                            16
Number of frames per multiframe                      32
==================================================== ===========

**Table 3: AD9083 Digital Parameters**

The different JESD204B output configurations can be seen on Table 24 on pages 49-50 of the AD9083 datasheet. It is important to note that although a JESD204B serial lane rate of 640*Fout is possible and fits a potential output configuration, it will not work for this application because it exceeds the maximum lane rate allowed by the AD9083 (16 Gbps). 16 bits per sample JESD204B word size is chosen to avoid truncation which negatively affects performance. 2 SERDES output lanes are utilized in this setup, and the remaining two outputs can be disabled via control bits for additional power savings. Lastly, to enable multi-chip synchronization, the 15.625 SYSREF input is JESD204B subclass 1 compatible and is sent from the on-tile LTC6953. This signal allows for clock and NCO synchronization across all tiles.

Transmitter Front End Overview and Theory of Operation
------------------------------------------------------

The Marlin transmit block diagram is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_txblockdiagram.png
   :width: 600px

**Figure 1: Full transmit front-end block diagram**

AD9106
~~~~~~

The :adi:`AD9106` is a quad-pack digital-to-analog converter (DAC) that utilizes an on-chip direct digital synthesizer (DDS) for complex waveform generation. The on-chip DDS has a 12-bit resolution and supports sample rates up to 180 MSPS. The low power dissipation of the :adi:`AD9106` makes this an ideal chip for the Marlin platform. The Marlin platform utilizes two of the four differential output pairs because both the in-phase and quadrature signals are generated. The frequency of the output signals from the :adi:`AD9106` are between 50-75 MHz. The two unused DACs can be disabled using the power status register.

Custom Differential to Single-Ended Conversion Circuit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The in-phase and quadrature signals generated by the :adi:`AD9106` are differential signals, and have to be converted to single-ended signals prior to sending into the mixer stage. Typically, this would be achieved using a balun. However, off-the-shelf (OTS) balun solutions do not cover many of the lower-end frequencies, especially towards DC. Also, the return loss incurred with OTS balun solutions would necessitate an amplifier stage which would increase power consumption of the chain while also increasing necessary board footprint. To counteract this issue, a custom circuit is utilized that maintains unity gain while also covering more frequencies, especially on the low end towards DC. The circuit and simulated performance are shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_balunaltscheme.png
   :width: 600px

**Figure 2: Balun Alternative Circuit**

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_balunaltschemesim.png
   :width: 600px

**Figure 3: Frequency Response of Balun Alternative Circuit**

.. _lfcn-105-1:

LFCN-105+
~~~~~~~~~

The same low pass filter in the Rx chain is used here in the Tx chain to filter out all noise or excess signal above our max desired IF frequency, which is 105MHz. This filter has a 1dB insertion loss from DC-105 MHz and a 25-55 dB insertion loss between 1-5 GHz. For information about why a bandpass filter was not selected, refer to the part description in :doc:`Receiver Front End Overview & Theory Of Operation </wiki-migration/resources/eval/developer-kits/x-band-lpdbf/receiver_front_end_overview_theory_of_operation>`.

HMC1056
~~~~~~~

The :adi:`HMC1056` is an image reject mixer/single sideband upconverter that utilizes two double balanced mixer cells and an integrated 90 degree hybrid that converts the I/Q signal into a single-ended RF output signal. An external local oscillator (LO) signal ranging between 9.1-10.1 GHz is mixed with the IF inputs ranging between 75-105MHz to produce an RF output between 9-10 GHz. The integrated 90 degree hybrid allows for power and cost savings along with less necessary board footprint.

HMC564LC4
~~~~~~~~~

Due to the conversion losses of 8-11 dB incurred in the mixer stage, an amplifier is needed to increase the gain of the signal prior to sending it off to the antenna. The :adi:`HMC564LC4` is ideal for this platform due to its 17 dB gain while still boasting a 1.8 dB noise figure and 25 dBm output IP3 across the 7-14 GHz operating frequency range. Additionally, this part has a low power consumption, low board footprint, and is input/output impedance matched at 50 Ohms.

LO Generation and Distribution
------------------------------

Overview
~~~~~~~~

The mixers (:adi:`HMC8108` and :adi:`HMC1056` on both the Rx and Tx side of the Marlin system require a local oscillator (LO) signal to mix with the input signals to generate output RF (Tx) or IF (Rx) signals ranging between 9.1-10.1 GHz. To do this, an LO is required that can handle X-Band outputs at the desired power level. The HMC8108 specifies an input power level between -10 and 0 dBm, whereas the HMC1056 datasheet indicates that although a typical input LO of +10 dBm is desired, conversion gain varies in the range of -10 to -7 dB for an RF frequency range of 9-10 GHz with an input LO power between 8-12 dBm. It is important to note that in the Marlin application, an LO signal is required at each of the 16 Rx channels along with 1 Tx channel, making it 17 total LO channels per tile. It would be difficult to achieve an individual LO signal for each channel, as that would not only cause pinout issues, but would also increase the power consumption per channel in an application that is specifically designed to minimize power. Therefore, a solution incorporating one LO signal going through splitter and amplifier stages has been implemented in the Marlin platform.

LO Generation: ADF5356
~~~~~~~~~~~~~~~~~~~~~~

The :adi:`ADF5356` is a microwave wideband synthesizer with an integrated VCO. This chip, when used with an external loop filter and external reference signal, allows implementation of fractional-N or integer N phase locked loop frequency synthesizers. The integrated voltage controlled oscillator (VCO) has a fundamental output frequency ranging between 3.4GHz - 6.8GHz.

In the case of the Marlin platform, the 10MHz reference signal is sent by the backplane LTC6953. Since the internal VCO core only outputs up to 6.8GHz, the internal RF N divider and RF doubler are utilized to get the desired output frequency of 9-10GHz. After going through the math while assuming about a 5 MHz channel spacing, it is determined that both the reference signal doubler and divider are unnecessary and can be disabled. The output stage RF doubler can be enabled by setting the prescaler value to 8/9 with register 0 in the controls. Below is a labeling of the internals of the ADF5356 for reference.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_adf5356.png
   :width: 600px

**Figure 1: ADF5356 signal path and settings**

The RF output power between 6.8GHz and 13.6GHz RF_outB is 0 to 2 dBm. This signal will incur insertion loss while passing through the series of splitters prior to hitting the mixers. Therefore, some amplification prior to running the signals through the splitters is necessary.

LO Distribution
~~~~~~~~~~~~~~~

Since the LO signal is needed among 17 channels as mentioned previously, splitters are necessary. The Marlin platform uses the `SEPS-8-153+ <https://www.minicircuits.com/pdfs/SEPS-8-153+.pdf>`__ 8-way splitter and the `EP2C+ <https://www.minicircuits.com/pdfs/EP2C+.pdf>`__ 2-way splitter modules. The signal is first sent to one 2-way splitter, out of which one output is sent straight to the HMC1056 on the Tx side. The other output of the first 2-way splitter is sent to another 2-way splitter, which outputs to two 8-way splitters. Each output of these 8-way splitters is sent to each one of the 16 HMC8108 modules in each RxFE signal chain. The LO signal incurs loss at each of the splitter stages on the way to the HMC8108 chips, and therefore amplification is needed prior to that. The diagram below highlights the power level of the LO signal at each stage of amplificaton, splitting, and attenuation. The end result is a +1dBm drive power to the HMC8108 (Rx) and +10dBm drive power to the HMC1056 (Tx), which both fall within the recommended ranges in the part datasheets.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_losplitpowerlevels.png
   :width: 600px

**Figure 2: Power Levels of LO Signal at each stage of distribution**

Clock Distribution Scheme and Backplane Design
----------------------------------------------

.. _overview-1:

Overview
~~~~~~~~

One of the main features of the Marlin platform is the ability to operate up to 8 tiles synchronously with one FPGA. This operation comes with many challenges, as the :adi:`AD9106`, :adi:`AD9083`, and :adi:`ADF5356` all operate on different reference clock frequency levels. Therefore, care has to be taken to make sure all clock signals to like chips are distributed appropriately across each tile to ensure signal integrity, isolation, and noise reduction. A combination of fanout buffers and clock distributors are used to create a scheme for single-tile and multi-tile use.

Key IC: LTC6953
~~~~~~~~~~~~~~~

The key IC that enables the clock distribution scheme for the Marlin platform is the :adi:`LTC6953`. This chip is a high performance, ultralow jitter, JESD204B/C clock distribution IC. It has the ability to output up to 11 general purpose clock outputs or 5 JESD204B/C subclass 1 device clock/SYSREF pairs plus 1 general purpose output. The LTC6953 comes with :adi:`EZSync <media/en/technical-documentation/product-selector-card/4pb_clocking.pdf>` or ParallelSync capabilities, which allow for multi-device synchronization. The Marlin platform utilizes an adaptation of the ParallelSync Multichip Synchronization scheme that is outlined in pages 20-21 of the part :adi:`datasheet <media/en/technical-documentation/data-sheets/ltc6953.pdf>`.

In the ParallelSync Multichip Synchronization scheme, two distributors are used to distribute the reference clock signal and EZS_SRQ signals, respectively. The frequency of the LTC6953 output clock signals are dictated by the frequency of the reference clock, which in the case of Marlin is 250 MHz provided from an external signal generator. The output signals from the LTC6953 can therefore be any divisor of 250 MHz. The :adi:`AD9083` supports multi-devices synchronization through the differential SYSREF, TRIG, and SYNCINB input pins, which are all sent by the LTC6953.

The clock signals necessary for each chip vary based on the part specifications. Below is a table that contains the frequencies of the necessary clock signals for each part.

Clock Distribution Scheme
~~~~~~~~~~~~~~~~~~~~~~~~~

Before delving into multi-tile clock distribution, it is important to establish clock distribution to the different chips on the tile itself. Below is a block diagram illustrating the distribution of clock signals within one tile.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_singletileclocking.png
   :width: 600px

**Figure 1: Single Tile Clock Distribution**

The on-tile LTC6953 takes in a 250 MHz reference clock signal from an external signal generator. When being operated in single-tile mode, the LTC6953 supplies the SYSREF, JRXJESD, and REFCLK signals directly to the FPGA. The AD9083 requires the SYSREF, TRIG, and SYNCINB signals to operate in multi-chip synchronization, and so those signals are sent to the chip from the on-tile LTC6953. Additionally, all of the follower chips (AD9106, AD9083, and ADF5356) need a reference clock signal which are all sent directly sent from the on-tile LTC6953 as well. Note that all the frequencies are a divisor of 250 MHz, which is the reference clock signal that is sent to the LTC6953 from the external signal generator. This is to abide with the reference distribution divider and DDEL settings for ParallelSync that are listed in Table 9 on page 21 of the part datasheet. One advantage of the LTC6953 is that in SYSREF generation mode, there are methods via control bits to shutdown as much circuitry as possible while maintaining the correct timing relationship between the SYSREF outputs and the clock outputs. The ParallelSync configuration also allows for improved jitter performance when devices are cascaded. The tighter restrictions with the control of the REF and EZS_SRQ signals that are mentioned in the datasheet are accounted for in the backplane clock scheme. Below is the block diagram illustrating the backplane clock distribution scheme for multi-tile enablement.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_multitileclocking.png
   :width: 600px

**Figure 2: Multi-tile Clock Distribution Scheme**

The reference clocks signals to each tile have to be synchronized. To do this, an EZSync signal must be utilized. The EZSync signal is sent from the FPGA to the first of 2 backplane LTC6953 chips. This signal ensures that all reference clock signals are synchronized, both to all eight tiles as well as the backplane :adi:`ADCLK854`, which distributes the SYSREF request (EZS_SRQ) to all eight tiles.

The ADCLK854 is a low-power clock fanout buffer capable of up to 12 LVDS (1.2GHz) or 24 CMOS (250MHz) signal outputs. This chip is used in three places in the multi-tile clocking scheme. The first use is for distributing the EZS_SRQ signals as mentioned before. The EZS_SRQ signals are distributed all eight tiles and also to the second backplane LTC6953 which interfaces with the FPGA. The other two uses of the ADCLK854 are for supplying the TRIG and SYNCINB signals that are distributed to the on-tile AD9083 chips straight from the FPGA. Using the clock buffer for distribution of these signals allows for isolation and reduces any chance of compromising signal integrity.

The second LTC6953 takes in the REFCLK and EZS_SRQ signals from the respective clock distribution chips and sends the JRXJESD, REFCLK, and SYSREF signals to the FPGA.

All in all, the clock distribution scheme is designed to enable the user to utilize both single-tile and multi-tile functionalities. It is essential for the successful operation of the platform and has been optimized to consume the least power possible as well.

Power Architecture
------------------

The power tree for this design is broken down into two parts: The on-tile chip power circuitries and the HMC8108 biasing/supply power circuitry. The reason this is done is to draw special attention to the intricacy of the power optimization for the HMC8108.

The power tree for the main circuit highlights a few power components. The :adi:`LTM8063` is a 40V/2A silent switcher uModule regulator that is used to power the ADF5356, MAX5351, LTC6953 and AD9106. Two :adi:`LTM8074` 40V/1.25A silent switcher uModule regulator chips are used to power the 1P0 and 1P8 rails of the AD9083 on the Rx side. A :adi:`LTM8020` 36V/200mA uModule regulator is used to power the ADF5356 and an :adi:`ADP5600` to power the LTC6269. The ADP5600 integrates a low ripple interleaved inverting charge pump with a high performance LDO to easily produce clean negative voltages to the AD8613 and LTC6269. Below is the power tree for the main circuit excluding the HMC8108 biasing/supply circuitry.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_mainpowertree.png
   :width: 600px

**Figure 1: Main Circuit Power Tree**

The power tree for the biasing circuit utilizes a couple of the same silent switching regulator power modules as the main circuit (:adi:`LTM8063` and :adi:`ADP5600`). The drain biasing supply comes from the LTM8063, whereas the gate biasing supplies come from the ADP5600. A detailed breakdown of the HMC8108 biasing and supply circuitry is located in `receiver_front_end_overview\_&_theory_of_operation <https://wiki.analog.com/resources/eval/developer-kits/x-band-lpdbf/receiver_front_end_overview_&_theory_of_operation>`__. Below is the power tree for the biasing/supply circuits.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_biasingcircuitpowertree.png
   :width: 600px

**Figure 2: HMC8108 Biasing/Supply Circuit Power Tree**

The total power per receive channel comes out to about 718mW. The per-part power draw numbers are outlined in the power trees above. Additionally, the table below shows the power numbers per chip family on the board.

+-----------------+-------------------------------------------+-----------------------+-------------------------+
| **Part Number** | **Description**                           | **Quantity on Board** | **Estimated Power (W)** |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD9083          | 16 Channel ADC                            | 1                     | 0.989                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LTC6953         | Low-Jitter Clock Distributor              | 1                     | 2.475                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| ADF5356         | Microwave Synthesizer with Integrated VCO | 1                     | 0.8124                  |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LTC6421-20      | Dual-Pack Differential Amplifier          | 8                     | 1.92                    |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC564LC4       | Low Noise Amplifier                       | 1                     | 0.153                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD8613          | Low Noise CMOS Rail-to-Rail Op Amp        | 1                     | 0.0000684               |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| MAX5351         | 13 Bit Voltage Output DAC                 | 1                     | 0.000842                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC8108         | Down Mixer                                | 16                    | 4.8                     |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| LT6017          | Precision Op-Amp Quad Pack                | 16                    | 0.016632                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| AD9106          | 4 Channel DAC/DDS                         | 1                     | 0.315249                |
+-----------------+-------------------------------------------+-----------------------+-------------------------+
| HMC516LC5       | Low Noise Amplifier                       | 1                     | 0.195                   |
+-----------------+-------------------------------------------+-----------------------+-------------------------+

**Table 1: Consumption numbers of powered parts on Marlin tile**

Mechanical and Thermal Considerations
-------------------------------------

Stacking Considerations
~~~~~~~~~~~~~~~~~~~~~~~

In order to maintain the dual-polarization lattice spacing of 7.5 mm between on-tile HMC8108s and between tiles when stacked vertically, there are a few things that need to be considered. The parts placement in layout needs to be done so that there is no more than 7.5 mm of space between each Rx channel on tile. Additionally, part heights need to be verified to make sure that stacking is possible. The tallest component in the BOM for this design is the LTM8020 power module, coming in at 2.42mm. This ensures that the tiles can be vertically stacked with leeway.

Another stacking consideration that is made is the choice of tile-to-backplane controls/data connector. The main points of concern for this connector selection are number of positions, right angle mount, part height, and on-board termination. For this application, the `SAMTEC ERF5-RA <https://www.samtec.com/products/erf5-ra>`__ right-angle board mounted socket is ideal. This connector has a height of 4.75mm while containing 100 positions and supporting high speed applications with up to 28 Gbps performance.

The same stacking consideration has to be made for the on-tile power connector. The main points of concern for this are voltage rating (12 V), continuous current rating (1.5 A) and surge current rating (4.5 A) in addition to the aforementioned physical specs including part height, PCB mount orientation and termination method. The standard `TSM-102-01-L-SH-P-TR <https://www.samtec.com/products/tsm-102-01-l-sh-p-tr>`__ surface mount 0.1000" pitch TSM series header from SAMTEC is ideal for fitting these specifications.

Thermal Considerations
~~~~~~~~~~~~~~~~~~~~~~

A steady-state thermal simulation on ANSYS FLUENT was conducted to assess the thermal safety of the power dissipating devices in an eight-tile stackup using preliminary on-tile parts placement. A fan was applied within the simulation with a rotational speed of 3000 RPM that was positioned 200mm away from the platform and blew laterally between the tiles. The results showed that with the fan on at 3000 RPM, all devices on all eight boards are thermally safe with the exception of the LTC6953 chip on Tile 6 in the stack. The simulation result is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_overalltemp.png
   :width: 600px

**Figure 1: Overall Thermal Simulation Result for 8-Tile Stackup**

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_tile6temp.png
   :width: 600px

**Figure 2: Tile 6 Temperature Hotspot**

It is observed that on Tile 6, the junction temperature of the LTC6953 chip is 131.91 degrees Celsius, which is 1.91 degrees over the rated junction temperature of the chip. It also seems that the main hotspot of each board is centered around the LTC6953. This makes sense due to the relatively higher power consumption of this chip compared to the other chips on the board. A few potential solutions for this problem include shifting these chips closer to the middle of the board so that there is more surface area for heat dissipation or including thermal vias underneath the LTC6953 chips which may not be possible due to the stacking considerations mentioned in the previous section.

Size Information
~~~~~~~~~~~~~~~~

Following X-Band dual-polarization lattice spacing, the receive channels are spaced out at a maximum of 7.5mm away from each other. Allowing for some room on both sides of about 20mm for any other on-tile parts plus the Tx-channel, that brings the board dimension of the tile to be 160mm x 75mm x 5mm. We can extrapolate some baseline estimations for the dimensions of the backplane from this information since each tile also has to fit within the aforementioned lattice spacing when stacking vertically on top of one another. With this information, the dimensions of the backplane come out to

Bill of Materials
-----------------

The table below contains a bill of materials for the full Marlin system including 8 tiles (128Rx/8Tx) and the associated backplane.

+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| *Circuit* |   | *QTY* |   | *Device*                                                            |   | *Description*                                                                           |   | *Package*                                                      |   | *Production Status*         |
+===========+===+=======+===+=====================================================================+===+=========================================================================================+===+================================================================+===+=============================+
| Rx        |   | 8     |   | :adi:`AD9083`                                                       |   | 16 Channel, 125MHz BW, JESD204B ADC                                                     |   | 9 mm × 9 mm, 100-ball CSP_BGA                                  |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx        |   | 128   |   | :adi:`LTC6421-20`                                                   |   | Dual Matched 1.3GHz Diff Amps/ADC Drivers                                               |   | 20-Lead 3mm × 4mm × 0.75mm QFN                                 |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx        |   | 128   |   | :adi:`HMC8108`                                                      |   | 9 to 10GHz X-Band GaAs MMIC Low Noise Converter                                         |   | 32-terminal, 5 mm × 5 mm, ceramic LCC                          |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx        |   | 128   |   | :adi:`LT6017`                                                       |   | Quad 3.2MHz, 0.8V/μs Low Power, Over-The-Top Precision Op Amp                           |   | Single 5-Lead SOT-23 (ThinSOT™) Package                        |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx        |   | 128   |   | :adi:`LTC4210-1`                                                    |   | Hot Swap Controller                                                                     |   | 6-Lead SOT-23 Package                                          |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx/Tx     |   | 144   |   | `LFCN-105+ <https://www.minicircuits.com/pdfs/LFCN-105+.pdf>`__     |   | DC to 105MHz Low Pass Filter                                                            |   | 98-TRF-71                                                      |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx        |   | 128   |   | `QCV-151+ <https://www.minicircuits.com/pdfs/QCV-151+.pdf>`__       |   | LTCC 90 degree Hybrid, 90-150MHz                                                        |   | 98-PL-340                                                      |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Rx/Tx     |   | 8     |   | `ERF5-RA <https://www.samtec.com/products/erf5-ra>`__               |   | 0.50 mm Edge Rate® Rugged High Speed Terminal, Right-Angle Connector                    |   | ---                                                            |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Tx        |   | 8     |   | :adi:`AD9106`                                                       |   | Quad Low Power 12-Bit 180 MSPS DAC and Waveform Generator                               |   | 5 mm × 5 mm with 3.5 mm × 3.6 mm exposed paddle, 32-lead LFCSP |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Tx        |   | 8     |   | :adi:`HMC1056`                                                      |   | GaAs MMIC I/Q Mixer 8-12GHz                                                             |   | 20 Lead 4x4 mm SM T Package: 16 mm²                            |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Tx        |   | 8     |   | :adi:`HMC564LC4`                                                    |   | GaAs SMT pHEMT Low Noise Amplifier 7-14GHz                                              |   | RoHS Compliant 4 x 4 mm Package                                |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| Tx        |   | 16    |   | :adi:`LTC6268`                                                      |   | 4GHz Ultra Low Bias Current FET Input Op Amp                                            |   | Dual in 8-Lead MS8                                             |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| LO        |   | 1     |   | :adi:`ADF5356`                                                      |   | Microwave Wideband Synthesizer with Integrated VCO                                      |   | 32-lead, lead frame chip scale package                         |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| LO        |   | 1     |   | :adi:`HMC516LC5`                                                    |   | SMT PHEMT Low Noise Amplifier 9-18GHz                                                   |   | RoHS Compliant 5x5 mm Package                                  |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| LO        |   | 1     |   | `SEPS-8-153+ <https://www.minicircuits.com/pdfs/SEPS-8-153+.pdf>`__ |   | 8 Way-0° Power Splitter/Combiner                                                        |   | 98-RS1539                                                      |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| LO        |   | 1     |   | `EP2C+ <https://www.minicircuits.com/pdfs/EP2C+.pdf>`__             |   | 2 Ways MMIC DC Pass Power Splitter, 1800 - 12500 MHz                                    |   | 98-PL-442                                                      |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| CLK       |   | 10    |   | :adi:`LTC6953`                                                      |   | Ultralow Jitter, 4.5GHz Clock Distributor with 11 Outputs and JESD204B/JESD204C Support |   | 52-Lead Plastic QFN (7mm × 8mm)                                |   | Last Time Buy               |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+
| CLK       |   | 24    |   | :adi:`ADCLK854`                                                     |   | 1.8 V, 12-LVDS/24-CMOS Output, Low Power Clock Fanout Buffer                            |   | 48-pin LFCSP package                                           |   | Recommended for New Designs |
+-----------+---+-------+---+---------------------------------------------------------------------+---+-----------------------------------------------------------------------------------------+---+----------------------------------------------------------------+---+-----------------------------+

Questions
---------

For additional questions or support, please contact Sid Das (sid.das@analog.com) or visit the Engineering Zone forum at ` <https://ez.analog.com/adef-system-platforms/>`__.

--------------
