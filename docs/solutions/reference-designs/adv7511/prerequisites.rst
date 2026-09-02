.. _adv7511 prerequisites:

Prerequisites
===============================================================================

What you need, depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. One of the ADV7511-equipped evaluation boards:

   - :xilinx:`Artix-7 AC701 <ac701>`
   - :xilinx:`Kintex-7 KC705 <kc705>`
   - :xilinx:`Virtex-7 VC707 <vc707>`
   - :xilinx:`Zynq ZC702 <zc702>`
   - :xilinx:`Zynq ZC706 <zc706>`
   - `ZedBoard <https://digilent.com/shop/zedboard-zynq-7000-arm-fpga-soc-development-board>`__

   The ADV7511 HDMI transmitter is integrated on-board these evaluation
   platforms.

#. Some way to interact with the FPGA platform:

   #. For the ARM/FPGA SoC platforms (ZC702, ZC706, ZED), this normally includes:

      - HDMI monitor (to view the output)
      - USB Keyboard
      - USB Mouse
      - UART cable (for serial console, baud rate 115200)

   #. For the FPGA-only solutions (AC701, KC705, VC707), this includes:

      - HDMI monitor (to view the output)
      - JTAG cable (for programming)
      - UART cable (for serial console, baud rate 115200)
      - Host PC (Windows or Linux)

#. Internet connection (without proxies makes things much easier) to download
   the necessary files and update scripts/binaries.
#. HDMI Monitor (required for display output)
#. An SD card with at least 16GB of memory (for Zynq platforms using Linux)

Software prerequisites
-------------------------------------------------------------------------------

Normally, for basic functionalities regarding HDMI video output and software
development, you will need the following:

For no-OS:
~~~~~~~~~~

**Regarding the project:**

The no-OS software reference design uses the ADV7511 Transmitter Library,
which provides APIs for configuring the HDMI TX hardware without low-level
register access. The library also provides interrupt service routines, HDCP
high-level control, and status information.

The no-OS driver performs the following:

#. Initializes the HDMI core
#. Initializes the ADV7511
#. Transmits to an HDMI monitor an image whose resolution can be changed by
   typing a number from 0 to 6 in the terminal
#. Transmits audio to the HDMI monitor

- :git-no-OS:`projects/adv7511`

**For development:**

#. :adi:`ADV7511 HDMI Transmitter Library <media/en/dsp-hardware-software/software-modules/ADV7511_API_Library.exe>`
   (Windows executable - requires Wine on Linux)
#. AMD Xilinx Vivado and Vitis (if building from source)
#. UART terminal (Putty/Tera Term/Minicom, etc.) - baud rate 115200 (8N1)

For Linux (Zynq platforms):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   If on Linux you would need Wine or similar compatibility layers for Windows
   to install the ADV7511 HDMI Transmitter Library.

**Regarding the project:**

The ADV7511 Linux driver is implemented as a DRM (Direct Rendering Manager)
encoder bridge driver. In a typical board design the ADV7511 is used as an
HDMI encoder frontend for a SoC or FPGA with a graphics core. Implementing
the driver as a DRM bridge allows it to be reused across different platforms.

The driver also supports audio via HDMI by implementing an ASoC codec driver,
enabling reuse across a variety of platforms.

The driver is mainlined in the Linux kernel:

- :git-linux:`DRM bridge driver <drivers/gpu/drm/bridge/adv7511>`

Supported devices:

- :adi:`ADV7511`
- :adi:`ADV7511W`
- :adi:`ADV7513`
- :adi:`ADV7533`
- :adi:`ADV7535`

**Kernel Configuration:**

The ADV7511 driver depends on ``CONFIG_DRM`` and ``CONFIG_I2C``.
Enable it under:

.. code-block:: text

   Device Drivers  --->
       Graphics support  --->
           <*> Direct Rendering Manager  --->
           ...
           <*> ADV7511 encoder

**For development:**

#. :external+kuiper:doc:`Kuiper Linux <index>` image (for SD card)
#. AMD Xilinx Vivado and Vitis (if building from source)
#. UART terminal (Putty/Tera Term/Minicom, etc.) - baud rate 115200 (8N1)

.. note::

   :adi:`ADI <>` does not offer FPGA carrier platforms for sale or loan;
   getting one yourself is the normal part of development or evaluation.