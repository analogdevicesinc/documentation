Ethernet driver and performance
===============================

Introduction
------------

This document describes how to enable the gigabit and 10/100 Ethernet devices on the ADSP-SC5xx Ezkit board in Linux. The performance benchmark data of the gigabit Ethernet device are provided for reference. The data is collected when running netperf testing with an Ubuntu host PC.

Hardware Requirement
--------------------

-  ADSP-SC589 Ezkit v1.1 and above, or,
-  ADSP-SC584 Ezkit v1.0 and above, or,
-  ADSP-SC573 Ezkit v1.2 (BOM 1.8) and above, or,
-  ADSP-SC589 MINI v1.4 and above
-  1 Ubuntu PC with Gigabit Ethernet port
-  1 Gigabit Ethernet switch

|

.. note::

   ADSP-SC573 EZ-kit board and ADSP-SC589 EZ-kit board version 2.0 have the TI DP83867 as the Gigabit Ethernet PHY device on the boards, other ADSP-SC5XX EZ-kit boards have the TI DP83865 as the Gigabit Ethernet PHY device on the boards.


   | ===== Software Configuration =====

Package Configuration
~~~~~~~~~~~~~~~~~~~~~

The netperf test utility is optional. You can build it for both the target board and your host Linux system. Add the netperf package in the filesystem, it's enabled in adsp-sc5xx-full image by default.

::

   vim build/conf/local.conf
   IMAGE_INSTALL_append = "netperf"

|

| ==== Kernel Configuration ====

Enable EMAC driver
^^^^^^^^^^^^^^^^^^

The on-chip Ethernet devices on the ADSP-SC5xx serial processors can be enabled in the Linux kernel configuration system using "**bitbake linux-adi -c menuconfig**".

::

   Device Drivers  --->
       [*] Network device support  --->
           [*]   Ethernet driver support  --->
               [*]   STMicroelectronics devices
                   <*>     STMicroelectronics 10/100/1000 Ethernet driver
                   <*>       STMMAC Platform bus support
                   < >         Support for snps,dwc-qos-ethernet.txt DT binding.
                   <*>         Generic driver for DWMAC
                   <*>         ADI DWMAC support

Enable Ethernet PHY device driver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Different version's EZ-kit has the different Gigabit Ethernet PHY device on board, therefore, various Ethernet PHY device drivers should be enabled in the Linux kernel configuration system for ADSP-SC5XX EZ-kit boards.

::

   For ADSP-SC5xx EZ-kit boards which have DP83867 PHY on board:
   Device Drivers  --->
       [*] Network device support  --->
           -*-   PHY Device support and infrastructure  --->
               <*>   Texas Instruments DP83867 Gigabit PHY

::

   For other versions ADSP-SC5XX EZ-kit boards which have National PHY(DP83865):
   Device Drivers  --->
       [*] Network device support  --->
           -*-   PHY Device support and infrastructure  --->
               <*>  National Semiconductor PHYs

| 
| ==== Configure Device Tree ==== **Gigabit Ethernet** 
| The GMAC device is based on the STM MAC IP.  MAC specific features can be tuned in the device tree Ethernet node. Node properties start with "snps" can be configured according to the requirement of the customer.  See the Documentation/devicetree/bindings/net/stmmac.txt document in the Linux sources for details.

::

   For ADSP-SC584 EZ-kit board (sc584-ezkit.dts) using NATIONAL PHY,
   &emac0 {
           enable-pin = <&ssw0 3 GPIO_ACTIVE_LOW>; /* ETH0_EN */
           snps,reset-gpio = <&gpb 14 0>;
           snps,reset-active-low;
           snps,reset-delays-us = <0 200 500>;
           phy-mode = "rgmii";
           pinctrl-names = "default";
           pinctrl-0 = <&eth0_default>;
           status = "okay";
   };

::

   For other ADSP-SC5XX EZ-kit boards using DP86867 PHY,
   &emac0 {
       snps,reset-gpio = <&gpb 7 0>;
       snps,reset-active-low;
       snps,reset-delays-us = <0 10000 1000000>;
       phy-handle = <&dp83867>;
       phy-mode = "rgmii-id";
       pinctrl-names = "default";
       pinctrl-0 = <&eth0_default>;
       status = "okay";
       mdio0 {
           compatible = "snps,dwmac-mdio";
           #address-cells = <1>;
           #size-cells = <0>;
           dp83867: ethernet-phy@0 {
                   reg = <0>;
                   ti,rx-internal-delay = <DP83867_RGMIIDCTL_2_00_NS>;
                   ti,tx-internal-delay = <DP83867_RGMIIDCTL_2_00_NS>;
                   ti,fifo-depth = <DP83867_PHYCR_FIFO_DEPTH_8_B_NIB>;
                   ti,dp83867-rxctrl-strap-quirk;
           };
       };
   };

| **100M Ethernet**
| The 100M EMAC device is based on the STM MAC IP.  MAC specific features start with "snps" in device node can be configured according to the Documentation/devicetree/bindings/net/stmmac.txt document in the Linux sources.

::

   &emac1 {
           enable-pin = <&ssw0 4 GPIO_ACTIVE_LOW>; /* ETH1_EN */
           phy-mode = "rmii";
           pinctrl-names = "default";
           pinctrl-0 = <&eth1_default>;
           status = "okay";
   };    

| 
| ===== Performance Benchmark Example ===== The Ethernet performance is tested with the netperf utility running on a Linux host on one end, and on the ADSP-SC5xx EZKIT board on the other end.

Netperf Example Usage
~~~~~~~~~~~~~~~~~~~~~

Run below command to test the ethernet performance using netperf.

::

   netperf -H $server_ip -t TCP_RR -l $testlen
   netperf -H $server_ip -t TCP_STREAM -l $testlen

Test
^^^^

**Run below command to make sure the netserver is running in HOST PC:**

::

   $ ps -ef


   | grep netserver
   root     16823     1  0 12:10 ?        00:00:00 /usr/bin/netserver
   test     17056  1732  0 12:11 pts/0    00:00:00 grep --color=auto netserver

**Run netperf in target board:**

::

   # netperf -H 10.100.4.174 -t TCP_RR -l 6
   MIGRATED TCP REQUEST/RESPONSE TEST from 0.0.0.0 () port 0 AF_INET to 10.100.4.174 () port 0 AF_INET : demo : first burst 0
   Local /Remote
   Socket Size   Request  Resp.   Elapsed  Trans.
   Send   Recv   Size     Size    Time     Rate        
   bytes  Bytes  bytes    bytes   secs.    per sec  
    
   16384  87380  1        1       6.00     1255.09  
   16384  87380
   # netperf -H 10.100.4.174 -t TCP_STREAM -l 6
   MIGRATED TCP STREAM TEST from 0.0.0.0 () port 0 AF_INET to 10.100.4.174 () port 0 AF_INET : demo
   Recv   Send    Send                         
   Socket Socket  Message  Elapsed             
   Size   Size    Size     Time     Throughput 
   bytes  bytes   bytes    secs.    10^6bits/sec 
    
    87380  16384  16384    6.03      315.89  

|

| ==== Netperf GMAC Ethernet Result ====

+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+
|            | No Preemption Client(250HZ) | No Preemption Server(250HZ) | Voluntary Preemption Client(250HZ) | Voluntary Preemption Server(250HZ) | Preemptible Client(250HZ) | Preemptible Server(250HZ) |
+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+
| TCP_STREAM | 306.95 Mbps                 | 200.38 Mbps                 | 285.79 Mbps                        | 195.34 Mbps                        | 289.40 Mbps               | 176.93 Mbps               |
+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+
| TCP_RR     | 1300.05 rps                 | 1305.18rps                  | 1266.92 rps                        | 1293.63 rps                        | 1273.37 rps               | 1275.15 rps               |
+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+
| UDP_STREAM | 304.04 Mbps                 | 604.73 Mbps                 | 304.40 Mbps                        | 601.08 Mbps                        | 277.51 Mbps               | 597.69 Mbps               |
+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+
| UDP_RR     | 1323.08 rps                 | 1341.38 rps                 | 1321.42 rps                        | 1338.78 rps                        | 1298.85 rps               | 1297.38 rps               |
+------------+-----------------------------+-----------------------------+------------------------------------+------------------------------------+---------------------------+---------------------------+

**Client** means the netperf tool is running as a test client on the ADSP-SC5xx EZKIT, while Server means it is running as a test server on the ADSP-SC5xx EZKIT. 

**No Preemption**, **Voluntary Preemption** and **Preemptible** are 3 different kernel schedule policies. The ARM A5 core runs at 450M clock while the DDR is at 225M clock during the test.  

| 
| ---- **Back to** :doc:`Kernel Features and Device Drivers for ADSP-SC5xx Yocto Linux </wiki-migration/resources/tools-software/linuxdsp/docs/linux-kernel-and-drivers/start>`
