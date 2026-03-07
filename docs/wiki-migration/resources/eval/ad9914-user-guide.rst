AD9914/AD9915 Evaluation Board User Guide
=========================================

Features
--------

::

   *PC evaluation software for control and measurement \\ of the [[:adi:`AD9914|AD9914]]` and [[:adi:`AD9915|AD9915]]` 
   *USB connection to PC
   *Microsoft Windows-based evaluation software with simple \\  graphical user interface (supports 64-bit versions of Windows) 

Applications
------------

-  Agile LO frequency synthesis
-  Programmable clock generator
-  FM chirp source for radar and scanning systems
-  Test and measurement equipment
-  Acousto-optic device drivers
-  Polar modulator
-  Fast frequency hopping

General Description
-------------------

This user guide describes how to set up and use the :adi:`AD9914` and :adi:`AD9915` evaluation board. The :adi:`AD9914` is a 3.5 GSPS direct digital synthesizer (DDS) with a 12-bit DAC; The :adi:`AD9915` is a 2.5 GSPS direct digital synthesizer (DDS) with a 12-bit DAC. The evaluation board software provides a graphical user interface (GUI) for easy communication with the device along with many user friendly features, such as the mouse-over effect. This user guide is intended for use in conjunction with the :adi:`AD9914` and :adi:`AD9915` data sheets.

|

.. container:: centeralign


   ..

|image1|

   *Figure 1. AD9914/PCBZ*


Evaluation Board Software
-------------------------

The :adi:`AD9914`/:adi:`AD9915` evaluation software allows the user to control the full functionality of the :adi:`AD9914`/:adi:`AD9915` through SPI communication on the evaluation board. 64-bit versions of Windows® are supported. Use the following instructions to set up the evaluation board software.

Installing the Software
~~~~~~~~~~~~~~~~~~~~~~~

Do not connect the evaluation board until the software installation is complete.

-  Uninstall any prior versions of the software before a new installation update. Note that administrative privileges are required for installation.
-  Go to the Analog Devices website to download the latest evaluation software for the :adi:`EVAL-AD9914`.
-  Click on the **Software and Tools** button and then click **AD9914 Evaluation Board Software** to download. The current version of software is **AD9914_Setup_v1.0.4595.26695.exe**. Note that a newer version may be available online.
-  Follow the installation instructions as prompted.

Installing the Device Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After the installation of the evaluation software is complete, follow these steps to install the device driver:

::

   -Power up the evaluation board and apply the REF CLK source. See the [[/resources/eval/ad9914-user-guide#evaluation_board_hardware|Evaluation Board Hardware]] section for properly powering the evaluation board.
   * Connect the evaluation board to the computer via the USB port using the USB cable included in the evaluation board kit. When the USB connection is recognized, a green LED light (D200) illuminates and the **Found New Hardware Wizard** dialog box appears.
   * Click **Next** to continue installing the new driver. 
   * Click **Continue Anyway** when the **Hardware Installation Warning** window appears.
   * Click **Finish** in the **Found New Hardware Wizard** when installation is complete. Note that another **Found New Hardware Wizard** dialog box usually appears to complete the device driver installation. 
   * Repeat Step 3 to Step 5 in this section.

Confirming the Connection
~~~~~~~~~~~~~~~~~~~~~~~~~

A successful connection of the software to the board is indicated by a green USB icon, which can be found at the bottom right corner of the main GUI window.

Troubleshooting
~~~~~~~~~~~~~~~

An unsuccessful connection is indicated by a flashing red USB icon located at the bottom right corner of the window. Most installation errors can be resolved by checking jumper settings, making sure that the evaluation board is powered up correctly, and inspecting the USB port and cable connections. When all power, USB port/cable connections, and jumper settings are correct, an error may still appear if the clock input is not configured properly. Check to make sure that the clock input source is connected and configured properly. Another reason an error may appear is due to the presence of a conflicting device driver. To resolve this issue, update the driver by plugging the USB connector into another USB port. When the **Found New Hardware Wizard** appears, install a device driver as follows:

-  Select **Install from a list or specific location (Advanced)**, and then click **Next**.

.. container:: centeralign

   
   | |image2|
   | *Figure 2. New Found Hardware Window*


-  Choose **Don’t search. I will choose the driver to install**, and then click **Next**.

.. container:: centeralign

   \


   |image3|

   | 
   | *Figure 3. Search and Installation Options Window*


-  Select the **AD9914 Firmware Loader**, and then click **Next**. Note that on occasion the operating system may load the wrong driver because the operating system detects multiple drivers, such as the evaluation board, that can be used by the hardware. In such a case, multiple drivers might be listed in this window. Select only the **AD9914 Firmware Loader**, and then click **Next**. A **Hardware Installation** box then appears. Click **Continue Anyway**, and then close the wizard by clicking **Finish**.

.. container:: centeralign

   \


   |image4|

   | 
   | *Figure 4. Select Device Driver Window*


Evaluation Board Hardware
-------------------------

The evaluation board provides all of the support circuitry required to operate the :adi:`AD9914` and :adi:`AD9915` in their various modes and configurations. Figure 1 shows the typical bench characterization connections used to evaluate the ac performance.

Power Supplies
~~~~~~~~~~~~~~

| The :adi:`AD9914` evaluation board has one power supply connector labeled P300 to power the USB interface circuitry and the :adi:`AD9914`/:adi:`AD9915`. This connector has four pins; connect individual wires back to power supplies to power the evaluation board. Table 1 shows the necessary connections and the appropriate supply voltage
| **Table 1. Power Supply Connections**

======= ===== =======
Pin No. Label Voltage
======= ===== =======
1, 3    GND   0
2       3.3 V 3.3
4       1.8 V 1.8
======= ===== =======

Input Reference Clock Signal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`AD9914`/:adi:`AD9915` architecture provides the user with two options when providing an input clock signal to the part:

-  Connect a high frequency input clock signal up to 3.5/2.5 GHz to J104.
-  Connect a lower input reference frequency to J104 and enable the internal clock multiplier (PLL).

The maximum frequency rate of the PFD of the internal PLL is 125 MHz. The input clock to the DDS is called the REF CLK. The internal system clock runs at the REF CLK rate if the internal REF CLK multiplier (PLL) is disabled. Otherwise, the internal system clock runs at the output frequency rate of the PLL. Note that the input clock path on the evaluation board uses an :adi:`ADCLK925` clock buffer to drive the :adi:`AD9914`/:adi:`AD9915` differentially. Therefore, if the input signal into the :adi:`ADCLK925` has a slow slew rate, the in-close phase noise performance of the :adi:`AD9914`/:adi:`AD9915` may be dramatically limited by the :adi:`ADCLK925`.

Refer to the :adi:`ADCLK925` data sheet for details on the maximum input speeds and input sensitivities. The SYNC_CLK runs at 1/24th the system clock rate and the default state is SYNC_CLK enabled. Thus, if the SYNC_CLK is not running, the device is powered down or the REF CLK is invalid.

DAC Output Signal
~~~~~~~~~~~~~~~~~

The main output signal of the DDS is the DAC output. Note that the output of the DDS may or may not have a DAC reconstruction filter after the balun on the evaluation board depending on the revision of the board.

Jumper Settings
~~~~~~~~~~~~~~~

The jumpers on the evaluation board are factory set so that the board is ready to use with PC control. The software GUI operates the evaluation board in a serial interface only; however, you can also opt to use an alternative external control. Note that this user guide does not cover all aspects of externally controlling the evaluation board.

| If you tri-state the USB circuitry to drive the board externally, you must control all tri-stated inputs to the :adi:`AD9914`/:adi:`AD9915`. Otherwise, the device may not response to the external stimulus. For example, if the master reset input or the EXT_PWR_DWN input are floating, any external programming will have intermittent issues. All digital inputs are accessible via the provided header connectors.

Jumper Settings for Communication Modes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For PC control (factory settings)

-  Set jumpers P203, P204, P205 to Enable.
-  Install jumpers P105, P202, P205 to Enable.
-  Set jumpers IOCFG0 to IOCFG4 to 1000.

For external control

-  Set jumpers P203, P204, P205 to Disable.
-  Control the :adi:`AD9914`/:adi:`AD9915` via external header connectors.

External Header Connectors
~~~~~~~~~~~~~~~~~~~~~~~~~~

The external I/O control headers provide a parallel or serial communication interface for the :adi:`AD9914`/:adi:`AD9915` when the part is under the command of an external controller. In addition, the headers provide an interface for modulation data depending on the setting of the function pins. See the data sheet for more details on the function pins settings.

Disabling Software GUI Control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disabling the ICs on the evaluation board allows operation of the board with an external serial or parallel control by configuring each buffer in its high impedance state by its nearby jumper.

USB Port
~~~~~~~~

When the part is under PC control (default mode), the evaluation board communicates with the :adi:`AD9914`/:adi:`AD9915` via the USB port.j

Modes of Operation
------------------

Profile Mode
~~~~~~~~~~~~

In profile mode, the three DDS signal control parameters (frequency, phase offset, and amplitude scaling) are supplied directly from 1 of 8 internal profile registers. A profile is an independent register that contains all three control parameters. You can use a profile register to output a single tone frequency or use multiple preprogram profile registers and the profile pins to hop between frequencies, phase offsets and/or different amplitude settings. The following example are the steps to program a single profile to output a single tone frequency using the software GUI.

===Single Tone Operation===

::

    -Power up the evaluation board and apply the REF CLK source to clock the [[:adi:`AD9914|AD9914]]/[[https://www`.analog.com/AD9915|AD9915]].    
    -Launch the evaluation software. After the software recongnizes the evaluation board, click the master reset icon in the main tool bar of the software GUI (labeled 1 in Figure 7). The master reset clears all memory elements and sets the registers to default values.
    -Enter the desired REF CLK frequency value in the **External Clock** box. If the internal PLL is to be used, enable and load those desired PLL settings at this time.
    -After the desired system clock frequency appears in the main tool bar of the software GUI, click the DAC calibration icon (labeled 3 in Figure 7). The DAC CAL is required once for the initial setup and/or every time the REF CLK frequency is changed.
    -Click the **Profiles** tab to access the Profiles window and enable profile mode via the check box.
    -Enter the desired output frequency in Profile 0. See Figure 5 for a view of an individual profile.
    -Click the flashing **Load** button (labeled 5 in Figure 7) near the top of the GUI. 
    -View the DAC output single tone frequency performance via an oscilloscope or spectrum analyzer.

To select a profile other than Profile 0, use the **Selected Profile** drop-down menu. Note that, unfortunately, the profile pin signals are sent asynchronously from the buffer ICs on the evaluation board to the profile pins. Thus, it is possible that the profile found may not be the profile you selected because the profile signals are not synchronous to the SYNC_CLK. If the selected profile setting does not point to the correct profile settings chosen, send an IO_UPDATE or click **Load** tocorrect the issue. This would not be an issue if the profile signals were sychrnonously transmitted to the :adi:`AD9914`/:adi:`AD9915`.

Profile Data Entry
^^^^^^^^^^^^^^^^^^

| 
|

.. container:: centeralign


   ..

|image5|

   | *Figure 5. Single Profile Window*


The **Frequency** box is used to set the frequency generated by the DDS. The input values are in megahertz. Refer to the data sheet for the acceptable range of output frequencies.

The **Phase Offset** box controls the phase of the DDS output. The input is in degrees and can be changed from 0° to 360° with 16-bit resolution.

The **Amplitude Scale Factor** box digitally controls the amplitude of the carrier from the DDS. This scalar ranges from 0 to 1 and has a 12-bit resolution. Note that this function works only if the **OSK enable** is selected in the **Control** tab.

Note that **Frequency**, **Phase Offset**, and **Amplitude Scale Factor** can accept native data that are to be loaded directly to the registers. This data is binary in form, but can also be expressed as hexadecimal or decimal. Change the format by clicking the drop-down button to the right of each box.

Sweep Mode
~~~~~~~~~~

The Digital Ramp Generator (DRG) window is accessible via the **Sweep** Tab directly below the GUI tool bar. The DRG can sweep frequency, phase, or amplitude. The DRG allows independent control of the slope of a rising sweep and the falling sweep along with other features (see Figure 5).


| 
|

.. container:: centeralign

   | |image6|
   | *Figure 6. Digital Ramp Generator Window*


To enable the DRG for configuration,

-  Select the **Enable Digital Ramp Generator** check box.
-  In the **Mode** section, select the parameter (**Frequency**, **Phase**, or **Amplitude**) to be sweeped.

In the **Settings** section, the **Auto Clear Digital Ramp Accumulator** check box allows the DRG to be cleared every time the I/O update signal is applied or when there is a profile pin change. The **Clear Digital Ramp Accumulator** check box keeps the DRG cleared until the check box is cleared. The **Load SRR @ I/O Update** check box allows the reload of a new digital ramp rate when an I/O update is issued or when there is a profile change.

If the parameter to be sweeped is **Frequency**, use the **Sweep Frequency 0** and **Sweep Frequency 1** boxes to enter the lower frequency limit value and upper frequency limit value, respectively. The units are megahertz for freqency, degrees for phase, and volts for amplitude. Note that the value in the **Sweep Frequency 0** box is required to be be less than the value in the **Sweep Frequency 1** box regardless of the parameter being swept. The **Rising Sweep Ramp Rate** and **Falling Sweep Ramp Rate** boxes are used to set the time between each rising or falling step on the ramp and is in units of microseconds.

The **No Dwell High** and **No Dwell Low** check boxes are used to instantaneously return to the lower or upper limit depending of which box is checked. To continously repeat a parameter sweep without clicking the up/down buttons or just enable both No Dwell bits. If not, use the **Up**, **Down**, and **Pause** buttons at the bottom of the window to control the sweep direction or to halt the sweep. The **Ramp Finished** indicator illuminates when the ramp is complete.

Keep the following points in mind:

-  The rising and falling ramp rate windows in the present version of software are reversed. This will be addressed in a software revision. For now, make the appropriate changes.
-  If the DRG is used to sweep amplitude, the OSK enable bit must be selected in the **Control** tab window.
-  After the desired configuration is completed, saving the setup is preformed using the save settings feature.

Programmable Modulus Mode
~~~~~~~~~~~~~~~~~~~~~~~~~

Programmable Modulus Window

The chip is in programmable modulus mode when the **Enable Programmable Modulus** check box is selected. Note that the digital ramp generator mode is automatically disabled.

The Programmable Modulus window is used to alter the frequency equation of the DDS core, making it possible to implement fractions that are not restricted to a power of 2 in the denominator.

When you enter the desired output frequency (in megahertz) in the **FOUT** box, the values in the **Register Values** boxes and the **Divide Ratio** boxes are automatically updated. You can also directly input a divide ratio, which in turn automatically updates the **Register Values** boxes and the **Output Frequency** box.

Overview of the GUI Windows
---------------------------

Toolbar
~~~~~~~

| The toolbar near the top of the evaluation software main window includes several buttons, each labeled with an icon, that allow you to easily initiate various actions (refer to Figure 6 for a detailed description of the requirements of each toolbar element).
|

.. container:: centeralign


   ..

|image7|

   | *Figure 7. Toolbar Description*


Tabs
~~~~

| There are five tabs available in the main window of the evaluation software: **Control**, **Profiles**, **Sweep**, **Modulus**, and **Debug**. The following tab descriptions provide a brief overview of each tab; more detailed information can be found in the Evaluation and Test section.
|

<WRAP centeralign>


|image8|

| *Figure 8. Tabs Available*

Control Tab
^^^^^^^^^^^

The **Control** tab provides control of the internal PLL, parallel port, auxiliary functions, I/O control, power-down functions, output shift keying (OSK), clock calibration, and multichip sync function of the :adi:`AD9914`/:adi:`AD9915`.

Profiles Tab
^^^^^^^^^^^^

The **Profiles** tab allows enabling of profile mode, in which the DDS signal control parameters are supplied directly from the profile programming registers. A profile is an independent register that contains the DDS signal control parameters.

Note that, unfortunately, it is not guaranteed that selecting a profile will switch to the correct profile setting. This is because the profile signals are sent asynchronously via the GUI hardware. The reality is that the profile signals need to meet setup and hold times to the SYNC_CLK.

Sweep Tab
^^^^^^^^^

Digital ramp generator (DRG) is synonymous with linear sweep. The ramp generation parameters in the **Sweep** tab allow you to control both the rising and falling slopes of the ramp, the upper and lower boundaries of the ramp, the step size and step rate of the rising portion of the ramp, and the step size and step rate of the falling portion of the ramp. This is digitally generated with a 32-bit output resolution that can be programmed to represent frequency, phase, or amplitude. Refer to the data sheet for more information on DRG.

Modulus Tab
^^^^^^^^^^^

The Modulus tab allows you to enable programmable modulus mode and to alter the frequency equation of the DDS core, making it possible to implement fractions that are not restricted to a power of 2 in the denominator. See the data sheet for more details.

Debug Tab
^^^^^^^^^

The Debug tab provides complete direct access to the register map as well as control of many external pins. The Debug tab is intended for debugging issues with the :adi:`AD9914`/:adi:`AD9915`. Although this tab can be used for all programming, it is not user friendly for programming purposes and, therefore, using the **Debug** tab for purposes other than debugging may result in improper programming of reserved bits.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/figure1_ad9914_evb.png
   :width: 700px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/figure2_found_new_hardware_wiz.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/figure3_found_new_hardware_wiz2.png
.. |image4| image:: https://wiki.analog.com/_media/{{/resources/eval/user-guides/ad9914/figure4_found_new_hardware_wiz3.png
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/drawing1.png
   :width: 600px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/sweep.png
   :width: 500px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/tool_bar.png
   :width: 900px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/ad9914/tabs.png
   :width: 300px
