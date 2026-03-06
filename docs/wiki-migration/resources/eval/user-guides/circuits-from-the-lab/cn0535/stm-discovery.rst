CN0535 and the STM Discovery Kit
================================

General Setup
-------------

The following sections on setup describe the steps for setting up the CN0540 board using the `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller boards.

Equipment
---------

-  `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller board
-  :adi:`EVAL-CN0535-FMCZ Evaluation Board <cn0535>`
-  PC with a USB port and Windows 7 (32-bit) or higher
-  Serial Terminal Software (Putty/TeraTerm or similar)
-  USB Standard-A to Mini-B cable
-  `32F746GDISCOVERY Discovery kit User Manual <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html#resource>`__

Hardware Setup
--------------

The following sections describe the process of setting up the hardware for the `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller boards. It's important to note that the Arduino headers on the CN0540 are surface mounted and as such the user should take care not to bend or break the headers.

EVAL-CN0535-FMCZ Prep for use with SDP-K1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The table below shows the components that the user must install to enable the use of the EVAL-CN0535-FMCZ with the `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller board.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/tbd.jpg
   :align: center
   :width: 600px

== ========= ============================
\  Component Manufacturing Part Number
== ========= ============================
1. P2, P4    TSM-108-04-T-SV
2. P3        TSM-110-04-T-SV
3. R38       ERJ-3GEY0R00V or equivalent
4. C25       0603YC104KAT2A or equivalent
5. Y1        SIT8008BI-21-33E-16.38400G
== ========= ============================

\|

32F746 Discovery
~~~~~~~~~~~~~~~~

Shown below is the **CN0535 board** mounted on the **32F746GDISCOVERY board** via the Arduino headers. The 32F746GDISCOVERY board only requires a Standard-A to Mini-B USB cable to connect to the PC. If properly connected the large red LED LD7 should light as well as the red LED LD2.


|image1|

Software Setup
--------------

Programming the 32F746 Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following are the steps then required to be completed to set up the :adi:`EVAL-CN0535-FMCZ Evaluation Board <CN0535>` using the **32F746G Discovery board**:

-  Download the `ST-LINK/V2 driver <https://os.mbed.com/teams/ST/wiki/ST-Link-Driver>`__ and run the .exe file. Follow the instructions on the window that appears to install the drives. **(Note: This requires a free account for my.st.com)**


|image2|

-  Plug the USB cables from the PC into the **32F746G Discovery board**. If installation was successful a new device named DIS_F746NG should appear under 'This PC' in Windows File Explorer.

|image3|

-  Download the AD7768_demo.bin firmware.
-  Copy and paste or drag and drop the AD7768_demo.bin file into the DIS_F746NG device/folder. This will load the firmware onto the board.
-  If the download fails, a FAIL.TXT file will appear on the DIS_F746NG device.
-  If the download is successful the .bin file will disappear from the DIS_F746NG device and there will be no FAIL.TXT file.
-  Unplug the **32F746G Discovery board** from the PC and plug it back in to hard reset the board and finalize installation.

Interfacing with the 32F746G Discovery board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the major features of the 32F746G Discovery board is the on-board touchscreen, which can be used by the CN0535 board. The use of the touchscreen doesn't require any additional setup after the software is installed, the screen should light and a welcome screen should appear, follow the onscreen instructions to show the command menu: |image4| This includes all of the commands detailed below with a few notable differences. Command 8: 'Read Data' will plot the ADC data in codes on the screen as shown: |image5| Similarly; Command 17: 'Do the FFT' will plot the FFT along with any notable values such as THD, SNR and DR. |image6| These features allow for quick and easy data gathering.

Command Summary
~~~~~~~~~~~~~~~

The following table shows every command along with a brief description. Some commands have recommended settings to apply for optimal results for narrow bandwidth measurements of 32 kHz.

+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     | Command                       | Description                                                                                                                                                                                         |
+=====+===============================+=====================================================================================================================================================================================================+
| 1.  | Set power mode                | Change the power mode of the :adi:`AD7768-1`. The available power modes are Low, Median and Fast, and are described in the datasheet. Low power mode is recommended.                                |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.  | Set clock divide              | Change the clock divide to: /16, /8, /4 or /2. /16 is recommended.                                                                                                                                  |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3.  | Set filter type               | Change the type of filter used. Also allows for the oversampling ratio to be changed. Recommended is the Low ripple FIR Filter, oversampled by 32.                                                  |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4.  | Set AIN and REF buffers       | Adjust the buffers for both AIN and REF. It is recommended to turn on both AIN precharge buffers and precharge both REF buffers.                                                                    |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5.  | Set Default config of the ADC | Resets the ADC configuration to the default.                                                                                                                                                        |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6.  | Set VCM output                | Choose the VCM output voltage, recommended is (AVDD1 – AVSS)/2.                                                                                                                                     |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7.  | Read desired register         | Read the ADC registers.                                                                                                                                                                             |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8.  | Read data                     | Reads voltages, codes and raw data from the ADC over a user-defined number of samples.                                                                                                              |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9.  | Reset ADC                     | Resets the ADC, either a soft reset over SPI or hard reset using the reset pin.                                                                                                                     |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10. | Power-down                    | Put the ADC into sleep mode or wake it up.                                                                                                                                                          |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11. | ADC GPIO                      | Control the ADC GPIOs by reading, writing or changing GPIO settings.                                                                                                                                |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 12. | Read master status            | Shows faults in master status register, allowing the user to pinpoint the source of problems.                                                                                                       |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13. | Set Vref and MCLK             | Change the values for Vref and MCLK.                                                                                                                                                                |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 14. | Print measured data           | Prints previously read voltages, codes and raw data to the terminal. Logging the terminal will allow the user to use extract this data. Requires the 'Read data' command to have been run.          |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 15. | Set data output mode          | Choose how data is output from the ADC.                                                                                                                                                             |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 16. | Set diagnostic mode           | Change which diagnostic mode is used for the ADC.                                                                                                                                                   |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 17. | Do the FFT                    | Does the FFT and prints useful information such as the Total Harmonic Distortion, Signal to Noise Ratio and Dynamic Range.                                                                          |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 18. | FFT settings                  | Change FFT settings such as sample count. Can also print FFT data to the terminal, which can be logged and plotted, requires command 'Do the FFT' to have been run.                                 |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 19. | Gains, Offsets                | Set the gain and offset values.                                                                                                                                                                     |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 20. | Scratchpad check              | Input an 8-bit number, if it is returned the ADC is interfacing with the software. This is a useful quick check for debugging and is good to run after setup.                                       |
+-----+-------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\|

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0535/cn0535_f746gdisco.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/f746gdisco_download.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_f746gdiscopc.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_menu.png
   :width: 600px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_data.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_gui_fft.png
   :width: 600px
