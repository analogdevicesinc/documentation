IEEE 1588 and Linux PTP
=======================

PTP Introduction
----------------

Precision Time Protocol(PTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Precision Time Protocol (PTP) is a high-precision time synchronization protocol for networked measurement and control systems. It is defined in the IEEE 1588 standard, which is designed for local systems requiring very high accuracies - beyond those attainable using NTP (Network Time Protocol). PTP makes it possible to synchronize distributed clocks with sub-microsecond accuracy via Ethernet networks, with relatively low demands on the local clocks and the network and computing capacity.

ADSP-SC573, SC584 and SC589 all support PTP. But only EMAC0 (the 10/100/1000 Mbps port) supports PTP, EMAC1 (the 10/100 Mbps port) is not capable of PTP operation.

| 
| ===== PTP Software Configuration =====

Package configuration
~~~~~~~~~~~~~~~~~~~~~

You should also enable the linuxptp test program to assist with testing. Add the linuxptp program in the filesystem images, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = " linuxptp"

| 
| ==== Kernel Configuration ==== The Linux kernel can be configured using the following command:

::

   $ bitbake linux-adi -c menuconfig 

   General Setup  --->
       -*- Configure standard kernel features (expert users)  --->
           [*]   Enable eventpoll support
           [*]   Enable timerfd() system call
    
   [*] Networking support  --->
       Networking options  --->
           [*] Timestamping in PHY devices
    
   Device Drivers  --->
       PPS support  --->
       PTP clock support  --->
       [*] Network device support  --->
           [*]   Ethernet driver support  --->
               [*]   STMicroelectronics devices
               <*>     STMicroelectronics 10/100/1000 Ethernet driver
               <*>       STMMAC Platform bus support

| 
| ==== Device tree configuration ==== The timestamps that are the basis of PTP can be acquired with greater accuracy when they are captured by the ethernet PHY hardware. The PHY interface can support hardware timestamps, the default phy-mode is RGMII.

| The phy-mode also can be changed to "rmii" in the device tree header in the linux kernel source arch/arm/boot/dts/sc589-ezkit.dts and other board specific sc5xx.dts files.

.. note::

   ... : ellipsis, means other properties in EMAC0 node stay the same

   | - : minus, means delete this property
   | + : plus, means add this property
   |


Run "**bitbake linux-adi -c devshell**" to enter into linux kernel source code and then change the dts file.

::

   $ vim arch/arm/boot/dts/sc589-ezkit.dts
   &emac0 {
   ...
   - phy-mode = "rgmii";
   + phy-mode = "rmii";
   ...
   };

Run "**bitbake linux-adi -C compile**" to generate zImage and dtb files, they are now ready to be loaded onto the target board.

| As to the linuxptp example needs the ethernet up, so users should use the ramboot rather than nfsboot. Run "**bitbake adsp-sc5xx-ramdisk -C compile**" to generate the file system. See :doc:`SC5xx ezkit Linux quick start guide </wiki-migration/resources/tools-software/linuxdsp/docs/quickstartguide/building>` for details.
| ===== Example =====

Preliminary work
~~~~~~~~~~~~~~~~

**1) Hardware Setup**

Two ADSP-SC5xx boards are required. One board act as a master, and the other act as a slave. The two boards are connected by their respective EMAC0 ports using a standard crossover network cable.

| **2) Master's MAC address must be different from slave's**
| In order to make the master's and the slave's MAC address different, change the slave's address in U-Boot.

::

   $ set ethaddr 00:20:22:fe:85:29

| **3) Master's ip address must be different from slave ip**
| Reset IP address after linux boot up.

::

   # ifconfig eth0 10.100.4.50 up 
   # ifconfig eth0 10.100.4.51 up 

| 
| ==== Run Example ====

1) Master
^^^^^^^^^

Note:  Master board should be configured first.

::

   # ifconfig eth0 10.100.4.51
   # date -s 2010.01.01-13:30
   Fri Jan  1 13:30:00 UTC 2010
   # testptp -g
   clock time: 0.000000000 or Thu Jan  1 00:00:00 1970
   # testptp -s
   set time okay
   # hwstamp_ctl -i eth0 -r 6 -t 1
   tx_type 1
   rx_filter 6

Change tx_timestamp_timeout to 100

::

   # vi /etc/ptp4l.cfg
   -tx_timestamp_timeout    1
   +tx_timestamp_timeout    100
   #
   # ptp4l -i eth0 -f /etc/ptp4l.cfg &
   # date
   Fri Jan  1 13:30:51 UTC 2010
   Date on master board is 2010.1.1-13:30:51.

2) Slave
^^^^^^^^

::

   # hwstamp_ctl -i eth0 -r 6 -t 1
   tx_type 1
   rx_filter 6
   # ptp4l -i eth0 -s &
   # date
   Mon Jan  1 00:02:24 UTC 2007
   # phc2sys -s /dev/ptp0 -O 0 &
   # date
   Mon Jan  1 00:02:24 UTC 2007
   ...
   # date
   Fri Jan  1 13:30:58 UTC 2010
   Date on the slave board is 2007.1.1-00:02:24 before synchronization, and changes to 2010.1.1-13:30:58 after a few seconds of synchronization with the master.

| 
| ===== More information =====

-  `Linux PTP project <http://linuxptp.sourceforge.net/>`_
-  `IEEE1588 standard <http://www.nist.gov/el/isd/ieee/ieee1588.cfm>`_
-  `PTP User guide <https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/ch-Configuring_PTP_Using_ptp4l.html>`_

| 
| ---- **Back to** :doc:`Yocto Linux Distrubution and Applications </wiki-migration/resources/tools-software/linuxdsp/docs/linux_yocto_distribution_and_applications/start>`
