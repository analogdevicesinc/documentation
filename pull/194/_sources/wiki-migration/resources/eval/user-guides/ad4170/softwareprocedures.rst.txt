Software Guide
==============

Ace Plugin
==========

Ace Plugin Install guide
------------------------

-  **Warning**: The evaluation software and drivers must be installed before connecting both the evaluation board and the Controller (SDP) board to the PC. This ensures that the evaluations system is correctly recognized when it is connected to the PC.

The software and drivers required for the installation walked through in this section can be found below:

-  :adi:`Ace Software <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>`
-  :adi:`AD4170 Ace Plugin <media/en/evaluation-boards-kits/evaluation-software/AD4170>` <fc #ff0000>UPDATE WHEN AVAIL</fc>
-  `SDP controller system demonstration platform drivers <http://swdownloads.analog.com/ACE/SDP/SDPDrivers.exe>`_

Installing the ACE Plugin software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the ACE software from the ACE software page or the AD4170 product page. Install ACE on a PC **before using** the EV-AD4170-ASD1Z-U1.

Installing ACE
~~~~~~~~~~~~~~

-  Download the ACE software to a Windows®-based PC.
-  Double click the ACEInstall.exe file to begin the installation. By default, the software is saved to the following location: C:\\Program Files (x86)\\Analog Devices\\ACE.
-  A dialog box opens asking for permission to allow the program to make changes to the PC. Click Yes to begin the installation process.
-  In the ACE Setup window, click Next > to continue the installation.

|image1|

-  Read the software license agreement and click I Agree

|image2|

-  Click Browse … to choose the installation location and then click Next >

|image3|

-  The ACE software components to install are preselected. Click Install.\

|image4|

-  The Windows Security window opens . Click Install

|image5|

-  The installation in progress in the window below. No action is required.

|image6|

-   When the installation is complete, click Next >, and then click Finish to complete the installation process

|image7|

AD417x Plugin Download
~~~~~~~~~~~~~~~~~~~~~~

Download the AD4170 Plugin software from your myanalog account. Steps to downloading AD4170 Plugin:

-  Login to your myAnalog.com account.
-  Click on your myanalog Dashboard.
-  Under “Special Resources” click on the link call “AD4170 ACE Plug In V 1.0 Software Download”. Note the version number could be different at time of downloading. <fc #ff0000>REPLACE with 4170 type</fc>\

|image8|

-   Once you clicked on the link a new tab will pop up.
-   Read the software license agreement, click the checkbox and I Accept

|image9|

-   Click Download.

|image10|

-   The AD4170 Plugin will download to you Download Location setup in your browser.

AD417x Plugin Install
~~~~~~~~~~~~~~~~~~~~~

After the AD4170 Plugin is downloaded follow the steps to install the file:

-  Double click on the AD4170 Plugin.
-  Connect up your EV-AD4170-ASD1Z-U1 to your pc through a controller board.

Alternatively, the AD4170 Plugin can be installed through the steps bellow:

-  From the Start menu of the PC, select All Programs > Analog Devices > ACE> ACE.exe to open the ACE software main window shown below.
-  Click on the Plug-in Manager Tab in the top left panel in Ace.
-  Click on the Settings… button.

|image11|

-  Hit the + button next to the Zipped Plug-in Sources.

|image12|

-  Under the Name write “AD4170”
-  Under Source hit the … button and set the path to where you have stored the AD4170 Plugin.
-  Press “Ok”.
-  Press “Close”.

ACE software Operation
----------------------

Launching the software
~~~~~~~~~~~~~~~~~~~~~~

After the EV-AD4170-ASD1Z-U1 and controller board are properly connected to the PC, launch the ACE software by taking the following steps:

-  From the Start menu of the PC, select All Programs > Analog Devices > ACE> ACE.exe to open the ACE software main window shown below
-  If the EV-AD4170-ASD1Z-U1 is not connected to the USB port via the controller board when the software launches, the AD4170 Eval Board icon does not appear in the Attached Hardware section in ACE (see Figure below).To make the AD4170 Eval Board icon appear, connect theEV-AD4170-ASD1Z-U1 and the controller board to the USB port of the PC, wait a few seconds, and then follow the instructions in the dialog box that opens.

|image13|

-  Double click the AD4170 Eval Board icon to open the AD4170 Eval Board view window shown below:

|image14|

-  Double click the AD4170 chip icon in the AD4170 Eval Board view window to open the AD4170 chip view window shown below:
-  Click Software Defaults and then click Apply Changes to apply the default settings to the AD4170 (see figure below)\

|image15|

Chip view window
~~~~~~~~~~~~~~~~

After completing the steps in the :doc:`Software Installation Procedures </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures>` section and the :doc:`Evaluation Board Set-up Procedures </wiki-migration/resources/eval/user-guides/ad4170/hardwareguide>` section, set up the system for data capture by taking the following steps:

-  Block icons that are dark blue are programmable blocks. Click a dark blue block icon to open a configurable pop-up window to customize the data capture.
-  The “Proceed to Memory Map” button brings the user to the memory map of the AD4170. This allows the user to configure the AD4170.
-  The “Proceed to Analysis” button brings the user to the Analysis tab. This allows the user to see the performance results of the AD4170 and displays the data.

Waveform Window
~~~~~~~~~~~~~~~

The Waveform tab graphs the conversions gathered and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

1) Waveform graph and controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The data waveform graph shows each successive sample of the ADC output. Zoom in on the data in the graph using the scroll wheel on your mouse or by selecting the magnifying glass.

2) Analysis Channel
~~~~~~~~~~~~~~~~~~~

The Result section shows the analysis of the channel selected


|image16|

3) Samples
~~~~~~~~~~

The Samples numeric control set the number of samples gathered per batch. This control is unrelated to the ADC mode. You can capture a defined sample set or continuously gather batches of samples. In both cases, the number of samples set in the Samples numeric input dictates the number of samples. The Noise Analysis section displays the results of the noise analysis for the selected analysis channel, including both noise and resolution measurements.

4) Capture
~~~~~~~~~~

Click the Run Once button to start gathering ADC results. Click the Run Continuously button to start gathering ADC results continuously. Results appear in the waveform graph (Label 1).

5) Display Units and Axis Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the Codes drop-down menu to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls is fixed. When selecting Fixed, the axis ranges can be programmed; however, these ranges do not automatically adjust after each batch of samples.

6) AC/DC Analysis
~~~~~~~~~~~~~~~~~

Selects the analysis performed by ACE

7) FFT Plot
~~~~~~~~~~~

Allows to view an FFT plot of the data collected.

Memory map Window
^^^^^^^^^^^^^^^^^

Use the Memory Map tab to access the registers of the AD4170, shown in the figure below. This tab changes register settings and shows additional information about each bit in each individual register.

1) Export Buttons
~~~~~~~~~~~~~~~~~

The Export buttons on the Register Map tab allow the user to save and load register settings. Click Save to save all the current register settings to a file for later use. Click Load to load a previously saved register map.

2) Register
~~~~~~~~~~~

The Register section shows the value that is set in the selected register. Check the value of the register in this window by clicking on the bits. Clicking any individual bit changes the bit from 1 to 0 or 0 to 1, depending on the initial state of the bit. The register value can also be changed by writing the hexadecimal value in the input field to the right of the individual bits.

3) Bitfields
~~~~~~~~~~~~

The Bitfields section shows the individual bitfield of the selected register. The register is broken by name into its bitfields, name of the bitfields, a description of each bitfield, and access information. Show each individual bitfield by pressing the show bitfield button (label 4). Apply these changes using label 5. Search for specific registers using label 6.


|image17|

AD4170 Demo Modes
-----------------

AD7124 Eval+ Demo Modes
=======================

| :doc:`Visit the demo mode section here </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
| **Contents of the demo modes section:**

-  :doc:`Noise Test Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`2 Wire RTD Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`3 Wire RTD Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`4 Wire RTD Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`Thermocouple Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`Thermistor Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`4 Wire Bridge Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`
-  :doc:`6 Wire Bridge Demo </wiki-migration/resources/eval/user-guides/ad4170/softwareprocedures/demo_modes>`

Virtual Eval Guide
------------------

This page provides a step by step guide to launching and using ADI's new Virtual Evaluation Tool.

-  Navigate to the Virtual Eval tool by clicking this link: `Virtual Eval <http://beta-tools.analog.com/virtualeval/>`_ or alternatively, by going to the AD4170 homepage on analog.com and finding the link there.
-  Select the AD4170 by going to 'Precision ADC < 10MSPS' and finding the part there.

|image18|

-  Now you are ready to start using the tool.

Firmware Instal Guide
---------------------

:doc:`Previous Page: Hardware Guide </wiki-migration/resources/eval/user-guides/ad4170/hardwareguide>`

:doc:`Return to Homepage </wiki-migration/resources/eval/user-guides/ad4170>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_1.png
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_2.png
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_3.png
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_4.png
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_5.png
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_6.png
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_page_7.png
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_download_page_1.png
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_download_page_2.png
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_download_page_3.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/softwareprocedures/4170_ace_plugin_install_page_1.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_install_page_2.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_launch_page_2.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_launch_page_3.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_launch_page_4.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_waveform_page_1.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4170/4170_ace_plugin_memory_page_1.png
   :width: 600px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-ad7124/software/v_eval_start.png
   :width: 600px
