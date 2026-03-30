# Pluto Hardware

At the heart of the Pluto is the AD9363 transceiver IC. This is part of the Catalina family of direct conversion transceivers from Analog Devices.  Direct conversion means that the radio mixes the the RF signal directly up (or down) from baseband--there is no IF stage.  This means that direct conversion is generally the simplest and lowest power. 

```{image} pluto_overview.svg
:alt: Put Text Here to Describe the Image
:width: 800px
:align: center
```

Shown above is the Pluto SDR after a modification (discussed {ref}`here <pluto setup adding-a-second-rx-and-tx-channel>`) to access the second transmit and receive ports.  These ports attach directly to RF baluns, which then interface to the AD9363's Rx1/2 ADC inputs and Tx1/2 DAC outputs.  

Within the AD9363's Rx circuitry is an LNA, followed by a quadrature down-conversion mixer (RF signals are mixed with LO phases separated by 90° to produce baseband I/Q signals).  After mixing down, the receive signals pass through programmable low-pass filters and variable gain amplifiers (VGA) --both of which are accessible via Pluto's software programming API. Finally, the I and Q receive signals are independently and simultaneously digitized using 12 bit ADCs operating at up to 61.44 MSPS.  These ADC codes are transmitted to the Zynq 7010 FPGA over a CMOS digital interface.

The AD9363's transmit circuitry is largely the inverse of the Rx circuitry.  I and Q samples are sent from the Zynq FPGA to the AD9363's 61.44 MSPS 12 bit DACs.  These DAC outputs are then passed through programmable low pass filters and transmit VGAs.  Using the same LO synthesizer structure as the receiver, these baseband I/Q signals are then upconverted to the desired RF frequency.

More information, and a complete overview of the Pluto hardware, please explore this [site](https://analogdevicesinc.github.io/documentation/tools/pluto/hacking/hardware.html#pluto-hacking-hardware).







```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```

