Software Guide
==============

Evaluation Board Software
=========================

Software Installation Procedures
--------------------------------

Download the :adi:`ACE <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>` software from the ACE software page or the AD4130 product page. Install ACE on a PC before using the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1. The ACE installation process in the Installing the ACE Software section includes the ACE software installation and the SDP driver installation. Install the ACE software and SDP drivers before connecting the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 and the SDP-B or SDP-K1 to the USB port of the PC to ensure that the evaluation system is properly recognized when it is connected to the PC.

Installing the ACE Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| To install the ACE software, take the following steps:
| \* Download the ACE software to a Windows®-based PC.

-  Double click the **ACEInstall.exe** file to begin the installation. By default, the software is saved to the following location: **C:\\Program Files (x86)\\Analog Devices\\ACE**.
-  A dialog box opens asking for permission to allow the program to make changes to the PC. Click **Yes** to begin the installation process.
-  In the **ACE Setup** window, click **Next** > to continue the installation.

|image1|

-  Read the software license agreement and click **I Agree**.

|image2|

-  Click **Browse …** to choose the installation location and then click **Next >**.

|image3|

-  The ACE software components to install are preselected. Click **Install**.

|image4|

-  The Windows Security window opens. Click **Install**. No action is required.
   |image5|\ |image6|
-  When the installation is complete, click **Next** >, and then click **Finish** to complete the installation process.

|image7|

| 
| ====Evaluation Board Setup Procedures==== The EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 connects to the SDP-B. The SDP-B is the communication link between the PC and the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1. ===Connecting the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 and the SDP-B to a PC==== After the ACE software is installed, take the following steps to set up the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 and the SDP-B.

-  Ensure that all configuration links are in the appropriate positions, as detailed in `hardware guide <http://wiki.analog.com/resources/eval-ad4130/hardwareguide>`__.
-  Connect the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 to the 160-way connector on the SDP-B. The EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 does not require an external power supply adapter.
-  Connect the SDP-B to the PC via the USB cable included in the SDP-B kit.

===Verifying the Board Connection=== After connecting the power and the USB cable from the SDP-B/ SDP-K1 to the PC, take the following steps to verify the board connection:

-  After connecting the SDP to the PC, allow the **Found New Hardware Wizard** to run. Choose to automatically search for the drivers for the SDP if prompted by the operating system.
-  Navigate to the **Device Manager** window on the PC.
-  A dialog box may open asking for permission to allow the program to make changes to the computer. Click **Yes**.
-  The **Computer Management** window opens. From the list labeled **System Tools**, click **Device Manager**. If the SDP driver is installed and the board is properly connected to the PC, **Analog Devices SDP** is shown in the **ADI Development Tools** list in the **Device Manager** window.

| ===Disconnecting the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1=== Disconnect power from the SDP-B / SDP-K1, or press the reset tact switch located alongside the mini USB port on the SDP, before removing the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 from the SDP. ====AD4130 Plugin Download==== Download the AD4130 Plugin software from your `myanalog <https://my.analog.com/en/app/>`__ account.
| Steps to downloading AD4130 Plugin:

-  Login to your myAnalog.com account.
-  Click on your myAnalog Dashboard.
-  Under “Special Resources” click on the link call “AD4130 ACE Plug In V 1.0 Software Download”. Note the version number could be different at time of downloading.
-   Once you clicked on the link a new tab will pop up.
-   Read the software license agreement, click the checkbox and **I Accept**.
-  Click Download.
-  The AD4130 Plugin will download to you Download Location setup in your browser.

====AD4130 Plugin Install==== After the AD4130 Plugin is downloaded follow the steps to install the file:

-  Double click on the AD4130 Plugin.
-  Connect up your EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1/EV-AD4130WASDZ-U1 to your pc through a SDP-B controller board.

Alternatively, the AD4130 Plugin can be installed through the steps bellow:

-  From the **Start** menu of the PC, select **All Programs >Analog Devices > ACE> ACE.exe** to open the ACE software main window.
-  Click on the Plug-in Manager Tab in the top left panel in ACE.
-  Click on the Settings… button.
-  Hit the + button next to the Zipped Plug-in Sources.
-  Under the Name write “AD4130”.
-  Under Source hit the … button and set the path to where you have stored the AD4130 Plugin.
-  Hit “Ok”.
-  Hit “Close”.

| 
| ====ACE Software Operation====

Launching The Software
~~~~~~~~~~~~~~~~~~~~~~

After the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 and SDP-B\\ SDP-K1 are properly connected to the PC, launch the :adi:`ACE <en/design-center/evaluation-hardware-and-software/evaluation-development-platforms/ace-software.html?doc=EVAL-AD7383FMCZ-ug-1770.pdf>` software by taking the following steps:

-  From the **Start** menu of the PC, select **All Programs > Analog Devices > ACE> ACE.exe** to open the ACE software main window.
-  If the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 is not connected to the USB port via the SDP when the software launches, the **AD4130 Eval Board** icon does not appear in the **Attached Hardware** section in ACE. To make the **AD4130 Eval Board** icon appear, connect the EV-AD4130-8ASDZ-U1/EV-AD4130WASDZ-U1 and the SDP to the USB port of the PC, wait a few seconds, and then follow the instructions in the dialog box that opens.
-  Double click the **AD4130 Eval Board** icon to open the **AD4130 Eval Board** view window.
-  Double click the **AD4130** chip icon in the **AD4130 Eval Board** view window to open the **AD4130** chip view window.
-  Click **Software Defaults** and then click **Apply Changes** to apply the default settings to the AD4130.

Description of Chip View Window
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the steps in the Software Installation Procedures section and the Evaluation Board Setup Procedures section, set up the system for data capture by taking the following steps:

-  Block icons that are dark blue are programmable blocks. Click a dark blue block icon to open a configurable pop-up window to customize the data capture.
-  The “Proceed to Memory Map” button brings the user to the memory map of the AD4130. This allows the user to configure the AD4130.
-  The “Proceed to Analysis” button brings the user to the Analysis tab. This allows the user to see the performance results of the AD4130 and displays the data.

Waveform Tab
~~~~~~~~~~~~

The **Waveform** tab graphs the conversions gathered and processes the data, calculating the peak-to-peak noise, rms noise, and resolution.

Waveform Graph and Controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The data waveform graph (Label 1) shows each successive sample of the ADC output. Zoom in on the data in the graph using the scroll wheel on your mouse or by selecting the magnifying glass.

Analysis Channel
^^^^^^^^^^^^^^^^

The **Result** section shows the analysis of the channel selected(Label 3).

Samples
^^^^^^^

The **Samples** numeric control (Label 4)set the number of samples gathered per batch. This control is unrelated to the ADC mode. You can capture a defined sample set or continuously gather batches of samples. In both cases, the number of samples set in the **Samples**\ (Label 4) numeric input dictates the number of samples.

Capture
^^^^^^^

Click the Run Once button (Label 2) to start gathering ADC results. Click the **Run Continuously** button (Label 2) to start gathering ADC results continuously. Results appear in the waveform graph (Label 1).

Display Units and Axis Controls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click the **Codes** drop-down menu (Label 5) to select whether the data graph displays in units of voltages or codes. This control affects both the waveform graph and the histogram graph. The axis controls is fixed. When selecting **Fixed**, the axis ranges can be programmed; however, these ranges do not automatically adjust after each batch of samples.

Noise Analysis
^^^^^^^^^^^^^^

| The **Noise Analysis** (Label 3) section displays the results of the noise analysis for the selected analysis channel, including both noise and resolution measurements.
| |image8|

Memory Map Tab
~~~~~~~~~~~~~~

Use the Memory Map tab to access the registers of the AD4130-8. This tab changes register settings and shows additional information about each bit in each individual register.

Export Buttons
^^^^^^^^^^^^^^

The **Export** buttons (Label 1) on the **Register Map** tab allow the user to save and load register settings. Click **Save** to save all the current register settings to a file for later use. Click **Load** to load a previously saved register map.

Register
^^^^^^^^

The **Register** section (Label 2) shows the value that is set in the selected register. Check the value of the register in this window by clicking on the bits. Clicking any individual bit changes the bit from 1 to 0 or 0 to 1, depending on the initial state of the bit. The register value can also be changed by writing the hexadecimal value in the input field to the right of the individual bits.

Bitfields
^^^^^^^^^

The **Bitfields** section (Label 3) shows the individual bitfield of the selected register. The register is broken by name into its bitfields, name of the bitfields, a description of each bitfield, and access information.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105322.png
   :width: 300px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105338.png
   :width: 300px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105352.png
   :width: 300px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105623.png
   :width: 300px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105652.png
   :width: 300px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105707.png
   :width: 300px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad4130/screenshot_2021-05-05_105719.png
   :width: 300px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval-ad4130/screenshot_2021-04-09_122534.png
   :width: 600px
