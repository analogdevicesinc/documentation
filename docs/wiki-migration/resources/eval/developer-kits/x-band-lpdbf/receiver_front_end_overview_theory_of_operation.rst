Receiver Front End Overview & Theory Of Operation
=================================================

The Marlin receive front-end block diagram is shown below.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_rxblockdiagram.png
   :width: 600px

**Figure 1: Full receive front-end block diagram**

The 3D directivity pattern generated using the MATLAB Sensor Array Analyzer is shown below. 8 by 16 elements spaced half wavelengths from each other with a rectangular lattice structure were the settings used for array geometry. For the isotropic antenna settings, propagation speed of 3e8 m/s and 10 GHz signal frequency were set. The antenna was back baffled to ensure the response was limited to azimuth angles between -90 and 90 degrees.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_beampattern.png
   :width: 600px

**Figure 2: 3D Directivity Pattern**

The system G/T value was found to be -4.3 dB, assuming 67% antenna aperture efficiency.

HMC8108
-------

The first step of the RxFE chain is the :adi:`HMC8108`. This is an X-Band low noise converter that contains a low noise amplifier followed by an image reject mixer that is driven by an active LO amplifier. This component takes in a radio frequency input (RFIn) signal of 9-10GHz, which is consistent with the target frequency range of the Marlin platform (X-Band). This signal is mixed with an external local oscillator signal that is in the range of 9.1-10.1GHz, thereby generating a single-ended intermediate frequency (IF) output of 90-110MHz. The gain of this stage is typically 13dB with a noise figure of around 2dB when operating at 90-110MHz IF frequencies. The plot below shows the spurious performance of the HMC8108 with the desired RF and IF center frequencies and bandwidths. This plot was generated using the WhatIF Frequency planner.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_whatif.png
   :width: 600px

**Figure 3: Spurious Performance of IFs at HMC8108 Mixer output**

The :adi:`HMC8108` is a very low power consuming part for what it does; however, that does come with some external circuitry needed. The biasing sequence (on page 15 of the part datasheet) is used to avoid damage to the transistors that are part of the active amplifier and local oscillator buffer stages. This sequence can either be done utilizing several power supplies on a lab bench, or through a biasing and supply circuitry on-board. The latter option is what we designed for in this platform. The biasing circuitry is centered around the :adi:`LT6017` quad-pack op-amp, which biases the LNA_VG1, LNA_VG2, and BUFF_VG pins on the :adi:`HMC8108`. The biasing circuit can be shown below. The :adi:`LT6015` op-amps are all part of the quad-pack in the :adi:`LT6017`, which is why they are placed separately in the LTSpice schematic for clarity purposes.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_hmc8108biasingcircuit.png
   :width: 600px

**Figure 4: HMC8108 gate biasing circuitry**

The supply circuit utilizes the :adi:`LTC4210-1`, which is a hot swap controller that is used to slowly ramp up the supply voltage of the mixer. This helps to accomplish the first 2 out of 8 steps in the :adi:`HMC8108` biasing sequence. The schematic for the supply circuit is shown below, as well as a table with some important specifications of the circuit. The Vdd output of the supply circuit corresponds with the Vdd inputs of the gate biasing circuits in Figure 3.

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
--------

Since the :adi:`HMC8108` has an internal 90-degree hybrid, an external 90-degree hybrid is necessary at the intermediate frequency (IF) output of the mixer to convert back to a single ended signal. The way this is achieved is by feeding the hybrid coupler with the differential signal output of the mixer and grounding the 90-degree phase shifted output. That way, the signal coming out of the 0-degree phase shifted output is used as the single=ended IF signal in the rest of the RxFE signal chain. The `QCV-151+ <https://www.minicircuits.com/pdfs/QCV-151+.pdf>`__ has a very low insertion loss of 0.4 dB and high isolation of 20dB between 90-118 MHz, making it ideal for this platform considering that the IF signal is ranging between 90-105 MHz.

LFCN-105+
---------

The desired IF range is 90 to 105MHz; therefore, our desired signal should be noise-free around that frequency range. In order to filter out all noise or excess signal above that frequency, we implement the `LFCN-105+ <https://www.minicircuits.com/pdfs/LFCN-105+.pdf>`__ low pass filter. This filter has a 1dB insertion loss from DC-105 MHz and a 25-55 dB insertion loss between 1-5 GHz. This will allow for appropriate filtering of all the unwanted signal above 105 MHz. A possible alternative is to use a bandpass filter so the spurious noise below 37.5MHz that is shown in Figure 3 can also be filtered out. For example, the `RBP-98+ <https://www.mouser.com/datasheet/2/1030/RBP_98_2b-1700954.pdf>`__ has a high insertion loss (44-97 dB) between DC-45 MHz, which is ideal considering the spurs occurred under 37.5 MHz. Additionally, the insertion loss between 75-103 MHz ranges between 1.65-2.29dB, which is only slightly higher than that of the LFCN-105+ around those frequencies. However, a bandpass filter was not chosen due to the much larger board footprint necessary as well as power consumption considerations.

A measured plot of the S parameters for this part is shown below. The target operation band (80-105 MHz) is highlighted on the left and the alias band (1895-1920 MHz) is highlighted on the right.

.. image:: https://wiki.analog.com/_media/resources/eval/developer-kits/x-band-lpdbf/02_077511a_lfcn105p_sparams.png
   :width: 600px

**Figure 7: Plot of S parameters of LFCN-105+ from measured data**

LTC6421-20
----------

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
-------------------

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
