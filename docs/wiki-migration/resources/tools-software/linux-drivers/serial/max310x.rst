MAX310x Driver
==============

Supported devices
-----------------

`MAX3107 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3107.html>`__

`MAX3108 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3108.html>`__

`MAX3109 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3109.html>`__

`MAX14830 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX14830.html>`__

Evaluation boards
-----------------

`MAX3107EVKIT <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3107EVKIT.html>`__

`MAX14830EVKIT <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX14830EVKIT.html>`__

Overview
--------

The MAX310x devices are advanced UART with 128 words each of receive and transmit FIFO that can be controlled through I²C or high-speed SPI™. Baud rates up to 24Mbps make them suitable for today’s high data rate applications.

A PLL, predivider, and fractional baud-rate generator allow high-resolution baud-rate programming and minimize the dependency of baud rate on reference clock frequency.

The `MAX3109 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3109.html>`__ is a dual-channel device, while the `MAX14830 <https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX14830.html>`__ is quad-channel.

Source Code
===========

Status
------

+----------------------------------------------------------------------------------------------------------------+------------+
| Source                                                                                                         | Mainlined? |
+================================================================================================================+============+
| `git <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/tty/serial/max310x.c>`__ | Yes        |
+----------------------------------------------------------------------------------------------------------------+------------+

Files
-----

+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function      | File                                                                                                                                                       |
+===============+============================================================================================================================================================+
| driver        | `max310x.c <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/tty/serial/max310x.c>`__                                       |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Documentation | `maxim,max310x.txt <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/devicetree/bindings/serial/maxim,max310x.txt>`__ |
+---------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example device tree

+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function | File                                                                                                                                                 |
+==========+======================================================================================================================================================+
| i2c dts  | :git-linux:`arch/arm/boot/dts/overlays/rpi-max14830-i2c-overlay.dts`                                                                                 |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| spi dts  | :git-linux:`arch/arm/boot/dts/overlays/rpi-max14830-spi-overlay.dts`                                                                                 |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Driver testing
==============

The driver exposes character devices starting with the ttyMAX name.

To connect to these devices, use a Serial Terminal Emulaor (like GTKTerm, Picocom, Minicom, Tera Term).

For example, to use Picocom to connect to UART port 0 of a MAX14830 device using a 9600 baud-rate, use the following command.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target

   
   ::
   
      picocom -b 9600 /dev/ttyMAX0
   

