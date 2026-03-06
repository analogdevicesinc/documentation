Microcontroller no-OS Drivers
=============================

The majority of ADI's products are peripherals to a non-ADI digital engine (FPGA, microprocessor, or microcontroller). While there is major work underway on FPGAs (Xilinx and Altera) and microprocessors (running an operating system like Linux), the efforts on microcontrollers are fragmented due to the diverse nature of the microcontroller market. The goal of these projects (microcontroller/no-OS) is to be able to provide reference projects for lower end processors, which can't run Linux or aren't running a specific operating system, to help customers using microcontrollers with ADI parts.

Drivers List
------------

Accelerometers
~~~~~~~~~~~~~~

-  `ADXL312: ±1.5 g/±3 g/±6 g/±12 g range, 13-bit resolution, 3-axis Digital Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl313>`__
-  `ADXL313: ±0.5 g/±1 g/±2 g/±4 g range, 13-bit resolution, 3-axis Digital Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl313>`__
-  `ADXL314: ±200 g range, 13-bit resolution, 3-axis Digital Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl313>`__
-  `ADXL345: 3-Axis, ±2 g/±4 g/±8 g/±16 g Digital Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl345>`__
-  `ADXL355: Low Noise, Low Drift, Low Power, 3-Axis MEMS Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl355>`__
-  `ADXL362: Micropower, 3-Axis, ±2 g/±4 g/±8 g Digital Output MEMS Accelerometer <https://wiki.analog.com/../tools-software/uc-drivers/adxl362>`__
-  `ADXL367: Micropower, 3-Axis, ±2 g/±4 g/±8 g Digital Output MEMS <https://wiki.analog.com/../tools-software/uc-drivers/adxl367>`__
-  `ADXL372: Micropower, 3-Axis, ±200 g Digital Output, MEMS <https://wiki.analog.com/../tools-software/uc-drivers/adxl372>`__

A/D & D/A Converter Combinations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD5592R: 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip Reference, SPI interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5592r>`__
-  `AD5593R: 8-Channel, 12-Bit, Configurable ADC/DAC with On-Chip Reference, I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5592r>`__
-  `AD74413R: 4 Channel, 16-Bit ADC 13-bit DAC, Configurable ADC/DAC with on-chip Reference, SPI interface <https://wiki.analog.com/../tools-software/uc-drivers/ad74413r>`__

Analog to Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD4030-24: 24-Bit, 2 MSPS, Single Channel, Precision Differential SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad463x>`__
-  `AD4111: Single Supply, 24-Bit, Sigma-Delta ADC with ±10 V and 0 mA to 20 mA Inputs, Open Wire Detection <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD4112: Single Supply, 24-Bit, Sigma-Delta ADC with ±10 V and 0 mA to 20 mA Inputs <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD4630-16: 16-Bit, 2 MSPS, Dual Channel, Precision Differential SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad463x>`__
-  `AD4630-24: 24-Bit, 2 MSPS, Dual Channel, Precision Differential SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad463x>`__
-  AD6673: 80 MHz Bandwidth, Dual IF Receiver
-  AD6676: Wideband IF Receiver Subsystem
-  AD7091: 1 MSPS, Ultralow Power 12-Bit ADC in 8-Lead LFCSP
-  `AD7091R: 1 MSPS, Ultralow Power, 12-Bit ADC in 10-Lead LFCSP and MSOP <https://wiki.analog.com/../tools-software/uc-drivers/ad7091r>`__
-  `AD7091R-2: 2-Channel, 1 MSPS, Ultralow Power, 12-Bit SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7091r8>`__
-  `AD7091R-4: 4-Channel, 1 MSPS, Ultralow Power, 12-Bit SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7091r8>`__
-  `AD7091R-8: 8-Channel, 1 MSPS, Ultralow Power, 12-Bit SAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7091r8>`__
-  `AD7124-4: 4-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC with PGA and Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad7124>`__
-  `AD7124-8: 8-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC with PGA and Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad7124>`__
-  `AD7172-2: Low Power, 24-Bit, 31.25 kSPS, Sigma-Delta ADC with True Rail-to-Rail Buffers <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7172-4: Low Power, with 4- or 8-channel, 24-bit, 31.25 kSPS, Sigma-Delta ADC with True Rail-to-Rail Buffers <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7173-8: Low Power, 8-/16-Channel, 31.25 kSPS, 24-Bit, Highly Integrated Sigma-Delta ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7175-2: 24-Bit, 250 kSPS, Sigma-Delta ADC with 20 µs Settling and True Rail-to-Rail Buffers <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7175-8: 24-Bit, 8-/16-Channel, 250 kSPS, Sigma-Delta ADC with True Rail-to-Rail Buffers <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7176-2: 24-Bit, 250 kSPS Sigma Delta ADC with 20 µs Settling <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7177-2: 32-Bit, 10 kSPS, Sigma-Delta ADC with 100 µs Settling and True Rail-to-Rail Buffers <https://wiki.analog.com/../tools-software/uc-drivers/ad717x>`__
-  `AD7190: 2-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA <https://wiki.analog.com/../tools-software/uc-drivers/ad7193>`__
-  `AD7192: 2-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA <https://wiki.analog.com/../tools-software/uc-drivers/ad7193>`__
-  `AD7193: 4-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA <https://wiki.analog.com/../tools-software/uc-drivers/ad7193>`__
-  `AD7194: 8-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA <https://wiki.analog.com/../tools-software/uc-drivers/ad7193>`__
-  `AD7195: 2-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA and AC Excitation <https://wiki.analog.com/../tools-software/uc-drivers/ad7193>`__
-  AD7280A: Lithium Ion Battery Monitoring System]]
-  `AD7466: 1.6 V Micro-Power 12-Bit ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7467: 1.6 V Micro-Power 10-Bit ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7468: 1.6 V Micro-Power 8-Bit ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7475: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or SOIC-8 <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7476: 1MSPS, 12-Bit ADC in 6 Lead SOT-23 <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7476A: 12-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7477: 1MSPS, 10-Bit ADC in 6 Lead SOT-23 <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7477A: 10-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7478: 8-Bit, 1 MSPS, Low Power Successive Approximation ADC Which Operates From A Single 2.35 V to 5.25 V Power Supply <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7478A: 8-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP Packages <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7495: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or SOIC-8 <https://wiki.analog.com/../tools-software/uc-drivers/ad7476>`__
-  `AD7606: 8-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7606>`__
-  `AD7682: 16-Bit, 4-Channel, 250 kSPS PulSAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7689>`__
-  `AD7689: 16-Bit, 8-Channel, 250 kSPS PulSAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7689>`__
-  `AD7699: 16-Bit, 8-Channel, 500 kSPS PulSAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7689>`__
-  AD7768: 8-Channel, 24-Bit, Simultaneous Sampling ADC, Power Scaling, 110.8 kHz BW
-  `AD7770: 8-Channel, 24-Bit Simultaneous Sampling ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7779>`__
-  `AD7771: 8-Channel, 24-Bit, Simultaneous Sampling ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7779>`__
-  `AD7779: 8-Channel, 24-Bit, Simultaneous Sampling ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7779>`__
-  `AD7780: 24-Bit Pin-Programmable Low Power Σ−Δ ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7780>`__
-  `AD7799: 3-Channel, Low Noise, Low Power, 16/24-Bit, Sigma Delta ADC with On-Chip In-Amp <https://wiki.analog.com/../tools-software/uc-drivers/ad7799>`__
-  `AD7949: 14-Bit, 8-Channel, 250 kSPS PulSAR ADC <https://wiki.analog.com/../tools-software/uc-drivers/ad7689>`__
-  `AD7980: 16-Bit, 1 MSPS, PulSAR ADC in MSOP/LFCSP <https://wiki.analog.com/../tools-software/uc-drivers/ad7980>`__
-  `AD7991: 4-Channel, 12-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 <https://wiki.analog.com/../tools-software/uc-drivers/ad7991>`__
-  `AD7995: 4-Channel, 10-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 <https://wiki.analog.com/../tools-software/uc-drivers/ad7991>`__
-  `AD7999: 4-Channel, 8-Bit ADC with I2C Compatible Interface in 8-Lead SOT-23 <https://wiki.analog.com/../tools-software/uc-drivers/ad7991>`__
-  AD9250: 14-Bit, 170 MSPS/250 MSPS, JESD204B, Dual Analog-to-Digital Converter
-  AD9265: 16-Bit, 125 MSPS/105 MSPS/80 MSPS, 1.8 V Analog-to-Digital Converter
-  AD9434: 12-Bit, 370 MSPS/500 MSPS, 1.8 V Analog-to-Digital Converter
-  AD9467: 16-Bit, 200 MSPS/250 MSPS Analog-to-Digital Converter
-  AD9625: 12-Bit, 2.6 GSPS/2.5 GSPS/2.0 GSPS, 1.3 V/2.5 V Analog-to-Digital Converter
-  AD9680: 14-Bit, 1.25 GSPS/1 GSPS/820 MSPS/500 MSPS JESD204B, Dual Analog-to-Digital Converter
-  LTC2312-12: 12-Bit, 500ksps Serial Sampling ADC in TSOT
-  LTC2312-14: 14-Bit, 500ksps Serial Sampling ADC in TSOT
-  `MAX9611: High-Side, Current-Sense Amplifiers with 12-Bit ADC and Op Amp/Comparator <https://wiki.analog.com/../tools-software/uc-drivers/max9611>`__
-  `MAX11205: 16-Bit, Single-Channel, Ultra-Low Power, Delta-Sigma ADC with 2-Wire Serial Interface <https://wiki.analog.com/../tools-software/uc-drivers/max11205>`__
-  `MAX14001:Configurable, Isolated 10-bit ADCs for Multi-Range Binary Inputs <https://wiki.analog.com/../tools-software/uc-drivers/max14001>`__

Analog Front End
~~~~~~~~~~~~~~~~

-  `AD4110: Complete, single-channel, universal input analog-to-digital front end <https://wiki.analog.com/../tools-software/uc-drivers/ad4110>`__

Capacitive to Digital & Touch Screen Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :doc:`AD7745: 24-bit, 1 Channel Capacitance to Digital Converter </wiki-migration/resources/tools-software/uc-drivers/ad7746>`
-  :doc:`AD7746: 24-bit, 2 Channel Capacitance to Digital Converter </wiki-migration/resources/tools-software/uc-drivers/ad7746>`
-  :doc:`AD7747: 24-Bit Capacitance-to-Digital Converter with Temperature Sensor </wiki-migration/resources/tools-software/uc-drivers/ad7746>`
-  `AD7156: Ultralow Power, 1.8 V, 3 mm × 3 mm, 2-Channel Capacitance Converter <https://wiki.analog.com/../tools-software/uc-drivers/ad7156>`__

D/A Converters (DAC)
~~~~~~~~~~~~~~~~~~~~

-  `AD5421: 16-Bit, Serial Input, Loop-Powered, 4mA to 20mA DAC <https://wiki.analog.com/../tools-software/uc-drivers/ad5421>`__
-  AD5446: 14-Bit High Bandwidth Multiplying DAC with Serial Interface including a Serial Data Output line
-  `AD5449: Dual 12-Bit, High Bandwidth Multiplying DAC with Serial Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5449>`__
-  `AD5628: Octal, 12-Bit, SPI Voltage Output denseDAC With 5 ppm/°C On-Chip Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5628>`__
-  `AD5629R: Octal, 12-bit, I2C Voltage Output denseDAC with 5 ppm/°C On-Chip Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5629r>`__
-  `AD5671R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C Reference, I2 Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5672R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C Reference, SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5674R: 16-channel, 12-Bit buffered voltage output digital-to-analog converters, SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5675: Octal, 16-Bit nanoDAC+ with I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5675R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C Reference, I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5676: Octal, 16-Bit nanoDAC+ with SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5676R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C Reference, SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5679R: 16-channel, 16-Bit buffered voltage output digital-to-analog converters, SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5684: Quad, 12-Bit nanoDAC+ with SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5684R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5685R: Quad, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5686: Quad, 16-Bit nanoDAC+ with SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5686R: Quad, 16-Bit nanoDAC+™ with 2 ppm/°C On-Chip Reference and SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5694: Quad, 12-Bit nanoDAC+™ with I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5694R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C Reference, I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5695R: Quad 14-Bit nanoDAC+ with 2 ppm/°C Reference, I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5696: Quad, 16-Bit nanoDAC+™ with I2C Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5681R: Tiny 12-Bit SPI nanoDAC+, with ±1 LSB INL and 2 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5682R: Tiny 14-Bit SPI nanoDAC+, with ±2 LSB INL and 2 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5683: Tiny 16-Bit SPI nanoDAC+, with ±2 (16-Bit) LSB INL and 2 ppm/°C External Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5683R: Tiny 16-Bit SPI nanoDAC+, with ±2 (16-Bit) LSB INL and 2 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5691R: Tiny 12-Bit I2C nanoDAC+, with ±1 LSB INL and 2 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5692R: Tiny 14-Bit I2C nanoDAC+, with ±4 LSB INL and 5 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5693: Tiny 16-Bit I2C nanoDAC+, with ±2 (16-Bit) LSB INL <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5693R: Tiny 16-Bit I2C nanoDAC+, with ±2 (16-Bit) LSB INL and 2 ppm/°C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5676>`__
-  `AD5721R: Multiple Range, 12-Bit, Unipolar Voltage Output DACs with 2 PPM/⁰C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5761r>`__
-  `AD5755: Quad Channel, 16-Bit, Serial Input, 4 mA to 20 mA and Voltage Output DAC, Dynamic Power Control <https://wiki.analog.com/../tools-software/uc-drivers/ad5755>`__
-  `AD5755-1: Quad Channel, 16-Bit, Serial Input, 4 mA to 20 mA and Voltage Output DAC, Dynamic Power Control, HART Connectivity <https://wiki.analog.com/../tools-software/uc-drivers/ad5755>`__
-  `AD5757: Quad Channel, 16-Bit, Serial Input, 4-20mA Output DAC, Dynamic Power Control, HART Connectivity <https://wiki.analog.com/../tools-software/uc-drivers/ad5755>`__
-  `AD5758: Single Channel, 16-Bit Current and Voltage Output DAC with Dynamic Power Control and HART Connectivity <https://wiki.analog.com/../tools-software/uc-drivers/ad5758>`__
-  `AD5761R: Multiple Range, 16-Bit, Bipolar Voltage Output DACs with 2 PPM/⁰C Reference <https://wiki.analog.com/../tools-software/uc-drivers/ad5761r>`__
-  `AD5766: 16-Channel, 16-Bit Voltage Output denseDAC <https://wiki.analog.com/../tools-software/uc-drivers/ad5766>`__
-  `AD5767: 16-Channel, 12-Bit Voltage Output denseDAC <https://wiki.analog.com/../tools-software/uc-drivers/ad5766>`__
-  `AD5770R: 6-Channel, 14-Bit, Current Output DAC with On-Chip Reference, SPI Interface <https://wiki.analog.com/../tools-software/uc-drivers/ad5770r>`__
-  `AD5791: 1 ppm 20-Bit, ±1 LSB INL, Voltage Output DAC <https://wiki.analog.com/../tools-software/uc-drivers/ad5791>`__
-  `AD7293: 12-Bit Power Amplifier Current Controller with ADC, DACs, and Temperature and Current Sensors <https://wiki.analog.com/../tools-software/uc-drivers/ad7293>`__
-  `AD7303: +2.7 V to +5.5 V, Serial Input, Dual Voltage Output 8-Bit DAC <https://wiki.analog.com/../tools-software/uc-drivers/ad7303>`__
-  AD9144: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog Converter
-  AD9152: Dual, 16-Bit, 2.25 GSPS, TxDAC+ Digital-to-Analog Converter
-  AD9739A: 14-Bit, 2.5 GSPS, RF Digital-to-Analog Converter
-  `LTC2672: Five-Channel, Low Dropout, 300 mA, Current Source Output, 12-/16-Bit SoftSpan DAC <https://wiki.analog.com/../tools-software/uc-drivers/ltc2672>`__
-  `MAX5380: Low-Cost, Low-Power, 8-Bit DACs with 2-Wire Serial Interface in SOT23 <https://wiki.analog.com/../tools-software/uc-drivers/max5380>`__

Digital Input/Output (DIO) Devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `MAX22196: Octal Industrial Sink/Source Digital Input <https://wiki.analog.com/../tools-software/uc-drivers/max22196>`__

Clock Generation Devices
~~~~~~~~~~~~~~~~~~~~~~~~

-  AD9517-1: 12-Output Clock Generator with Integrated 2.5 GHz VCO
-  AD9523: 14-Output, Low Jitter Clock generator
-  AD9528: JESD204B Clock Generator with 14 LVDS/HSTL Outputs
-  `AD9833: Low Power, 12.65 mW, 2.3 V to +5.5 V, Programmable Waveform Generator <https://wiki.analog.com/../tools-software/uc-drivers/ad9833>`__
-  ADF4106: 6 GHz integer-N PLL
-  ADF4153: Fractional-N Frequency Synthesizer
-  ADF4156: 6.2 GHz Fractional-N Frequency Synthesizer
-  ADF4157: High Resolution 6 GHz Fractional-N Frequency Synthesizer
-  ADF4350: Wideband Synthesizer with Integrated VCO
-  `ADF4377: 12.8 GHz Wideband Integer-N Synthesizer and RF Sampling Clock <https://wiki.analog.com/../tools-software/uc-drivers/adf4377>`__
-  `ADF5355: Microwave Wideband Synthesizer with Integrated VCO <https://wiki.analog.com/../tools-software/uc-drivers/adf5355>`__
-  `HMC7044: High Performance, 3.2 GHz, 14-Output Jitter Attenuator with JESD204B <https://wiki.analog.com/../tools-software/uc-drivers/hmc7044>`__
-  `ADRF6780: 5.9 GHz to 23.6 GHz, Wideband, Microwave Upconverter <https://wiki.analog.com/../tools-software/uc-drivers/adrf6780>`__
-  `ADMV1013: 24 GHz to 44 GHz, Wideband, Microwave Upconverter <https://wiki.analog.com/../tools-software/uc-drivers/admv1013>`__
-  `ADMV1014: 24 GHz to 44 GHz, Wideband, Microwave Downconverter <https://wiki.analog.com/../tools-software/uc-drivers/admv1014>`__

Filter Devices
~~~~~~~~~~~~~~

-  `ADMV8818: 2 GHz to 18 GHz, Digitally Tunable, High-Pass and Low-Pass Filter <https://wiki.analog.com/../tools-software/uc-drivers/admv8818>`__

Gyroscopes
~~~~~~~~~~

-  `ADXRS453: High Performance, Digital Output Gyroscope <https://wiki.analog.com/../tools-software/uc-drivers/adxrs453>`__

IMUs (Inertial Measurement Units)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADIS16505: Precision, Miniature MEMS IMU
-  ADIS1657x: Precision, Miniature MEMS IMU

Impedance Analyzer
~~~~~~~~~~~~~~~~~~

-  `AD5933: 1 MSPS, 12-Bit Impedance Converter, Network Analyzer <https://wiki.analog.com/../tools-software/uc-drivers/ad5933>`__

Mobile I/O Expander & Keypad Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `ADP5589: Keypad Decoder and I/O Expansion <https://wiki.analog.com/../tools-software/uc-drivers/adp5589>`__

Multiplexers
~~~~~~~~~~~~

-  `ADGS1408: SPI Interface, 4 Ω RON, ±15 V/+12 V/±5 V, 1.8 V Logic Control, 8:1 Muxes <https://wiki.analog.com/../tools-software/uc-drivers/adgs1408>`__
-  `ADGS1409: SPI Interface, 4 Ω RON, ±15 V/+12 V/±5 V, 1.8 V Logic Control, Dual 4:1 Muxes <https://wiki.analog.com/../tools-software/uc-drivers/adgs1408>`__
-  `ADGS1208: SPI-Interface, Low CON & QINJ, ±15V/+12V, 1.8V Logic Control, 8:1 Mux <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1209: SPI-Interface, Low CON & QINJ, ±15V/+12V, 1.8V Logic Control, Dual 4:1 Muxes <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1212: SPI Interface, Quad SPST Switch, Low QINJ, Low CON, ±15 V/+12 V, Mux Configurable <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1408: SPI Interface, 4 Ω RON, ±15 V/+12 V/±5 V, 1.8 V Logic Control, 8:1 Muxes <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1409: SPI Interface, 4 Ω RON, ±15 V/+12 V/±5 V, 1.8 V Logic Control, Dual 4:1 Muxes <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1412: SPI Interface, 1.5 Ω RON, ±15 V/+12 V, Quad SPST Switch, Mux Configurable <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS5412: SPI Interface, 4× SPST Switches, 9.8 Ω RON, ±20 V/+36 V, Mux Configurable <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS1612: SPI Interface, 1 Ω RON, ±5 V, 12 V, 5 V, 3.3 V, Mux Configurable, Quad SPST Switch <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__
-  `ADGS5414: SPI Interface, Octal SPST Switches, 13.5 Ω RON, ±20 V/+36 V, Mux <https://wiki.analog.com/../tools-software/uc-drivers/adgs5412>`__

Optical
~~~~~~~

-  `ADPD188: Integrated Optical Module with Ambient Light Rejection and Two LEDs <https://wiki.analog.com/../tools-software/uc-drivers/adpd188>`__
-  `ADPD1080: Photometric Front Ends <https://wiki.analog.com/../tools-software/uc-drivers/adpd1080>`__
-  `ADPD1081: Photometric Front Ends <https://wiki.analog.com/../tools-software/uc-drivers/adpd1080>`__

Digital Potentiometers
~~~~~~~~~~~~~~~~~~~~~~

-  `AD5110: Single Channel, 128-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://wiki.analog.com/../tools-software/uc-drivers/ad5110>`__
-  `AD5112: Single Channel, 64-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://wiki.analog.com/../tools-software/uc-drivers/ad5110>`__
-  `AD5114: Single Channel, 32-Position, I2C, ±8% Resistor Tolerance, Nonvolatile Digital Potentiometer <https://wiki.analog.com/../tools-software/uc-drivers/ad5110>`__
-  AD5232: Nonvolatile Memory, Dual, 256-Position Digital Potentiometer
-  AD5235: Nonvolatile Memory, Dual 1024-Position Digital Potentiometer
-  AD5251: I2C, Nonvolatile Memory, Dual 64-Position Digital Potentiometer
-  AD5252: I2C, Nonvolatile Memory, Dual 256-Position Digital Potentiometer
-  AD5253: Quad 64-Position I2C Nonvolatile Memory Digital Potentiometer
-  AD5254: Quad 256-Position I2C Nonvolatile Memory, Digital Potentiometer
-  ADN2850: Nonvolatile Memory, Dual 1024-Position Digital Resistor

RF Transceivers
~~~~~~~~~~~~~~~

-  `ADF7023: High Performance, Low Power, ISM Band FSK/GFSK/OOK/MSK/GMSK Transceiver IC <https://wiki.analog.com/../tools-software/uc-drivers/adf7023>`__
-  :doc:`ADF5902: 24 GHz, ISM Band, Multichannel FMCW Radar Transmitter </wiki-migration/resources/tools-software/uc-drivers/adf5902>`

Digital Temperature Sensors
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `ADT7420: ±0.25°C Accurate, 16-Bit Digital I2C Temperature Sensor <https://wiki.analog.com/../tools-software/uc-drivers/adt7420>`__
-  `MAX31865: RTD-to-Digital Converter Temperature Sensor <https://wiki.analog.com/../tools-software/uc-drivers/max31865>`__

Power
~~~~~

-  `LTC3337: Primary Battery SOH Monitor with Precision Coulomb Counter <https://wiki.analog.com/../tools-software/uc-drivers/ltc3337>`__
-  `ADP1050: Digital Controller for Isolated Power Supply with PMBus Interface <https://wiki.analog.com/../tools-software/uc-drivers/adp1050>`__
