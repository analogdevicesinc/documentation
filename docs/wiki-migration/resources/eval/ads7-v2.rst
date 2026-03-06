ADS7-V2EBZ HIGH SPEED EVALUATION BOARD
======================================

Preface
-------

The :adi:`ADS7-V2 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS7-V2>` Evaluation Board was developed to support the evaluation of Analog Devices high speed A/D converters, D/A converters and Transceivers with JESD204B bit rates up to 12.5 Gbps. This Wiki site provides a high level overview of the platform. In addition, each use case of the board has its own section (e.g. Using the ADS7-V2 for High Speed A/D Converter Evaluation). The ADS7-V2 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS7-V2 is not intended to be used as a development platform, and no support is available for standalone operation. Please refer to Xilinx and its approved distributors for FPGA Development Kits.

| Additional DAC specific :adi:`ADS7-V2 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS7-V2>` Applications Support is available at :doc:`/wiki-migration/resources/eval/dpg/ads7`

ADS7-V2EBZ Features
-------------------

1. Xilinx Virtex-7 XC7VX330T-3FFG1157E FPGA (326,400 logic cells).

2. One (1) FMC-HPC connector.

3. Ten (10) 13.1 Gbps transceivers supported by one(1) FMC-HPC connector.

4. Two (2) DDR3-1866 DIMMs.

5. Simple USB port interface (2.0).

| |image1|

.. container:: centeralign

   *Figure 1. ADS7-V2EBZ High Speed Evaluation Board*


| ====== Using the ADS7-V2EBZ to evaluate High Speed A/D Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed adc evaluation board, the ADS7-V2 works as a data acquistion board. Designed to support the highest speed JESD204B A/D Converters, the FPGA on the ADS7-V2 acts as the data receiver, while the ADC is the data transmitter. A typical test setup is shown below.
| |image2|

.. container:: centeralign

   *Figure 2. ADS7-V2 connected to High Speed A/D Converter Evaluation Board*


Helpful Documents
-----------------

-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*

Software Download Links
-----------------------

-  ACE, Evaluation Software for many converters, :adi:`ace-software.html <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html>`
-  High Speed ADC SPI Control Software, :adi:`spicontroller.html <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/spicontroller.html>`
-  High Speed ADC VisualAnalog Software, :adi:`visualanalog.html <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/visualanalog.html>`

Design and Integration Files
----------------------------

-  Schematic, BOM, Gerber & Cadence BRD File Archive, `ads7-v2ebz_13052_revc_design_files.zip <https://wiki.analog.com/_media/resources/eval/ads7-v2ebz_13052_revc_design_files.zip>`__

| The ADC data sheets and User Guides provide additional product specific information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`High Speed ADC Eval Boards <hsadcevalboard>`. For additional information or questions, send an email to highspeed.converters@analog.com.

ADS7-V2EBZ Supported ADC Evaluation Boards
------------------------------------------

| Refer to the Analog Devices High Speed ADC capture board product page at :adi:`High Speed ADC Eval Boards <hsadcevalboard>` for a table of ADS7-V2EBZ compatible ADC evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ADS7-V2EBZ.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/AD9680_ADS7-V2EBZ_Setup.jpg
   :width: 600px
