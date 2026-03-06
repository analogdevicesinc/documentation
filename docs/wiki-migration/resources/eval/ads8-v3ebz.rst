ADS8-V3EBZ HIGH SPEED CARRIER CARD
==================================

Preface
-------

The :adi:`ADS8-V3 <ADS8-V1EBZ>` Carrier Card was developed to support the evaluation of Analog Devices High Speed Data Converters with serial line rates up to 16Gbps. This Wiki site provides a high level overview of the platform. The ADS8-V3 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS8-V3 is not intended to be used as a general purpose development platform, and no support is available for standalone operation. The ADS8-V3 may contain hardware features not fully productized or supported by our default customer evaluation configurations. Please refer to Xilinx and its approved distributors for general purpose FPGA Development Kits.

ADS8-V3EBZ Features
-------------------

1. Xilinx Kintex Ultrascale XCKU040-3FFVA1156E FPGA.

2. One (1) FMC+ connector.

3. Twenty (20) 16Gbps transceivers supported by one (1) FMC+ connector.

4. DDR4 SDRAM.

5. Simple USB 3.0 port interface.


|image1|

.. container:: centeralign

   *Figure 1. ADS8-V3EBZ High Speed Carrier Card (Top)*


   |image2|

.. container:: centeralign

   *Figure 2. ADS8-V3EBZ High Speed Carrier Card (Bottom)*


| 
| ====== Using the ADS8-V3EBZ to evaluate High Speed Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed converter evaluation board, the ADS8-V3EBZ works as a data generation and acquisition board. Designed to support the highest speed JESD204B converters, the FPGA on the ADS8-V3EBZ acts as the data and control interface. A typical test setup is shown below.
| |image3|

.. container:: centeralign

   *Figure 3. ADS8-V3EBZ connected to High Speed Converter Evaluation Board*


Helpful Documents
-----------------

-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Download Links
-----------------------

-  High Speed Converter SPI Control Software, :adi:`spicontroller.html <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/spicontroller.html>`
-  Analysis \| Control \| Evaluation (ACE) Software, :adi:`ace-software.html <en/design-center/evaluation-hardware-and-software/ace-software.html>`

Design and Integration Files
----------------------------

-  Artwork Archive: `09-064925-01a.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/09-064925-01a.zip>`__
-  Assembly Archive: `01-064925-01a.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/01-064925-01a.zip>`__
-  BOM Archive: `05-064925-01-a.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/05-064925-01-a.zip>`__
-  BRD Archive: `08_064925a.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/08_064925a.zip>`__
-  Schematic Archive: `02-064925-01-a.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/02-064925-01-a.zip>`__

| Data sheets and user guides provide additional product specific information and should be consulted when using high speed converter evaluation boards. All documents and software tools are available at :adi:`High Speed Converter Eval Boards <hsadcevalboard>`. For additional information or questions, visit our High-Speed ADC and DAC Ezone Support Portal at :ez:`Data Converters EngineerZone <data_converters>` or call 1-800-ANALOGD.

ADS8-V3EBZ Supported Evaluation Boards
--------------------------------------

| Refer to the Analog Devices High Speed Converter evaluation board product page at :adi:`High Speed Converter Eval Boards <hsadcevalboard>` for a table of ADS8-V3EBZ compatible evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads8-v3ebztop-web.gif
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads8-v3ebzbottom-web.gif
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/ads8v2.png
   :width: 600px
