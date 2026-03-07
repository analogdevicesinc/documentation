Customizing the M2K configuration
=================================

If you are already on a 192.168.2.\* network
--------------------------------------------

In `RFC 1918 <https://tools.ietf.org/html/rfc1918>`_ the `Internet Engineering Task Force <http://ietf.org/>`_ has directed the `Internet Assigned Numbers Authority <https://www.iana.org/>`_ to reserve the IPv4 address range the ``192.168.*.*`` (and others) for `private networks <https://en.wikipedia.org/wiki/Private_network>`_. Analog Devices picked the ``192.168.2.*`` subnet for it's private network for host to M2K devices, but there isn't anything stopping other people (including yourself) to be running a real network on the ``192.168.2.*`` subnet.

It's a quick update to change the M2K network settings, which is described below.

Multiple devices
----------------

When using multiple M2K devices on the same host, there are a few options:

-  usb mode via libiio, no changes are required, and things will work out of the box
-  network mode, where changes to the network settings are required (more below).

In network mode, the default configuration is to have an `IP address <https://en.wikipedia.org/wiki/IP_address>`_ for the host (``192.168.2.10``), and the actual M2K device (``192.168.2.1``). As one can expect - IP addresses are expected to be unique, and the default configuration works well when you have one device, but not as well when you have multiple.

In order to use multiple devices, you must change their IP address. This is managed by updating the ``config.txt`` file on the M2K mass storage device.

.. image:: https://wiki.analog.com/_media/university/tools/adalm2000/common/win_config_file.png
   :width: 800px

::

   # Device Configuration File
   # Edit, Save and then Eject the USB Drive

   [NETWORK]
   hostname = m2k
   ipaddr = 192.168.2.1
   ipaddr_host = 192.168.2.10
   netmask = 255.255.255.0

It's a simple matter of updating the ``[NETWORK]`` settings of the M2K ``ipaddr`` (default is ``192.168.2.1``), and your host PC settings ``ipaddr_host`` (default of 192.168.2.10). ``ip_addr`` and ``ipaddr_host`` must be unique, and must be on the same subnet. Separate M2Ks on the same machine must be assigned different subnets. It's not recommended to use the real internet subnet. After saving the file back to the M2K mass storage device, simply eject (not unplug) the M2K mass storage device from your host.

Zeroconf
~~~~~~~~

There is a `Avahi <http://avahi.org/>`_ deamon running on the M2K. Avahi is a free `Zero-configuration networking <https://en.wikipedia.org/wiki/Zero-configuration_networking>`_ (zeroconf) implementation, including a system for multicast DNS/DNS-SD service discovery. If you ``hostname`` is unique and your host is zeroconf enabled, you can simply connect to your M2K using ``hostname``.local.

Config File ACTIONS
-------------------

::

   [ACTIONS]
   diagnostic_report = 0
   dfu = 0
   reset = 0

This section allows the user to perform certain ``[ACTIONS]`` The procedure is always the same. The ``config.txt`` file is edited using your favorite editor. Then the file is saved, finally the drive is ejected. (Not unplugged) After 2-3 seconds the drive reappears and may have some new file indicating some status.

Diagnostic Report
~~~~~~~~~~~~~~~~~

Setting this to ``1`` will generate a file called ``diagnostic_report``, which contains various status information about the system and the Hardware.

The information contained in this report can be used to asses and debug system problems or failures. In order to guarantee fast and precise support it is recommended to always include a diagnostic when reporting a problem.

DFU
~~~

Setting this to ``1`` will put the system into `DFU <https://en.wikipedia.org/wiki/Device_Firmware_Upgrade>`_ mode. Device Firmware Upgrade (DFU) is a vendor- and device-independent mechanism for upgrading the firmware of USB devices.

Reset
~~~~~

Setting this to ``1`` simply resets and reboots the device.

Calibrate
~~~~~~~~~

Setting this to ``1`` will calibrate the board.

~~REDIRECT>university:tools:m2k:common:customizing~~
