Residential Smart Smoke Sensor​
===============================

Overview​
---------

The Residential Smart Smoke Sensor Demo provides a demonstration on how to implement ADI's :adi:`CN0583` smoke detector solution that can be incorporated in many systems such as in industrial and commercial settings.

The :adi:`CN0583` smoke detector module is composed of two parts -- the EVAL-CN0583-SOM smoke detector system-on-module (SOM), and the EVAL-CN0583-CRR1 carrier board.

The EVAL-CN0583-SOM is a standalone module designed for development of smoke detection applications, which integrates an ADPD188BI smoke sensor, a MAX32660 microcontroller, and regulated DC power supplies needed for proper operation.

The EVAL-CN0583-CRR1 is an easy-to-use carrier board developed for evaluation of the SOM and enable rapid prototyping. The CN0583 carrier board has an onboard debugger based on the MAX32625PICO that allows drag-and-drop programming of the SOM and USB-UART communication.

This provides a UL-217 and EN 14604 compliant solution to smoke detection.

Demo Requirements​
------------------

Residential Smart Smoke Sensor Demo Requirements​
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  :adi:`EVAL-CN0583-SOM <CN0583>`
-  :adi:`EVAL-CN0583-CRR1 <CN0583>`
-  ADPD188BI Smoke Chamber (included with the SOM)
-  USB Micro-B Cable
-  Host PC with installed serial terminal program (e.g. Putty, TeraTerm)
-  Smoke Check Smoke Detector Tester or any similar

| |image1|
| ===== Setup​ =====

Block Diagram​
^^^^^^^^^^^^^^

Hardware Setup​
^^^^^^^^^^^^^^^

-  Install the ADPD188BI smoke chamber on the primary side of the SOM.
-  Carefully insert the SOM between P1 and P2 of the carrier board, following the cutout on the center. The proper orientation of the module will have pin 1 closest to the buzzer, and pin 28 on the side with the test button.
-  Connect the P6 on the carrier board to the computer using the micro-USB cable.
-  On the computer, check if the CN0583 hardware setup is recognized as a DAPLINK drive. This will indicate that the necessary drivers are complete and correct.

| 
| ==== Software Setup​ ====

Programming the SOM​
~~~~~~~~~~~~~~~~~~~~

This step is only required if you want to update the firmware of the CN0583 SOM. The programming may be done over DAPLINK, as following: *Insert warning that we are going to need the firmware file that enables the buzzer of the CN0583 board on a smoke event.*

-  Download the hex file for the demo application. Alternatively, you may use your own hex file.

.. admonition:: Download
   :class: download

   
   +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | **Algorithm for UL 217 8th Edition Standard** | `UL 217 hex with CLI stream <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/cn0583_cli_ul217.zip>`__    |
   +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | **Algorithm for EN14604:2005 Standard**       | `EN14604 hex with CLI stream <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/cn0583_cli_en14604.zip>`__ |
   +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | **No Algorithm**                              | `no-alarm CLI hex <https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/cn0583_no_alarm.zip>`__               |
   +-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   


-  Connect the EVAL-CN0583-CRR1 carrier board to your PC using an USB cable.
-  Wait for the DAPLINK directory to appear on your PC's filesystem.
-  Copy the hex file to the DAPLINK directory.
-  The hex file will now be written in the MAX32660's flash memory (this should take a few seconds). After that, the DAPLINK directory will be deleted.
-  Wait for the DAPLINK directory to be created again (without unplugging the USB cable). After that, the CN0583 SOM is programmed with the new firmware. You may now use the CLI application by following the steps in the next section.

| 
| === Serial Terminal Setup ===

-  Plug in your connected device using a USB cable or other serial cable.
-  Wait for the device driver of the connected device to install on your PC or Laptop.
-  Open your device manager, and find out which COM port was assigned to your device.

|image2|

   \* Open up your serial terminal program (e.g., PuTTY)
-  Click on the serial configuration tab or window, and input the settings to match the requirements of your connected device. The default baud rate for most of the reference designs is 115200. Make sure that you use the correct baud rate for your application.

|image3|

   \* Ensure you click on the checkboxes for **Implicit CR in every LF** and **Implicit LF in every CF**.
-  Ensure that local echo and line editing are enabled, so that you can see what you type and are able to correct mistakes. (Some devices may echo typed characters - if so, you will see each typed character twice. If this happens, turn off local echo.)

|image4|

   \* Click on the open button, and as long as your connected device and serial terminal program are setup the same, then you should be able to start entering commands.

Running the Demo​
-----------------

-  With the hardware and software setup properly, expect the following output in the terminal below.
-  Fix the CN0583 board on a flat surface facing up or in an upright position with a sturdy stand. The smoke sensor tester can will be used in this section.
-  See Table at the end of this section for a list of commands useful for this demo.
-  With the terminal console open, press ENTER.
-  Enter the following commands to start the stream:

::

   os 1 ---- Set the sample rate to 1 sample per second

| Press ENTER.
| ``s ---- Start the device in GO mode and stream data`` Press ENTER.
| A stream of data in PTR value will appear. |image5| Observe that the alarm status is '0' which implies that there is no smoke event detected by the CN0583.
| Set the opening of the smoke tester nozzle facing the CN0583 sensor 2 to 4 ft. away. Spray for 1-2 quick seconds and then observe that the alarm status on the terminal console will turn high '1'. |image6|

.. tip::

   Note that the alarm will settle down to go back to its normal state after a few seconds along with the buzzer.


::

   i ---- Put the device in idle mode/stop data stream

Typing **help** (or simply **h**) after the initial calibration sequence will display the list of commands and their shortened versions.

+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| Function            | Short Command    | Verbose Command      | Description                                                                                                                                 | Example                                                 |
+=====================+==================+======================+=============================================================================================================================================+=========================================================+
| Application Control | **h**            | **help**             | Display the help tooltip.                                                                                                                   |                                                         |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **s** <*no*>     | **stream** <*no*>    | Put the device in GO mode and stream data from the device to the terminal.                                                                  | To stream data indefinitely:                            |
|                     |                  |                      | <**no**> = number of samples to stream to the terminal. If left unspecified, this is automatically assumed infinite when **s** is executed. | **s**                                                   |
|                     |                  |                      |                                                                                                                                             | To stream only 5 samples:                               |
|                     |                  |                      |                                                                                                                                             | **s 5**                                                 |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **i**            | **idle**             | Stop the stream and put the device in program mode.                                                                                         |                                                         |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **ms** <*opt*>   | **mode_set** <*opt*> | Set the output mode of the data.                                                                                                            | To set the output mode to PTR:                          |
|                     |                  |                      | <**opt**> = 'code' to stream data in codes; 'ptr' to stream data in PTR.                                                                    | **ms ptr**                                              |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **os** <*odr*>   | **odr_set** <*odr*>  | Set the output data rate.                                                                                                                   | To set the output data rate to 2.45 samples per second: |
|                     |                  |                      | <**odr**> = new data rate.                                                                                                                  | **os 2.45**                                             |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **og**           | **odr_get**          | Display the current output data rate.                                                                                                       |                                                         |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+
| :::                 | **n** <*string*> | **note** <*string*>  | Print user note on the console.                                                                                                             | To print 'Note 1' on the console:                       |
|                     |                  |                      | <**string**> = text to be printed.                                                                                                          | **n Note 1**                                            |
+---------------------+------------------+----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/start/requirements.png
.. |image2| image:: https://wiki.analog.com/_media/wiki/device_manager.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0583/putty_settings.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/wiki/putty_terminal_options.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/start/stream.png
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn-0583/start/stream_high.png
