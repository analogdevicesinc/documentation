USB to Wireless Dongle (Wifi) Support
=====================================

`Wireless_USB <https://en.wikipedia.org/wiki/Wireless_USB>`__ provides a approach for user to use the WIFI by adding a USB wireless dongle to the host (e.g. adsp-sc5xx board ) and the corresponding software configurations. This page describes how to use the USB Wireless (Wifi) feature on ADSP-sc5xx boards.

**Using USB wireless Dongle in Linux:**

Most of the **USB Wireless Dongle need** their own support drivers, and as the wireless driver in Linux kernel is to support the associated **Wireless Network Chipset** ``[e.g, Atheros/Qualcomm, Broadcom, Intel, Realtek]`` no mater which the manufacturer ``(e.g. A-Link, Dell, D-Link, Philips, TP-link)`` of the wireless card is, so we should make sure which **chipset** your device is using and enable/prepare the corresponding **Linux drivers** and **Firmware** first.

--------------

Identify & Confirm the Chipset
------------------------------

**STEP1:** Plug the USB Wireless Dongle into a Linux host PC and use the command "lsusb" to find the information of the device.

.. code:: c++

   test@madara:~# lsusb
   Bus 002 Device 020: ID 2001:3306 D-Link Corp. DWL-G122 Wireless Adapter(rev.F1) [Realtek RTL8188SU]
   Bus 002 Device 019: ID 0cf3:7015 Atheros Communications, Inc. TP-Link TL-WN821N v3 / TL-WN822N v2 802.11n [Atheros AR7010+AR9287]
   Bus 002 Device 021: ID 0bda:818b Realtek Semiconductor Corp. RTL8192EU 802.11b/g/n WLAN Adapter

From the visit `Linux-USB site <http://www.linux-usb.org/usb.ids>`__: **ID 2001:3306** is the number given to this chipset, The number before: indicates the manufacture ID and number after : indicates device ID.

**STEP2:** Query the Wireless Chipset corresponding supported driver and firmware from Google or other ways, here are some quick reference:

-  Chipset drivers: `Linux wireless LAN support; chipset <http://linux-wless.passys.nl>`__
-  Chipset firmware: `linux firmware <https://kernel.googlesource.com/pub/scm/linux/kernel/git>`__

Now we can get the information of the chipset and it corresponding drivers and Firmware:

::

   ;
   ; **ID 2001:3306**
   : chipset: ''Realtek RTL8188SU''
   : driver: ''rtl8172u.ko''
   : firmware: ''lib/firmware/rtlwifi/rtl8712u.bin''
   ; **ID 0cf3:7015**
   : chipset: ''Atheros AR7010+AR9287''
   : driver: ''ath9k.ko''
   : firmware ''lib/firmware/ath9k_htc/htc_7010-1.4.0.fw''
   ; **ID 0bda:818b**
   : chipset:''Realtek RTL8192EU 802.11b/g/n ''
   : driver: '' RTL8xxxEU.ko'' 
   : firmware: ''lib/firmware/rtlwifi/rtl8192eu_nic.bin''

--------------

Hardware Configuration
----------------------

Connect the USB micro-A plug to A receptacle adaptor cable (found in the EZ-Board box) to the OTG port, below photo shows when it acts as Host and connected to a USB Wireless dongle device.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/host_mode/wireless.jpg
   :align: center
   :width: 600px

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Host only mode, and enable the USB wireless relevant supported operations.

**Configure the USB drivers to host mod or (dual role mode)**

.. code:: shell

   Device Drivers  --->
          [*] USB support  --->
               <*>   Support for Host-side USB
                   [*]   Enable USB persist by default 
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Dual role mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra 

dual role mode need the g_serial and CDC module

.. code:: shell

   Device Drivers  --->
          [*] USB support  --->
                   <*>   USB Gadget Support  --->
                         <M>   USB Gadget precomposed configurations
                         <M>     Serial Gadget (with CDC ACM and CDC OBEX support) 
                         <M>     CDC Composite Device (Ethernet and ACM)  

**Configure the USB Wifi corresponding options**

.. code:: shell

   [*] Networking support  --->
           Networking options --->
               [*] TCP/IP networking 
           [*]   IP: kernel level autoconfiguration 
           [*]     IP: DHCP support  
           [*]     IP: BOOTP support
           [*]     IP: RARP support 
           <*>   The IPv6 protocol  ---> 
       [*]   Wireless  --->
           <*>   cfg80211 - wireless configuration API 
           [*]     cfg80211 wireless extensions compatibility  
           <*>   Generic IEEE 802.11 Networking Stack (mac80211) 
           [*]   Minstrel
               [*]     Minstrel 802.11n support
           [*]       Minstrel 802.11ac support 

**Enable the Wireless Chipset supported Drivers**

For the ID **``2001:3306``** chipset Realtek **``RTL8188SU``**

.. code:: shell

   Device Drivers  --->
          [*] Network device support  --->
                 [*]   Wireless LAN  --->
                       [*]   Realtek devices
          [*] Staging drivers  --->
                 <*>   RealTek RTL8712U (RTL8192SU) Wireless LAN NIC driver

For the ID **``0cf3:7015``** chipset: Atheros **``AltAR7010+AR9287``** 

.. raw:: html

   <details><summary>Click to expand</summary>

.. code:: shell

   Device Drivers  --->
          [*] Network device support  --->
                 [*]   Wireless LAN  --->
                       [*]   Atheros/Qualcomm devices 
                       <*>     Atheros 802.11n wireless cards support
                       [*]     Atheros bluetooth coexistence support
                       [*]       Atheros ath9k AHB bus support
                       [*]       Atheros ath9k ACK timeout estimation algorithm (EXPERIMENTAL) 
                       [*]       Channel Context support 
                       [*]       Atheros ath9k support for PC OEM cards   
                       <*>     Atheros HTC based wireless cards support  
                       <*>     Linux Community AR9170 802.11n USB support 
                       [*]       SoftLED Support

.. raw:: html

   </details>


For the ID **``0bda:818b``** chipset **``rtl8188eu``** 

.. raw:: html

   <details><summary>Click to expand</summary>

.. code:: shell

   Device Drivers  --->
          [*] Network device support  --->
                 [*]   Wireless LAN  --->
                       [*]   Realtek devices
                       <*>     RTL8723AU/RTL8188[CR]U/RTL819[12]CU (mac80211) support   
                       [*]       Include support for untested Realtek 8xxx USB devices (EXPERIMENTAL)
          [*] Staging drivers  --->
                 <M>   Realtek RTL8188EU Wireless LAN NIC driver
             [*]     Realtek RTL8188EU AP mode

.. raw:: html

   </details>


**Adding the corresponding Firmware**

Standard Yocto layer provides a "sources/poky/meta/recipes-kernel/linux-firmware/linux-firmware_git.bb" for user to get some common firmware. please modify and add the below codes to ``sources/meta-adi/meta-adi-adsp-sc5xx/recipes-adi/images/adsp-sc5xx-full.bb`` to enable the \**wpa-supplicant \*\* and \**wireless-tools \*\* tools and the chipset corresponding Firmware.

.. code:: java

   USB_WIFI = " \
       wpa-supplicant \
       wireless-tools \
       linux-firmware-ath9k \
       linux-firmware-rtl8192su \
   "
   IMAGE_INSTALL += " \
       ${USB_WIFI} \
   "

Add the additional Firmware: 

.. raw:: html

   <details><summary>Click to expand</summary>

If we can't find the target chipset supported firmware from the linux-firmware_git.bb, we should write our own .bb file to fetch the corresponding Firmware or just adding it manually.

**1. Manually fetch Firmware**

.. code:: c++

   git clone https://kernel.googlesource.com/pub/scm/linux/kernel/git/vkoul/firmware
   sudo cp -r firmware/rtlwifi/rtl8192eu_nic.bin /romfs/lib/firmware/rtlwifi

.. raw:: html

   </details>


Reference:

-  ``sources/poky/meta/recipes-kernel/linux-firmware/linux-firmware_git.bb``
-  https://kernel.googlesource.com/pub/scm/linux/kernel/git/vkoul/firmware/+/byt_new/rtlwifi/

\**Busy box configuration \*\*

.. code:: c++

   bitbake busybox -c menuconfig

.. code:: shell

   Coreutils  --->  
          [*] mktemp (4 kb) 
   Networking Utilities  --->
          [*] Enable IPv6 support  
          [*] udhcpc
          [*]   Verify that the offered address is free, using ARP ping 
          [*]   Do not pass malformed host and domain names
          --- Common options for DHCP applets 
          (9) Maximum verbosity level (0..9)
          (80) DHCP options slack buffer size 
          [*] Support RFC 3397 domain search options
          [*] Support 802.1Q VLAN parameters options
          (-R -b) ifup udhcpc command line options 

--------------

Example Usage
-------------

Boot the generated Images and connect the USB Wireless Dongle to the target hardware board:

**Step1. USB Wireless Dongle Detected**

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe g_serial      (USB Dual mode)
   g_serial gadget: Gadget Serial v2.4
   g_serial gadget: g_serial ready
   usb 1-1: new high-speed USB device number 2 using musb-hdrc
   r8712u: register rtl8712_netdev_ops to netdev_ops
   usb 1-1: r8712u: USB_SPEED_HIGH with 4 endpoints
   usb 1-1: r8712u: Boot from EFUSE: Autoload OK
   usb 1-1: r8712u: CustomerID = 0x0000
   usb 1-1: r8712u: MAC Address from efuse = f0:7d:68:f1:3d:50
   usb 1-1: r8712u: Loading firmware from "rtlwifi/rtl8712u.bin"

**Step2. Enable the ``wlan0`` and Scan the available wifi host**

.. code:: c++

   root@adsp-sc589-ezkit:~# ifconfig wlan0 up
   r8712u 1-1:1.0 wlan0: 1 RCR=0x153f00e
   r8712u 1-1:1.0 wlan0: 2 RCR=0x553f00e
   IPv6: ADDRCONF(NETDEV_UP): wlan0: link is not ready
   root@adsp-sc589-ezkit:~# iwconfig wlan0
   wlan0     unassociated  Nickname:"rtl_wifi"
             Mode:Auto  Access Point: Not-Associated   Sensitivity:0/0
             Retry:off   RTS thr:off   Fragment thr:off
             Encryption key:off
             Power Management:off
             Link Quality:0  Signal level:0  Noise level:0
             Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
             Tx excessive retries:0  Invalid misc:0   Missed beacon:0
   root@adsp-sc589-ezkit:~# iwlist wlan0 scanning | grep ESSID
                       ESSID:"ADIWLAN"
                       ESSID:"ADIWLAN"
                       ESSID:"iPhone"
                       ESSID:"ADI-VISITOR"
                       ESSID:"corpave"
                       ESSID:"ChinaNet-7359"
                       ESSID:"ADI-VISITOR"

**Step3. Connect the WIFI Router host via** `wpa_supplicant <https://wiki.archlinux.org/index.php/wpa_supplicant>`__ **tool**

Configure the `/etc/wpa_supplicant.conf <https://w1.fi/cgit/hostap/plain/wpa_supplicant/wpa_supplicant.conf>`__ to add the ``name`` and ``password`` of the target Router host as below:

.. code:: c++

   ctrl_interface=/var/run/wpa_supplicant
   ctrl_interface_group=0
   update_config=1

   network={
           key_mgmt=NONE
   }

   network={
           ssid="corpave"                          # name 
           psk="ADI12345"                          # password   
           key_mgmt=WPA-EAP WPA-PSK IEEE8021X NONE # way of encryption
           priority=1                              # priority    
   }

   network={
           ssid="iPhone"
           psk="12345678"
           key_mgmt=WPA-EAP WPA-PSK IEEE8021X NONE
           priority=2
           scan_ssid=1
   }

Run the **wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant.conf** to create the wireless establishment

.. code:: c++

   root@adsp-sc589-ezkit:~# wpa_supplicant -B -Dwext -iwlan0 -c/etc/wpa_supplicant.conf
   Successfully initialized wpa_supplicant
   rfkill: Cannot get wiphy information
   USHIPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
   root@adsp-sc589-ezkit:~# iwconfig wlan0
   wlan0     IEEE 802.11bgn  ESSID:"corpave"  Nickname:"rtl_wifi"
             Mode:Managed  Frequency:2.437 GHz  Access Point: 14:D6:4D:32:3B:EA
             Bit Rate:150 Mb/s   Sensitivity:0/0
             Retry:off   RTS thr:off   Fragment thr:off
             Encryption key:****-****-****-****-****-****-****-****   Security mode:open
             Power Management:off
             Link Quality=100/100  Signal level=100/100  Noise level=0/100
             Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
             Tx excessive retries:0  Invalid misc:0   Missed beacon:0

**Step4. Dynamic IP acquisition with the ``udhcpc`` and Verification the wifi connection**

.. code:: c++

   root@adsp-sc589-ezkit:~# udhcpc -i wlan0
   udhcpc: started, v1.29.3
   udhcpc: sending discover
   udhcpc: sending select for 192.168.0.104
   udhcpc: lease of 192.168.0.104 obtained, lease time 86400
   /etc/udhcpc.d/50default: Adding DNS 192.168.0.1
   root@adsp-sc589-ezkit:~# ifconfig wlan0
   wlan0     Link encap:Ethernet  HWaddr F0:7D:68:F1:3D:50
             inet addr:192.168.0.104  Bcast:192.168.0.255  Mask:255.255.255.0
             inet6 addr: fe80::f27d:68ff:fef1:3d50/64 Scope:Link
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:58 errors:0 dropped:53 overruns:0 frame:0
             TX packets:34 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:16072 (15.6 KiB)  TX bytes:8747 (8.5 KiB)
   root@adsp-sc589-ezkit:~# route
   Kernel IP routing table
   Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
   default         10.99.24.1      0.0.0.0         UG    0      0        0 eth0
   default         sqe-l12.ad.anal 0.0.0.0         UG    10     0        0 wlan0
   10.99.24.0      *               255.255.255.0   U     0      0        0 eth0
   192.168.0.0     *               255.255.255.0   U     0      0        0 wlan0
   root@adsp-sc589-ezkit:~# ping 192.168.0.1
   PING 192.168.0.1 (192.168.0.1): 56 data bytes
   64 bytes from 192.168.0.1: seq=0 ttl=64 time=1.088 ms
   64 bytes from 192.168.0.1: seq=1 ttl=64 time=0.956 ms
   64 bytes from 192.168.0.1: seq=2 ttl=64 time=0.938 ms
   64 bytes from 192.168.0.1: seq=3 ttl=64 time=0.898 ms
   64 bytes from 192.168.0.1: seq=4 ttl=64 time=0.909 ms
   ^C
   --- 192.168.0.1 ping statistics ---
   5 packets transmitted, 5 packets received, 0% packet loss
   round-trip min/avg/max = 0.898/0.957/1.088 ms

**Help of Command wpa_supplicant** 

.. raw:: html

   <details><summary>Click to expand</summary>

.. code:: c++

   root@adsp-sc589-ezkit:~# wpa_supplicant -h
   wpa_supplicant v2.6
   Copyright (c) 2003-2016, Jouni Malinen <j@w1.fi> and contributors

   This software may be distributed under the terms of the BSD license.
   See README for more details.

   usage:
     wpa_supplicant [-BddhKLqqtuvW] [-P<pid file>] [-g<global ctrl>] \
           [-G<group>] \
           -i<ifname> -c<config file> [-C<ctrl>] [-D<driver>] [-p<driver_param>] \
           [-b<br_ifname>] [-e<entropy file>] \
           [-o<override driver>] [-O<override ctrl>] \
           [-N -i<ifname> -c<conf> [-C<ctrl>] [-D<driver>] \
           [-p<driver_param>] [-b<br_ifname>] [-I<config file>] ...]

   drivers:
     nl80211 = Linux nl80211/cfg80211
     wext = Linux wireless extensions (generic)
     hostap = Host AP driver (Intersil Prism2/2.5/3)
     wired = Wired Ethernet driver
   options:
     -b = optional bridge interface name
     -B = run daemon in the background
     -c = Configuration file
     -C = ctrl_interface parameter (only used if -c is not)
     -d = increase debugging verbosity (-dd even more)
     -D = driver name (can be multiple drivers: nl80211,wext)
     -e = entropy file
     -g = global ctrl_interface
     -G = global ctrl_interface group
     -h = show this help text
     -i = interface name
     -I = additional configuration file
     -K = include keys (passwords, etc.) in debug output
     -L = show license (BSD)
     -N = start describing new interface
     -o = override driver parameter for new interfaces
     -O = override ctrl_interface parameter for new interfaces
     -p = driver parameters
     -P = PID file
     -q = decrease debugging verbosity (-qq even less)
     -t = include timestamp in debug messages
     -u = enable DBus control interface
     -v = show version
     -W = wait for a control interface monitor before starting
   example:
     wpa_supplicant -Dnl80211 -iwlan0 -c/etc/wpa_supplicant.conf

.. raw:: html

   </details>


--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`
