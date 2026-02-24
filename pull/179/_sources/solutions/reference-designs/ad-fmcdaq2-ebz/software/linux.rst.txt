.. _ad-fmcdaq2-ebz linux:

AD-FMCDAQ2-EBZ Linux Support
==============================

Analog Devices provides full Linux support for the AD-FMCDAQ2-EBZ. Depending on
which FPGA platform you are using the steps to perform to setup the system
slightly differ:

- :doc:`KCU105, KC705, VC707 (Microblaze) <linux/microblaze>`
- :doc:`ZC706 (Zynq) <linux/zynq>`

Descriptions of the individual Linux device drivers for the different parts on
the AD-FMCDAQ2-EBZ can be found at:

- :git-linux:`AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29
  LVCMOS Outputs <drivers/iio/frequency/ad9523.c>`
- AD9680: 14-BIT, 1000 MSPS JESD204B, Dual Analog-to-Digital Converter
- AD9144: Quad, 16-BIT, 2.8 GSPS, TxDAC+ Digital-to-Analog Converter
- :git-linux:`JESD204B/C Transmit Linux Driver
  <drivers/iio/jesd204/axi_jesd204_tx.c>`:
  Linux driver for the JESD204B transmit core.
- :git-linux:`JESD204B/C Receive Linux Driver
  <drivers/iio/jesd204/axi_jesd204_rx.c>`:
  Linux driver for the JESD204B receive core.
- :git-linux:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver
  <drivers/iio/jesd204/axi_adxcvr.c>`
