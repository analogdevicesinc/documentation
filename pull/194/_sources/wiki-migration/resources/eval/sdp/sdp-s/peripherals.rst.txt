SDP-S Peripherals Explained
===========================

The SDP-S’s peripherals are a subset of the SDP-B's peripherals. This document aims to outline these peripherals and their implementation on the SDP board.

TWI/I2C : TWO WIRE INTERFACE
----------------------------

| The TWI / I\ :sup:`2`\ C bus is fully compatible with the widely used I\ :sup:`2`\ C bus standard as defined by Philips I\ :sup:`2`\ C Bus Specification version 2.1.
| Pull up Resistors are required on both the SDA and SCL lines, so the lines will idle high at all times.
| Data Rates :up to 100K bits/second (Standard Mode)and up to 400K bits/second (Fast Mode)data rates

For more details on TWI/I\ :sup:`2`\ C, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-s/peripherals/twi>`!

SPI: Serial Port Interface
--------------------------

The SPI interface on the SDP-S is a full duplex, synchronous serial interface. The SDP-S is the Master for all SPI transfers. When an SPI transfer occurs, data is simultaneously transmitted as new data is received. The SPI_CLK signal synchronises the shifting of data out and the sampling of data in on the two serial data pins (MOSI and MISO).

For more details on SPI, click :doc:`here </wiki-migration/resources/eval/sdp/sdp-s/peripherals/spi>`!
