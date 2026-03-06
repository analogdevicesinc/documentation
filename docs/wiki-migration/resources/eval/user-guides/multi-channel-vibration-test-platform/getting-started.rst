Multi-Channel Vibration Test Platform User Guide
================================================

GENERAL DESCRIPTION
-------------------

The Multi-Channel Vibration Test Platform is a system board capable of reading data from analog (IEPE) or digital (SPI, I2C, Extended SPI) accelerometers. The analog IEPE inputs also contain current source switches to accommodate sensors that might need external power and individual channel offset voltage setting.

Aside from sensor data reading, the board is also capable of providing a variable amplitude and frequency signal to an external vibration shaker as a stimulus.

With this, the board can provide a signal to an external shaker and measure the data from a mounted sensor, forming a closed feedback loop.

--------------

REQUIREMENTS
------------

The Multi-Channel Vibration Test Platform is a complete system from Hardware, Firmware, to Software for performing basic Data acquisition (DAQ) functions and vibration tests.

The following sections will detail the necessary steps and conditions needed to fully operate the system.

FIRMWARE
~~~~~~~~

Once the Multi-Channel Vibration Test Platform software is installed via the given installer (Refer to Multi-Channel Vibration Test Platform GUI Installer Section), the compatible firmware is located within the same folder as the GUI executable file.

At startup, the GUI uploads the firmware to the board for easier use. Do not remove the firmware (.img file) in the folder to avoid errors.

Should there be any updates, the existing GUI version should be uninstalled and the new installer with its new compatible firmware should be used.

Multi-Channel Vibration Test Platform Temporary Shared Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The files, codes, executables, and other necessary documents are located on a temporary sharepoint folder for access:

-  link for


|Repository|

Note: Contact the repository administrators in case access is denied or for any concerns, suggestions, or feedback through the following e-mail addresses:

-   Jose.Sanbuenaventure@analog.com
-   Anthony.Raterta@analog.com
-   Mark.Ochoco@analog.com

USB controller SDK Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The files provided in the temporary shared repository are the finalized codes for release and immediate customer use. Should the user want to proceed with his / her / their own development, the necessary SDK’s and files would be needed:

-   USB CONTROLLER:


|Setup_1.3.4.exe|

Equipment Needed
~~~~~~~~~~~~~~~~

-   Computer running Windows 10 OS
-   Signal Generator (optional).
-   Digital Multimeter (optional).
-   Vibration Shaker (i.e., King Design).
-   Piezo Reference Sensor (i.e., 352C67 from PCB Piezotronics).
-   Test Sensor (i.e., Type 4394 from Brüel and Kjær).

Accessories Needed
~~~~~~~~~~~~~~~~~~

-   BNC-to-SMA cable (x1).
-   SMA-to-SMA cable (x4).
-   USB Type C cable
-   5V power Supply(optional).

Power Supply Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~

The board can be powered up via USB3.0 or external Power Supply:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_power_supply.png
   :align: center
   :width: 600px

The Multi-Channel Vibration Test Platform can automatically prioritize the external power supply if detected then switch back to USB port if unplugged. Since Multi-Channel Vibration Test Platform has the capability to operate as Dual-Role Port (DRP), it can also adjust power requirements as needed based on the application such as when a device is connected, it will provide power and will act as HOST.

.. important::

   NOTE: For the External Power Supply, the Recommended voltage is from 4.5V to 5.5V.


GUI Installation
~~~~~~~~~~~~~~~~

The GUI installer can be accessed in the Multi-Channel Vibration Test Platform temporary shared repository. Refer to the Multi-Channel Vibration Test Platform Temporary Shared Repository section for the link to access the repository.

Download the necessary files, then run the USB 3.0 Based Multi-Channel Test Platform for Vibration Sensors.exe installer to setup the dependencies folder which will contain also contain the Multi-Channel Vibration Test Platform GUI executable file.

GUI Removal
~~~~~~~~~~~

To uninstall the GUI, run the file named Uninstall.exe in the same location as the GUI executable file. Running this will remove the folder created by the installer and its contents.

.. note::

   The folder containing the screenshots from the file export functionality (Multi-Channel Vibration Test Platform File Exports folder) isn’t deleted by this installer so this should be deleted manually.


--------------

QUICK START GUIDE
-----------------

Interconnection
~~~~~~~~~~~~~~~

The Multi-Channel Vibration Test Platform requires any type C connector to interface with host and is backward compatible with USB2.0. For Best performance, it is recommended to connect with USB3.0 ports and corresponding cable.

Boot options
~~~~~~~~~~~~

The Multi-Channel Vibration Test Platform has 2 boot options: SPI and USB boot. SPI boot loads the firmware stored in the SPI flash memory. This boot option will have the board loaded with the default onboard firmware during power-up and is useful when a final / release firmware is already developed.

USB boot allows temporary loading of firmware onto the Multi-Channel Vibration Test Platform. Resetting the power will clear the firmware loaded and it will be registered as a Bootloader device. This boot option is usually used during testing and debugging for easier firmware change (if necessary).

.. container:: center round box

   
   .. container:: group

         
         .. container:: 1/3 column

            BOOT

                     
                     USB
                     
            SPI

         
         .. container:: 1/3 column

            S1-1

                     
                     <fc #ff0000>ON</fc>
                     
            OFF

         
         .. container:: 1/3 column

            S1-2

                     
                     ON
                     
            <fc #ff0000>ON</fc>

         

   


-   USB Boot

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_usbboot.png
   :align: center
   :width: 600px

-   SPI Boot

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_spiboot.png
   :align: center
   :width: 600px

GUI USAGE
~~~~~~~~~

The Multi-Channel Vibration Test Platform Board default boot setup is for USB boot, allowing the firmware to be loaded via software. The installer, once done running, sets up the dependencies, firmware, and the executable file to run the GUI itself.

At every startup, the GUI uploads the firmware and proceeds if successful. Otherwise, the GUI won’t proceed while giving prompts for next actions.

At exit, the GUI resets the different board settings such as the signal generator output amplitude and frequency, channel offset, and current source button status. This is for the board to have a known state upon exit and ensure safety for connected components.

--------------

GUI START UP
^^^^^^^^^^^^

DAQ SETTINGS
------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq.png
   :align: center
   :width: 600px

The DAQ window allows changing the capture parameters for each channel such as current source, coupling, and gain. The signal generator output can also be set here as well data capture for Time and Frequency Domain.

Device Selection
~~~~~~~~~~~~~~~~

Listed through the dropdown are all the Multi-Channel Vibration Test Platform Board your machine detects where the user is required to choose one (1) to be paired with the GUI.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_deviceselection.png
   :align: center
   :width: 600px

It’s assumed that Multi-Channel Vibration Test Platform devices are only to be used with the GUI. Connecting a non 4CH. DAQ board or one with different firmware will result to an incorrect or different string message.

Channel Settings
~~~~~~~~~~~~~~~~

This control group gives control to different input parameters per channel such as input offset, current source toggling, and gain.

::

   1. CURRENT SOURCE

This control group is responsible for providing a standard IEPE sensor an external power supply if needed (4mA / channel). Individual channel external power supply is enabled/disabled by toggling their corresponding slider

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_currentsource.png
   :align: center
   :width: 600px

.. important::

   Note: It is best to check the IEPE sensor requirements before using supplying external power supply to avoid incurring permanent damage to either board or sensor.


::

   2. COUPLING

Allows either DC or AC coupling of the input signal. The coupling selected affects the necessary offset to ensure optimal data capture. Refer to input offset section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_coupling.png
   :align: center
   :width: 600px

::

   3. CHANNEL GAIN

Allows changing the signal gain for a corresponding channel.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_gain.png
   :align: center
   :width: 600px

.. note::

   Allowable Gain Values:

   
   -  1
   -  2
   -  5
   -  10
   -  20
   -  50
   -  100
   


::

   4. INPUT OFFSET

The input offset adjusts the signal such that it falls within the circuit blocks’ capture range, allowing a proper read by the ADC. The availability of this feature depends on the status of other buttons

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_inputoffset.png
   :align: center
   :width: 600px

For a signal with DC offset A, GUI settings can be computed as follows: ( for more details, refer to |CNxxx| )

.. container:: center round box

   <WRAP> \*\* Offset= (2.52V+ G (A))/(1+G)*1000**


</WRAP>

.. note::

   
   -  Offset = GUI offset settings in mV
   -  A = Signal DC offset
   -  2.52V = VOCM settings (default)
   -  G = 0.3 = circuit gain
   


::

   5. 4-20MA SENSOR MODE

Channel 3 provides an interface for interfacing with 4-20mA sensors upon toggling the slider under Channel 3 in the GUI:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_sensormode.png
   :align: center
   :width: 600px

By default, this is unselected to cater to other input sources. Enable this by toggling the slider. Doing so also yields the following offset settings:

.. note::

   
   .. container:: group

         
         .. container:: 1/5 column

                     
                     Current Source
                     
                     Disabled
                     
                     Disabled
                     
                     Disabled
                     

         
         .. container:: 1/5 column

                     

         
         .. container:: 1/5 column

                     
                     Coupling
                     
                     DC
                     
                     AC
                     
                     \*DC
                     

         
         .. container:: 1/5 column

                     

         
         .. container:: 1/5 column

            Offset (mV)

                     
                     2169, changeable
                     
                     2450, fixed
                     
                     1938, changeable
                     

         

   


.. important::

   *Offset result when changing from DC to AC and back to DC.


Capture Settings
~~~~~~~~~~~~~~~~

This control group is responsible for the type of data capture to be performed and the channel/s to be displayed.

::

   1. CHANNEL SELECTOR

The Channel selector buttons control which channel or channels are displayed in the graphs. Should have at least 1 selected channel before data capture.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_ch_selector.png
   :align: center
   :width: 600px

::

   2. CAPTURE MODE

This button selects whether to perform a single capture (snapshot) or a continuous capture of the selected plot type (Time, Frequency, Both).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_capturemode.png
   :align: center
   :width: 600px

Signal Generator Settings
~~~~~~~~~~~~~~~~~~~~~~~~~

This control group allows the changing of the board’s signal generator output parameters.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_siggen.png
   :align: center
   :width: 600px

::

   1. FREQUENCY

In the frequency field, type the frequency you want to set in Hertz (Hz). Allowable frequency values are from 0 to 25 kHz. Once a frequency has been chosen, click the SET button on the right side of the field.

::

   2. AMPLITUDE 

The amplitude field dictates the output amplitude (in peak to peak, Volts) from the BNC connector. Valid values are from 0 to 3300mV (3.3Vpk2pk ~ 1.2Vrms). Once an amplitude has been set, click the SET button on the right side of the field.

::

   3. BANDWIDTH

Allows selection between two different output paths: a) Full bandwidth or no Sallen Key Filter or b) 25kHz Sallen Key Filtered output. Toggle the slider to the desired output path.

Graph Display Settings
~~~~~~~~~~~~~~~~~~~~~~

This control group allows changing the visualization parameters to match the intended range of observation or region of the waveform/s.

::

   1. PLOT TYPE

Selects the plot type for the DAQ window (Time, Frequency, or Both). Pressing START without a selected plot type will yield a prompt message.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_plottype.png
   :align: center
   :width: 600px

-  TIME DOMAIN

Plots time domain data for enabled channels. Y-axis is Volts, X – axis is time (uS).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_timedomin.png
   :align: center
   :width: 600px

-  FREQUENCY DOMAIN

Plots frequency domain data of enabled channels. Y-axis is dBm, X – axis is frequency (Hz).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_freqdomain.png
   :align: center
   :width: 600px

-  TIME AND FREQUENCY DOMAIN

This plot option allows simultaneous display of both Time and Frequency Domain representation of captured data.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_freq_time_domain.png
   :align: center
   :width: 600px

::

   2. File Export 

Saves a screenshot of the selected graph/s.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_file_export.png
   :align: center
   :width: 600px

-  TIME DOMAIN

Saves screenshot of Time Domain graph.

-  FREQUENCY DOMAIN

Saves screenshot of Frequency Domain graph.

::

   3. External Trigger 

When selected, a positive pulse must be sent to the trigger in connector to begin capture, allowing beginning of capture via hardware trigger.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_daq_trigger.png
   :align: center
   :width: 600px

--------------

VIBRATION TEST
--------------

Vibration Test process for calibrating one or more DUT vs. a reference sensor.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration.png
   :align: center
   :width: 600px

::

   1. Device Selection

Listed through the dropdown are all the Multi-Channel Vibration Test Platform Board your machine detects where the user is required to choose one (1) to be paired with the GUI. Refer to the Device Selection section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_devsel.png
   :align: center
   :width: 600px

::

   2. Sine Sweep Range

The frequency range for the vibration test to be performed.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_sinesweep.png
   :align: center
   :width: 600px

.. note::

   
   -  Start Frequency - Initial frequency for the vibration test.
   -  Frequency Step - Frequency step from one frequency point to another.
   -  Stop Frequency - Final frequency for the vibration test.
   


::

   3. G-Settings

Sets the amount of G to be used and the measure

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_gsetting.png
   :align: center
   :width: 600px

.. note::

   
   -  Peak
   -  Peak to Peak
   -  RMS
   


::

   4. Limit Lines

Shows line options available to display with captured data for limit testing.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_limitline.png
   :align: center
   :width: 600px

.. note::

   
   -  3dB Line
   -  10% Sensitivity
   -  Both
   


::

   5. Reference & DUT Sensor Setup Section

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_ref_dut.png
   :align: center
   :width: 600px

.. note::

   Current Source, Coupling, Gain, and Offset settings operate similar to DAQ counterpart. Refer to DAQ section for reference on these items.


::

   6. SENSOR SENSITIVITY

Sets the sensitivity (Volts / G) for each sensor attached on the input channels. Channel 0 (topmost) serves as the reference amplitude for the vibration test while other channels are for other DUT.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_sensitivity.png
   :align: center
   :width: 600px

::

   7. ENABLE

Selects which channels would be displayed for the vibration test results. Default settings: CH0 always enabled, other channels enabled upon toggling.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_enable.png
   :align: center
   :width: 600px

.. important::

   ADXL digital sensor functionality not yet incorporated as of this version.


::

   8. Plot Type

Selects the plot type to be displayed. Options include Voltage scale, DUT, or Self-Scan.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_plottype.png
   :align: center
   :width: 600px

.. note::

   
   -  Voltage Scale: amplitude setting used to reach target sensitivity for each frequency point.
   -  DUT: compares reference channel measurement with DUT from other channel/s.
   -  Self-Scan: reference channel + setup calibration.
   


::

   9. Plot Scale

Selects the scale for the Y-axis of the graph. Options include Magnitude (g), Decibel (Log(g)), Vrms, or Decibel (Log(Vrms)).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_plotscale.png
   :align: center
   :width: 600px

.. note::

   
   -  Magnitude (g): Y-axis is in g’s.
   -  Decibel (Log(g)): Y-axis is log(g)
   -  Vrms: Y-axis is in Vrms.
   -  Decibel (Log(Vrms)): Y-axis is log(Vrms).
   


::

   10. Graph Display

Displays the reference sensor and DUT amplitude/s vs. frequency for the performed vibration test.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_graphdisplay.png
   :align: center
   :width: 600px

::

   10. File Export

Exports screenshot of Frequency Response graph.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_fileexport.png
   :align: center
   :width: 600px

::

   11. External Trigger

Similar to external trigger from DAQ section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_vibration_ext.png
   :align: center
   :width: 600px

--------------

SINE GENERATION WINDOW
----------------------

This window is used for generating a sweeping sinusoid pattern:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration.png
   :align: center
   :width: 600px

::

   1. Device Selection

Refer to the Device Selection section.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration_devsel.png
   :align: center
   :width: 600px

::

   2. Amplitude

Sets the amplitude of the sinusoid to be output from the board (in mVpp).

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration_ampsel.png
   :align: center
   :width: 600px

::

   3. Sine Generation Range

The frequency range of sinusoids to be output.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration_freqsel.png
   :align: center
   :width: 600px

.. note::

   
   -  Start Frequency – starting frequency to be generated to the output.
   -  Frequency Step – increment from one frequency point to another.
   -  Stop Frequency – last frequency to be generated to the output.
   


::

   4. Duration Per Frequency(mS)

Delay (in milliseconds / mS) before switching from one frequency output to another.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/multi-channel-vibration-test-platform/multi-channel_vibration_test_sinegeneration_duration.png
   :align: center
   :width: 600px

.. |Repository| image:: https://wiki.analog.com/_media/insert link here
.. |Setup_1.3.4.exe| image:: https://www.cypress.com/file/424276/download
.. |CNxxx| image:: https://wiki.analog.com/_media/insert link here
