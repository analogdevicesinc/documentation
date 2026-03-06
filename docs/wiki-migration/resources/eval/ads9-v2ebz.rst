ADS9-V2EBZ HIGH SPEED CARRIER CARD
==================================

Preface
-------

The :adi:`ADS9-V2EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADS9-V2EBZ.html>` Carrier Card was developed to support the evaluation of Analog Devices High Speed Data Converters with serial line rates up to 28Gbps. This Wiki site provides a high level overview of the platform. The ADS9-V2 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS9-V2 is not intended to be used as a general purpose development platform, and no support is available for standalone operation. The ADS9-V2 may contain hardware features that are not fully productized or supported by our default customer evaluation configurations. Please refer to Xilinx and its approved distributors for general purpose FPGA Development Kits if needed.

ADS9-V2EBZ Package Contents
---------------------------

1. ADS9-V2EBZ board

2. Avnet MicroZed daughter board

3. Two MicroSD cards.

4. 12V 200 W AC/DC External Desktop (Class I) Adapter with Power Cord

5. CAT5E Ethernet and USB3 Cables

6. USB to Ethernet Adapter

ADS9-V2EBZ Features
-------------------

1. Xilinx Kintex Ultrascale+ XCKU15P-2FFVE1517E FPGA.

2. One (1) FMC+ connector.

3. Twenty (20) 28Gbps transceivers supported by one (1) FMC+ connector.

4. HMC Gen2 DRAM.

5. Simple USB 3.0 port interface.

6. Two (2) Micro SD cards are included: "TRX" for ADRV9026 evaluation boards and "HSX" for MxFE(tm) evaluation boards.


|image1|

.. container:: centeralign

   *Figure 1. ADS9-V2EBZ High Speed Carrier Card (Top)*


   |image2|

.. container:: centeralign

   *Figure 2. ADS9-V2EBZ High Speed Carrier Card (Bottom)*


| 
| ====== Using the ADS9-V2EBZ to evaluate High Speed Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed converter evaluation board, the ADS9-V2EBZ works as a data generation and acquisition board. Designed to support the highest speed JESD204B/C converters, the FPGA on the ADS9-V2EBZ acts as the data and control interface. A typical test setup is shown below.
| |image3|

.. container:: centeralign

   *Figure 3. ADS9-V2EBZ connected to High Speed Converter Evaluation Board*


Helpful Documents
-----------------

-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Download Links
-----------------------

-  Analysis \| Control \| Evaluation (ACE) Software, :adi:`ace-software.html <en/design-center/evaluation-hardware-and-software/ace-software.html>`

Design and Integration Files
----------------------------

-  Artwork Archive: `ART-09-045361-01C.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ART-09-045361-01C.zip>`__
-  Assembly Archive: `ASY-01-045361-01C.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ASY-01-045361-01C.zip>`__
-  BOM Archive: `BOM-05-045361-01-e.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/BOM-05-045361-01-e.zip>`__
-  BRD Archive: `BRD-08_045361c.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/BRD-08_045361c.zip>`__
-  Schematic Archive: `SCH-02-045361-01-e.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/SCH-02-045361-01-e.zip>`__

| Data sheets and user guides provide additional product specific information and should be consulted when using high speed converter evaluation boards. All documents and software tools are available at :adi:`High Speed Converter Eval Boards <hsadcevalboard>`. For additional information or questions, visit our High-Speed ADC and DAC Ezone Support Portal at :ez:`Data Converters EngineerZone <data_converters>` or call 1-800-ANALOGD.

ADS9-V2EBZ Supported Evaluation Boards
--------------------------------------

| Refer to the Analog Devices High Speed Converter evaluation board product page at :adi:`High Speed Converter Eval Boards <hsadcevalboard>` for a table of ADS9-V2EBZ compatible evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads9-v2ebztop-web.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads9-v2ebzbottom-web.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/system.png
   :width: 600px
