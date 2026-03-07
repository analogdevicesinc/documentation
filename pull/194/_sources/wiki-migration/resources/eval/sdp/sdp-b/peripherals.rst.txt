SDP-B Peripheral Interfaces
===========================

| The SDP’s peripherals are a subset of the Blackfin BF527's available peripherals. This document aims to outline these peripherals and their implementation on the SDP board. For further details on any of these peripheral interfaces, consult the Blackfin Hardware Reference Manual.

SPORT: Synchronous Serial Peripheral Port
-----------------------------------------

Sport interface supports a variety of serial data communication protocols. Key features and capability of SPORT interface are

-  Continuously running clock
-  Serial data words from 3 to 32 bits in lengths, either MSB or LSB first
-  Two synchronous transmit and two synchronous receive data signals and buffers to double the total supported data stream
-  Configurable frame synchronisation signals

For more details on SPORT, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-b/peripherals/sport>`!

TWI/I2C : TWO WIRE INTERFACE
----------------------------

| The TWI / I\ :sup:`2`\ C bus is fully compatible with the widely used I\ :sup:`2`\ C bus standard as defined by Philips I\ :sup:`2`\ C Bus Specification version 2.1.
| Pull up Resistors are required on both the SDA and SCL lines, so the lines will idle high at all times.
| Data Rates :up to 100K bits/second (Standard Mode)and up to 400K bits/second (Fast Mode)data rates

For more details on TWI/I\ :sup:`2`\ C, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-b/peripherals/twi>`!

SPI: Serial Port Interface
--------------------------

The SPI interface on the SDP is a full duplex, synchronous serial interface. The SDP is the Master for all SPI transfers. When an SPI transfer occurs, data is simultaneously transmitted as new data is received. The SPI_CLK signal synchronises the shifting of data out and the sampling of data in on the two serial data pins (MOSI and MISO).

For more details on SPI, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-b/peripherals/spi>`!

PPI: Parallel Peripheral Interface
----------------------------------

| PPI is a half-duplex, bi-directional port accommodating up to 16 bits of data. It has a dedicated clock pin and three multiplexed frame sync pins. PPI supports up to 16 bits of data with programmable clock and frame sync polarities. PPI requires an externally generated free running clock.
| The maximum PPI Clock Frequency achievable on the SDP for a single frame transfer is 50MHz. The maximum transfer rate on SDP for streaming data over the PPI is achievable by using a 20-25 MHz PPI clock.

For more details on PPI, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-b/peripherals/ppi>`!
