Prerequisites for AD9371 based boards
=====================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

-  The AD9371 based card.
-  A carrier platform. ADI does not offer these boards for sale or loan, getting
   one yourself is normal part of development or evaluation of the AD9371. Our
   recommended carriers (the ones we use all the time) are either:

   -  The `Xilinx ZC706 <https://www.xilinx.com/zc706>`_. The fabric on this device is much larger, and if you are looking at targeting - this is the recommended option.
   -  There are a few more boards, which do work, but are currently not yet
      supported. The experience of the fabric only solutions is very close to
      the ARM/FPGA SoC based solutions, but the GUI runs on a host PC (Windows
      or Linux).

::

     *

.. note::

   See `quickstart <https://wiki.analog.com/quickstart#supported_carriers>`_

-   some way to interact with the platform,

   -  for the ARM/FPGA SoC platforms, this normally includes:

      -  HDMI monitor (1080p is best) or VGA Monitor
      -  USB Keyboard
      -  USB Mouse

   -  for the FPGA only solutions, this includes:

      -  LAN cable (Ethernet)
      -  Host PC (Windows or Linux)

-  Internet connection (without proxies makes things much easier) to update the scripts/binaries on the SD Card that came with the ADI FMC Card. (Firewalls are OK, proxies make things a pain).
-  RF Test equipment
