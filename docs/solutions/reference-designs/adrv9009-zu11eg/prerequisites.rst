.. _adrv9009-zu11eg prerequisites:

Prerequisites
==============

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

- The :adi:`ADRV9009-ZU11EG` SoM board
- The :adi:`ADRV2CRR-FMC` carrier board

   .. note::

      If you want to use it with :adi:`FMCOMMS8`, please refer to
      :dokuwiki:`FMCOMMS8 Quick Start Guide <resources/eval/user-guides/ad-fmcomms8-ebz/quick-start-guide>`.

Required Software
-----------------

- SD Card 16GB image using the instructions here:
  :dokuwiki:`Zynq & Altera SoC Quick Start Guide <https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux>`
- A UART terminal (Putty/Tera Term/Minicom, etc.), Baud rate 115200 (8N1).

.. note::

   Instructions on how to build the ZynqMP/ MPSoC Linux kernel and devicetrees
   from source can be found here:

   - :ref:`Building the ZynqMP/ MPSoC Linux kernel and devicetrees from source <linux-kernel zynqmp>`
   - :external+hdl:ref:`How to build the ZynqMP boot image BOOT.BIN <build_boot_bin>`

Required Hardware
-----------------

- :adi:`ADRV9009-ZU11EG` SoM board
- :adi:`ADRV2CRR-FMC` carrier board
- Micro-USB cable
- Ethernet cable
- Power Supply

Optional Hardware
-----------------

- Reference clock source
- USB Type-C multiport HUB
- USB keyboard and mouse
- DisplayPort compatible monitor
