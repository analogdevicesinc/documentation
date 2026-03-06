**\*AD353XR**\ \* HDL Reference Design
======================================

Overview
--------

AD353XR is a high-density low voltage supply DAC targeted but not limited to optical communications applications to perform biasing and control of PICs and power management block inside an optical modem and optical module. The two main specifications are the output headroom and the package size. - With an ultra low headroom, power dissipation on the part is reduced thus achieving improved system efficiency. In an optical module, customers will be able to achieve their biasing requirements by powering Blackwater directly from a typical 3.3V system supply. - WLCSP ensures lower board footprint utilization which is very important for smaller optical modules such as QSFP-DD and OSFP.

Supported devices
-----------------

AD353XR Eval Board

Supported carriers
------------------

`CoraZ7-07s FPGA Board <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`__

`DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__

`ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__

Hardware requirements
---------------------

-  Eval AD353XR
-  Other boards for connection like SDP-I-FMC, etc
-  `CoraZ7-07s FPGA Board <https://store.digilentinc.com/cora-z7-zynq-7000-single-core-and-dual-core-options-for-arm-fpga-soc-development/>`__, `DE10-Nano FPGA Board <https://www.terasic.com.tw/cgi-bin/page/archive.pl?Language=English&No=1046>`__, or `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
-  Ethernet cable (for network access)
-  Micro USB to USB Type A for UART access
-  1x SD card (at least 16GB); follow :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`
-  Jumper Wires to tap SPI
-  VADJ of Zedboard must be set to **2.5V**

Block design
------------

Block diagram
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/ad353xr_hdl_bd.svg
   :alt: ad353xr_hdl_bd.svg
   :width: 800px

SPI connections
~~~~~~~~~~~~~~~

========== ============== ================ ===============
Signal     Coraz7s Pinout DE10 Nano Pinout Zedboard Pinout
========== ============== ================ ===============
sclk       H15            AG18             D18/FMC-CLK1_P
ss0/sync_n F16            AE19             M19/FMC-LA00_P
mosi/sdo   T12            AG15             N19/FMC-LA01_P
miso/sdi   W15            AF18             N20/FMC-LA01_N
========== ============== ================ ===============

GPIOs
~~~~~

======= ============== ================ ===============
Signal  Coraz7s Pinout DE10 Nano Pinout Zedboard Pinout
======= ============== ================ ===============
reset_n V13            AE20             T19/FMC-LA10_N
ldac_n  T14            AE17             J18/FMC_LA05_P
======= ============== ================ ===============

Building the HDL project
------------------------

ADI does not distribute the bit/elf files of these projects so they must be built from the sources available :git-hdl>`__. To get the source you must `clone <https::`here </git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>` the HDL repository.

Then go to the **\*PROJECT LOCATION WITHIN HDL (EX: projects/ad353xr/coraz7s or projects/ad353xr/de10nano)**\ \* location and run the make command by typing in your command prompt:

**Linux/Cygwin**

::

   user@analog:~$ cd hdl/projects/ad353xr/coraz7s
   user@analog:~/hdl/projects/ad353xr/coraz7s$ make

| Check :doc:`this guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` on how to prepare your SD card with the proper boot files.
| A more comprehensive build guide can be found in the :doc:`HDL User Guide </wiki-migration/resources/fpga/docs/hdl>`.

Connections
~~~~~~~~~~~

-  How the jumpers/switches should be set on the board/carrier

   -  Coraz7s: Place a jumper on JP2, shorting the two pins together. Select JP3 connection depending on power supply source (USB or external).


   |image1|

   -  • DE10 nano: Adjust switch to FPGA configuration Mode.

   |image2|

   -  Zedboard: Set the Jumpers MIO[6:2] as 01100.

   |image3|

-  The Zedboard FMC is low pin count.

Resources
---------

-  Link to the project source code (See projects/ad353xr: `HDL Repository <https://github.com/analogdevicesinc/hdl>`__
-  Links to the Linux driver and devicetree source code and wiki documentation : TBD
-  Links to the datasheets/schematics of the boards used in this wiki page : :adi:`Datasheet <media/en/technical-documentation/data-sheets/ad3530_ad530r.pdf>`

More information
----------------

-  :doc:`How to prepare an SD card </wiki-migration/resources/tools-software/linux-software/kuiper-linux>` with boot files
-  :doc:`ADI reference designs HDL user guide </wiki-migration/resources/fpga/docs/hdl>`
-  :doc:`ADI HDL architecture </wiki-migration/resources/fpga/docs/arch>` wiki page
-  :doc:`How to build an ADI HDL project </wiki-migration/resources/fpga/docs/build>`

Support
-------

Analog Devices will provide **limited** online support for anyone using the reference design with Analog Devices components via the :ez:`EngineerZone FPGA reference designs <community/fpga>` forum.

It should be noted, that the older the tools' versions and release branches are, the lower the chances to receive support from ADI engineers.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cora_hw_config.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/de10-nano_fpga_switch_matrix.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/zedboard_jumpers.svg
   :width: 600px
