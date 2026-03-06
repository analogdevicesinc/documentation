Evaluation of ADcmXL1021-1 (or ADcmXL3021) ON A PC
==================================================

| The **ADCMXL Evaluation Software** enables PC-based evaluation of the ADcmXL1021-1 and/or ADcmXL3021, using the following hardware: an ADcmXL interface board (ADCMXL_BRKOUT/PCBZ), FX3 Eval iSensor breakout board and a Cypress FX3™ SuperSpeed Explorer Kit. See the picture below for the evaluation kit.
| **ADcmXL3021** is a 3-axis version of z-axis **ADcmXL1021-1**.
| Installation and User Guide can be downloaded here: `Evaluation Kit Installation and User Guide <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/eval-adcm_kit-installation_and_user_guide.pdf>`__
| |image1|
| Picture of ADCMXL Evaluation System: FX3 Board + ADCMXL_BRKOUT/PCBZ + ADcmXL3021 (or ADcmXL1021-1) Module. The picture above shows how to connect the evaluation kit.

| 
| === EVALUATION OPTION PART NUMBERS TO ORDER===
| The following options are available to be used to evaluate the ADcmXL family and can be ordered by contacting an ADI distributor to place the order.
| **ADCMXL_BRKOUT/PCBZ**
| For simple breakout of the ADcmXL1021-1 or ADcmXL3021 flex tail connector to header pins.
| NOTE: The ADcmXL1021-1 (or ADcmXL3021) module is required to be ordered separately.

| **EVAL-ADCM**
| Evaluation kit for ADcmXL3021, which includes ADCMXL_BRKOUT/PCBZ, the module and additional hardware to use ADI's ADCMXL Evaluation Software.
| **EVAL-ADCM-1**
| Evaluation kit for ADcmXL1021-1, which includes ADCMXL_BRKOUT/PCBZ, the module and additional hardware to use ADI's ADCMXL Evaluation Software.
| === EVALUATION OPTIONS DESCRIPTION===
| The *ADCMXL_BRKOUT/PCBZ* is a breakout board that has a Hirose DF12(3.0)-14DP-05V(86) receptor which accepts the mating connector on the flex tail of the either ADcmXL1021-1 or ADcmXL3021 Module. This breaks out the connections from the ADcmXL1021-1 (or ADcmXL3021) module to a 16 pin 2mm header connector. This is available as an option in the case that the user has an existing backend available to power, configure and capture directly to the ADcmXL1021-1 or ADcmXL3021 and needs an interface option to connect to the Hirose header without soldering to the module. The 14 pin, 0.5 mm pitch Hirose connector has the pin configuration shown in Figure below. The ADCMXL_BRKOUT/PCBZ silk screen and schematic are available for download using the links below.
| |image2|
| ADcmXL3021 Hirose connector pinout
| `ADCMXL_BRKOUT/PCBZ Top Silk Screen <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/01-047904-01-b-1.pdf>`__
| `ADCMXL_BRKOUT/PCBZ Schematic <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/02-047904-01-a-1.pdf>`__

| The *EVAL-ADCM* is an orderable kit that includes the evaluation hardware. It includes the following:
| - ADcmXL3021 module
| - ADCMXL_BRKOUT/PCBZ (more details above)
| - ADcmXL FX3 Interface board
| - Cypress FX3 Evaluation Kit
| - Acrylic mounting plate (2”x3”)
| - 8 Mounting screws (SCREW, PAN HEAD PHILLIPS, M2.5X6MM)
| - 2” long Ribbon cable, 16 pin conductor, 2mm connector pitch (required for RTS Mode communications link)
| - 12” long Ribbon cable, 16 pin conductor, 2mm connector pitch
| The *EVAL-ADCM-1* is an orderable kit that includes the evaluation hardware. It includes the following:
| - ADcmXL1021-1 module
| - ADCMXL_BRKOUT/PCBZ (more details above)
| - ADcmXL FX3 Interface board
| - Cypress FX3 Evaluation Kit
| - Acrylic mounting plate (2”x3”)
| - 8 Mounting screws (SCREW, PAN HEAD PHILLIPS, M2.5X6MM)
| - 2” long Ribbon cable, 16 pin conductor, 2mm connector pitch (required for RTS Mode communications link)
| - 12” long Ribbon cable, 16 pin conductor, 2mm connector pitch

NOTE: Both ADcmXL1021-1 and ADcmXL3021 use the following Hirose connector and would require the following mating plug: DF12(3.0)–14DS–0.5V(86) – Hirose Receptacle – will be used on flex tail of product DF12(3.0)–14DP–0.5V(86) – Hirose Plug – to be used on customer boards, test, eval boards, etc.

| 
| === SOFTWARE TO DOWNLOAD===
| ADCMXL Evaluation Software installation requires two downloads:
| 1. Download and unzip the file called FX3Driver.zip (click here to see the download link)
| `(click here to download fx3driver.zip) <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/fx3_driver.zip>`__
| 2. Run DriverSetup.exe
| 3. Download and unzip the file called “ADCMXL_Evaluation_revision.zip”, where revision is currently identified as “2192”. This version supports both ADcmXL1021-1 and ADcmXL3021 modules.
| `(click here to download adcmxl_evaluation_rev_2192.zip) <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adcmxl_evaluation_rev_2192.zip>`__
| (NOTE: ADCMXL Evaluation Software revisions 2.1.8.6 and higher, need the most recent `FX3Driver <https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/fx3_driver.zip>`__ to operate.)
| 4. Connect the evaluation setup to the computer

| 
| === PC SYSTEM REQUIREMENTS=== - Windows XP, Vista, 7, 10
| - .NET Framework 3.5

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/imu/adcmxl3021bmlzx-kit.gif
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/adcmxl_brkout_p1pinout.gif
   :width: 200px
