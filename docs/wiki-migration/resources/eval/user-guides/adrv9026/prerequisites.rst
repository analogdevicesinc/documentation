Supported Carriers
==================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/documentation/eval/user-guide/transceiver/adrv9026/prerequisites.html\


The :adi:`EVAL-ADRV9026/ADRV9029 <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV9026.html>` are, by definition "FPGA mezzanine cards" (FMC), that means they need a carrier to plug into. The carrier we currently support is:

+----------------------------------------------------------------------------------------------------------------------+------------------------+
| Board                                                                                                                | EVAL-ADRV9026/ADRV9029 |
+======================================================================================================================+========================+
| `ZCU102 <https://www.xilinx.com/ZCU102>`_                                                                            | √                      |
+----------------------------------------------------------------------------------------------------------------------+------------------------+
| `Arria 10 SoC <https://www.altera.com/products/boards_and_kits/dev-kits/altera/arria-10-soc-development-kit.html>`_  | √                      |
+----------------------------------------------------------------------------------------------------------------------+------------------------+

-   some way to interact with the platform,

   -  for the ARM/FPGA SoC platforms, this normally includes:

      -  DisplayPort monitor
      -  USB Keyboard
      -  USB Mouse

   -  for the FPGA only solutions, this includes:

      -  LAN cable (Ethernet)
      -  Host PC (Windows or Linux)

-  Internet connection (without proxies makes things much easier) to update the scripts/binaries on the SD Card that came with the ADI FMC Card. (Firewalls are OK, proxies make things a pain).
-  RF Test equipment
