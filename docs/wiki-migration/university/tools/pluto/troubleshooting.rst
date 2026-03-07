ADALM-PLUTO Troubleshooting
===========================

Here are some common solutions to problems users run into when setting up or using PlutoSDR. If you issue is not address please create a post in the :ez:`Virtual Classroom subforum <university-program>`. Search in the EngineerZone forums is also a great resource.

Please make sure you are using the latest firmware, drivers, and interface libraries when possible. Everything gets updated regularly to fix bugs and add features. Here are some useful links for reference:

-  `Main PlutoSDR documentation <https://wiki.analog.com/plutosdr>`_
-  :doc:`Quickstart </wiki-migration/university/tools/pluto/users/quick_start>`

Pluto Cannot be found
---------------------

**Problem**: PlutoSDR cannot be address from a specific application or the terminal

**Solution**: Usually the issue related to not having the necessary drivers or tools installed. Follow these steps to check connectivity:

-  Install :git-libiio:`libIIO <releases>`
-  **Linux only if libIIO installed from package manager:** Install `libiio-utils <https://packages.ubuntu.com/xenial/libs/libiio-utils>`_
-  **Windows Only:** :git-plutosdr-m2k-drivers-win:`Install Pluto driver <releases>`
-  Unplug Pluto
-  Reboot machine
-  Plugin Pluto
-  From a terminal/command-prompt run "iio_info -s", which should return something similar to:``tcollins@winston:/tmp$ iio_info -s
   Library version: 0.15 (git tag: v0.15)
   Compiled with backends: xml ip usb
   Available contexts:
       0: 0456:b673 (Analog Devices Inc. PlutoSDR (ADALM-PLUTO)), serial=10440004278a0007f9fblahce8fedd622 [usb:20.2.5]``

Now you should be able to access the device in your development application.

Firmware Update Doesn't Update Firmware
---------------------------------------

**Problem:** After updating PlutoSDR's firmware in the traditional methods and rebooting the device the firmware version remains the same.

**Solution:** Flash is in protected mode, which usually happens when users are modifying the HDL or u-boot. To fix a user needs to

-  Access PlutoSDR's UART through a JTAG connection
-  While the system boots conterminously press CTRL-C.
-  At the u-boot prompt enter:``sf probe && sf protect unlock 0 100000 && sf protect lock 0 100000``

Now flash is unlocked and the board can be updated.

Pluto Reboots Randomly
----------------------

**Problem**: When using PlutoSDR the device seems to disconnect randomly. When plugging the device in it appears correctly in hardware manager or dmesg, and through **iio_info**.

**Solution**: The likely problem here is that the USB port from the host PC is not providing enough power. To fix this, plug in both USB ports. The second port (power only port) can be either connected to the same machine, another machine, or external supply.

With "real" signals the receive data modulates (goes crazy) undesirably
-----------------------------------------------------------------------

See article here: :doc:`/wiki-migration/university/tools/pluto/users/non_quad`
