Customizing the Pluto configuration
===================================

If you are already on a 192.168.2.\* network
--------------------------------------------

In `RFC 1918 <https://tools.ietf.org/html/rfc1918>`_ the `Internet Engineering Task Force <http://ietf.org/>`_ has directed the `Internet Assigned Numbers Authority <https://www.iana.org/>`_ to reserve the IPv4 address range the ``192.168.*.*`` (and others) for `private networks <https://en.wikipedia.org/wiki/Private_network>`_. Analog Devices picked the ``192.168.2.*`` subnet for it's private network for host to PlutoSDR devices, but there isn't anything stopping other people (including yourself) to be running a real network on the ``192.168.2.*`` subnet.

It's a quick update to change the PlutoSDR network settings, which is described below.

Multiple devices
----------------

When using multiple PlutoSDR devices on the same host, there are a few options:

-  usb mode via libiio, no changes are required, and things will work out of the box
-  network mode, where changes to the network settings are required (more below).

In network mode, the default configuration is to have an `IP address <https://en.wikipedia.org/wiki/IP_address>`_ for the host (``192.168.2.10``), and the actual PlutoSDR device (``192.168.2.1``). As one can expect - IP addresses are expected to be unique, and the default configuration works well when you have one device, but not as well when you have multiple.

In order to use multiple devices, you must change their IP address. This is managed by updating the ``config.txt`` file on the PlutoSDR mass storage device.

.. image:: https://wiki.analog.com/_media/university/tools/pluto/users/win_config_file.png
   :width: 500px

::

   # Device Configuration File
   # Edit, Save and then Eject the USB Drive

   [NETWORK]
   hostname = pluto
   ipaddr = 192.168.2.1
   ipaddr_host = 192.168.2.10
   netmask = 255.255.255.0

It's a simple matter of updating the ``[NETWORK]`` settings of the PlutoSDR ``ipaddr`` (default is ``192.168.2.1``), and your host PC settings ``ipaddr_host`` (default of 192.168.2.10). ``ip_addr`` and ``ipaddr_host`` must be unique, and must be on the same subnet. Separate Plutos on the same machine must be assigned different subnets. It's not recommended to use the real internet subnet. After saving the file back to the PlutoSDR mass storage device, simply eject (not unplug) the PlutoSDR mass storage device from your host.

Zeroconf
~~~~~~~~

There is a `Avahi <http://avahi.org/>`_ deamon running on the PlutoSDR. Avahi is a free `Zero-configuration networking <https://en.wikipedia.org/wiki/Zero-configuration_networking>`_ (zeroconf) implementation, including a system for multicast DNS/DNS-SD service discovery. If your ``hostname`` is unique and your host is zeroconf enabled, you can simply connect to your PlutoSDR using ``hostname``.local.

::

   michael@mhenneri-D04:~$ **iio_info -n <fc #ff0000>**pluto.local**</fc>**
   Library version: 0.9 (git tag: f7cde8f)
   Compiled with backends: local xml ip usb
   IIO context created with network backend.
   Backend version: 0.9 (git tag: v0.9   )
   Backend description string: 192.168.2.1 Linux (none) 4.6.0-25369-g51ebbb9 #120 SMP PREEMPT Thu Apr 6 09:04:26 CEST 2017 armv7l
   IIO context has 2 attributes:
       local,kernel: 4.6.0-25369-g51ebbb9
       ip,ip-addr: 192.168.2.1
   IIO context has 5 devices:

   [--snip--]

Host issues
^^^^^^^^^^^

The `Zeroconf <https://en.wikipedia.org/wiki/Zero-configuration_networking>`_ implementation for Linux `Avahi <http://avahi.org/>`_, implements IPv4LL, mDNS and DNS-SD. It is part of most Linux distributions, and is installed by default on some. If you end up with weird errors, it's a simple matter of making sure it is installed:``rgetz@brain:~$ **sudo apt-get install avahi-daemon avahi-utils**``

If you are on Windows, it's a little trickier. The Windows default implementation of zeroconf implements the `Link-Local Multicast Name Resolution <https://en.wikipedia.org/wiki/Link-Local_Multicast_Name_Resolution>`_ (LLMNR) standard/protocol. However, LLMNR isn't supported by the Linux Avahi running on the PlutoSDR, so you may need to install something that supports the protocols supported by Avahi. A few popular applications slip it in for their own needs, including Skype, Apple’s iTunes and Adobe Photoshop CS3 or later. So you might not need to add anything at all, or you might need to install one of those applications. There are some great instructions at `AdaFruit <https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux>`_ for those needed this.

Once everything is installed, you should be able to use ``pluto.local`` as the hostname.\ ``rgetz@brain:~/github/libiio$ **ping pluto.local**
PING pluto.local (192.168.2.1) 56(84) bytes of data.
64 bytes from 192.168.2.1 (192.168.2.1): icmp_seq=1 ttl=64 time=0.208 ms
64 bytes from 192.168.2.1 (192.168.2.1): icmp_seq=2 ttl=64 time=0.387 ms
^C
--- pluto.local ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 0.208/0.297/0.387/0.091 ms``

Changing the ``hostname`` in the config file:

::

   # Device Configuration File
   # Edit, Save and then Eject the USB Drive

   [NETWORK]
   hostname = fm_radio_antenna

will allow you to use ``fm_radio_antenna.local`` as the hostname:``rgetz@brain:~/github/libiio$ **iio_attr -u ip:fm_radio_antenna.local -C**
IIO context with 5 attributes:
hw_model: Analog Devices PlutoSDR Rev.A (Z7010-AD9363)
hw_serial: 1000002355237309001600070902169101
ad9361-phy,xo_correction: 40000000
local,kernel: 4.6.0-08871-g6297a9e
ip,ip-addr: 192.168.2.1``

To find the IP number, if you know the name, try:``analog@imhotep:~$ **avahi-resolve --name pluto.local**
pluto.local 192.168.2.1``

If you have multiple radios on the your network, and you want to find out the IP address of them, the pluto devices advertise an ssh and sftp-ssh servers :``analog@imhotep:~$ **avahi-browse -d local _ssh._tcp --resolve -t**
+   wlo1 IPv4 pluto                                         SSH Remote Terminal  local
=   wlo1 IPv4 pluto                                         SSH Remote Terminal  local
   hostname = [pluto.local]
   address = [192.168.1.149]
   port = [22]
   txt = []
analog@imhotep:~$ **avahi-browse -d local _sftp-ssh._tcp --resolve -t**
+   wlo1 IPv4 pluto                                         SFTP File Transfer   local
=   wlo1 IPv4 pluto                                         SFTP File Transfer   local
   hostname = [pluto.local]
   address = [192.168.1.149]
   port = [22]
   txt = []``

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

Updating to the AD9364
----------------------

+------------------------------------------------------------------+-----------------+-----------+-----------------+
| RF Transceiver                                                   | LO tuning range | Bandwidth | Number Channels |
+==================================================================+=================+===========+=================+
| :adi:`AD9363` (Default ADALM-PLUTO)                              | 325 - 3800 MHz  | 20 MHz    | 2 Rx, 2 Tx      |
+------------------------------------------------------------------+-----------------+-----------+-----------------+
| :adi:`AD9364`                                                    | 70 - 6000 MHz   | 56 MHz    | 1 Rx, 1 Tx      |
+------------------------------------------------------------------+-----------------+-----------+-----------------+
| :adi:`AD9361`                                                    | 70 - 6000 MHz   | 56 MHz    | 2 Rx, 2 Tx      |
+------------------------------------------------------------------+-----------------+-----------+-----------------+

There were some early PlutoSDR devices which use the :adi:`AD9364`, which is nearly identical to the :adi:`AD9363` used the production builds. If you have one of the AD9364 based PlutoSDR devices, it's a quick matter of using the U-Boot's `fw_printenv <http://man.cx/fw_printenv(8)>`_ and `fw_setenv <http://man.cx/fw_setenv(8)>`_ commands to get that device's larger tuning range (70-6000 MHz) and larger bandwidth (56MHz).

From your favorite serial application (`Windows <https://wiki.analog.com/../drivers/windows>`_, `Linux <https://wiki.analog.com/../drivers/linux>`_ or `macos <https://wiki.analog.com/../drivers/osx>`_), just open a serial connection (or ssh to 192.168.2.1, `Windows <https://wiki.analog.com/../drivers/windows>`_, `Linux <https://wiki.analog.com/../drivers/linux>`_ or `macos <https://wiki.analog.com/../drivers/osx>`_) to the PlutoSDR. The username is ``root`` and the password is ``analog``.

``fw_setenv`` takes a ``name`` and ``value`` pair. Depending on the revision of firmware/hardware that you have, different ``name`` and ``values`` are enabled.

Revision B / All Firmware versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
| Control            | Default | min FW  | HW Rev | ``name`` ``value`` pairs | configuration meaning                |
|                    |         | Version |        |                          |                                      |
+====================+=========+=========+========+==========================+======================================+
|                    |         |         |        |                          |                                      |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
| Tuning Range       | Y       | All     | B/C    | ``attr_name <blank>``    | tuning range is 325 - 3800 MHz       |
|                    |         |         |        | ``attr_val <blank>``     | 1r1t or 2r2t                         |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         |         |        |                          |                                      |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         | All     | B/C    | ``attr_name compatible`` | tuning range is 70 - 6000 MHz        |
|                    |         |         |        | ``attr_val ad9364``      | 1r1t only                            |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         |         |        |                          |                                      |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         | 0.32    | C      | ``attr_name compatible`` | tuning range is 70 - 6000 MHz        |
|                    |         |         |        | ``attr_val ad9361``      | 1r1t or 2r2t                         |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         |         |        |                          |                                      |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
| Number of channels | Y       | 0.32    | B/C    | ``mode 1r1t``            | 1 Rx, 1 Tx, 61.44 MSPS max data rate |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         |         |        |                          |                                      |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+
|                    |         | 0.32    | C      | ``mode 2r2t``            | 2 Rx, 2 Tx, 30.72 MSPS max data rate |
|                    |         |         |        |                          | (requires ad9363 or AD9361 settings) |
+--------------------+---------+---------+--------+--------------------------+--------------------------------------+

To learn more about how these are managed, and other settings, check out the `Boot Magic Explained <https://wiki.analog.com/../devs/booting>`_ docs.

Example
~~~~~~~

This will be the default (based on the AD9363):

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **fw_printenv attr_name**
      ## Error: "attr_name" not defined
      # **fw_printenv attr_val**
      ## Error: "attr_val" not defined
      #
   


To change things to the AD9364 configuration:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **fw_setenv attr_name compatible**
      # **fw_setenv attr_val ad9364**
      # **reboot**
   


Starting with PlutoSDR firmware revision **v0.32** an additional variable should be set:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **fw_setenv compatible ad9364**
      # **reboot**
   


Note that when setting the mode of a Rev. C PlutoSDR to ``2r2t``, the following would be sequence of commands:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **fw_setenv attr_name compatible**
      # **fw_setenv attr_val ad9361**
      # **fw_setenv compatible ad9361**
      # **fw_setenv mode 2r2t**
      # **reboot**
   


To learn more about resetting, check out the `developer documentation <https://wiki.analog.com/../devs/reboot>`_.

After rebooting the device, this is what the AD9364 configuration looks like:

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      Welcome to Pluto
      pluto login: **root**
      Password: **analog**
      # **fw_printenv attr_name**
      attr_name=compatible
      # **fw_printenv attr_val**
      attr_val=ad9364
      #
   


Changing the root password on the target
----------------------------------------

In PlutoSDR firmware version v0.32 and later there are three new command/scripts, facilitating persistent SSH key and password changes.

The first time you want to use this new feature you need to format/erase the mtd2 partition. Please use the ``device_format_jffs2`` command for that. On M2k this command is not included, since the partition is already formatted, and device calibration values are stored here already.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **device_format_jffs2**
      Are you sure to delete/format your mtd2 JFFS2 partition? (yes/no) yes
      Erasing 64 Kibyte @ 0 --  0 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 10000 --  7 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 20000 -- 14 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 30000 -- 21 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 40000 -- 28 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 50000 -- 35 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 60000 -- 42 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 70000 -- 50 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 80000 -- 57 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 90000 -- 64 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ a0000 -- 71 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ b0000 -- 78 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ c0000 -- 85 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ d0000 -- 92 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ d0000 -- 100 % complete 
   


After this is done you can use the ``device_passwd`` command to permanently change the password. This script/command calls the Linux passwd command and stores all user/password related files on mtd2 (JFFS2). The next time the system boots it will check all the MD5 sums and then uses this password instead.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **device_passwd** 
      Changing password for root
      New password: 
      Bad password: too short
      Retype password: 
      passwd: password for root changed by root
      #
   


**Note:** In case you forgot your password, there a mechanism which allows you to revert to the default password using the config.txt file on the mass storage device. Add ``revert_passwd = 1`` under the ``[ACTIONS]`` sections, then follow the procedure described here: :doc:`Config File ACTIONS </wiki-migration/university/tools/pluto/users/customizing>`

Enabling persistent SSH keys
----------------------------

In PlutoSDR firmware version v0.32 and later there are three new command/scripts, facilitating persistent SSH key and password changes.

The first time you want to use this new feature you need to format/erase the mtd2 partition. Please use the ``device_format_jffs2`` command for that. On M2k this command is not included, since the partition is already formatted, and device calibration values are stored here already.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **device_format_jffs2**
      Are you sure to delete/format your mtd2 JFFS2 partition? (yes/no) yes
      Erasing 64 Kibyte @ 0 --  0 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 10000 --  7 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 20000 -- 14 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 30000 -- 21 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 40000 -- 28 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 50000 -- 35 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 60000 -- 42 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 70000 -- 50 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 80000 -- 57 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ 90000 -- 64 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ a0000 -- 71 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ b0000 -- 78 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ c0000 -- 85 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ d0000 -- 92 % complete flash_erase:  Cleanmarker Updated.
      Erasing 64 Kibyte @ d0000 -- 100 % complete 
   


After this is done you can use the ``device_persistent_keys`` command to permanently store your private SSH dropbear keys. This script/command copies the current key or generates one, which is now stored on mtd2 (JFFS2). The next time the system boots it will check the MD5 sum and then uses this key instead.

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **device_persistent_keys** 
      Generating 256 bit ecdsa key, this may take a while...
      Public key portion is:
      ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBH+cMtkirbmWjOq+EjW0Lzir5LVuWXFwRTOMOnb0eWo
      Fingerprint: sha1!! 10:9c:40:18:f8:e3:10:f1:c8:62:ba:8d:27:48:1b:35:16:8d:a5:f5
      #
   


Changing the USB Ethernet Compatibility Mode
--------------------------------------------

Starting with PlutoSDR Firmware version :git-plutosdr-fw:`releases/tag/v0.33`, M2k (:git-m2k-fw:`releases/tag/v0.27`) there is now support for selecting the USB Ethernet Compatibility Mode by setting/changing the ``usb_ethernet_mode`` variable. The main industry protocols are (in chronological order): Remote NDIS (`RNDIS <https://en.wikipedia.org/wiki/RNDIS>`_, a Microsoft vendor protocol), Ethernet Control Model (`ECM <https://en.wikipedia.org/wiki/Ethernet_over_USB>`_), and Network Control Model (`NCM <https://en.wikipedia.org/wiki/Ethernet_over_USB>`_) - all supported by both Pluto and M2k. You may need to change this based on your host PC operating system type:

+-----------------+--------------------+--------------------+--------------------+--------------------+--------------------+
|                 | Windows            | Linux              | MacOS              | iPadOS             | Android            |
+=================+====================+====================+====================+====================+====================+
| RNDIS (default) | <fc #00ff00>✔</fc> | <fc #00ff00>✔</fc> | <fc #ff0000>✘</fc> | <fc #ff0000>✘</fc> | <fc #ff0000>✘</fc> |
+-----------------+--------------------+--------------------+--------------------+--------------------+--------------------+
| CDC-NCM         | <fc #ff0000>✘</fc> | <fc #00ff00>✔</fc> | <fc #00ff00>✔</fc> | <fc #00ff00>✔</fc> | <fc #ff0000>✘</fc> |
+-----------------+--------------------+--------------------+--------------------+--------------------+--------------------+
| CDC-ECM         | <fc #ff0000>✘</fc> | <fc #00ff00>✔</fc> | <fc #ff0000>✘</fc> | <fc #ff0000>✘</fc> | <fc #00ff00>✔</fc> |
+-----------------+--------------------+--------------------+--------------------+--------------------+--------------------+

As you can see - the default of RNDIS does not work on Mac OS (sorry). The platform you are testing on - needs to support high power USB 2.0 devices (500mA). (iPad will support, iPhone will not).

======= =======================================
Mode    Value of ``usb_ethernet_mode`` variable
======= =======================================
RNDIS   rndis (or blank)
CDC-NCM ncm
CDC-ECM ecm
======= =======================================

There are two methods to set the compatibility mode

-  Using the Config File (config.txt).
-  Setting the u-boot environment variable directly.

Config File
~~~~~~~~~~~

::

   # Device Configuration File
   # Edit, Save and then Eject the USB Drive

   [SYSTEM]
   xo_correction = 
   udc_handle_suspend = 0
   # USB Communication Device Class Compatibility Mode [rndis|ncm|ecm]
   **usb_ethernet_mode = ncm**

u-boot environment
~~~~~~~~~~~~~~~~~~

.. container:: box bggreen

   
   .. note::

      This specifies any shell prompt running on the target. The ``#`` is the prompt, and the **``bold``** is what you type

   
   ::
   
      # **fw_setenv usb_ethernet_mode ncm**
      # **reboot**
   

