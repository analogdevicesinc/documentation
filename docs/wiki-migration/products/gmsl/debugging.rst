General Debugging Procedures
============================

Every GMSL device is slightly different but the debugging techniques can be applied across the product lines.

For more specific debugging techniques, refer to the technology specific guides:

-  :doc:`Camera Debugging </wiki-migration/products/gmsl/debugging/camera>`
-  :doc:`Display Debugging </wiki-migration/products/gmsl/debugging/display>`

Do You Have LOCK?
=================

Confirm that the GMSL link has LOCK. Link lock, or LOCK, indicates the GMSL PHYs are locked in both forward and reverse channels. LOCK will happen automatically without any interaction with the GMSL devices.

LOCK can be seen on the EV kits or via reading a register.

.. note::

   The lock sequence is initiated by the release of the PWDNB pin or the RESET_LINK bit in either the serializer or the deserializer.


Without having LOCK, something fundamental with the GMSL devices is not correct.

Connectors and Cables
---------------------

Not all connectors are rated for multiple insertions and can wear out over time. Cables can also wear out due to temperature or age. Ensure the connector is making good contact with mating connector and inspect for any signs or wear or even cold solder joints.

.. tip::

   Try replacing an older cable with a new cable that may not be as worn out.


Power Rails
-----------

Ensure all the rails are stable and within regulation.

GMSL Signal Polarity
--------------------

GMSL physical layer signals can't be swapped in the IC. Confirm the schematic symbol with the datasheet and Ohm out the cable connections if needed.

External Crystal/Oscillator Stability
-------------------------------------

Confirm that the 25MHz signal feeding the device is stable, jitter free, and clean clock edges.

GMSL Variant Differences
------------------------

Many GMSL parts have multiple variants with different feature sets. One example is the "F" and "non-F" variants of the camera/sensor devices where they operate at 6Gbps and 3Gbps respectively. A GMSL 6Gbps part can't communicate to a 3Gbps part. This is a common issue with EV kits when different variants are ordered for the same project.

Configuration Pins
------------------

One of the most common problems is the parts not booting up in the intended configuration. If a single EV kit is being used for different applications, ensure the EV kit matches the intended configuration.

When a SerDes device is on a board, ensure the CFG pin voltages match the intended configuration. There are two main issues to keep in mind. If the CFG pins are used for another function after boot up, ensure there is no noise or glitching on the CFG pin. If possible, have the processor connected to the pin keep it in Hi-Z until the GMSL device is operational. A second issue is that the CFG pins are referenced to a voltage different than VDDIO. This can happen if the device is discretely connected to a power rail instead of the specific VDDIO rail.

Configuration Pin Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Common bootstrap configuration settings include:

-  Cable type selection of coax or STP which controls the GMSL signal drive level
-  I2C address
-  Communication interface of I2C or UART
-  GMSL TX/RX speed of 3/6/12 Gbps

Silicon Revision and Errata
---------------------------

It is always important to confirm what silicon revision is being used and if any errata needs to be implemented on the specific revision.

Additional Support
------------------

If you've gone through all the general debugging techniques and still having issues, please reach out to `Create a Technical Support Case <https://support.analog.com/en-US/technical-support/create-case-techsupport/>`__ and provide all the debugging information you've collected.
