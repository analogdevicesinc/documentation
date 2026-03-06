| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetapplication>`
| =====Audio Input-Output Modes===== This section describes the different types of inputs and outputs which are supported by SigmaStudio for SHARC (ADSP-SC5xx/ADSP-215xx) Target Framework.
| =====Analog\\Digital Co-existence===== Analog\\Digital Co-existence Audio I/O mode supports Analog/Digital Inputs and Analog Outputs.
| =====Routing scheme for ADSP-SC58x\\ADSP-2158x\\ADSP-SC59x\\ADSP-2159x===== The routing scheme for Analog\\Digital Co-existence mode for ADSP-SC58x\\ADSP-2158x\\ADSP-SC59x\\ADSP-2159x processors is illustrated in Figure below.
| The analog data path consisting of CODEC and SPORT’s are configured in TDM mode. The digital S/PDIF path is in I2S mode. ASRC and PCG’s are used by the framework to facilitate this configuration.
| Default Audio I/O mode Configuration - Analog\\Digital Co-existence for ADSP-SC58x\\ADSP-2158x\\ADSP-SC59x\\ADSP-2159x
| |image1|
| The master clock for PCG C is derived from 24.576 MHz which is available through DAI1_PIN03. The bit clock and frame sync for CODEC and the SPORTs are derived from PCG C using appropriate clock and frame sync dividers. By default, PCG C is configured to generate clock and frame sync signals for TDM8 configuration at 48 kHz sample rate. The clock and frame sync from PCG C are also available on DAI0_PIN10 and DAI0_PIN12 respectively. These pins are used for clocking the SPORTs of DAI0.
| The master clock for PCG A is derived from 24.576 MHz which is available through DAI0_CRS_PIN03. The bit clock and frame sync for SRC 0 and SPORT used for obtaining the data from S/PDIF are derived from PCG A using appropriate clock and frame sync dividers. SRC 0 is used to de-jitter the S/PDIF recovered clock. By default, PCG A is configured to generate clock and frame sync signals for I2S configuration at 48 kHz sample rate. The clock and frame sync from PCG A are also available on DAI1_PIN11 and DAI1_PIN19 respectively. These pins are used for clocking the SPORTs of DAI1.
| =====Routing Scheme for ADSP SC57x\\2157x===== |image2|
| The master clock for PCG A and PCG B is derived from 24.576 MHz which is available through DAI0_PIN03. By default, PCG B is configured to generate clock and frame sync signals for TDM8 configuration at 48 kHz sample rate and PCG A is configured to generate clock and frame sync signals for I2S configuration at 48 kHz sample rate.
| The bit clock and frame sync for CODEC and SPORTs are derived from PCG B. The bit clock and frame sync for SRC 0 and SPORT used for obtaining the data from S/PDIF are derived from PCG A. SRC 0 is used to de-jitter the S/PDIF recovered clock.
| =====Routing Scheme for SC589 SAM===== |image3|
| The master clock for PCG A and PCG B is derived from 12.288 MHz which is available through DAI0_PIN06. By default, PCG B is configured to generate clock and frame sync signals for TDM8 configuration at 48 kHz sample rate and PCG A is configured to generate clock and frame sync signals for I2S configuration at 48 kHz sample rate.
| The bit clock and frame sync for CODEC and SPORTs are derived from PCG B. The bit clock and frame sync for SRC 0 and SPORT used for obtaining the data from S/PDIF are derived from PCG A. SRC 0 is used to de-jitter the S/PDIF recovered clock.
| =====Routing Scheme for ADSP 2156x===== |image4|
| For the ADSP-2156x processors, the default IO routing is as shown in Figure 9. The master clock for PCG C is derived from 24.576 MHz which is available through DAI1_PIN03. The bit clock and frame sync for CODEC and the SPORTs are derived from PCG C using appropriate clock and frame sync dividers. By default, PCG C is configured to generate clock and frame sync signals for TDM8 configuration at 48 kHz sample rate. The clock and frame sync from PCG C are also available on DAI0_PIN07 and DAI0_PIN19 respectively. These pins are used for clocking the SPORTs of DAI0.
| The master clock for PCG A is derived from 24.576 MHz which is available through DAI0_CRS_PIN03. The bit clock and frame sync for SRC 0 and SPORT used for obtaining the data from S/PDIF are derived from PCG A using appropriate clock and frame sync dividers. SRC 0 is used to de-jitter the S/PDIF recovered clock. By default, PCG A is configured to generate clock and frame sync signals for I2S configuration at 48 kHz sample rate. The clock and frame sync from PCG A are also available on DAI1_PIN07 and DAI1_PIN19 respectively. These pins are used for clocking the SPORTs of DAI1.
| =====Clocking Scheme===== ADSP-SC58x and ADSP-SC57x processor clocks are configured for functional Mode 0:
| ^ **Clock** ^ **Computation** ^ **Frequency** ^

========== ============== =======
XTAL       = CLK\_        25 MHz
CCLK0_0/1  = CLK\_/CSEL   400 MHz
CCLK1_0/1  = CLK\_/CSEL   400 MHz
SYSCLK_0/1 = CLK\_/SYSSEL 200 MHz
========== ============== =======

| **Table:** Processing Clocks
| The clock sources for different peripherals in ADSP-SC58x and ADSP-2158x processor are as tabulated below:
| ^ **Processor**\ ^ **Peripheral** ^ **Source** ^ **Frequency** ^

================ ================================ ========= ==========
ADSP-2158x/SC58x SHARC-XI 0                       CCLK0_0   400 MHz
:::              SHARC-XI 1                       CCLK0_0   400 MHz
:::              ARM                              CCLK1_0   400 MHz
:::              SPORT BCLK (TDM8 Configuration)  PCG0_CLKC 12.288 MHz
:::              SPORT FSCLK (TDM8 Configuration) PCG_FSC   48 kHz
:::              SPORT BCLK (I2S Configuration)   PCG0_CLKA 3.072 MHz
:::              SPORT FSCLK(I2S Configuration)   PCG_FSA   48 kHz
:::              L2                               SYSCLK_0  200 MHz
:::              ADC BCLK                         PCG0_CLKC 12.288 MHz
:::              ADC LRCLK                        PCG_FSC   48 kHz
:::              DAC BCLK                         PCG0_CLKC 12.288 MHz
:::              DAC LRCLK                        PCG_FSC   48 kHz
:::              DAI                              SCLK_0    100 MHz
:::              TWI                              SCLK_0    100 MHz
:::              SPI1 TX                          Host      385 KHz
:::              SPI1 RX                          Host      385 KHz
================ ================================ ========= ==========

**Table:** Peripheral Clocks – ADSP-SC58x and ADSP-2158x

| The clock sources for different peripherals in ADSP-SC57x and ADSP-2157x processor are as tabulated below:
| ^ **Processor**\ ^ **Peripheral** ^ **Source** ^ **Frequency** ^

+----------------------------+----------------------------------+-----------+------------+
| ADSP-2157x/SC57x/SC589 SAM | SHARC-XI 0                       | CCLK0_0   | 400 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SHARC-XI 1                       | CCLK0_0   | 400 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | ARM                              | CCLK1_0   | 400 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPORT BCLK (TDM8 Configuration)  | PCG0_CLKB | 12.288 MHz |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPORT FSCLK (TDM8 Configuration) | PCG_FSB   | 48 kHz     |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPORT BCLK (I2S Configuration)   | PCG0_CLKA | 3.072 MHz  |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPORT FSCLK(I2S Configuration)   | PCG_FSA   | 48 kHz     |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | L2                               | SYSCLK_0  | 200 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | ADC BCLK                         | PCG0_CLKB | 12.288 MHz |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | ADC LRCLK                        | PCG_FSB   | 48 kHz     |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | DAC BCLK                         | PCG0_CLKB | 12.288 MHz |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | DAC LRCLK                        | PCG_FSB   | 48 kHz     |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | DAI                              | SCLK_0    | 100 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | TWI                              | SCLK_0    | 100 MHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPI1 TX                          | Host      | 385 KHz    |
+----------------------------+----------------------------------+-----------+------------+
| :::                        | SPI1 RX                          | Host      | 385 KHz    |
+----------------------------+----------------------------------+-----------+------------+

**Table:** Peripheral Clocks – ADSP-SC57x, ADSP-SC589 SAM and ADSP-2157x

The clock sources for different peripherals in ADSP -2156x processor are as tabulated below:

============= ================================ ========== =============
**Processor** **Peripheral**                   **Source** **Frequency**
============= ================================ ========== =============
ADSP-2156x    SHARC-XI 0                       CCLK0_0    1000 MHz
:::           SPORT BCLK (TDM8 Configuration)  PCG0_CLKC  12.288 MHz
:::           SPORT FSCLK (TDM8 Configuration) PCG_FSC    48 kHz
:::           SPORT BCLK (I2S Configuration)   PCG0_CLKA  3.072 MHz
:::           SPORT FSCLK(I2S Configuration)   PCG_FSA    48 kHz
:::           L2                               SYSCLK_0   500 MHz
:::           ADC BCLK                         PCG0_CLKC  12.288 MHz
:::           ADC LRCLK                        PCG_FSC    48 kHz
:::           DAC BCLK                         PCG0_CLKC  12.288 MHz
:::           DAC LRCLK                        PCG_FSC    48 kHz
:::           DAI                              SCLK_0     125 MHz
:::           TWI                              SCLK_0     125 MHz
:::           SPI1 TX                          Host       385 KHz
:::           SPI1 RX                          Host       385 KHz
============= ================================ ========== =============

| **Table:** Peripheral Clocks – ADSP-2156x
| ADSP-SC59x and ADSP-2159x processor clocks are configured for functional Mode 0:
| ^ **Clock** ^ **Computation** ^ **Frequency** ^

========== ============== =======
XTAL       = CLK\_        25 MHz
CCLK0_0/1  = CLK\_/CSEL   1 GHz
CCLK1_0/1  = CLK\_/CSEL   1 GHz
SYSCLK_0/1 = CLK\_/SYSSEL 500 MHz
========== ============== =======

| **Table:** Processing Clocks
| The clock sources for different peripherals in ADSP -SC59x and ADSP-2159x processor are as tabulated below:
| ^ **Processor**\ ^ **Peripheral** ^ **Source** ^ **Frequency** ^

================ ================================ ========= ==========
ADSP-2159x/SC59x SHARC-XI 0                       CCLK0_0   1 GHz
:::              SHARC-XI 1                       CCLK0_0   1 GHz
:::              ARM                              CCLK1_0   1 GHz
:::              SPORT BCLK (TDM8 Configuration)  PCG0_CLKC 12.288 MHz
:::              SPORT FSCLK (TDM8 Configuration) PCG_FSC   48 kHz
:::              SPORT BCLK (I2S Configuration)   PCG0_CLKA 3.072 MHz
:::              SPORT FSCLK(I2S Configuration)   PCG_FSA   48 kHz
:::              L2                               SYSCLK_0  500 MHz
:::              ADC BCLK                         PCG0_CLKC 12.288 MHz
:::              ADC LRCLK                        PCG_FSC   48 kHz
:::              DAC BCLK                         PCG0_CLKC 12.288 MHz
:::              DAC LRCLK                        PCG_FSC   48 kHz
:::              DAI                              SCLK_0    125 MHz
:::              TWI                              SCLK_0    125 MHz
:::              SPI1 TX                          Host      385 KHz
:::              SPI1 RX                          Host      385 KHz
================ ================================ ========= ==========

| **Table:** Peripheral Clocks – ADSP-SC59x and ADSP-2159x

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/defaultioconfigsc58x.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/defaultiomodesc57x.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/defaultiomodesc589sam.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/targetintegration/targetapplication/defaultiomode2156x.png
   :width: 400px
