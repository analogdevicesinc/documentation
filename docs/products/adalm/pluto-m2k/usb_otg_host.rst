.. _pluto-m2k usb_otg_host:

USB OTG – HOST function Support
===============================

When the device is powered from the Auxiliary Power Supply it support various
HOST functions, such as USB WIFI, Storage and HID. Using the correct cables is
the key to `OTG <https://en.wikipedia.org/wiki/USB_On-The-Go>`__ operation.

USB Wifi Support
----------------

PlutoSDR or M2k allows WIFI connectivity using ESSID and WPA-PSK passphrase. The
ESSID and Passphrase is set using the ``config.txt`` file in the Mass Storage
Device. The ESSID string is at most 32 alphanumeric characters, and the
passphrase is at least 8 and at most 63 ASCII characters.

Supported WIFI chipsets
~~~~~~~~~~~~~~~~~~~~~~~

Linux supports a large number of USB 802.11 WIFI modules. Most of these also
require a firmware file to be available on the host device. Given the
constrained flash memory footprint of the device, the decision was made to
support only a number of popular Ralink and Realtek based chipset modules. This
includes also a few unstable drivers from the kernel staging area, so not all
modules will work equally well.

Supported chipsets:

- Ralink rt2501/rt61
- Ralink rt73
- Ralink rt27xx/rt28xx/rt30xx
- Realtek 81xx
- Realtek 87xx
- Realtek 88xx

Many cheap and widely available modules will work - If you need a
recommendation. The models listed below have been tested:

- TP-Link TL-WN725N Nano WLAN
- Cisco WUSB600N V2

USB Wired Ethernet Support
--------------------------

If you want to integrate the PlutoSDR or M2k into a wired Ethernet network
directly, without PC in between. Use a wired USB Ethernet adapter. Even though
the USB support on PlutoSDR or M2k is only USB 2.0 HIGH SPEED. It’s still
beneficial to purchase a USB 3.0 Gigabit Ethernet Adapter. Using those USB 3.0
Gigabit Ethernet Adapters (in IIOD network back-end mode) the throughput can be
on par of with the IIOD USB back-end.

Supported chipsets:

- ASIX AX88xxx Based USB 2.0 Ethernet Adapters
- ASIX AX88179/178A USB 3.0/2.0 to Gigabit Ethernet
- Microchip LAN78XX Based USB Ethernet Adapters
- Realtek RTL8152/RTL8153 Based USB Ethernet Adapters
- SMSC LAN75XX based USB 2.0 gigabit ethernet devices
- SMSC LAN95XX based USB 2.0 10/100 ethernet devices

Many cheap and widely available modules will work - If you need a
recommendation. The models listed below have been tested:

- `Serach Amazon RTL8153 (USB 3.0 10/100/1000) <http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=RTL8153>`__
- `Serach Amazon AX88772 (USB 2.0 10/100) <http://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=AX88772>`__

Mass Storage Drive Support
--------------------------

PlutoSDR or M2k allows in `OTG <https://en.wikipedia.org/wiki/USB_On-The-Go>`__
Host mode the attachment of USB Mass Storage Devices. The supported file system
is currently `FAT/FAT32 <https://en.wikipedia.org/wiki/File_Allocation_Table>`__
only. Kernel Hotplug mechanisms are used to automount the available partitions
under /media. Once the storage is mounted the LED1 will stay constantly ON. Upon
storage removal the media is un-mounted and the **LED1** will resume its
heartbeat flash. There is also a save unmount functionality implemented using
the :ref:`hidden button <pluto hacking hardware connectors>`. If pressed while a media
is mounted the media is unmounted and the **LED1** will also resume to heartbeat
flash.

Someone may ask what’s the purpose of the USB Mass Storage Device Support?

Auto Run Support
~~~~~~~~~~~~~~~~

After mounting the attached storage the filesystem root is scanned for files
named ``runme[XX][.sh]``. Where XX is optional or can be any decimal numbers
starting from 0..99. The number defines the sequence in which the scripts or
executables are executed. If the file extension is ``.sh`` the shell script is
sourced for speed. If no ``.sh`` extension a subprocess is forked.
