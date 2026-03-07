JESD204 Interface Framework
===========================

.. warning::

   We are in the process of migrating our documentation to GitHubIO. This page is outdated and the new one can be found at https://analogdevicesinc.github.io/hdl/library/jesd204/index.html\


The JESD204, JESD204A, JESD204B and the JESD204C data converter serial interface standard was created through the JEDEC committee to standardize and reduce the number of data inputs/outputs between high-speed data converters and other devices, such as FPGAs (field-programmable gate arrays). Fewer interconnects simplifies layout and allows smaller form factor realization without impacting overall system performance. These attributes are important to address the system size and cost constraints of a range of high speed ADC applications, including wireless infrastructure (GSM, EDGE, W-CDMA, LTE, CDMA2000, WiMAX, TD-SCDMA) transceiver architectures, software-defined radios, portable instrumentation, medical ultrasound equipment, and Mil/Aero applications such as radar and secure communications. Analog Devices is an original participating member of the JEDEC JESD204 standards committee and we have concurrently developed compliant data converter technology and tools, and a comprehensive product roadmap to fully enable our customers to take advantage of this significant interfacing breakthrough.

Analog Devices supplies a full-stack supporting JESD204B/C which provides a fully integrated system level experience. This solution includes

.. admonition:: Download
   :class: download

   
   -  `Reference hardware platforms <https://wiki.analog.com/>`_ for rapid-prototyping
   -  `FPGA HDL <https://wiki.analog.com/>`_ for interfacing JESD204B/C ADCs, DACs, and RF Transceivers
   -  `Software <https://wiki.analog.com/>`_ to configure the converter devices and FPGA HDL peripherals
   


How to Obtain a License
-----------------------

When customers and partners download software from GitHub, or email downloaded software to someone, they are obligated to comply to the terms and conditions of the :git-hdl:`Software License Agreement <LICENSE_ADIJESD204>`. The core is released under two difference licenses. You may choose either:

-  **Commercial licenses** may be purchased from Analog Devices, Inc. or any authorized distributor by ordering :adi:`ADSW-JESD204-PRODLIC <en/resources/evaluation-hardware-and-software/embedded-development-software/jesd204-interface-framework.html>`. This license allows customers to use the core in a closed system.
-  **GPL 2**, this allows you to use the core for any purpose, but you must release anything else that links to the JESD204 core (this would normally be your algorithmic IP). You do not need to sign anything purchase anything to use the JESD204 core under the GPL license.

There is only one core, the only difference is the license and support.

If you have a question about the license: you can email <fc #6495ed>\ **jesd204-licensing@analog.com**\ </fc>

FPGA HDL Support
----------------

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204_layers2.png
   :align: right
   :width: 100px

The JESD204B/C standard defines multiple layers, each layer being responsible for a particular function. The Analog Devices JESD204B/C HDL solution follows the standard here and defines 4 layers. Physical layer, link layer, transport layer and application layer. For the first three layers Analog Devices provides standard components that can be linked up to provide a full JESD204B/C protocol processing chain.

Depending on the FPGA and converter combinations that are being interfaced different components can be chosen for the physical and transport layer. The FPGA defines which physical layer component should be used and the interfaced converter defines which transport layer component should be used.

The link layer component is selected based on the direction of the JESD204B/C link.

The application layer is user defined and can be used to implement application specific signal processing.

.. image:: https://wiki.analog.com/_media/resources/fpga/peripherals/jesd204_chain.png
   :align: center

Physical Layer
~~~~~~~~~~~~~~

Physical layer peripherals are responsible for interfacing and configuring the high-speed serial transceivers. Currently we have support for GTXE2, GTHE3, GTHE4, GTYE4 for Xilinx and Arria 10 transceivers for Intel.

-  `AXI_ADXCVR <https://wiki.analog.com/../docs/axi_adxcvr>`_: JESD204B Gigabit Transceiver Register Configuration Peripheral
-  `UTIL_ADXCVR <https://wiki.analog.com/../docs/util_xcvr>`_: JESD204B Gigabit Transceiver Interface Peripheral for Xilinx FPGAs

Link Layer
~~~~~~~~~~

Link layer peripherals are responsible for JESD204B/C protocol handling, including scrambling/descrambling, lane alignment, character replacement and alignment monitoring.

-  :doc:`JESD204B/C Transmit Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_tx>`: JESD204B/C Link Layer Transmit Peripheral
-  :doc:`JESD204B/C Receive Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/axi_jesd204_rx>`: JESD204B/C Link Layer Receive Peripheral

Transport Layer
~~~~~~~~~~~~~~~

Transport layer peripherals are responsible for converter specific data framing and de-framing.

-  :doc:`ADC JESD204B/C Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_adc>` : JESD204B/C Transport Layer Receive Peripheral
-  :doc:`DAC JESD204B/C Transport Peripheral </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_tpl_dac>` : JESD204B/C Transport Layer Transmit Peripheral

Interfaces
~~~~~~~~~~

Interfaces are a well-defined collection of wires that are used to communicate between components. The following interfaces are used to connect components of the HDL JESD204B/C processing stack.

Software Support
----------------

Linux
~~~~~

-  :doc:`JESD204 (FSM) Interface Linux Kernel Framework </wiki-migration/resources/tools-software/linux-drivers/jesd204/jesd204-fsm-framework>`
-  :doc:`JESD204B/C Transmit Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_tx>`: Linux driver for the JESD204B transmit core.
-  :doc:`JESD204B/C Receive Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_jesd204_rx>`: Linux driver for the JESD204B receive core.
-  :doc:`JESD204B/C AXI_ADXCVR Highspeed Transceivers Linux Driver </wiki-migration/resources/tools-software/linux-drivers/jesd204/axi_adxcvr>`
-  :doc:`JESD204B Statistical Eyescan Application </wiki-migration/resources/tools-software/linux-software/jesd_eye_scan>`
-  :doc:`JESD204B Status Utility </wiki-migration/resources/tools-software/linux-software/jesd_status>`
-  :doc:`AXI DAC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/axi-dac-dds-hdl>`

   -  :doc:`AD9172 DAC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-dds/ad9172>`
   -  :doc:`AD9081 MxFE Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
   -  :doc:`ADRV9009, ADRV9008 highly integrated, wideband RF transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
   -  :doc:`AD9371, AD9375 highly integrated, wideband RF transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`

-  :doc:`AXI ADC HDL Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/axi-adc-hdl>`

   -  :doc:`AD9208 ADC Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-adc/ad9208>`
   -  :doc:`AD9081 MxFE Linux Driver </wiki-migration/resources/tools-software/linux-drivers/iio-mxfe/ad9081>`
   -  :doc:`ADRV9009, ADRV9008 highly integrated, wideband RF transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/adrv9009>`
   -  :doc:`AD9371, AD9375 highly integrated, wideband RF transceiver Linux device driver </wiki-migration/resources/tools-software/linux-drivers/iio-transceiver/ad9371>`

No-OS
~~~~~

-  :doc:`ADI JESD204B/C AXI_ADXCVR Highspeed Transceivers No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/jesd204/axi_adxcvr>`
-  :doc:`ADI JESD204B/C Receive Peripheral No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/jesd204/axi_jesd204_rx>`
-  :doc:`ADI JESD204B/C Transmit Peripheral No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/jesd204/axi_jesd204_tx>`
-  :doc:`AXI ADC No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/jesd204/axi_adc_core>`
-  :doc:`AXI DAC No-OS Driver </wiki-migration/resources/tools-software/uc-drivers/jesd204/axi_dac_core>`

Tutorial
--------

-  :doc:`Introduction </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/introduction>`
-  :doc:`System Architecture </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/system_architecture>`
-  :doc:`Generic JESD204B block designs </wiki-migration/resources/fpga/docs/hdl/generic_jesd_bds>`. This will help you understand the generic blocks for the next steps.
-  Checkout the :doc:`HDL Source </wiki-migration/resources/fpga/docs/build>`, and then build either one of:

   -  :doc:`HDL Xilinx </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/hdl_xilinx>`
   -  :doc:`HDL Altera </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/hdl_altera>`

-  :doc:`Linux </wiki-migration/resources/fpga/peripherals/jesd204/tutorial/linux>`

Example Projects
----------------

-  :doc:`AD-FMCADC2-EBZ Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcadc2-ebz>`

   -  :git-hdl:`Xilinx VC707 <projects/fmcadc2/vc707>`
   -  :git-hdl:`Xilinx ZC706 <projects/fmcadc2/zc706>`

-  :doc:`AD-FMCADC3-EBZ Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcadc3-ebz>`

   -  :git-hdl:`Xilinx VC707 <projects/fmcadc2/vc707>`
   -  :git-hdl:`Xilinx ZC706 <projects/fmcadc2/zc706>`

-  :doc:`AD-FMCADC4-EBZ Reference Design (retired) </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcadc4-ebz>`

   -  :git-hdl:`Xilinx ZC706 <projects/fmcadc4/zc706>`

-  :doc:`AD-FMCJESDADC1-EBZ Reference Design </wiki-migration/resources/fpga/xilinx/fmc/ad-fmcjesdadc1-ebz>`

   -  :git-hdl:`Xilinx KC705 <projects/fmcjesdadc1/kc705>`
   -  :git-hdl:`Xilinx VC707 <projects/fmcjesdadc1/vc707>`
   -  :git-hdl:`Xilinx ZC706 <projects/fmcjesdadc1/zc706>`

-  :doc:`AD-FMCOMMS11-EBZ Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcomms11-ebz>`

   -  :git-hdl:`Xilinx ZC706 <projects/fmcomms11/zc706>`

-  :doc:`AD-FMCDAQ2-EBZ Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`

   -  :git-hdl:`Intel A10SOC <projects/daq2/a10soc>`
   -  :git-hdl:`Xilinx KC705 <projects/daq2/kc705>`
   -  :git-hdl:`Xilinx KCU105 <projects/daq2/kcu105>`
   -  :git-hdl:`Xilinx VC707 <projects/daq2/vc707>`
   -  :git-hdl:`Xilinx ZC706 <projects/daq2/zc706>`
   -  :git-hdl:`Xilinx ZCU102 <projects/daq2/zcu102>`

-  :doc:`AD-FMCDAQ3-EBZ Reference Design </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz>`

   -  :git-hdl:`Xilinx KCU105 <projects/daq3/kcu105>`
   -  :git-hdl:`Xilinx VCU118 <projects/daq3/vcu118>`
   -  :git-hdl:`Xilinx ZC706 <projects/daq3/zc706>`
   -  :git-hdl:`Xilinx ZCU102 <projects/daq3/zcu102>`

-  :doc:`ADRV9371 Reference Design </wiki-migration/resources/eval/user-guides/mykonos>`

   -  :git-hdl:`Intel A10SOC <projects/adrv9371x/a10soc>`
   -  :git-hdl:`Xilinx KCU105 <projects/adrv9371x/kcu105>`
   -  :git-hdl:`Xilinx ZC706 <projects/adrv9371x/zc706>`
   -  :git-hdl:`Xilinx ZCU102 <projects/adrv9371x/zcu102>`

-  :doc:`ADRV9009 Reference Design </wiki-migration/resources/eval/user-guides/adrv9009>`

   -  :git-hdl:`Xilinx ZCU102 <projects/adrv9009/zcu102>`

-  :doc:`ADRV9009-ZU11EG-SOM Reference Design </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg>`

   -  :git-hdl:`ADRV9009-ZU11EG-SOM <projects/adrv9009zu11eg>`

-  :doc:`AD917X Reference Design </wiki-migration/resources/eval/user-guides/ad-dac-fmc-ebz>`

   -  :git-hdl:`Intel A10SOC <projects/dac_fmc_ebz/a10soc>`
   -  :git-hdl:`Xilinx ZC706 <projects/dac_fmc_ebz/zc706>`
   -  :git-hdl:`Xilinx ZCU102 <projects/dac_fmc_ebz/zcu102>`

-  :doc:`AD9081 Reference Design </wiki-migration/resources/eval/user-guides/ad9081_fmca_ebz/ad9081_fmca_ebz_hdl>`

   -  :git-hdl:`Xilinx ZCU102 <projects/ad9081_fmca_ebz/zcu102>`
   -  :git-hdl:`Xilinx VCU118 <projects/ad9081_fmca_ebz/vcu118>`

Additional Information
----------------------

-  :doc:`JESD204B Glossary </wiki-migration/resources/fpga/peripherals/jesd204/jesd204_glossary>`

Technical Articles
~~~~~~~~~~~~~~~~~~

-  :adi:`JESD204B Survival Guide <media/en/technical-documentation/technical-articles/JESD204B-Survival-Guide.pdf>`
-  :adi:`Synchronizing Sample Clocks of a Data Converter Array <media/en/technical-documentation/technical-articles/Synchronizing-Sample-Clocks-of-a-Data-Converter-Array-Web.pdf>`

JESD204B Rapid Prototyping Platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-ADRV9371` (:doc:`User Guide </wiki-migration/resources/eval/user-guides/mykonos>`)
-  :adi:`EVAL-ADRV9008-9009` (:doc:`User Guide </wiki-migration/resources/eval/user-guides/adrv9009>`)
-  ADRV9009-ZU11EG (:doc:`User Guide </wiki-migration/resources/eval/user-guides/adrv9009-zu11eg>`)
-  :adi:`AD-FMCJESDADC1-EBZ`
-  :adi:`AD-FMCOMMS11-EBZ` (:doc:`User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms11-ebz>`)
-  :adi:`AD-FMCADC2-EBZ`
-  :adi:`AD-FMCADC3-EBZ <EVAL-AD-FMCADC3-EBZ>`
-  :adi:`AD-FMCADC4-EBZ <EVAL-AD-FMCADC4-EBZ>`\ (retired)
-  :adi:`AD-FMCDAQ2-EBZ` (:doc:`User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`)
-  :adi:`EVAL-FMCDAQ3-EBZ` (:doc:`User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz>`)
-  :adi:`EVAL-AD917X`

JESD204B Analog-to-Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`AD6673`: 80 MHz Bandwidth, Dual IF Receiver
-  :adi:`AD6674`: 385 MHz BW IF Diversity Receiver
-  :adi:`AD6676`: Wideband IF Receiver Subsystem
-  :adi:`AD6677`: 80 MHz Bandwidth, IF Receiver
-  :adi:`AD6684`: 135 MHz Quad IF Receiver
-  :adi:`AD6688`: RF Diversity and 1.2GHz BW Observation Receiver
-  :adi:`AD9208`: 14-Bit, 3GSPS, JESD204B, Dual Analog-to-Digital Converter
-  :adi:`AD9234`: 12-Bit, 1 GSPS/500 MSPS JESD204B, Dual Analog-to-Digital Converter
-  :adi:`AD9250`: 14-Bit, 170 MSPS/250 MSPS, JESD204B, Dual Analog-to-Digital Converter
-  :adi:`AD9625`: 12-Bit, 2.6 GSPS/2.5 GSPS/2.0 GSPS, 1.3 V/2.5 V Analog-to-Digital Converter
-  :adi:`AD9656`: Quad, 16-Bit, 125 MSPS JESD204B 1.8 V Analog-to-Digital Converter
-  :adi:`AD9680`: 14-Bit, 1.25 GSPS/1 GSPS/820 MSPS/500 MSPS JESD204B, Dual Analog-to-Digital Converter
-  :adi:`AD9683`: 14-Bit, 170 MSPS/250 MSPS, JESD204B, Analog-to-Digital Converter
-  :adi:`AD9690`: 14-Bit, 500 MSPS / 1 GSPS JESD204B, Analog-to-Digital Converter
-  :adi:`AD9691`: 14-Bit, 1.25 GSPS JESD204B, Dual Analog-to-Digital Converter
-  :adi:`AD9694`: 14-Bit, 500 MSPS JESD204B, Quad Analog-to-Digital Converter
-  :adi:`AD9083`: 16-Channel, 125 MHz Bandwidth, JESD204B Analog-to-Digital Converter

JESD204B Digital-to-Analog Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`AD9135`: Dual, 11-Bit, high dynamic, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter
-  :adi:`AD9136`: Dual, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter
-  :adi:`AD9144`: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter
-  :adi:`AD9152`: Dual, 16-Bit, 2.25 GSPS, TxDAC+ Digital-to-Analog Converter
-  :adi:`AD9154`: Quad, 16-Bit, 2.4 GSPS, TxDAC+® Digital-to-Analog Converter
-  :adi:`AD9161`: 11-Bit, 12 GSPS, RF Digital-to-Analog Converter
-  :adi:`AD9162`: 16-Bit, 12 GSPS, RF Digital-to-Analog Converter
-  :adi:`AD9163`: 16-Bit, 12 GSPS, RF DAC and Digital Upconverter
-  :adi:`AD9164`: 16-Bit, 12 GSPS, RF DAC and Direct Digital Synthesizer
-  :adi:`AD9172`: Dual, 16-Bit, 12.6 GSPS RF DAC with Channelizers
-  :adi:`AD9173`: Dual, 16-Bit, 12.6 GSPS RF DAC with Channelizers
-  :adi:`AD9174`: Dual, 16-Bit, 12.6 GSPS RF DAC and Direct Digital Synthesizer
-  :adi:`AD9175`: Dual, 11-Bit/16-Bit, 12.6 GSPS RF DAC with Wideband Channelizers
-  :adi:`AD9176`: Dual, 16-Bit, 12.6 GSPS RF DAC with Wideband Channelizers

JESD204B RF Transceivers
~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`AD9371`: SDR Integrated, Dual RF Transceiver with Observation Path
-  :adi:`AD9375`: SDR Integrated, Dual RF Transceiver with Observation Path and DPD
-  :adi:`ADRV9009`: SDR Integrated, Dual RF Transceiver with Observation Path
-  :adi:`ADRV9008-1`: SDR Integrated, Dual RF Receiver
-  :adi:`ADRV9008-2`: SDR Integrated, Dual RF Transmitter with Observation Path

JESD204B/C Mixed-Signal Front Ends
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`AD9081`: MxFE™ Quad, 16-Bit, 12GSPS RFDAC and Quad, 12-Bit, 4GSPS RFADC
-  :adi:`AD9082`: MxFE™ QUAD, 16-Bit, 12GSPS RFDAC and DUAL, 12-Bit, 6GSPS RFADC

JESD204B Clocking Solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`AD9528`: JESD204B Clock Generator with 14 LVDS/HSTL Outputs
-  :adi:`HMC7043`: High Performance, 3.2 GHz, 14-Output Fanout Buffer
-  :adi:`HMC7044`: High Performance, 3.2 GHz, 14-Output Jitter Attenuator with JESD204B
-  :adi:`LTC6952`: Ultralow Jitter, 4.5GHz PLL, JESD204B/JESD204C
