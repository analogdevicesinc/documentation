.. _m2k intro:

Introduction to the ADALM2000
=============================

Basic Description
-----------------

To use the :adi:`ADALM2000`` Active Learning Module, you have:

* Two-channel oscilloscope with differential inputs
* Two-channel arbitrary function generator
* 16-channel digital logic analyzer (3.3V CMOS and 1.8V or 5V tolerant,
  100MS/s)
* 16-channel pattern generator (3.3V CMOS, 100MS/s)
* 16-channel virtual digital I/O
* Two input/output digital trigger signals for linking multiple instruments
  (3.3V CMOS)
* Two-channel voltmeter (AC, DC, ±25V)
* Network analyzer – Bode, Nyquist, Nichols transfer diagrams of a circuit.
  Range: 1Hz to 10MHz
* Spectrum Analyzer – power spectrum and spectral measurements (noise floor,
  SFDR, SNR, THD, etc.)
* Digital Bus Analyzers (SPI, I²C, UART, Parallel)
* Two programmable power supplies (0…+5V , 0…-5V)
* USB which for your host connectivity (used to stream data).

   * USB 2 (480 Mbits/seconds)
   * libiio USB device for communicating to the RF device
   * Network device

      * `Remote Network Driver Interface Specification (RNDIS) <https://en.wikipedia.org/wiki/RNDIS>`__
      * This will enumerate with the 192.168.2.1 IP address by default.

   * USB serial device

      * provides access to the Linux console on the M2K device via `USB Communication Device Class Abstract Control Model (USB CDC ACM) <https://en.wikipedia.org/wiki/USB_communications_device_class>`__ specification

   * Mass Storage Device : this will appear to the host as a disk, where you can find links for software uploads, and the serial number of the device.

* External Power

   * The equipment shall be powered by SELV with limited energy according to IEC 61010-1cl.9.4 or LPS/PS2 power source according to IEC 60950-1 / IEC 62368-1.
   * An example external adapter (like `this one from Adafruit <https://www.adafruit.com/product/1995?gclid=CjwKEAjwjqO_BRDribyJpc_mzHgSJABdnsFWlRs2FrqbAVZt9erVQDN6LakvKxmYjiLjTHKe_7ZqVxoCPu3w_wcB>`__).

* The device digital input/output is SELV compliant and less than 5 V and 5 A
* Environmental Conditions

   * Indoor use only
   * Operating Temperature @25C Ambient
   * Relative Humidity – 50%


Block Diagram
-------------

.. image:: ./images/block_m2k.png
   :align: center
   :width: 600px

Pinout
------

.. image:: ./images/adalm2000_pinout.png
   :align: center
   :width: 600px

.. image:: ./images/adalm2000-pin-wires.png
   :align: center
   :width: 600px
