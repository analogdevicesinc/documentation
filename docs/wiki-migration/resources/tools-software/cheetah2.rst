**EVALUATING THE AD9625 ANALOG-TO-DIGITAL CONVERTER**

--------------

**INTRODUCTION**

This user guide describes the AD9625 evaluation board, AD9625EBZ, which provides all of the support circuitry required to operate this part in the various modes and configurations. The application software used to interface with the devices is also described.

The AD9625 data sheet provides additional information and should be consulted when using the evaluation board. All documents and software tools are available at www.analog.com/hsadcevalboard. For additional information or questions, send an email to highspeed.converters@analog.com.

The AD9625 is a 12-bit ADC with sampling speeds of up to 2000 MSPS. It is designed to support wideband applications where high sample rates, small size, wide bandwidth and versatility are desired. The ADC cores feature a multistage, differential pipelined architecture with integrated output error correction logic. This reference design includes the device data capture board via the JESD204B serial interface and the SPI interface. The samples are written to the internal memory on the FPGA capture board. It allows programming the device and monitoring its internal registers via SPI.

**Features**

-  Full featured evaluation board for the AD9625
-  SPI interface for setup and control
-  Balun input drive option
-  On-board LDO regulator needing a single external 6 V, 2 A dc supply
-  VisualAnalog® and SPI controller software interfaces

**Helpful Documents**

-  AD9625 data sheet http://www.analog.com/AD9625
-  High Speed ADC Capture Evaluation Kit Rev E (HSC-ADC-EVALEZ) :doc:`/wiki-migration/resources/eval/hsc-adc-evale`
-  AN-905 Application Note, //VisualAnalog Converter Evaluation Tool Version 1.0 User Manual //
-  AN-878 Application Note, *High Speed ADC SPI Control Software*
-  AN-877 Application Note, *Interfacing to High Speed ADCs via SPI*
-  AN-835 Application Note, *Understanding ADC Testing and Evaluation*
