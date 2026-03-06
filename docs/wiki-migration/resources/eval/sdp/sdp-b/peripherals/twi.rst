TWI/I2C : TWO WIRE INTERFACE
============================

| The TWI / I\ :sup:`2`\ C bus is fully compatible with the widely used I\ :sup:`2`\ C bus standard as defined by Philips I\ :sup:`2`\ C Bus Specification version 2.1.
| Pull up Resistors are present on both the SDA and SCL lines, so the lines will idle high at all times.
| Data Rates:up to 100K bits/second (Standard Mode)and up to 400K bits/second (Fast Mode)data rates

+-------------------+--------------------------------+-----------------------------------------------------+
| Pin Blackfin Name | Pin SDP 120 Pin Connector Name | Description                                         |
+===================+================================+=====================================================+
| SDA               | SDA_0                          | In/Out TWI serial data, high impedance reset value  |
+-------------------+--------------------------------+-----------------------------------------------------+
| SCL               | SCL_0                          | In/Out TWI serial clock, high impedance reset value |
+-------------------+--------------------------------+-----------------------------------------------------+

Table 1: I\ :sup:`2`\ C Pin Assignments

| |sdp-b_periphexpl6.png|
| Figure 1 : I\ :sup:`2`\ C Start & Stop Conditions

Normal Data Transfer
--------------------

| S = Start
| P = Stop
| ^S^7-BIT ADDRESS^R/W^ACK^8-BIT DATA^ACK^P^

Repeated Start
--------------

| A repeated start is where the control of the bus is help by the current master between two consecutive transfers. It is the absense of a stop command betwen two transfers. Transfers can be of any direction.

+---+---------------+-----+-----+------------+-----+---+---------------+-----+-----+------------+-----+---+
| S | 7-BIT ADDRESS | R/W | ACK | 8-BIT DATA | ACK | S | 7-BIT ADDRESS | R/W | ACK | 8-BIT DATA | ACK | P |
+===+===============+=====+=====+============+=====+===+===============+=====+=====+============+=====+===+
+---+---------------+-----+-----+------------+-----+---+---------------+-----+-----+------------+-----+---+

.. |sdp-b_periphexpl6.png| image:: https://wiki.analog.com/_media/resources/eval/sdp/sdp-b/sdp-b_periphexpl6.png
   :width: 500px
