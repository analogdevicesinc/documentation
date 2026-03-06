AMR Current Sensing Protocol Addendum
=====================================

Features
--------

-  Data Visualization
-  Data Logging
-  Real-Time Data Capture
-  Peripheral Configuration
-  System Calibration

Hardware Required
-----------------

-  AMR Current Sensing System

   -  Castor Sensor Board
   -  Gemini Acquisition Board

-  5V Wall Adapter
-  Standard USB A to Micro-B USB cable
-  PC running Windows 10

.. container:: centeralign

   \ |image1|\ *Figure 1. User Interface*


.. container:: centeralign

   \ |image2|\ *Figure 2. Gemini and Castor System*


General Description
-------------------

| This is an addendum to the software user guide describing additional steps that may be required for the AMR Array Based Contactless Current Sensing Evaluation System shown in Figure 1. The Gemini platform has used two different communication protocols. This addendum describes how to change these settings to ensure stable communication.
| The Castor and Gemini boards together make up an AMR array based contactless current sensing system shown in Figure 2. Please refer to the AMR Current Sensing User Guide for more detailed information on the hardware and its configuration.
| To operate the board, plug in the wall adaptor and press and hold the ON/OFF button for more than 1 second. The LCD will turn on and display measurement results. Connect the USB cable and launch the software (after installation procedure) to get started.

Software Installation Details
-----------------------------

The AMR Current sensing software uses LabView from National Instruments. The following National Instruments packages are installed and required to run. Runtime engines will be installed in the C:\\Program Files (x86)\\National Instruments\\ directory during installation of the application.

-  NI LabVIEW Runtime 2016f7 (32-bit)
-  NI-488.2 Runtime 19.0
-  NI-Serial Runtime 19.0
-  NI-VISA Runtime 19.0

The default destinations of other installed files are shown below for reference. Application Directory:

-  “C:\\Program Files (x86)\\ADI\\Contactless AMR Current Measurement\\Contactless AMR Current Measurement.exe”

Configuration Files Directory:

-  “C:\\ProgramData\\ADI\\Contactless AMR Current Measurement\\Configuration Files\\

Evaluation Hardware Procedures
------------------------------

The AMR Array based contactless current sensing system can be connected via USB and the supplied power adaptor. **Connecting the Evaluation Hardware to a PC** To connect the evaluation board to a PC and measure a current. Refer to the AMR Current Sensing User Guide for specific details on the hardware.

-  Separate the Castor board.
-  Connect the Castor board to the Gemini Board.
-  Place the wire to be measured in the Castor board and reconnect the removable jaw and plastic spacers.
-  Plug in the wall adapter completely so that it is flush with the connector.
-  Press and hold the ON/OFF button for more than 1 second to power on.
-  The LCD will turn on and will start displaying the measurement results.
-  Connect the USB Cable.

**Verifying Hardware Connections** Once the evaluation board is connected and powered, proper connection can be verified by taking the following steps.

-  Navigate to This PC in Windows Explorer.
-  Verify that DAPLINK (D:) is displayed per Figure 3. The drive letter D: may differ for each PC.

.. container:: centeralign

   \ |image3|\ *Figure 3. Verifying PC to Evalaution Board Connection*


The evaluation hardware can also be checked in the DEVICE Manager window under Ports (COM & LPT) as mbed Serial Port (COMXX), where XX will be a two digit number.

.. container:: centeralign

   \ |image4|\ *Figure 4. Board Status Device Manager*


Updating Firmware
-----------------

The microcontroller firmware can be updated or revised easily. A hex file or “.hex” file can used to update the µC configuration over USB by following the steps below.

-  Ensure hardware is powered on and connected as described in the previous section
-  Navigate to the directory DAPLINK(D:),See Figure 5
-  Copy and paste or drag and drop the supplied .hex file into the directory.
-  Wait until coping completes, this may take 5-10seconds.
-  The LCD panel on Gemini will stop updating.
-  Push the reset button on the Gemini Hardware to complete the process. See Figure 6

Once these steps are complete the µC will reset and the new firmware will have been flashed. Ensure that power and connection to the board is maintained throughout this process. Normal operation can resume.

.. container:: centeralign

   \ |image5|\ *Figure 5. DAPLINK(D:) folder*


.. container:: centeralign

   \ |image6|\ *Figure 6. Hexfile copy to DAPLINK(D:) by USB*


.. container:: centeralign

   \ |image7|\ *Figure 7. Gemini Button Location*


.. |image1| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini12.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz_kit_top.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini13.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini14.png
   :width: 450px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini15.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/gemini16.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/ev-adaf1080-16ebz/buttons_leds.png
   :width: 400px
