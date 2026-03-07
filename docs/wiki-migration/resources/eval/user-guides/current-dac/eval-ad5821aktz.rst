AD5821A Evaluation Kit User Guide
=================================

GENERAL DESCRIPTION
-------------------

| The EVAL-AD5821AKTZ Evaluation Kit is designed to allow the user to evaluate the performance of the AD5821A Auto Focus (AF) driver. This user guide describes how to download and use the AD5821A Evaluation Software which is available for Windows and allows the user to easily program the AD5821A and check the basic functionality of the part.
| The EVAL-AD5821A Evaluation Kit contains the following boards:

-  **EVAL-AD5821A-DBZ**: A board that includes the AD5821A device and Voice Coil Motor (VCM) loads. It also includes connectors for external VCM loads and a connector for external I2C
-  **EVAL-APOLLO-LD-MBZ**: Contains several LDOs to generate the AD5821A supplies and other voltages necessary to the system, connectors for external supplies, level shifters, current sense amplifiers and an ADC to measure voltages and currents
-  **APOLLO-CORTEX-M3**: Apollo controller board
-  **USB Standard Micro-B-cable** that connects the boards to the computer

| 
|

.. container:: leftalign


   ..

|image1|

   |
   
   .. container:: leftalign

      // \*\* Figure 1. AD5821A Evaluation Kit \*\* //

   


EVALUATION KIT HARDWARE
-----------------------

The EVAL-AD5821AKTZ Evaluation Kit consists of three boards:

-  EVAL-AD5821A-DBZ
-  EVAL-APOLLO-LD-MBZ
-  APOLLO-CORTEX-M3

| 
| ==== Hardware Connections ====

-  Insert the AD5821A daughterboard onto the main board
-  Verify that the links position conforms to the description in the next sections
-  Connect the Apollo board J8 connector to the main board P6 connector
-  Connect the USB cable to the Apollo board J1 connector (Do not connect the USB cable to the computer yet, see *Software Download and Installation* section)

.. important::

   Pay special attention to connect the daughterboard P1 connector to the main board P1 connector, and the daughterboard P3 to the main board P3. Opposite insertion may damage one or both boards


EVAL-AD5821A-DBZ
~~~~~~~~~~~~~~~~

| It contains the AD5821A device and the decoupling capacitors (100 nF and 10 µF) and a simulated Voice Coil Motor (VCM) load (22 µH coil and 11.5 Ω resistor). It also includes a connector for external load, a connector for external I2C and test points.
| The main components included in the board are shown in the next figure.
|

.. container:: leftalign


   ..

|image2|

   |
   
   .. container:: leftalign

      // \*\* Figure 2. EVAL-AD5821A-DBZ Daughterboard \*\* //

   


| To connect the on-board VCM load, links should connect positions of JP3 and JP4 as indicated in Table 1.
| Link positions are outlined in Table 1. Default positions are in bold.
| === Table 1: EVAL-AD5821A-DBZ Link Positions and Function ===

==== ======== ======================
Link Position Description
==== ======== ======================
JP1  **ON**   Internal
JP2  OFF      External
:::  :::      ::
JP3  **ON**   Internal VCM load
JP4  OFF      External VCM load
:::  :::      ::
P8   **1-2**  Load supplied by AVDD1
     3-4      Load supplied by AVDD2
:::  :::      ::
==== ======== ======================

| P2 connector can be used to connect and external I2C host. To do that disconnect the links on JP1 and JP2.
| JP3 and JP4 connectors allow the access to the typical VCM resistances and inductances. When the links are connected to the typical VCM resistances and inductances, the user also has access to test the ±VCM pins (TP1 and TP2) and the middle point between the resistor and the inductor (TP3).
| To use an external VCM load, disconnect the links on JP3 and JP4 and connect the external load to P5.
| ==== EVAL-APOLLO-LD-MBZ ==== This board has been designed to connect different daughterboards that support different products. It also features a connector to the Apollo microcontroller board.
| The EVAL-APOLLO-LD-MBZ also contains LDOs to generate the required voltages for AD5821A and other ICs like level shifters, current sense amplifiers and one ADC, who provides support to measure the AVDD1/AVDD2 supply voltages and currents.
| By using different configuration of links, the user can select either AVDD1 or AVDD2 supply to power the AD5821A and is also possible to configure the supplies as fixed or adjustable. DVDD is the IO voltage for I2C level of AD5821A and can also be configured via links.
| A more detailed explanation of AVDD1/AVDD2 and DVDD configuration is given in the *Software/Plugins/Hardware Setup* section of this document.
| Table 2 shows the default link positions (default positions are in bold) and Figure 3 shows the default links position in green as well as the board connectors and test points.
| === Table 2: EVAL-APOLLO-LD-MBZ Link Positions and Function ===

======= ========== ===================================
Link    Position   Description
======= ========== ===================================
JP4/JP5 OFF/OFF    Reserved
        **OFF/ON** AVDD1 internal adjustable
        ON/OFF     3.3 V fixed
        ON/ON      5 V fixed
P11     1-2        External AVDD1
        **3-4**    Internal AVDD1
P17     1-2        Bypass current measurement
        **3-4**    Measure current of AVDD1
JP1     **ON**     AVDD1 connected to daughterboard
        OFF        AVDD1 disconnected on daughterboard
JP7/JP8 OFF/OFF    Reserved
        **OFF/ON** AVDD2 internal adjustable
        ON/OFF     3.3 V fixed
        ON/ON      5 V fixed
P12     1-2        External AVDD2
        **3-4**    Internal AVDD2
P2      1-2        Bypass current measurement
        **3-4**    Measure current of AVDD2
JP13    **ON**     AVDD2 connected to daughterboard
        OFF        AVDD2 disconnected on daughterboard
P16     **1-2**    GPIO 3 level by software
        3-4        GPIO 3 connected to DVDD
        5-6        GPIO 3 connected to GND
P18     **1-2**    GPIO 2 level by software
        3-4        GPIO 2 connected to DVDD
        5-6        GPIO 2 connected to GND
P15     **1-2**    GPIO 1 level by software
        3-4        GPIO 1 connected to DVDD
        5-6        GPIO 1 connected to GND
P21     **1-2**    DVDD = 1.8 V internal
        3-4        DVDD external connector
        5-6        DVDD = 3.3 V
P23     1-2        I2C VREFB is 5 V
        **3-4**    I2C VREFB is 3.3 V
======= ========== ===================================

| 
|

.. container:: leftalign


   ..

|image3|

   |
   
   .. container:: leftalign

      // \*\* Figure 3. EVAL-APOLLO -LD_MBZ Motherboard \*\* *

   


===== AD5821A EVALUATION SOFTWARE =====
  ==== SOFTWARE DOWNLOAD AND INSTALLATION ==== The software required to run the AD5821A Evaluation Kit is available in the Analog Devices web. Go to* :adi:`EVAL-AD5821A.html <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5821A.html>` *and click on the link to download a zip file with the installer, see Figure 4.

.. container:: leftalign

   
   .. container:: leftalign

      * \*\* Figure 4. Download AD5821A Evaluation Software \*\* //


      | On clicking the link a zip file containing the installer is downloaded. After that, follow the steps below:

-  Extract the contents of the zip file to some location in a local hard drive
-  Download and install the LabVIEW Runtime (https://www.ni.com/en-ie/support/downloads/software-products/download.labview-runtime.html#346222) needed for running the Evaluation System GUI automatically from ni.com:

   -  Supported OS: Windows
   -  Included Editions: Runtime
   -  Version: 2016
   -  Application Bitness: 64-bit

-  Download and install the NI-VISA from ni.com https://www.ni.com/en-ie/support/downloads/drivers/download.ni-visa.html#306035:

   -  Supported OS: Windows
   -  Included Editions: Full
   -  Version:16.0

-  Run the *Setup.exe* file located in the Volume folder and read carefully and accept the AD5821A Evaluation License Agreement to proceed with the installation. Follow the steps until the application is installed.
-  Before plugging the USB cable to the Apollo board, install the Apollo driver. Go to Signed USB Driver folder and right-click on ADI-NXP_vista_7.inf and select Install. This will install the driver for the Apollo controller board.

|

| Once the application is installed in your computer, the board can be powered up by plugging the USB interface. After power-up, two blue LEDs (LED1 and LED4) light up in the Apollo board. An orange LED (LED3) keeps blinking until running the application in the Apollo board.
| ==== RUNNING THE SOFTWARE ==== When the software installation is complete, run the shortcut to the application found in the start menu, under *AD5821A Eval Software*.
| To verify the firmware is properly downloaded, the user should see the “1 board(s) found” and “Download Successful. Reconnecting” screen shown below. Also, in the Apollo board the green LED2 blinks and the orange LED3 turns off.
| If the *No Apollo Boards Found* message is shown when the application is executed, Apollo must be reset by pressing the white switch (SW1), next to the USB connector, and then click “Retry”. Apollo will be recognized after the Plug and Play Windows function detects the new device connected.
|

.. container:: leftalign


   ..

|image4|

   |
   
   .. container:: leftalign

      // \*\* Figure 5. Firmware download pop-up screen \*\* *

   


Once the firmware is properly downloaded, a screen like the one below is shown.

.. container:: leftalign

   
   .. container:: leftalign

      * \*\* Figure 6. Application view upon opening \*\* //

   


| The AD5821A Evaluation Software consists of a general framework to initialize the system, provide access to the AD5821A input register that controls the AF driver sink current, show the application status and handle the hardware setup to adjust power supply levels or configure different options in the board.
| By clicking on each entry under List of Plugins section, the corresponding plugin will appear on the main panel. The function of each plugin will be explained in the next section.
| ==== USING THE SOFTWARE ==== As shown in Figure 7, the AD5821A Evaluation Software is made up of four parts:

-  Top menu

   -  *File*: Print the Window or exit the application
   -  *Window*: Allows for selecting full-screen window
   -  *Version*: Show the application version
   -  *Re-Init HW*: Resets the Apollo and download the firmware again
   -  *Documents*: Allows the user to open different documents, like datasheets, schematics, license, etc.
   -  *Help*: Shows information about this application

-  List of plugins

   -  *Register Map*: Read/write the input register

      -  *Hardware Setup*: Configure AVDD1 and AVDD2 sources, DVDD and GPIOs
      -  *AF Driver*: Controls the sink current of AD5821A
      -  *AF Driver Sweep*: Allows for a sweep of the sink current between two configurable values

-  Register Map tree: The register selected here will be shown in the main panel when the *Register Map* is selected in the *List of Plugins*.
-  Register access and logging: Allows reading/writing one or all registers. It is also possible to log a session and save the registers configuration in a test file. The user can load this test file later to produce a specific writing to a set of registers.
-  Main Panel: This panel is dynamic and its content changes depending on the plugin selected by the user in the *List of Plugins* section.

| 
|

.. container:: leftalign


   ..

|image5|

   |
   
   .. container:: leftalign

      // \*\* Figure 7. AD5821A Evaluation Software Overview \*\* //

   


| ==== PLUGINS ====
| === REGISTER MAP === This plugin provides access to all the registers and register fields of the part. For the AD5821A there is only one register, the input register, so it is recommended to control the device using the AF Driver plugin that will be explained later.
| Clicking on *RegMap1* in *Register Map Tree* the whole register map is inserted in the main subpanel as shown in Figure 8. The information shown is updated from the device and the user can expand/contract a specific register to update it and show the fields inside. When the value or enumeration column is modified, the new configuration is written to the device.
|

.. container:: leftalign


   ..

|image6|

   |
   
   .. container:: leftalign

      // \*\* Figure 8. Register view \*\* *

   


=== HARDWARE SETUP === The Hardware Setup plugin helps the user to configure AVDD1, AVDD2 and DVDD supplies and three GPIOs, as well as selecting the appropriate links for a given configuration.
  An image of the EVAL-APOLLO -LD_MBZ silkscreen is shown in the panel to the right (Figure 9), showing the default link positions highlighted in green. When changing the options on the left panel, the link positions also change in the board image. The user must ensure that the positions of the jumpers in the silkscreen image match the current positions of the links in the board when any of the options is changed. After moving the jumper to the indicated position click OK next to the warning message that appears on the bottom of the panel.

.. container:: leftalign

   
   .. container:: leftalign

      * \*\* Figure 9. Hardware Setup plugin \*\* //

   


| == AVDD1 and AVDD2 == The configuration options for AVDD1 and AVDD2 are the same. The difference between these two supplies is that AVDD1 powers the AD5821A and the VCM load and the AVDD2 powers only the load. The two supplies are mutually exclusive. The VDD pin of AD5821A (see Daughterboard Schematic under Documents menu) is always connected to AVDD1.
| The first option is to choose AVDD1/AVDD2 Internal (default) or External. In case external supply is selected, the user must connect the power supply cable to P9 (AVDD1) or P22 (AVDD2). The positive is pin 1 and ground is pin 2.
| There are three possibilities under Internal Supply Options (only when Internal supply is selected):

-  *Adjustable 2.7 V – 4.8 V* (default): Uses a LDO that can be adjusted by software. An external supply is required for voltages higher than 4.8 V.
-  *3.3 V fixed*: 3.3 V from a fixed LDO
-  *5 V fixed*: 5 V from USB

| 
| When *Adjustable 2.7 V – 4.8 V* is selected, the control boxes under *AVDD1/AVDD2* can be used to set the desired voltage. A voltage monitor box is positioned to the right side of the correspondent control box. The voltage measurements are provided by an on-board ADC. When *IAVDD1/IAVDD2* checkbox is set, the current from AVDD1 and AVDD2 supplies are also measured.

GPIOs
^^^^^

There are three possible sources for the GPIOs:

-  *Software* (default): The software controls the GPIO level
-  *DVDD*: GPIO is at level high, voltage equal to DVDD
-  *GND*: GPIO is at level low, voltage equal to 0 V

| 
| GPIO1 is connected to AD5821A’s XSHUTDOWN pin. Setting the Level to low puts the AD5821A in power-down mode. Setting the Level to high (default) puts the part in operating mode again.
| GPIO2 and GPIO3 are not connected in this evaluation board so their settings have no effect on the AD5821A.

DVDD
^^^^

The DVDD is the digital IO for the I2C level of AD5821A.

-  *1.8 V* (default): Internal LDO
-  *3.3 V*: Internal LDO
-  *EXT*: External. In this case the level is internally limited to 3.3 V

| 
| == AF DRIVER == Figure 10 shows the *AF Driver* plugin. This plugin is used to control the power-down function and the sink current of the AD5821A in an easy manner. It controls the AD5821A *XSHUTDOWN* software function (bit 15 of input register) and the AF code data D0..D9 (bits 4 to 13 of input register) to set the desired sink current.
| At start up the AD5821A is in power-down mode. The button in *Auto Focus Drive Control* shows the text POWER UP. By clicking on the button, the AD5821A goes to operating mode and the button text toggles to POWER DOWN. By clicking again, the part returns to power-down. The button works in an alternate function between POWER UP and POWER DOWN.
| Once in operating mode, the current sink by the AD5821A can be controlled in one of three ways:

-  Moving the slider
-  Typing the current value in the *Current* box (in mA)
-  Typing the *DAC Code* in the corresponding box (See Ad5821A datasheet for information about the DAC code)

| 
| Below the current control section is the Input Register. Its value automatically updates when the user changes the current level or click on *POWER UP/POWER DOWN* button. Although the user can read/write the input register, it is preferable to control the AD5821A using the functions explained before. The *Input Register* is not necessary to control the part; it is shown for informative purposes only.
|

.. container:: leftalign


   ..

|image7|

   |
   
   .. container:: leftalign

      // \*\* Figure 10: AF Driver plugin \*\* //

   


| == AF DRIVER SWEEP == This plugin is used to sweep the AD5821A current between a minimum current and maximum current, at time intervals defined at *Time Step* control box (time intervals below 10 ms are not accurate).
| The value of the current is updated in the slider and monitor boxes to the right of the min/max current setting boxes, as shown in Figure 11.
| Click on *Start Sweep* button to start the sweep, Stop Sweep button to stop it and the Reset button to bring the AF Driver current to 0 mA.
|

.. container:: leftalign


   ..

|image8|

   |
   
   .. container:: leftalign

      // \*\* Figure 11: Auto Focus Driver Sweep \*\* //

   


| ===== DESIGN FILES ===== **EVAL-APOLLO-LD-MBZ** Board schematic, layout and BOM files. `eval-apollo-ld-mbz_design_files.zip <https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/eval-apollo-ld-mbz_design_files.zip>`_
| **EVAL-AD5821A-DBZ** Board schematic, layout and BOM files. `eval-ad5821a-dbz_design_files.zip <https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/eval-ad5821a-dbz_design_files.zip>`_

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/eval-ad5821a_kit_angle-web.jpg
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_2_blue.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_3_blue.png
   :width: 600px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_5.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_7_blue.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_8_blue.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_10_blue.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/current-dac/figure_11.png
   :width: 400px
