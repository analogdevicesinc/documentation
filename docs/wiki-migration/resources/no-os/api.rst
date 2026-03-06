no-OS API
=========

no-OS framework provides a collection of baremetal drivers and reference projects for Analog Devices parts.

The part drivers and the reference projects may be run on various platforms. In order to do so, the no-OS has a common API for doing what a part driver would typically do: initialize and control a GPIO, set up an interrupt and bind it to a callback, initialize and transfer data over SPI, UART, I2C etc. As such, the common API is used by the part drivers to be able to provide clean code that does not contain platform specific instructions.

Reference projects bind the part driver with the corresponding platform implementation by compiling them together.

The following diagram explains how the no-OS API is broken into 2 components: hardware independent utilities and peripheral drivers.

Hardware independent utilities have their .c implementation of the API in *util*.

Peripheral drivers have their .c implementation of the API in *drivers/platform*.

Some peripherals may have multiple implementations. For example, FPGA peripherals can be either implemented in hardware or as programmable logic peripherals. To be able to target either one of these implementations, a thin-layer is introduced for a subset of no-OS peripheral drivers which is able to select the peripheral implementation using platform ops. Platform ops are a collection of function pointers that are specific to the peripheral implementation. The user is responsible for specifying the platform ops when it initializes any peripheral driver listed under *drivers/api*.

.. image:: https://wiki.analog.com/_media/resources/no-os/no-os-api.png
   :align: center

no-OS peripheral driver API
---------------------------

Some no-OS peripheral drivers need to be initialized from application code directly. In order to better understand how to initialize and use no-OS peripheral drivers, here are some links to further documentation by peripheral.

-  :doc:`GPIO </wiki-migration/resources/no-os/drivers/gpio>`
-  :doc:`I2C </wiki-migration/resources/no-os/drivers/i2c>`
-  :doc:`IRQ </wiki-migration/resources/no-os/drivers/interrupt>`
-  :doc:`SPI </wiki-migration/resources/no-os/drivers/spi>`
-  :doc:`Timer </wiki-migration/resources/no-os/drivers/timer>`
-  :doc:`UART </wiki-migration/resources/no-os/drivers/uart>`
