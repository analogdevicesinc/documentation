USB Gadget Ethernet
===================

Gadget Ethernet allows `Ethernet emulation over USB <https://en.wikipedia.org/wiki/Ethernet_over_USB>`__, allowing the reading/writing at higher speeds than most Wifi connections. This page provides a approach how to use the USB Gadget Ethernet Feature on ADSP-SC5xx board and give a brief Example usage:

--------------

Hardware Configuration
----------------------

Connect the USB micro-B plug cable into the USB HS/OTG Device port, as showing below:


|image1|

--------------

Software Configuration
----------------------

On the Yocto, Configure the linux-kernel as below to set the USB controller in Gadget only mode, and enable the USB Ethernet Gadget relevant options.

.. code:: c++

   $ bitbake linux-adi -c menuconfig

Configure the USB drivers to Gadget only mode (or Dual role mode )
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   Device Drivers  --->
       [*] USB support  --->
                   <*>   Support for Host-side USB  
                   <*>   Inventra Highspeed Dual Role Controller
                           MUSB Mode Selection (Dual role mode)  --->
                           *** Platform Glue Layer *** 
                   <*>     ADI
                           *** MUSB DMA mode ***
                   [N]     Disable DMA (always use PIO)  
                   [*]       Inventra
                   <*>   USB Gadget Support  --->

Configure the Gadget Ethernet Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: shell

   Device Drivers  --->  
        <*> USB support
        <*>   USB Gadget Support  --->
        <M>     Ethernet Gadget (with CDC Ethernet support)
        [*]       RNDIS support

--------------

Example Usage
-------------

**Ez-Kit target board**

-  **Install the USB Ethernet module**

.. code:: c++

   root@adsp-sc589-ezkit:~# modprobe g_ether host_addr=00:dc:c8:f7:75:05 dev_addr=00:dd:dc:eb:6d:f1
   using random self ethernet address
   using random host ethernet address
   using host ethernet address: 00:dc:c8:f7:75:05
   using self ethernet address: 00:dd:dc:eb:6d:f1
   usb0: HOST MAC 00:dc:c8:f7:75:05
   usb0: MAC 00:dd:dc:eb:6d:f1
   using random self ethernet address
   using random host ethernet address
   g_ether gadget: Ethernet Gadget, version: Memorial Day 2008
   g_ether gadget: g_ether ready
   g_ether gadget: high-speed config #1: CDC Ethernet (ECM)
   oot@adsp-sc589-ezkit:~# lsmod | grep g_ether
   g_ether                16384  0
   usb_f_rndis            24576  2 g_ether
   u_ether                20480  3 usb_f_ecm,g_ether,usb_f_rndis
   libcomposite           40960  6 usb_f_ecm,usb_f_uac2,u_audio,g_audio,g_ether,usb_f_rndis

-  \*\* Enable the usb0 \*\*

Enable the **usb0** and config the ``IP address`` via the "ifconfig"command:

.. code:: c++

   root@adsp-sc589-ezkit:~# ifconfig usb0 192.168.1.66 up
   IPv6: ADDRCONF(NETDEV_CHANGE): usb0: link becomes ready
   root@adsp-sc589-ezkit:~# ifconfig usb0
   usb0      Link encap:Ethernet  HWaddr 00:DD:DC:EB:6D:F1
             inet addr:192.168.1.66  Bcast:192.168.1.255  Mask:255.255.255.0
             inet6 addr: fe80::2dd:dcff:feeb:6df1/64 Scope:Link
             UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
             RX packets:59 errors:0 dropped:0 overruns:0 frame:0
             TX packets:36 errors:0 dropped:0 overruns:0 carrier:0
             collisions:0 txqueuelen:1000
             RX bytes:7156 (6.9 KiB)  TX bytes:7508 (7.3 KiB)

**On the Linux-Host PC**

With following command you should be able to see the USB Ethernet device is there on your HOST:

.. code:: c++

   test@madara:~# sudo su
   root@madara:~# lsusb
   Bus 002 Device 040: ID 0525:a4a2 Netchip Technology, Inc. Linux-USB Ethernet/RNDIS Gadge
   root@madara:~# dmesg
   [84172.819820] usb 2-1.4: new high-speed USB device number 41 using ehci-pci
   [84172.929056] usb 2-1.4: New USB device found, idVendor=0525, idProduct=a4a2
   [84172.929059] usb 2-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
   [84172.929061] usb 2-1.4: Product: RNDIS/Ethernet Gadget
   [84172.929063] usb 2-1.4: Manufacturer: Linux 4.19.0-yocto-standard with musb-hdrc
   [84172.939552] cdc_subset: probe of 2-1.4:1.0 failed with error -22
   [84172.940300] cdc_ether 2-1.4:1.0 eth2: register 'cdc_ether' at usb-0000:00:1d.0-1.4, CDC Ethernet Device, 00:dc:c8:f7:75:05

.. code:: c++

   test@madara:~# ifconfig
   enp2s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet 10.99.24.131  netmask 255.255.255.0  broadcast 10.99.24.255
           inet6 fe80::939d:a9eb:5e47:8d9e  prefixlen 64  scopeid 0x20<link>
           ether f4:8e:38:a2:b4:a2  txqueuelen 1000  (Ethernet)
           RX packets 1927975  bytes 1412135935 (1.4 GB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 1836232  bytes 1655848202 (1.6 GB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

   enx00dcc8f77505: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet6 fe80::5e85:dcad:f5f7:1bfc  prefixlen 64  scopeid 0x20<link>
           ether 00:dc:c8:f7:75:05  txqueuelen 1000  (Ethernet)
           RX packets 37  bytes 6943 (6.9 KB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 37  bytes 7288 (7.2 KB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

   lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
           inet 127.0.0.1  netmask 255.0.0.0
           inet6 ::1  prefixlen 128  scopeid 0x10<host>
           loop  txqueuelen 1000  (Local Loopback)
           RX packets 11377  bytes 1017513 (1.0 MB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 11377  bytes 1017513 (1.0 MB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

Thought compared the commands output of dmesg and ifconfig, we can see the ether address of enx00dcc8f77505 is same with CDC Ethernet Device. So the "**enx00dcc8f77505**" is the target USB Ethernet Device.

.. code:: c++

   test@madara:~# ifconfig enx00dcc8f77505 up
   test@madara:~# ifconfig enx00dcc8f77505 192.168.1.67

   enx00dcc8f77505: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
           inet 192.168.1.67  netmask 255.255.255.0  broadcast 192.168.1.255
           inet6 fe80::5e85:dcad:f5f7:1bfc  prefixlen 64  scopeid 0x20<link>
           ether 00:dc:c8:f7:75:05  txqueuelen 1000  (Ethernet)
           RX packets 40  bytes 7373 (7.3 KB)
           RX errors 0  dropped 0  overruns 0  frame 0
           TX packets 86  bytes 18058 (18.0 KB)
           TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

--------------

Ping the target board:

.. code:: c++

   test@madara:~# ping -c 5 192.168.1.66
   PING 192.168.1.66 (192.168.1.66) 56(84) bytes of data.
   64 bytes from 192.168.1.66: icmp_seq=1 ttl=64 time=0.263 ms
   64 bytes from 192.168.1.66: icmp_seq=2 ttl=64 time=0.313 ms
   64 bytes from 192.168.1.66: icmp_seq=3 ttl=64 time=0.236 ms
   64 bytes from 192.168.1.66: icmp_seq=4 ttl=64 time=0.179 ms
   64 bytes from 192.168.1.66: icmp_seq=5 ttl=64 time=0.307 ms

   --- 192.168.1.66 ping statistics ---
   5 packets transmitted, 5 received, 0% packet loss, time 4100ms
   rtt min/avg/max/mdev = 0.179/0.259/0.313/0.052 ms

--------------

**Go TO** :doc:`USB Interface </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/start>`

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/usb/gadget-mode/002_usb_interface-device_application.jpg
   :width: 600px
