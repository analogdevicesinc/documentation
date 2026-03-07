Prerequisites for AD9361/AD9364 based boards
============================================

What you need, depends on what you are trying to do. As a minimum, you need to start out with:

-  The AD9361/AD9364 based card. To determine which card is best for you, check out the `introduction <https://wiki.analog.com/introduction>`_ section.
-  A carrier platform. ADI does not offer these boards for sale or loan, getting one yourself is normal part of development or evaluation of the AD9361/AD9364. Our recommended carriers (the ones we use all the time) are either:

   -  The `ZedBoard <http://zedboard.org/product/zedboard>`_. This is a low cost board, which can be used for basic HDL designs, or just for looking at the AD9361/AD9364. Most of our software and RF developers have this board.
   -  The `Xilinx ZC706 <https://www.xilinx.com/zc706>`_. The fabric on this device is much larger, and if you are looking at targeting - this is the recommended option.
   -  The `Arrow SoCKit <https://www.arrow.com/en/products/sockit/arrow-development-tools>`_. This is a low cost board, which can be used for basic HDL designs, or just for looking at the AD9361.
   -  There are a few more boards, which do work, and are supported, but they are just not tested as often (most of the full time developers who work with the AD9361/AD9364 based boards use the Zed or the ZC706). The experience of the fabric only solutions is very close to the ARM/FPGA SoC based solutions, but the GUI runs on a host PC (Windows or Linux).
   -  
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
