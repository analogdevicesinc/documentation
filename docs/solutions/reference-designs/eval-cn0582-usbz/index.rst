.. _eval-cn0582-usbz:

EVAL-CN0582-USBZ
================

USB 3.0 Quad-Channel IEPE Vibration Sensor Measurement System
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

General Description
-------------------

:adi:`CN0582` or the USB 3.0 Quad-Channel IEPE Vibration Sensor
Measurement System is a system board capable of reading data
from analog (IEPE) accelerometers. The analog IEPE inputs also
contain current source switches to accommodate sensors that might
need external power and individual channel offset voltage setting.

Aside from IEPE sensor measurements, the board is also an arbitrary
sinewave generator providing stimulus to an external vibration shaker
and a multi-channel data acquisition system.

Requirements
------------

The USB 3.0 Quad-Channel IEPE Vibration Sensor Measurement System is a
complete system from Hardware, Firmware, to Software for performing
basic Data acquisition (DAQ) functions and vibration tests.

The following sections will detail the necessary steps and conditions
needed to fully operate the system.

**Firmware**

Once the USB 3.0 Quad-Channel IEPE Vibration Sensor Measurement System
is installed via the given installer (Refer to the Installation Guide
section), the compatible firmware is located within the same folder as
the GUI executable file.

At startup, the GUI uploads the firmware to the board for easier use.
Do not remove the firmware (.img file) in the folder to avoid errors.

.. figure:: firmware_image.png
   :align: center

   CN0582 Firmware

Should there be any updates necessary, uninstall the GUI and
corresponding files using the uninstaller (C:\\Analog Devices\\USB3.0
Based Multi-Channel Test Platform for Vibration
Sensor\\Uninstall.exe). An updated installer containing the updated
firmware and other files will be uploaded for download.

**Equipment Needed**

- Computer running Windows 10 OS
- Signal Generator (optional).
- Digital Multimeter (optional).
- Vibration Shaker (i.e., King Design).
- Piezo Reference Sensor (i.e., 352C67 from PCB Piezotronics).
- Test Sensor (i.e., Type 4394 from Brüel and Kjær).

**Accessories Needed**

- BNC-to-SMA cable (x1).
- SMA-to-SMA cable (x4).
- USB Type C cable
- 5V power Supply(optional).

**Power Supply Requirements**

The board can be powered up via USB3.0 or external Power Supply:

.. figure:: multichannel_vibration_test_power_supply.png
   :align: center

   Multi-Channel Vibration Test Power Supply

The Multi-Channel Vibration Test Platform can automatically prioritize
the external power supply if detected then switch back to USB port if
unplugged. Since Multi-Channel Vibration Test Platform has the
capability to operate as Dual-Role Port (DRP), it can also adjust
power requirements as needed based on the application such as when a
device is connected, it will provide power and will act as HOST.

.. note::

    NOTE: For the External Power Supply, the recommended voltage
    is from 4.5 V to 5.5 V.

Installation Guide
------------------

The CN0582 Evaluation Software.exe is a single file installer that
includes the GUI installer, uninstaller, and driver installer. The
installer will create the files and folders required to operate CN0582
and the corresponding applications.

.. admonition:: Download

   :download:`CN0582 Evaluation Software Installer <http://swdownloads.analog.com/cse/cftl/CN0582/CN0582%20EVALUATION%20SOFTWARE%20INSTALLER.EXE>`

**GUI Installer**

This will setup the dependencies folder which will also contain the
USB 3.0 Quad-Channel IEPE Vibration Sensor Measurement System GUI
executable file.

**Driver Installer**

Running the driver installer is necessary to fully setup the necessary
drivers and make the board recognizable by the software.

.. figure:: driver_installer.png
   :align: center

   Multi-Channel Vibration Test Platform

**GUI Removal**

To uninstall the GUI, run the file named Uninstall.exe in the same
location as the GUI executable file. Running this will remove the
folder created by the installer and its contents.

.. figure:: uninstall.png
   :align: center

   Uninstall Multi-Channel Vibration Test Platform

.. note::

    The folder containing the screenshots from the file export
    functionality (Multi-Channel Vibration Test Platform File
    Exports folder) isn’t deleted by this installer so this
    should be deleted manually.

Quick Start Guide
-----------------

**Interconnection**

The Multi-Channel Vibration Test Platform requires any type C
connector to interface with host and is backward compatible with
USB2.0. For Best performance, it is recommended to connect with USB3.0
ports and corresponding cable.

**Boot options**

The Multi-Channel Vibration Test Platform has 2 boot options: SPI and
USB boot. SPI boot loads the firmware stored in the SPI flash memory,
if any. This is useful when a custom firmware already loaded onboard
is needed or for instances where the board would undergo a power
restart and immediate loading, with no software intervention, is
needed.

The other option, USB boot, is the default for all CN-0582 boards.
Restarting the board in this mode registers the board as a bootloader
instead of a valid device. This allows bundling the software with the
hardware since the GUI will be responsible for uploading the firmware
to the board and not having the necessary software renders the
hardware unusable.

==== ==== ====
BOOT S1-1 S1-2
USB  ON   ON
SPI  OFF  ON
==== ==== ====

**USB Boot**

.. figure:: test_usbboot.png
   :align: center

   Multi-Channel Vibration Test USB Boot

**SPI Boot**

.. figure:: test_spiboot.png
   :align: center

   Multi-Channel Vibration Test SPI Boot

**GUI Usage**

The Multi-Channel Vibration Test Platform Board default boot setup is
for USB boot, allowing the firmware to be loaded via software. The
installer, once done running, sets up the dependencies, firmware, and
the executable file to run the GUI itself.

At every startup, the GUI uploads the firmware and proceeds if
successful. Otherwise, the GUI won’t proceed while giving prompts for
next actions.

At exit, the GUI resets the different board settings such as the
signal generator output amplitude and frequency, channel offset, and
current source button status. This is for the board to have a known
state upon exit and ensure safety for connected components.


Graphical User Interface Start Up
---------------------------------

.. figure:: user_interface.png
   :align: center

   CN0572 Evaluation Software User Interface

DAQ Settings
------------

.. figure:: daq_settings.png
   :align: center

   DAQ Settings

The DAQ window allows changing the capture parameters for each channel
such as current source, coupling, and gain. The signal generator
output can also be set here as well as data capture for Time
and Frequency Domain.

**1. Device Selection**

Listed through the dropdown are all the Multi-Channel Vibration Test
Platform Board your machine detects where the user is required to
choose one (1) to be paired with the GUI.

It’s assumed that Multi-Channel Vibration Test Platform devices are
only to be used with the GUI. Connecting a non 4CH. DAQ board or one
with different firmware will result in an incorrect or different
string message.

**2. Number of Cycles**

This determines the number of cycles to be displayed in the Graph
Display. The dropdown menu contains the options for the number of
cycles (1, 2, 3, 4, 5 or full cycle) that can be applied.

**3. Channel Settings**

This control group gives control to different input parameters per
channel such as sensor dc bias, current source toggling, and gain.

.. important::

    Note: It is best to check the IEPE sensor requirements before
    using supplying external power supply to avoid incurring
    permanent damage to either board or sensor.

**Current Source**

This control group is responsible for providing a standard
IEPE sensor an external power supply if needed
(4mA / channel). Individual channel external power supply is
enabled/disabled by toggling their corresponding slider.

**4-20mA Sensor Mode**

Channel 3 provides an interface for interfacing with 4-20mA
sensors upon toggling the slider under Channel 3 in the GUI:
By default, this is unselected to cater to other input sources.
Enable this by toggling the slider.

**Coupling**

Allows either DC or AC coupling of the input signal. The coupling
selected affects the necessary offset to ensure optimal
data capture. Refer to input offset section.

**Channel Gain**

Allows changing the signal gain for a corresponding channel.

.. note::

    Allowable Gain Values:
     - 1
     - 2
     - 5
     - 10
     - 20
     - 50
     - 100

**Sensor DC Bias**

The sensor DC bias converts the input based on corresponding
sensor’s bias specification to a voltage offset such that the
signal falls within the ADC’s optimal capture range.

**4. Channel Selector**

The Channel selector buttons control which channel or channels are
displayed in the graphs. Should have at least 1 selected channel
before data capture.

**Capture Mode**

This button selects whether to perform a single capture (snapshot) or
a continuous capture of the selected plot type (Time, Frequency, Both).

**5. Signal Generator Settings**

This control group allows the changing of the board’s signal generator
output parameters.

**Frequency**

In the frequency field, type the frequency you want to set in Hertz
(Hz). Allowable frequency values are from 0 to 25 kHz. Once a
frequency has been chosen, click the SET button on the right side of
the field.

**Amplitude**

The amplitude field dictates the output amplitude (in peak to peak,
Volts) from the BNC connector. Valid values are from 0 to 3300mV
(3.3Vpk2pk ^ 1.2Vrms). Once an amplitude has been set, click
the SET button on the right side of the field.

**Bandwidth**

Allows selection between two different output paths: a. Full
bandwidth or no Sallen Key Filter or b. 25kHz Sallen Key Filtered
output. Toggle the slider to the desired output path.

**6. Graph Display Settings**

This control group allows changing the visualization parameters to
match the intended range of observation or region of the waveform/s.

**Plot Type**

Selects the plot type for the DAQ window (Time, Frequency, or Both).
Pressing START without a selected plot type will yield a prompt
message.

 - **Time Domain**

   Plots time domain data for enabled channels. Y-axis is Volts,
   X – axis is time (uS).

 - **Frequency Domain**

   Plots frequency domain data of enabled channels. Y-axis is dBm,
   X – axis is frequency (Hz).

 - **Time and Frequency Domain**

   This plot option allows simultaneous display of both Time and
   Frequency Domain representation of captured data.

**File Export**

Saves a screenshot of the selected graph/s.

 - **Time Domain**

   Saves screenshot of Time Domain graph.

 - **Frequency Domain**

   Saves screenshot of Frequency Domain graph.

 - **External Trigger**

   When selected, a positive pulse must be sent to the trigger in
   connector to begin capture, allowing beginning of capture via
   hardware trigger.

Vibration Test
--------------

Vibration Test process for calibrating one or more DUT vs.
a reference sensor.

.. figure:: vs_interface.png
   :align: center

   Vibration Test Interface

**1. Device Selection**

Listed through the dropdown are all the Multi-Channel Vibration TesT
Platform Board your machine detects where the user is required to
choose one (1) to be paired with the GUI. Refer to the Device
Selection section.

**2. Sine Sweep Range**

The frequency range for the vibration test to be performed.

    .. note::

        - Start Frequency - Initial frequency for the vibration test.
        - Frequency Step - Frequency step from one
          frequency point to another.
        - Stop Frequency - Final frequency for the vibration test.

**3. G-Settings**

Sets the amount of G to be used and the measure.

.. note::

   - Peak
   - Peak to Peak
   - RMS

**4. Limit Lines**

Shows line options available to display with captured data for limit
testing.

.. note::

   - 3dB Line
   - 10% Sensitivity
   - Both

**5. Reference & DUT Sensor Setup Section**

Current Source, Coupling, Gain, and Sensor DC Bias settings operate
similar to DAQ counterpart. Refer to DAQ section for reference on
these items.

**Sensor Sensitivity**

Sets the sensitivity (Volts / G) for each sensor attached on the
input channels. Channel 0 (topmost) serves as the reference
amplitude for the vibration test while other channels are for
other DUT.

 **Enable**

 Selects which channels would be displayed for the vibration test
 results. Default settings: CH0 always enabled, other channels enabled
 upon toggling.

 .. important::

    ADXL digital sensor functionality not yet incorporated as of this
    version.

**6. Graph Display Settings**

**Plot Type**

Selects the plot type to be displayed. Options include Voltage scale,
DUT, or Self-Scan.

 .. note::

     - Voltage Scale: amplitude setting used to reach target sensitivity
       for each frequency point.
     - DUT: compares reference channel measurement with DUT
       from other channel/s.
     - Self-Scan: reference channel + setup calibration.

**Plot Scale**

Selects the scale for the Y-axis of the graph. Options include
Magnitude (g), Decibel (Log(g)), Vrms, or Decibel (Log(Vrms)).

 .. note::

    - Magnitude (g): Y-axis is in g’s.
    - Decibel (Log(g)): Y-axis is log(g)
    - Vrms: Y-axis is in Vrms.
    - Decibel (Log(Vrms)): Y-axis is log(Vrms).

**Graph Display**

Displays the reference sensor and DUT amplitude/s vs. frequency for
the performed vibration test.

**File Export**

Exports screenshot of Frequency Response graph.

**External Trigger**

Similar to external trigger from DAQ section.


Sine Generation Window
----------------------

This window is used for generating a sweeping sinusoid pattern:

.. figure:: sine_interf.png
   :align: center

   Sine Interface

**1. Device Selection**

Refer to the Device Selection section.

**2. Amplitude**

Sets the amplitude of the sinusoid to be output from the board
(in mVpp).

**3. Sine Generation Range**

The frequency range of sinusoids to be output.

 .. note::

    - Start Frequency – starting frequency to be generated
      to the output.
    - Frequency Step – increment from one frequency point
      to another.
    - Stop Frequency – last frequency to be generated
      to the output.

**4. Duration Per Frequency(mS)**

Delay (in milliseconds / mS) before switching from one frequency
output to another.


Hardware Setup
--------------


Before simulating the program, setting up the hardware is necessary.

#. Connect the EVAL-CN0582 to the Vibration Shaker
   using a BNC connector.

#. By using SMA connector, connect the Piezo Reference Sensor of
   the Vibration Shaker to channel 0.

#. Attach another SMA connector from the Test Sensor going to
   channel 1 of the EVAL-CN0582.

#. Power up the CN0582 by connecting the Type C end of the USB
   cable to the board and the other end to the host. There should
   be a RED and GREEN LED lit up on the board to note proper power up.

   .. figure:: hardware_setup.jpg
      :align: center

      Hardware Setup

How to Use the Program
----------------------

To test the program with IEPE sensors the following equipment
is needed:

**Equipment needed:**

#. EVAL-CN0582-USBZ.

#. BNC-SMA coaxial cable.

#. USB C cable

#. Analog input source (optional): *Signal Generator (Square, Sine,
   Sawtooth etc.)*

   *IEPE Accelerometer (i.e., PCB MC325C67) + Shaker + SMA coaxial cables.*

**Procedure:**

#. Run the CN0582 Evaluation Software. Follow the prompts until
   the GUI main window appears. Only the GREEN LED should be lit up
   on the board to note a successful firmware upload as well.

#. Navigate to the DAQ or Vibration Test window by clicking the
   following image on the left side of the GUI.

   .. figure:: htu_overview.png
      :align: center

#. Depending on the available setup, perform the following
   actions:

   - IEPE Accelerometers + Shaker: Connect one accelerometer
     (reference) to Analog Input Channel 0. If applicable, connect
     the other accelerometers to other Analog Input Channels.
   - With or without external signal generator: Use the
     BNC-to-SMA coaxial cable to connect the signal generator output
     to Analog Input Channel 0. If there’s an external signal
     generator, connect this to another Analog Input Channel.
   - The Shaker must be initially off before setting and
     running the necessary parameters.

#. Toggle the current source (for IEPE accelerometer),
   gain, coupling, and sensor dc bias settings as needed.

   .. figure:: htu_vibration_test.png
      :align: center


   .. important::

      Vibration Testing Window Settings

#. On the channel selector section, enable the channel
   where the other Analog Input source is connected.

#. Click set when the parameters have been chosen,
   then press Start to launch the test.

Help and Support
----------------

For questions and more information about this product, connect with us through
the :ez:`reference-designs`.
