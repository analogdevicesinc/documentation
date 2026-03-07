ADS8-V1EBZ HIGH SPEED EVALUATION BOARD
======================================

Preface
-------

The :adi:`ADS8-V1 <en/content/CU_High-Speed_ADC_FIFO_evaluation_tools/fca.html#ADS8-V1>` Evaluation Board was developed to support the evaluation of Analog Devices High Speed Data Converters with JESD204B bit rates up to 16Gbps. This Wiki site provides a high level overview of the platform. In addition, each use-case of the board has its own section (e.g. Using the ADS8-V1 for High Speed A/D Converter Evaluation). The ADS8-V1 is intended to be used only with specified Analog Devices Evaluation Boards. The ADS8-V1 is not intended to be used as a general purpose development platform, and no support is available for standalone operation. The ADS8-V1 may contain hardware features not fully productized or supported by our default customer evaluation configurations. Please refer to Xilinx and its approved distributors for general purpose FPGA Development Kits.

ADS8-V1EBZ Features
-------------------

1. Xilinx Kintex Ultrascale XCKU040-3FFVA1156E FPGA.

2. One (1) FMC+ connector.

3. Twenty (20) 16Gbps transceivers supported by one (1) FMC+ connector.

4. DDR4 SDRAM.

5. Simple USB 3.0 port interface.


|image1|

.. container:: centeralign

   *Figure 1. ADS8-V1EBZ High Speed Evaluation Board (Top)*


   |image2|

.. container:: centeralign

   *Figure 2. ADS8-V1EBZ High Speed Evaluation Board (Bottom)*


| 
| ====== Using the ADS8-V1EBZ to evaluate High Speed A/D Converters ======

Overview
--------

| When connected to a specified Analog Devices high speed adc evaluation board, the ADS8-V1 works as a data acquistion board. Designed to support the highest speed JESD204B A/D Converters, the FPGA on the ADS8-V1 acts as the data receiver, while the ADC is the data transmitter. A typical test setup is shown below.
| |image3|

.. container:: centeralign

   *Figure 3. ADS8-V1 connected to High Speed A/D Converter Evaluation Board*


Helpful Documents
-----------------

-  :adi:`AN-905 Application Note <an-905>`, *VisualAnalog Converter Evaluation Tool Version 1.0 User Manual*
-  :adi:`AN-878 Application Note <an-878>`, *High Speed ADC SPI Control Software*
-  :adi:`AN-877 Application Note <an-877>`, *Interfacing to High Speed ADCs via SPI*
-  :adi:`AN-835 Application Note <an-835>`, *Understanding ADC Testing and Evaluation*
-  `ads8-v1_triggered_capture.pdf <https://wiki.analog.com/_media/resources/eval/ads8-v1_triggered_capture.pdf>`_, *ADS8-V1 Triggered Capture*

Software Download Links
-----------------------

-  High Speed ADC SPI Control Software, :adi:`spicontroller.html <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/spicontroller.html>`
-  High Speed ADC VisualAnalog Software, :adi:`visualanalog.html <en/design-center/advanced-selection-and-design-tools/interactive-design-tools/visualanalog.html>`
-  Analysis \| Control \| Evaluation (ACE) Software, :adi:`ace-software.html <en/design-center/evaluation-hardware-and-software/ace-software.html>`

Design and Integration Files
----------------------------

-  Schematic, BOM, & Cadence BRD File Archive, `20_041151d.zip <https://wiki.analog.com/_media/resources/eval/20_041151d.zip>`_

| The ADC data sheets and User Guides provide additional product specific information and should be consulted when using the evaluation board. All documents and software tools are available at :adi:`High Speed ADC Eval Boards <hsadcevalboard>`. For additional information or questions, send an email to highspeed.converters@analog.com.

ADS8-V1EBZ Supported ADC Evaluation Boards
------------------------------------------

| Refer to the Analog Devices High Speed ADC capture board product page at :adi:`High Speed ADC Eval Boards <hsadcevalboard>` for a table of ADS8-V1EBZ compatible ADC evaluation boards.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ads8-v1ebztop.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ads8-v1ebzbottom.jpg
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ADS8-V1EBZ-AD9208 Typ Setup.png
   :width: 600px
