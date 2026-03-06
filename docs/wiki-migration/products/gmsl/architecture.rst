Architecture Design Considerations
==================================

GMSL, and SerDes devices in general, requires coordination of the serial link configuration on both ends of the link. Some settings can be changed via software after boot up but PHY level configuration such as GMSL speed or cable type needs to be agreed upon in the beginning.

GMSL from a System Perspective
------------------------------

Since GMSL connects to another system outside of the PCB it's on, there are a handful of factors to consider on your GMSL design.

Physical Placement
~~~~~~~~~~~~~~~~~~

GMSL devices sit in between the main processor and a connector out of the board. It is likely the processor and connector placement are fixed for a variety of reasons. Due to this, the GMSL device needs to sit between the PHY interface on the SoC and the connector. The PHY interface is typically a handful of differential signals that require length matching, controlled impedance, and a good chunk of board real-estate.

On the other side, the GMSL PHY to connector routing requires even more care with the trace. This is also a controlled impedance trace but moving at a higher frequency than the processor PHY interface. GMSL also has the :adi:`GMSL2 Channel Specification <media/en/technical-documentation/user-guides/gmsl2-channel-specification-user-guide.pdf>` which outlines the RF requirements for a robust link to operate over the lifetime of the design. These requirements include insertion/return losses, link margin, crosstalk, etc.

.. note::

   The question then becomes which design consideration to prioritize: processor PHY interface routing or GMSL PHY to connector routing.


Power
-----

Most GMSL devices share the same core rail names like VDD, VDDIO, VDD18, etc. The datasheet explicitly outlines the decoupling capacitor requirements for each rail.

.. tip::

   A minimum of 10uF bulk capacitance is needed for most rails. Consider where the power supply is located to help meet this requirement, is the supply right next to the GMSL device or on the other side of the board. If it's right next to the device, the output rail bulk capacitance could be sufficient to meet this requirement.


The VDD rail can accept 1.0V to 1.2V as the core supply but internally regulates down to 1.0V if necessary. CAP_VDD is the decoupling capacitor pin for the core supply.

.. important::

   Some older GMSL devices only accept 1.0V OR 1.2V so please always double check the datasheet.


The VDDIO rail can support 1.8V to 3.3V. This rail is used for the peripheral interface operating voltage but also the configuration pin voltage.

.. tip::

   In the schematics, it is highly recommended to have all the GMSL interfaces connect to a "VDDIO" rail rather than a discrete 1.8V or 3.3V. This is because IO voltage could change and naming the local VDDIO rail "VDDIO" ensures the devices will always reference the same VDDIO.


For some of the bigger GMSL devices, there are multiples of the power pins and each pin has local capacitor requirements.

.. important::

   Coordinate the pin requirements between schematics and layout. Avoid lumping all the capacitance together and neglecting the power distribution. Schematic notes can help be a reminder.


Configuration Pins
------------------

The configuration, config, or CFG pins help to bootstrap the GMSL configuration at startup therefore it is crucial to treat these pins with care. If not handled properly, you may end up :doc:`debugging configuration pins </wiki-migration/products/gmsl/debugging>`.

On the EV kits, they can be :doc:`configured in the GUI </wiki-migration/products/gmsl/gui/tools/set_cfg_pin_levels>` but in end applications, the CFG pins are set with a resistor divider and voltage percentage of VDDIO.

| Below is an excerpt from the MAX96717 datasheet for the settings of CFG0 and CFG1. |image1|
| |image2|

You can see important system details like cable type, GMSL speed, I2C address, etc. These settings need to be coordinated for both sides of the link and ensure the devices are booting correctly for communication.

.. warning::

   If certain settings are not matching, the devices may not be able sending data correctly or may not even be able communicate at all.


Multi-Function Pins (MFPs)
--------------------------

Multi-Function Pins (MFPs) allow for customization the reverse channel communication interfaces. Each GMSL device has slightly different pinout configurations so please ensure to check each device's capabilities.

Multi-Function Pins are exactly that, pins with multiple functions. Each MFP has a default feature after reset. To be able to use any of the non-default features requires some software configuration and coordination.

Below is an excerpt from the MAX96717 datasheet for the MFP Pin Function Map.


|image3|

Pin Selection Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^

Since every device has a finite number of MFPs and each MFP can be multiple functions, time should be taken to plan out which features will go on which pins.

Referring to the excerpt above, we can work through the table of pins to prioritize.

-  CFG pins (MFP1 and MFP2): CFG pins latch the voltage on power-up and should be saved for last.
-  Main Control Channel (MFP9 and MFP10): This is the main control interface and typically used for the primary communication channel.
-  LOCK/ERRB (MFP3): The ERRB pin is typically connected to a processor's interrupt pin for indication of errors on the camera deserializer side.
-  Interfaces with multiple pins: SPI, UART, and I2C interfaces span across multiple pins so ensure all pins are available for the interface.

After those, it becomes application dependent as to what else make be needed.

.. important::

   When using the non-default MFP features, the device must be configured in software to enable those features. The details must be communicated to the software or systems lead.


GMSL GPIOs
----------

All MFPs can provide GPIO capabilities that need to be configured but they are highly flexible to support different system requirements. GPIOs do have internal (but weak) pull-up/down resistors and stronger external resistors are recommended. GMSL GPIOs are not high power and require a driver outside of logic levels.

.. tip::

   It's helpful to be very specific in the schematics when naming the GPIO nets to ensure the functionality aligns with the intended configuration.


GPIOs can also be remapped or rerouted internally to the GMSL device by utilizing the TX/RX IDs in the GPIO configuration.

By default: ``MFP0 = GPIO0`` and ``TX_ID = RX_ID = 0``

The TX and RX IDs must match to properly route the GPIO signal. GPIO reassignment is usually needed for most applications that utilize multiple MFP features.

Communication Channel
---------------------

Outside of the main control channel functionality, there are other features to enable flexible system architectures.

Pass-Through Channel
^^^^^^^^^^^^^^^^^^^^

The pass-through I2C/UART channels are independent of the main I2C/UART control channel. The pass-through channels provide a direct connection to remote I2C/UART peripherals but do not provide any access to internal GMSL2 device registers (except GMSL2 CSI-2 Quad Deserializers).

The pass-through I2C channels provide a connection to a remote I2C port without the GMSL2 devices’ internal I2C register subordinates hanging off the bus. This provides a mechanism to separate I2C channels and avoid multi-main conflicts.

The pass-through UART channels provide a direct point-to-point connection to the remote UART peripheral without necessitating UART Bypass Mode (as required by the main UART CC).

I2C Address Reassignment
^^^^^^^^^^^^^^^^^^^^^^^^

All GMSL I2C addresses can be changed after initialization. In multi camera or multi sensor applications, address reassignment should be used to avoid address conflicts and data collisions.

I2C Broadcasting
^^^^^^^^^^^^^^^^

I2C broadcasting can be used to simplify programming in GMSL2 systems consisting of a deserializer connected to two identical camera modules. I2C broadcasting enables the deserializer to configure the connected camera modules as a group to identical settings. The deserializer uses the I2C address of the image sensors assigned at power-up and the I2C address of the serializers assigned through I2C address translation as the broadcasting address.

I2C Address Translation
^^^^^^^^^^^^^^^^^^^^^^^

Address translation is a function in I2C mode that enables mapping one device address to a virtual device address. In GMSL2 serial link systems, two separate device addresses can be translated to another two separate device address. This function is used when two identical modules with the same device address are used within the same system. Address translation allows the host µC to separately access different devices and peripherals with the same device address through software configuration.

GMSL PHY
--------

The GMSL PHY is the interface to the world outside of the module through a connector. It can support either coax (single-ended) or STP (differential) configurations. Link isolation capacitors are required to protect the PHY.

For coax applications, the pin not carrying the GMSL signal must be terminated with a 49.9Ω resistor. Coax also allows for power over coax (PoC) and the implementation details are outlines in the :adi:`GMSL2 Hardware Design Guide <media/en/technical-documentation/user-guides/gmsl2-hardware-design-guide.pdf>`.

The GMSL devices do offer ESD protection but if additional protection is needed, please refer to the the :adi:`GMSL2 Hardware Design Guide <media/en/technical-documentation/user-guides/gmsl2-hardware-design-guide.pdf>`.

Additional Pins
===============

Power-Down "Bar" (PWDNB)
------------------------

The GMSL device is in power-down mode when the PWDNB pin is low.

.. important::

   If PWDNB is low, the device will not turn on. It is recommended to have a pull-up resistor on this pin to ensure the device boots up. If no pull-up is there, the application will be dependent on software asserting this signal for the GMSL device to turn on.


Exposed Pad (EP)
----------------

The EP is the main slug on the bottom of the device. It is needed for both a low impendence return for ground and for thermal dissipation. The exposed pad of the package must be connected to the PCB ground plane by an array of vias. This approach simultaneously provides the lowest electrical and thermal impedances.

Camera/Sensor Specific
======================

MIPI-CSI2 PHY Lane Mapping
--------------------------

To help alleviate layout and routing complexities, each MIPI port can reassign and remap the active lanes of the port. Clock lanes are fixed and can't be remapped. Additionally, each data and clock lane supports polarity inversion allowing swapping "P" and "N" signals on the MIPI port.

Tunnel/Pixel Mode
-----------------

Prior GMSL2 solutions supported only Pixel mode for transporting received data from a MIPI CSI-2 interface over the GMSL link. In Pixel mode, the CSI-2 data is depacketized at the serializer's CSI-2 input interface. The received CSI-2 packet header includes an error correction code (ECC), which is checked and removed at the serializer input. The received CSI-2 packet footer contains the CSI-2 cyclic redundancy check (CRC), which is also checked and removed.

In Tunneling mode, the received CSI-2 ECC byte and CRC bytes are checked at the serializer input. These, as well as routing and pixel data, are received as a byte stream. The byte stream is split into smaller packets that are encapsulated using GMSL2 protocol. Tunneling mode is more bandwidth-efficient if multiple data types are being sent. Because data received at the serializer input and data output from the deserializer are verified to be identical.

Reference Clock over Reverse (ROR)
----------------------------------

Newer GMSL devices supports the generation of the reference clock for the device using the reverse-channel data stream. This eliminates the need for a local 25MHz crystal in each sensor. A phase-locked loop is used to synchronize the serializer's reference clock to the reference clock in the deserializer. This eliminates the need for a local crystal and synchronizes the timing for all devices using the serializer's reference clock output.

 

.. |image1| image:: https://wiki.analog.com/_media/products/gmsl/cfg_example.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/products/gmsl/cfg1_example.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/products/gmsl/mfp_map.png
   :width: 600px
