AXI_HDMI_RX IP core
===================

.. important::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/axi_hdmi_rx/index.html\


The :git-hdl:`library/axi_hdmi_rx` IP core can be used to interface the :adi:`ADV7611` device using an FPGA.

Features
--------

-  AXI based configuration
-  Supports multiple resolution (max 1080p)
-  Supports embedded sync video reception (16bit data)
-  YCbCr or RGB color space output
-  Supported on FMC-IMAGEON Xilinx Reference Design

Block Diagram
-------------

.. image:: https://wiki.analog.com/_media/resources/fpga/docs/hdl/axi_hdmi_rx_core_3.svg

Configuration Parameters
------------------------

+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| Name               | Description                                                                                                                                  | Default Value |
+====================+==============================================================================================================================================+===============+
| ``​ID``\ ​         | Core ID should be unique for each axi_hdmi_rx IP in the system                                                                               | 0             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------+
| ``IO_INTERFACE``   | Type of the IO interface. 0 - Allow sampling of data on falling edge of the HDMI clock. others - always sample the input data on rising edge | 1             |
+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------+

Interfaces
----------

+--------------------------+------------------------------------+---------------------+-----------------------+
| Interface                | Pin                                | Type                | Description           |
+==========================+====================================+=====================+=======================+
| ``HDMI interfaces part`` | \*\* HDMI interface signals \*\*   |                     |                       |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_clk ''                     | '' input ''         | pixel clock           |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_rx_data ''                 | '' input [15:0] ''  | hdmi data             |
+--------------------------+------------------------------------+---------------------+-----------------------+
| ``DMA interface``        | \*\* DMA Write FIFO interface \*\* |                     |                       |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_clk''                      | '' output ''        | Output clock signal   |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_dma_sof ''                 | '' output ''        | start of frame        |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_dma_de ''                  | '' output ''        | data enable           |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_dma_data ''                | '' output [63:0] '' | HDMI DMA data         |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_dma_ovf ''                 | '' input ''         | data overflow signal  |
+--------------------------+------------------------------------+---------------------+-----------------------+
|                          | '' hdmi_dma_unf ''                 | '' input ''         | data underflow signal |
+--------------------------+------------------------------------+---------------------+-----------------------+
| '' s\_ axi ''            | \*\* AXI Memory Map interface \*\* |                     |                       |
+--------------------------+------------------------------------+---------------------+-----------------------+

Detailed description
--------------------

| The top module, axi_hdmi_rx, instantiates:
| \* axi_hdmi_rx_core module
| \* the HDMI RX register map
| \* the AXI handling interface
| In axi_hdmi_rx_core module, the video information is manipulated by passing through more processing blocks (see `#block_diagram <https://wiki.analog.com/>`_):

-  Embedded Sync module acquires the video information and splits it into video data and synchronization signals.
-  Chroma supersampling block, super samples the video information to obtain a 24 bit video information, has no impact on the video quality.
-  CSC (Color Space Conversion) –converts the video information from YCbCr color space to RGB color space. If YCbCr is the desired output color space the CSC block can be bypassed by setting to 1 the value of CSC_BYPASS in REG_CNTRL register.
-  Sync monitoring - monitors the recovered hsync and vsync against the programmed expected resolution. Asserts out of sync and resoulutions mismatch indicators in the ``REG_TPM_STATUS2`` regsiter.

Design considerations
---------------------

Additional IPs needed
~~~~~~~~~~~~~~~~~~~~~

-  :doc:`axi_dmac </wiki-migration/resources/fpga/docs/axi_dmac>`
-  axi_spdif_tx (audio)

| The axi_dmac is used to get the video information from the core into memory. The audio path is separated from the video path, for **audio axi_spdif_tx** core (:git-hdl:`library/axi_spdif_tx`) is needed to receive the audio information from the ADV7611 device and transmit it to the memory. The whole system needs to be controlled by a processor (ARM or a softcore) that can program the registers.

Example design
~~~~~~~~~~~~~~

The core is used to interface the :adi:`ADV7611 <media/en/technical-documentation/data-sheets/ADV7611.pdf>` located on the FMC IMAGEON board. Although the device support multiple pixel output formats, the core is supporting just the 16-bit 4:2:2 in SDR mode.

-  :git-hdl:`IMAGEON HDL project <projects/imageon>`

Register Map
------------

.. include:: hdl/regmap.rst

Software support
----------------

The core can be controlled by Linux or no-Os

-  :doc:`Xilinx Reference Design </wiki-migration/resources/fpga/xilinx/fmc/fmc-imageon>`
-  :git-linux:`ADV7604, ADV7611, ADV7612 <drivers/media/i2c/adv7604.c>`

References
----------

-  :doc:`FMC-IMAGEON Xilinx Reference Design </wiki-migration/resources/fpga/xilinx/fmc/fmc-imageon>`
-  :git-hdl:`axi_hdmi_rx core <library/axi_hdmi_rx>`
-  :git-hdl:`Imageon project <projects/imageon>`
-  :doc:`Zynq & Altera SoC Quick Start Guide </wiki-migration/resources/tools-software/linux-software/kuiper-linux>`

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#ip_cores
   :alt: IP cores#hdl|Main page#tips|Using and modifying the HDL design
