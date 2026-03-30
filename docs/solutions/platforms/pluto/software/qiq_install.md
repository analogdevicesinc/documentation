# QIQ Systems Installation and Examples

[QIQ Systems](https://qiqsystems.com/) software comprises a suite of powerful applications for a variety of Analog Devices transceivers and high speed data converters.  This software is used in a variety of debug and prototyping use cases.  And also provides complete VSA (vector signal analyzer) and VSG (vector signal generator) functionality.

```{image} resources/qiq1.svg
:width: 300px
:align: right
```  

The QIQ software is offered as a subscription license.  However, as a courtesy to the educational and hobbyist community, QIQ Systems often makes the Pluto plugs available at no cost.  This provides a compelling, professional environment to explore signal modulations and their impact on EVM.  In particular, there are three QIQ applications that are very valuable to pair with the PlutoSDR:
1. [QIQ Generator](https://qiqsystems.com/products/qiq-generator/):
   - Waveform synthesis -- make the IQ data
   - Output to file or output directly to Pluto's transmitter
   - Equivalent to a VSG (vector signal generator)
2. [QIQ Receiver](https://qiqsystems.com/products/qiq-receiver/):
   - Receive, demodulate, and measure waveforms
   - Takes input from a file, or acquires directly from Pluto's receiver
   - Equivalent to a VSA (vector signal analyzer)
3. [QIQ Transceiver](https://qiqsystems.com/products/qiq-transceiver/):
   - Transmit, receive, demodulate and measure waveforms all from one PlutoSDR
   - Use Pluto to transmit a waveform created in QIQ Generator
   - Receive (loopback) that waveform the same Pluto
   - Same analysis types as qIQ Receiver
   - Allows signal modifications for transmit and receive


```{image} resources/qiq2.svg
:width: 600px
:align: center
```  


Installation is very straightforward -- simply download the application's "msi" file from the links above and follow the install guide.  When asked for the license code, hit cancel (no code is necessary if only using PlutoSDR).  

A comprehensive video on using QIQ Transceiver with Pluto is available here:

```{video} https://www.youtube.com/watch?v=kiN-ZRU2PeY
:align: left
```

```{clear-content}
```
```{note}
For questions or help with the Pluto SDR, please visit:
{ez}`adieducation/university-program`
```
