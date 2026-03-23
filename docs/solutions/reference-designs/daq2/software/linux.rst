AD-FMCDAQ2-EBZ Linux support
============================

.. image:: ../images/tux.png
   :align: right

Analog Devices provides full Linux support for the AD-FMCDAQ2-EBZ. Depending on
which FPGA platform you are using the steps to perform to setup the system
slightly differ:

-  :doc:`KCU105, KC705, VC707 (Microblaze) </solutions/reference-designs/daq2/software/linux/microblaze>`
-  :doc:`ZC706 (Zynq) </solutions/reference-designs/daq2/software/linux/zynq>`

Descriptions of the individual Linux device drivers for the different parts on
the AD-FMCDAQ2-EBZ can be found at:

-  `AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29 LVCMOS Outputs <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/ad9523>`_
-  `AD9680: 14-BIT, 1000 MSPS JESD204B, DUAL ANALOG-TO-DIGITAL CONVERTER <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`_
-  `AD9144: QUAD, 16-BIT, 2.8 GSPS, TxDAC+® DIGITAL-TO-ANALOG CONVERTER <https://wiki.analog.com/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`_
-  `JESD204B/C Transmit Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`_: Linux driver for the JESD204B transmit core.
-  `JESD204B/C Receive Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`_: Linux driver for the JESD204B receive core.
-  `JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver <https://wiki.analog.com/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`_
