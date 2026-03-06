CN0540 and the SDP-K1
=====================

General Setup
-------------

The following sections on setup describe the steps for setting up the CN0540 board using both the :adi:`SDP-K1`.

Equipment
---------

-  :adi:`SDP-K1` micro-controller board
-  :adi:`EVAL-CN0540-ARDZ Shield <cn0540>`
-  PC with a USB port and Windows 7 (32-bit) or higher
-  Serial Terminal Software (Putty/TeraTerm or similar)
-  USB Standard-A to Mini-B cable
-  ICP/IEPE piezo vibration sensor

   -  Such as the :adi:`CN0532 featuring the ADXL1002 <cn0532>`

-  :adi:`SDP-K1 User Guide <media/en/technical-documentation/user-guides/EVAL-SDP-CK1Z-UG-1539.pdf>`

Hardware Setup
--------------

The following sections describe the process of setting up the hardware for both the :adi:`SDP-K1` and `32F746GDISCOVERY <https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-mpu-eval-tools/stm32-mcu-mpu-eval-tools/stm32-discovery-kits/32f746gdiscovery.html>`__ micro-controller boards. It's important to note that the Arduino headers on the CN0540 are surface mounted and as such the user should take care not to bend or break the headers.

SDP-K1
~~~~~~

Shown below is the **CN0540 board** mounted on the **SDP-K1 board** via the Arduino headers. The SDP-K1 only requires a single Standard-A to Mini-B USB cable to connect to the PC. Both the orange Connected LED and green SYS PWR should light on the SDP-K1 if connected correctly.


|image1|

Software Setup
--------------

Importing the EVAL-CN0540-ARDZ MBED Example program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If the user doesn’t have an mbed online id account, the user must create one at https://ide.mbed.com/.
-  After having a account, open the Example program for EVAL-CN0540-ARDZ https://os.mbed.com/teams/AnalogDevices/code/EVAL-CN0540-ARDZ
-  After that, click the import button to import example program to your online compiler.\ |image2|\

|image3|

-  Then compile the code and the extracted binary can be loaded to SDP-k1 by dragging and dropping it to the SDP-k1 directory.\

|image4|

Note: you can refer to this video on how to import an mbed example program: https://youtu.be/3xbzuPLcmCk?t=189

Connecting to a serial terminal application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to communicate with the board using the SDP-K1 the user needs to install a serial terminal software on their PC. It is recommended to use PuTTY which is available for free download on the internet. The following steps were written with PuTTY in mind however any other serial terminal application should follow a similar procedure. Following are the steps required to interface with the board.

-  Open Device Manager through the Windows control panel and plug the micro-controller board into the PC, when the board is detected it will appear in device manager, displaying as USB Serial Device. This also displays which port the board is connected to. (COM5 in this case)


|image5|

-  Right-clicking on the COM port in device manager will allow the user to view and change the properties of the port, such as the transfer speed.
-  Open the serial terminal application and enter the correct values to configure it to connect to the board. The serial line should be the COM port noted earlier and the speed should be set to 115200 to ensure data transfer works correctly. Also note the changes in the Terminal tab, this is required for the menu to display properly.\ |image6|\

|image7|

-  Upon connection, the interface menu should appear. If not, press the reset button on the micro-controller board, this will call up the command menu for the user to interact with. **(Note: This does not work with the current version of the SDP-K1)**

|image8|

-  From here, the user should type the number corresponding to their desired choice and press 'Enter'. Note that many choices will create sub-menus, prompting the user to make another choice.

Command Summary
~~~~~~~~~~~~~~~

The following table shows every command along with a brief description. Some commands have recommended settings to apply for optimal results for narrow bandwidth measurements of 32 kHz.

+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|     | Command                        | Description                                                                                                                                                                                         |
+=====+================================+=====================================================================================================================================================================================================+
| 1.  | Set ADC power mode             | Change the power mode of the :adi:`AD7768-1`. The available power modes are Low, Median and Fast, and are described in the datasheet. Low power mode is recommended.                                |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.  | Set ADC MCLK divider           | Change the clock divide to: /16, /8, /4 or /2. /16 is recommended.                                                                                                                                  |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3.  | Set ADC filter type            | Change the type of filter used. Also allows for the oversampling ratio to be changed. Recommended is the Low ripple FIR Filter, oversampled by 32.                                                  |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4.  | Set ADC AIN and REF buffers    | Adjust the buffers for both AIN and REF. It is recommended to turn on both AIN precharge buffers and precharge both REF buffers.                                                                    |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5.  | Set ADC to default config      | Resets the ADC configuration to the default.                                                                                                                                                        |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6.  | Set ADC VCM output             | Choose the VCM output voltage, recommended is (AVDD1 – AVSS)/2.                                                                                                                                     |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7.  | Read desired ADC register      | Read the ADC registers.                                                                                                                                                                             |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8.  | Read continuous ADC data       | Reads voltages, codes and raw data from the ADC over a user-defined number of samples.                                                                                                              |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9.  | Reset ADC                      | Resets the ADC, either a soft reset over SPI or hard reset using the reset pin.                                                                                                                     |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10. | ADC Power-down                 | Put the ADC into sleep mode or wake it up.                                                                                                                                                          |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11. | Set ADC GPIOs                  | Control the ADC GPIOs by reading, writing or changing GPIO settings.                                                                                                                                |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 12. | Read ADC master status         | Shows faults in master status register, allowing the user to pinpoint the source of problems.                                                                                                       |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13. | Set ADC Vref and MCLK          | Change the values for Vref and MCLK.                                                                                                                                                                |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 14. | Print ADC measured data        | Prints previously read voltages, codes and raw data to the terminal. Logging the terminal will allow the user to use extract this data. Requires the 'Read data' command to have been run.          |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 15. | Set ADC data output mode       | Choose how data is output from the ADC.                                                                                                                                                             |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 16. | Set ADC diagnostic mode        | Change which diagnostic mode is used for the ADC.                                                                                                                                                   |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 17. | Do the FFT                     | Does the FFT and prints useful information such as the Total Harmonic Distortion, Signal to Noise Ratio and Dynamic Range.                                                                          |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 18. | FFT settings                   | Change FFT settings such as sample count. Can also print FFT data to the terminal, which can be logged and plotted, requires command 'Do the FFT' to have been run.                                 |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 19. | Gains, Offsets                 | Set the gain and offset values.                                                                                                                                                                     |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 20. | Scratchpad check               | Input an 8-bit number, if it is returned the ADC is interfacing with the software. This is a useful quick check for debugging and is good to run after setup.                                       |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 21. | Compensate Piezo sensor offset | Automatically compensates for voltage offsets in the sensor, giving more accurate data. The user should run this after connecting a new sensor.                                                     |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 22. | Set DAC output                 | Choose what voltage and codes the :adi:`LTC2606 DAC <LTC2606>` should output. This sets the Shift voltage and can be used to manually compensate for any voltage offset.                            |
+-----+--------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. important::

   After connecting a sensor to the board the user should be sure to run option 21 'Compensate Piezo sensor offset' to ensure they get accurate results using their sensor.


*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_sdp-k1.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_mbed.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_mbed_link_2.png
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_mbed_link_3.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540devicemanager.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540putty.png
   :width: 600px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540putty2.png
   :width: 600px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0540/cn0540_putty.png
