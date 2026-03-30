# Details of the RF Board

This section will provide a deeper look at the major sections of the RF Board:

1.  Receive antenna
2.  Beamformers
3.  Local Oscillator Synthesizer
4.  Mixers and Filtering
5.  Transmitter Signal paths
6.  Power Architecture

This video will also walk through much of the same material:

```{video} https://www.youtube.com/watch?v=-Vqbgf0MjPk
:align: left
```
```{clear-content}
```

<div style="clear: both;"></div> <!-- Ensures clean section break -->

***

## Receive Antenna

The receive antenna consists of a total of 32 antenna patches. However, each column of 4 patches are summed equally via printed circuit board (PCB) trace Wilkinson splitters. This yields 8 effective antenna elements. 

```{image} AntennaColumn.svg
:alt: Summation of 4 Antenna Elements
:width: 300px
```


```{image} RxAntenna.svg
:alt: Receive Antenna
:width: 400px
```

Each of these combined group of 4 elements will have a higher gain, and narrower beam, than any one individual antenna patch. Also built into the antenna is a quarter-wavelength shorting stub to provide some electrostatic discharge (ESD) protection. Each element is AC coupled, via 10 nF capacitors, to the 24 dB gain ADL8107 low noise amplifier. The LNAs increase the sensitivity of the array, providing a sharp beam pattern even with low power microwave sources.

```{image} AntennaGain.svg
:alt: Antenna Gain
:width: 300px
```

This graph shows the typical built in receive antenna gain vs. frequency. The -3 dB bandwidth is about 9.9 to 10.8 GHz.

The 32 patch board antenna can be bypassed by connecting an 8 element external antenna to the optional subminiature push-on (SMP) connectors. If doing this, the 10nF capacitor must also be rotated to connect to the SMP, and disconnected from the built in receive array. For additional isolation, it is recommended to cover the built in receive array with aluminum tape when using the external antennas.


***
## Beamformers

At the center of the RF board is a pair of ADAR1000 4-channel, 8 GHz to 16 GHz, beamforming ICs. The ADAR1000 allows per-channel, 360° phase adjustment with 2.8° resolution, and 31 dB gain adjustment with 0.5 dB resolution. The two ADAR1000s are capable of bidirectional, half-duplex operation; however, the CN0566 only connects the ADAR1000 receive paths. The outputs of the ADL8107 LNAs are phase and amplitude shifted by an ADAR1000, and then summed together at its RFIO output as shown below.

```{image} ADAR1000.svg
:alt: Antenna Gain
:width: 600px
```

***
## Local Oscillator Synthesizer

The ADF4159 phase-locked loop (PLL) and the HMC735 voltage-controlled oscillator (VCO) combine to form a frequency synthesizer with a range of 10.5 GHz to 12.7 GHz as shown below. This signal is used to drive the LO port of all the mixers. For communications and other fixed-frequency applications, the LO frequency is typically set to 2.2 GHz above the desired signal at the antenna. Therefore, the LO is generally between 12.2 GHz and 12.7 GHz. The ADF4159 is also capable of generating FMCW ramps or "chirps" for radar applications. The ADF4159 includes a variety of chirp ramp rates and shapes including sawtooth, triangular, and parabolic.

```{image} synth.svg
:alt: LO Generation
:width: 600px
```

Alternatively, the on-board synthesizer can be disabled, and an external LO can be applied to the LO input SMA connector. This allows the Phaser to be synchronized to an external radio, or several Phaser boards to be synchronized to a single LO. Whether generated on-board or externally, the local oscillator is split using monolithic microwave integrated circuit (MMIC) splitter or combiners to the two receive mixers, and to either the on-board transmit path or to an LO output port.

***

## Mixers and Filtering

The RFIO output of the ADAR1000 passes through a 10.6 GHz low pass filter and then enters the RF port of the LTC5548 mixer.

```{image} mixers.svg
:alt: Mixers
:width: 500px
```

The low pass filter removes the high-side image of the mixer (which in the figure above will appear at 12.2 GHz + 2.2 GHz = 14.4 GHz) as well as any reradiation of the LO (12.2 GHz). The LTC5548 mixer outputs an IF of 2.2 GHz, which is filtered by a 2.5 GHz low pass filter.

Figure 11 shows the measured results of the receive signal path (ADL8107 + ADAR1000 + 10.62 GHz low pass filter + LTC5548 + 2.5 GHz low pass filter). This is for an LO of 12.2 GHz, antenna input of 10 GHz, and an IF of 2.2 GHz. Note that the 12.2 GHz and the 14.4 GHz will be further attenuated by the input bandwidth of the PlutoSDR, resulting in an SFDR of approximately 56 dBc as shown by markers M1 to M4 (-23 dBm + 79 dBm = 56 dBc).

```{image} SFDR_Rx1.svg
:alt: SFDR of Rx1
:width: 600px
```

***
## Transmitter Signal Path

While the beamforming section of the Phaser is receive only, a transmit output is provided for driving an external antenna. For antenna pattern measurements, the antenna can be positioned facing the array at various angles. The frequency of the transmit is known exactly as it is derived from the on-board LO, simplifying digital signal processing. The transmitter can also be used to illuminate a target scene when the CN0566 is used in Doppler and FMCW radar applications.

As shown below, the transmitter signal path starts with the transmit input SMA connector.  It is then mixed up, filtered, amplified, and finally output to a separate transmit antenna through the two transmit output SMA connectors, TX1 and TX2.

```{image} transmit.svg
:alt: Transmit Signal Path
:width: 600px
```

The transmit input is generally the same frequency as the receive IF, which is about 2.2 GHz. This transmit input can either be a continuous wave, modulated communications, or radar signal. Since the output of many SDRs (including that of the PlutoSDR) use a square wave LO, it produces harmonics of the LO frequency. Therefore, the transmit input signal must first pass through a low pass filter. 

After passing through the 2.5 GHz low pass filter, the signal is then fed onto the IF of the LTC5548 mixer and upconverted to 10 GHz.  This is then filtered by a 10.6 GHz low pass filter, and amplified by an ADL8107 24 dB LNA, and finally bandpass filtered by a 9.7 GHz to 11.95 GHz filter.  The final output tone is shown below:

```{image} TxSFDR.svg
:alt: Transmit Output SFDR
:width: 600px
```

***
## Power Architecture

The Phaser derives power directly from a single USB-C receptacle that provides 5 V, 3 A power. This is forwarded to the Raspberry Pi through the 40-pin expansion header, as well as the rest of the on-board power management. 

```{image} power_tree.svg
:alt: Power Tree
:width: 600px
```

The LTC4217 integrated hot swap controller allows the CN0566 to be safely inserted and removed by limiting the amount of inrush current to the load supply during power-up, and provides a convenient means of measuring the board's power consumption via the IMON output.

The LT8609S is a monolithic constant frequency current-mode step-down DC/DC converter. This device steps down the 5 V input voltage to 3.3 V. This output is then fed into the ADP7158 LDO, which powers the beamformers, LNA, mixers, switches, and ADC at 3.3 V.

The ADM7150 LDO provides the 1.8 V analog supply rail for the digital-level translators and ADF4159.

The ADM7170 is a low quiescent current, low dropout linear regulator that powers the HMC735 VCO. This high output current LDO is ideal for regulation in noise-sensitive applications such as ADC and DAC circuits, precision amplifiers, PLLs/VCOs, and clocking ICs.

The LT3460 step-up DC/DC converter and ADP7118 LDO boost the 5 V input voltage to 15 V, then regulate to 14 V, which is used as the supply of the AD8065 amplifier. It uses a constant frequency, current-mode control scheme to provide line and load regulation. The ADP7118 is a CMOS, low dropout linear regulator that provides high power supply rejection, minimizing synthesizer phase noise.




<div style="clear: both;"></div> <!-- Ensures clean section break -->

```{note}
For questions or help with the Phaser, please visit:
{ez}`adieducation/university-program`
```






