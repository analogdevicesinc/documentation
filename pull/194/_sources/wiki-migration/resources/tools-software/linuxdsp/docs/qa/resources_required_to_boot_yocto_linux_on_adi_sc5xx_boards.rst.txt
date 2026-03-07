Resources required to boot Yocto Linux on ADI SC5XX boards
==========================================================

This page provides the resources which are required by Linux to boot on ADI SC5XX boards.

| 
| ==== Required Hardware Features ====

+---------------------+---------------+----------------------------------------------+
| ``Type``            | ``Hardware``  | ``Notes``                                    |
+=====================+===============+==============================================+
| CPU                 | ARM Cortex A5 | Core 0 running u-boot & Linux                |
+---------------------+---------------+----------------------------------------------+
| Core Timer          | GPTimer 0 & 1 | Used by Linux as the Core Timer              |
+---------------------+---------------+----------------------------------------------+
| Non-Volatile Memory | Nor flash     | Stores u-boot LDR file                       |
+---------------------+---------------+----------------------------------------------+
| Volatile Memory     | DDR           | Used by u-boot and Linux                     |
+---------------------+---------------+----------------------------------------------+
|                     | L2            | Used by u-boot and Linux                     |
+---------------------+---------------+----------------------------------------------+
| GPIO                | gpio          | Used by u-boot/Linux                         |
+---------------------+---------------+----------------------------------------------+
| Serial I/O          | UART0         | Used by Linux as the default UART Log output |
+---------------------+---------------+----------------------------------------------+
| Ethernet            | ETH0          | Used by u-boot/Linux as the default network  |
+---------------------+---------------+----------------------------------------------+

| 

Memory Details
--------------

L2 Memory Layout
~~~~~~~~~~~~~~~~

================ ================= ======== =========
``Machine``      ``Start Address`` ``size`` ``usage``
================ ================= ======== =========
adsp-sc589-ezkit 0x20080000        0x1000   Core0 ICC
adsp-sc584-ezkit 0x20080000        0x1000   Core0 ICC
adsp-sc573-ezkit 0x20000000        0x1000   Core0 ICC
ads-sc589-mini   0x20080000        0x1000   Core0 ICC
================ ================= ======== =========

|

DDR Memory Layout
~~~~~~~~~~~~~~~~~

================ ================= ====================
``Machine``      ``Start Address`` ``size``
================ ================= ====================
adsp-sc589-ezkit 0xc2000000        depends on the image
adsp-sc584-ezkit 0xc2000000        depends on the image
adsp-sc573-ezkit 0x82000000        depends on the image
adsp-sc589-mini  0xc2000000        depends on the image
================ ================= ====================

| 

--------------

Back To :doc:`Linux for SC5xx: Frequently Asked Questions </wiki-migration/resources/tools-software/linuxdsp/docs/qa/start>`
