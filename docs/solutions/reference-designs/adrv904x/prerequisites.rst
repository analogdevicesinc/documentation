Supported Carriers
==================

The :adi:`ADRV904x-HB/PCBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-ADRV904x.html>` is, by definition an "FPGA mezzanine card" (FMC), that means it needs a carrier to plug into. The carrier we currently support is:

========================================== ================
Board                                      ADRV904x-HB/PCBZ
========================================== ================
`ZCU102 <https://www.xilinx.com/ZCU102>`_  √
========================================== ================

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
