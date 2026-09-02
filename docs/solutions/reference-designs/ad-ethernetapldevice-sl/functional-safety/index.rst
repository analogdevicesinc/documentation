.. _ethernet-apl functional-safety:

Functional Safety Features
==========================

Introduction
~~~~~~~~~~~~

The :adi:`AD-ETHERNETAPLDEVICE-SL` integrates safety-certified and uncertified components.
An FMEDA for the design is available in PDF format. It also uses ADI functional safety certified
components such as the :adi:`MAX42500` and :adi:`ADFS7124-4` as diagnostics to improve
systematic capability and functional safety compliance. This reference design demonstrates
how FS-certified parts can be implemented in a real system.

FMEDA Target/Requirements Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The aim of the FMEDA is to demonstrate that the hardware safety metrics,
PFDavg and SFF, can be met for low demand using the assumptions in Table 1.

.. csv-table:: Targets for Safety Function of AD-EthernetAPLDevice-SL
   :file: safety-targets.csv

.. csv-table:: General FMEDA Definitions
   :file: fmeda-definition.csv

**FMEDA and safety manuals available on request. An NDA may be required.**

Diagnostic Circuit for Safe Microcontroller and Internal Power Supplies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the functional safety circuit of AD-EthernetAPLDevice-SL, the main microcontroller MAX32690
connects its RESET pin to the MAX42500 supervisor. The supervisor monitors the voltages of the
three main supplies powering the MAX32690: 3.3V, 1.8V, and 1.1V. If any of those supplies deviates
from its nominal voltage, the supervisor triggers a reset on the microcontroller.

The MAX42500 also provides a challenge/response watchdog timer when connected to the MAX32690
over I2C. The watchdog is refreshed through the I2C interface. When configured as a challenge/
response watchdog, a key value register described in the MAX42500 datasheet must be read and used
to compute the appropriate response. The watchdog has status bits to communicate status and past
faults. Separate flags indicate an update-too-early fault, a wrong-key fault, and a no-update-
received fault. These fields are cleared when read, supporting the implementation of a simple
windowed watchdog.

The MAX42500 is an IEC 61508 SIL-3 certified four-to-seven-channel power supply monitor with a
windowed watchdog timer enabled by default. Two variants with corresponding enabled trims are shown
in Table 3. The AD-EthernetAPLDevice-SL uses the MAX42500ATEAA+T, which utilizes only three channels.

.. csv-table:: Default Voltage Monitoring Channels
   :file: voltage-monitoring.csv

The design also monitors the MAX32690 temperature using the MAX6613 small-package temperature
sensor IC. The MAX6613 is placed near the MAX32690 and senses the microcontroller temperature,
then sends the temperature reading as an analog voltage to one of the MAX32690 analog input pins.

Together, the MAX42500 supply monitor and the MAX6613 temperature monitor form the diagnostics
circuit for the MAX32690. To ensure the circuit detects a microcontroller failure, the diagnostic
components' power rail must be separate from the rails being monitored. This provides independence
between the diagnostic circuit and the microcontroller. For example, if the MAX42500 and MAX6613
require 3.3V and the microcontroller is powered by a monitored 3.3V rail, the diagnostic components
should not draw from that same monitored line. Instead, they should be supplied by a separate 3.3V
rail. Otherwise, a failure or deviation on the monitored line could cause incorrect readings or cause
the diagnostic components to fail to power up.

.. figure:: diagnostic-circuit.png
   :width: 700 px
   :alt: Diagnostic Circuit for the Microcontroller

   Diagnostic Circuit for the Microcontroller

ADFS7124-4 Diagnostic Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ADFS7124-4 is a variant of the AD7124-4, a 24-bit Sigma-Delta ADC with PGA and built-in reference,
with additional self-diagnostic features for functional safety. The ADFS7124-4 is compliant with SC3 by
TÜV Rheinland. The diagnostic functions that aid SIL certification are based on the following
features of the component:

1. ``SIGNAL CHAIN CHECK`` - ADFS7124-4 can check all voltages connected to the device.

2. ``REFERENCE DETECT`` - ADFS7124-4 includes on-chip circuitry to detect whether a valid reference
   is present for conversions or calibrations when using an external reference.

3. ``CALIBRATION, CONVERSION, AND SATURATION ERRORS`` - These diagnostics check the analog input, the
   modulator, and the digital filter during conversions or calibration.

4. ``OVERVOLTAGE/UNDERVOLTAGE DETECTION`` - The overvoltage/undervoltage monitors check the absolute
   voltage on the AINx analog input pins.

5. ``POWER SUPPLY MONITORS`` - Along with converting external voltages, the ADC can monitor the
   voltages on its analog supply pin and digital I/O supply pins.

6. ``LDO CAPACITOR DETECT`` - The analog and digital LDOs require an external decoupling capacitor of
   at least 0.1 µF. The ADFS7124-4 can check for the presence of this capacitor.

7. ``MCLK COUNTER`` - The ADFS7124-4 allows the user to monitor the controller clock. A stable controller
   clock is important because the output data rate, filter settling time, and filter notch frequencies
   depend on it.

8. ``SPI SCLK COUNTER`` - The SPI SCLK counter counts the number of SCLK pulses used in each read and
   write operation.

9. ``SPI READ/WRITE ERRORS`` - The ADFS7124-4 can check the read and write operations to ensure valid
   registers are being addressed.

10. ``CHECKSUM PROTECTION`` - A checksum ensures that only valid data is written to a register and allows
    data read from a register to be validated.

11. ``BURNOUT CURRENTS`` - The ADFS7124-4 contains two constant current generators that can be programmed
    to 0.5 µA, 2 µA, or 4 µA. Use these currents to verify that an external transducer is still operational
    before taking measurements on that channel.

12. ``TEMPERATURE SENSOR`` - The ADFS7124-4 has an embedded temperature sensor that is useful to monitor
    the die temperature of the IC.

The datasheet explains how to use all of these diagnostics. The safety manual for this part is also
available upon request.

Safety Related Data Communications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is assumed that the MAX32690 will implement an IEC 61784-3 compliant black channel protocol
with the ADIN1100 thus existing in the black channel.

System Capability
~~~~~~~~~~~~~~~~~

The MAX42500 and ADFS7124-4 are safety rated and suitable for use in applications up to SC3.

For the MAX32690 the challenge response mode of the MAX42500 gives additional confidence
and a completed IEC 61508-2:2010 table F.1 is available under NDA to support the design-in of the MAX32690.

Other components such as the ADIN1100, power limitation and regulators are covered by the
black channel safety concept for communications, are to implement diagnostics,
or are covered by the MAX42500 diagnostics.
