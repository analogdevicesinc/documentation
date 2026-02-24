.. _pluto-m2k reboot:

Rebooting
=========

There are few different use cases, and methods to locally (USB/Serial), or
remotely (USB/Network) to reboot a Pluto/M2k.

Pluto/M2k was designed never to have to be rebooted - but software bugs happen.
Before you reboot things - try to ask yourself "why", what went wrong, how do I
reproduce, and how can I file a bug report that will help someone debug.

.. shell::

    Welcome to:
    ______ _       _        _________________
    | ___ \ |     | |      /  ___|  _  \ ___ \
    | |_/ / |_   _| |_ ___ \ `--.| | | | |_/ /
    |  __/| | | | | __/ _ \ `--. \ | | |    /
    | |   | | |_| | || (_) /\__/ / |/ /| |\ \
    \_|   |_|\__,_|\__\___/\____/|___/ \_| \_|

    v0.20
    http://wiki.analog.com/university/tools/pluto

   $device_reboot
    Usage: /usr/sbin/device_reboot {ram|sf|reset|verbose|break}
      sf     : Reboot and enter Serial Flash DFU mode
      ram    : Reboot and enter RAM DFU mode
      reset  : Reboot
      verbose: Reboot and start serial console Verbose
      break  : Reboot and HALT in u-boot
   $

.. _pluto-m2k reboot dfu-ram:

Reboot to DFU-RAM
-----------------

.. shell::

   $device_reboot ram
    Stopping input-event-daemon: done
    Stopping dropbear sshd: OK
    Stopping MSD Daemon: OK
    Stopping dhcpd Daemon & httpd Server: FAIL
    Stopping network: OK
    Stopping system message bus: done
    Stopping UDC Gadgets
    configfs-gadget gadget: unbind function 'rndis'/cbcaa480
    configfs-gadget gadget: unbind function 'Mass Storage Function'/cbc4e9c0
    configfs-gadget gadget: unbind function 'acm'/cc35e000
    configfs-gadget gadget: unbind function 'Function FS Gadget'/cc35e9e4
    Stopping logging: OK
    umount: devtmpfs busy - remounted read-only
    umount: can't unmount /: Invalid argument
    The system is going down NOW!
    Sent SIGTERM to all processes
    Sent SIGKILL to all processes
    Requesting system reboot
    reboot: Restarting system

    U-Boot PlutoSDR v0.20-PlutoSDR-00041-g4bdff59 (Apr 19 2017 - 17:45:50 +0200)

    I2C:   ready
    DRAM:  ECC disabled 512 MiB
    SF: Detected N25Q256A with page size 256 Bytes, erase size 4 KiB, total 32 MiB
    In:    serial@e0001000
    Out:   serial@e0001000
    Err:   serial@e0001000
    Model: Zynq Pluto SDR Board
    Hit any key to stop autoboot:  0
    Entering DFU RAM mode ...
    Copying Linux from DFU to RAM...

.. hint::

   This specifies any shell prompt running on the development host.

Following commands can be used to boot a fresh build of the firmware image. To
simply things, there is a script in :git-plutosdr_scripts:`plutosdr_scripts <master:>`
``pluto_ramboot`` that can do all
these steps in one command.

.. shell::

    $sshpass -p analog ssh root@pluto '/usr/sbin/pluto_reboot ram;'
    $sleep 5
    $sudo dfu-util -l
     dfu-util 0.9

     Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
     Copyright 2010-2016 Tormod Volden and Stefan Schmidt
     This program is Free Software and has ABSOLUTELY NO WARRANTY
     Please report bugs to http:%%//%%sourceforge.net/p/dfu-util/tickets/

     Found DFU: [0456:b674] ver=0221, devnum=11, cfg=1, intf=0, path="1-4", alt=1, name="firmware.dfu", serial="UNKNOWN"
     Found DFU: [0456:b674] ver=0221, devnum=11, cfg=1, intf=0, path="1-4", alt=0, name="dummy.dfu", serial="UNKNOWN"

    $sudo dfu-util -d 0456:b673,0456:b674 -D ./build/pluto.dfu -a firmware.dfu
    $sudo dfu-util -d 0456:b673,0456:b674  -a firmware.dfu -e

Reboot to DFU-Flash
-------------------

.. shell::

   $device_reboot sf
    Stopping input-event-daemon: done
    Stopping dropbear sshd: OK
    Stopping MSD Daemon: OK
    Stopping dhcpd Daemon & httpd Server: FAIL
    Stopping network: OK
    Stopping system message bus: done
    Stopping UDC Gadgets
    configfs-gadget gadget: unbind function 'rndis'/df624600
    configfs-gadget gadget: unbind function 'Mass Storage Function'/cbc13600
    configfs-gadget gadget: unbind function 'acm'/cbc12780
    configfs-gadget gadget: unbind function 'Function FS Gadget'/cbc4e9e4
    Stopping logging: OK
    umount: devtmpfs busy - remounted read-only
    umount: can't unmount /: Invalid argument
    The system is going down NOW!
    Sent SIGTERM to all processes
    Sent SIGKILL to all processes
    Requesting system reboot
    reboot: Restarting system

    U-Boot PlutoSDR v0.20-PlutoSDR-00041-g4bdff59 (Apr 19 2017 - 17:45:50 +0200)

    I2C:   ready
    DRAM:  ECC disabled 512 MiB
    SF: Detected N25Q256A with page size 256 Bytes, erase size 4 KiB, total 32 MiB
    In:    serial@e0001000
    Out:   serial@e0001000
    Err:   serial@e0001000
    Model: Zynq Pluto SDR Board
    Hit any key to stop autoboot:  0
    Entering DFU SF mode ...
    SF: Detected N25Q256A with page size 256 Bytes, erase size 4 KiB, total 32 MiB

Reboot
------

.. shell::

   $reboot
