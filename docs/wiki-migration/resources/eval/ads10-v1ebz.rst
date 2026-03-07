ADS10-V1EBZ HIGH SPEED CARRIER CARD
===================================

Preface
-------

The :adi:`ADS10-V1EBZ <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/ADS10-V1EBZ.html>` Carrier Card was developed to support the evaluation of Analog Devices High Speed Data Converters with serial line rates up to 32.5Gbps. This Wiki site provides a high level overview of the platform. The ADS10-V1 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS10-V1 is not intended to be used as a general purpose development platform, and no support is available for standalone operation. The ADS10-V1 may contain hardware features that are not fully productized or supported by our default customer evaluation configurations. Please refer to Xilinx and its approved distributors for general purpose FPGA Development Kits if needed.

ADS10-V1EBZ Features
--------------------

1. Xilinx Virtex Ultrascale+ XCVU35P-3FSHV2892E FPGA.

2. One (1) FMC+ connector.

3. Twenty (24) 32.75Gbps transceivers supported by one (1) FMC+ connector.

4. On-board HBM DRAM in FPGA.

5. Simple USB 3.0 port interface.

6. Two (2) Micro SD cards are included: for "TRX" evaluation boards and "HSX" evaluation boards.


|image1|

.. container:: centeralign

   *Figure 1. ADS10-V1EBZ High Speed Carrier Card (Top)*


   |image2|

.. container:: centeralign

   *Figure 2. ADS10-V1EBZ High Speed Carrier Card (Bottom)*


| 
| ====== Using the ADS10-V1EBZ to evaluate High Speed Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed converter evaluation board, the ADS10-V1EBZ works as a data generation and acquisition board. Designed to support the highest speed JESD204B/C converters, the FPGA on the ADS10-V1EBZ acts as the data and control interface. An example test setup is shown below.
| |image3|

.. container:: centeralign

   *Figure 3. ADS10-V1EBZ connected to High Speed Converter Evaluation Board*


Helpful Documents
-----------------

-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Download Links
-----------------------

-  Analysis \| Control \| Evaluation (ACE) Software can be requested via the applicable high-speed converter product webpage.

Design and Integration Files
----------------------------

-  Artwork Archive: `ART-09-053489-01C.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ART-09-053489-01C.zip>`_
-  Assembly Archive: `ASY-01-053489-01C.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ASY-01-053489-01C.zip>`_
-  BOM Archive: `BOM-05-053489-01-f.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/BOM-05-053489-01-f.zip>`_
-  BRD Archive: `BRD-08-053489c.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/BRD-08-053489c.zip>`_
-  Schematic Archive: `SCH-02-053489-01-f-1.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/SCH-02-053489-01-f-1.zip>`_
-  Kit Contents Archive: `KIT-053489-01-f.zip <https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/KIT-053489-01-f.zip>`_

| Data sheets and user guides provide additional product specific information and should be consulted when using high speed converter evaluation boards. All documents and software tools are available at :adi:`High Speed Converter Eval Boards <hsadcevalboard>`. For additional information or questions, visit our High-Speed ADC and DAC Ezone Support Portal at :ez:`Data Converters EngineerZone <data_converters>` or call 1-800-ANALOGD.

ADS10-V1EBZ Supported Evaluation Boards
---------------------------------------

| Refer to the Analog Devices High Speed Converter evaluation board product page at :adi:`High Speed Converter Eval Boards <hsadcevalboard>` for a table of ADS10-V1EBZ compatible evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads10-v1ebztop.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads10-v1ebzbottom.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/fpga/xilinx/adsx/ads10.png
   :width: 600px
