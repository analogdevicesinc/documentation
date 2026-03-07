General Bluetooth Dongle via USB
================================

Introduction
------------

Bluetooth is a low-cost, low-power, short-range wireless technology. It was designed as a replacement for cables and other short-range technologies like IrDA. Bluetooth operates in "personal area" range, that typically extends up to 10 meters. More information about Bluetooth can be found at <http://www.bluetooth.com/>.

Linux has support for almost any Bluetooth USB dongle. This document will guide users on how to set up a Bluetooth USB dongle on Linux.

Hardware Setup
--------------

::

   ; ADSP-SC5xx Board:
   : ADSP-SC589 Ezkit v1.1 and above, or,
   : ADSP-SC589 MINI 
   : ADSP-SC584 Ezkit v1.0 and above, or,
   : ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above
   ; Bluetooth USB dongle
   : Bluetooth 5.0 
   : Bluetooth 4.0

Software Configuration
----------------------

Configure Linux Kernel
~~~~~~~~~~~~~~~~~~~~~~

Please enable Bluetooth Support and the HCI USB driver.

.. code:: shell

   [*] Networking support --->
        <*> Bluetooth subsystem support --->
           [*]   Bluetooth Classic (BR/EDR) features
           <*>     RFCOMM protocol support
           [*]       RFCOMM TTY support
           <*>     BNEP protocol support
           [*]       Multicast filter support
           [*]       Protocol filter support
           <*>     HIDP protocol support 
           [*]     Bluetooth High Speed (HS) features (NEW) 
           [*]   Bluetooth device drivers
                 <*> HCI USB driver             

Note that by the default configuration, the USB port works on OTG mode. Users need to probe the USB Bluetooth dongle before it can work.

Otherwise users can select USB host mode for the USB dongle. For detailed information about how to configure USB, please refer to USB interface

(Optional)

.. code:: shell

   Device Drivers  --->
         [*] USB support  --->
               MUSB Mode Selection (Host only mode)--->
           (X) Host only mode
           ( ) Gadget only mode
           ( ) Dual Role only mode

Configure package
~~~~~~~~~~~~~~~~~

Add the Bluetooth relevant packages in the filesystem, they're enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = " \
           dbus \
           bluez5 \
           packagegroup-tools-bluetooth \
           expat \
           play "
   DISTRO_FEATURES_append = " \
          bluetooth \ 
          "

Then run “bitbake adsp-sc5xx-minimal -C compile” or “bitbake adsp-sc5xx-full -C compile” to generate the filesystem.

Example
-------

Plug in the USB dongle. If the USB interface is in host mode the device should be detected automatically:

.. code:: c++

   usbhid: USB HID core driver 
   usb 1-1: new full-speed USB device number 2 using musb-hdrc

If the USB interface is in OTG mode then the device must be probed first:

.. code:: c++

   # modprobe g_serial

Bring up the interface:

.. code:: c++

   # hciconfig hci0 up
   # hciconfig 
   hci0:   Type: BR/EDR  Bus: USB
           BD Address: 00:18:E4:08:CC:30  ACL MTU: 192:8  SCO MTU: 64:8
           UP RUNNING PSCAN
           RX bytes:383 acl:0 sco:0 events:16 errors:0
           TX bytes:300 acl:0 sco:0 commands:15 errors:0

Users can use "hcitool" to set the configuration of Bluetooth connections.

.. code:: c++

   # hcitool
   hcitool - HCI Tool ver 4.101
   Usage:
           hcitool [options] <command> [command parameters]
   Options:
           --help  Display help
           -i dev  HCI device
   Commands:
           dev     Display local devices
           inq     Inquire remote devices
           scan    Scan for remote devices
           name    Get name from remote device
           info    Get information from remote device
           spinq   Start periodic inquiry
           epinq   Exit periodic inquiry
           cmd     Submit arbitrary HCI commands
           con     Display active connections
           cc      Create connection to remote device
           dc      Disconnect from remote device
           sr      Switch master/slave role
           cpt     Change connection packet type
           rssi    Display connection RSSI
           lq      Display link quality
           tpl     Display transmit power level
           afh     Display AFH channel map
           lp      Set/display link policy settings
           lst     Set/display link supervision timeout
           auth    Request authentication
           enc     Set connection encryption
           key     Change connection link key
           clkoff  Read clock offset
           clock   Read local or remote clock
           lescan  Start LE scan
           lewladd Add device to LE White List
           lewlrm  Remove device from LE White List
           lewlsz  Read size of LE White List
           lewlclr Clear LE White list
           lecc    Create a LE Connection
           ledc    Disconnect a LE Connection
           lecup   LE Connection Update

For more information on the usage of each command use:

.. code:: c++

           hcitool <command> --help

Take some commands as example, such as show HCI devices

.. code:: c++

   # hcitool -i hci0 dev
   Devices:
           hci0    00:18:E4:08:CC:30

Scan and inquire for Bluetooth devices in the area:

.. code:: c++

   # hcitool -i hci0 scan
   Scanning ...
           30:F9:ED:E1:9E:A9       DR-BT140Q
           34:80:B3:4D:5F:5A       mi4
   # hcitool -i hci0 inq
   Inquiring ...
           34:80:B3:4D:5F:5A       clock offset: 0x2555    class: 0x5a020c
           30:F9:ED:E1:9E:A9       clock offset: 0x57f5    class: 0x240408

Get some information from these devices:

.. code:: c++

   # hcitool -i hci0 info 30:F9:ED:E1:9E:A9
   Requesting information ...
           BD Address:  30:F9:ED:E1:9E:A9
           Device Name: DR-BT140Q
           LMP Version: 2.0 (0x3) LMP Subversion: 0x1225
           Manufacturer: Cambridge Silicon Radio (10)
           Features: 0xff 0xff 0x8f 0x7e 0x98 0x19 0x00 0x80
                   <3-slot packets> <5-slot packets> <encryption> <slot offset>
                   <timing accuracy> <role switch> <hold mode> <sniff mode>
                   <park state> <RSSI> <channel quality> <SCO link> <HV2 packets>
                   <HV3 packets> <u-law log> <A-law log> <CVSD> <paging scheme>
                   <power control> <transparent SCO> <broadcast encrypt>
                   <EDR ACL 2 Mbps> <EDR ACL 3 Mbps> <enhanced iscan>
                   <interlaced iscan> <interlaced pscan> <inquiry with RSSI>
                   <AFH cap. slave> <AFH class. slave> <3-slot EDR ACL>
                   <5-slot EDR ACL> <AFH cap. master> <AFH class. master>
                   <extended features>

Ping a device:

.. code:: c++

   # l2ping 30:F9:ED:E1:9E:A9
   Ping: 30:F9:ED:E1:9E:A9 from 00:18:E4:08:CC:30 (data size 44) ...
   4 bytes from 30:F9:ED:E1:9E:A9 id 0 time 30.38ms
   4 bytes from 30:F9:ED:E1:9E:A9 id 1 time 8.70ms
   4 bytes from 30:F9:ED:E1:9E:A9 id 2 time 8.48ms
   4 bytes from 30:F9:ED:E1:9E:A9 id 3 time 8.90ms
   4 bytes from 30:F9:ED:E1:9E:A9 id 4 time 8.51ms

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`
