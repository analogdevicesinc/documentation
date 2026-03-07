ADS7-V1EBZ HIGH SPEED EVALUATION BOARD
======================================

<fc #ff0000>**\* Please note the ADS7-V1EBZ is obsolete and no longer manufactured or supported by Analog Devices. All High Speed ADC Products previously using the ADS7-V1EBZ have migrated to the newer ADS7-V2EBZ Evaluation Platform \***</fc>

Preface
-------

| The :adi:`ADS7-V1 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS7-V1>` Evaluation Board was developed to support the evaluation of Analog Devices high speed A/D converters, D/A converters and Transceivers with JESD204B bit rates up to 12.5 Gbps. This Wiki site provides a high level overview of the platform. In addition, each use case of the board has its own section (e.g. Using the ADS7-V1 for HIgh Speed A/D Converter Evaluation). The ADS7-V1 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS7-V1 is not intended to be used as a development platform, and no support is available for standalone operation. Please refer to Xilinx and its approved distribuitors for FPGA Development Kits.

ADS7-V1 Features
----------------

1. Xilinx Virtex-7 XC7VX690T-FFG1761 FPGA (693,120 logic cells).

2. Two(2) FMC-HPC connectors.

3. Ten(10) 13.1 Gbps transceivers per FMC-HPC connector.

4. Two(2) DDR3-1866 DIMMs.

5. Simple USB port interface (2.0).

| |image1|

.. container:: centeralign

   *Figure 1. ADS7-V1EBZ High Speed Evaluation Board*


| ====== Using the ADS7-V1EBZ to evaluate High Speed A/D Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed adc evaluation board, the ADS7-V1 works as a data acquistion board. Designed to support the highest speed JESD204B A/D Converters, the FPGA on the ADS7-V1 acts as the data receiver, while the ADC is the data transmitter. A typical test setup is shown below.
| |image2|

.. container:: centeralign

   *Figure 2. ADS7-V1 connected to High Speed A/D Converter Evaluation Board*


| The ADC data sheets and User Guides provide additional product specific information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`High Speed ADC Eval Boards <hsadcevalboard>`. For additional information or questions, send an email to highspeed.converters@analog.com.

ADS7-V1EBZ Supported ADC Evaluation Boards
------------------------------------------

| Refer to the Analog Devices High Speed ADC capture board product page at :adi:`High Speed ADC Eval Boards <hsadcevalboard>` for a table of ADS7-V1EBZ compatible ADC evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ADS7V1 Photo.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ad9680_setup_new_smaller.jpg
   :width: 600px
