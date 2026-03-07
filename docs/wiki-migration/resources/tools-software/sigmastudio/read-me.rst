~~GOTO>resources/tools-software/sigmastudio/releaseinfo?0~~

.. warning::

   This page is not maintained. Please refer to the following page instead.

   
   :doc:`/wiki-migration/resources/tools-software/sigmastudio/releaseinfo`


Analog Devices Inc. SigmaStudio™ Version History
================================================

Analog Devices Inc. SigmaStudio™
--------------------------------

Welcome to Analog Devices, Inc. (ADI) SigmaStudio™ 3.12 ReadMe file. SigmaStudio Graphical Development Tool supports SigmaDSP™ and other audio processor products. Learn more about ADI’s Audio Signal Processors by visiting :adi:`http://www.analog.com/sigmadsp <SigmaDSP>`.

:doc:`Click here to return to the SigmaStudio and SigmaDSP Documentation top page. </wiki-migration/resources/tools-software/sigmastudio>`

Installation Notes
~~~~~~~~~~~~~~~~~~

System Requirements
^^^^^^^^^^^^^^^^^^^

| Windows 7 x86/x64\*
| Windows Vista\*
| Windows XP Professional or Home Edition with SP2*\*
| Microsoft .NET Framework 3.5
| 256 MB of RAM (256 MB recommended)
| 50 MB of available hard disk space
| 1024 x 768 screen resolution
| USB 2.0 data port (Required for use with Evaluation hardware only)

| \* The user must be an administrator when installing SigmaStudio.
| \* \* ADI no longer supports Windows XP

To install SigmaStudio™ 3.12 or higher versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Quit any applications you are running.
-  Double-click on the SigmaStudio 3.x installer, “Sigma Studio xxx.exe”, to start the installation.
-  Review the contents of the license agreement, if you agree click “I Agree”.
-  SigmaStudio 3.x may be installed alongside or over an existing copy of SigmaStudio, Select an existing installation directory if you want to overwrite a previous SigmaStudio version.
-  If you are installing SigmaStudio for the first time, restart your computer when the installation is complete.

Updates SigmaStudio 3.12.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Initial phase can be configured now in Sin, Square, Triangle and Sawtooth wave oscillators for ADAU145x.
-  Audio signal router algorithms are added.
-  ‘Value Hold’ algorithm can hold multiple input channels for ADAU145x.
-  ‘Export System Files’ generates the Netlist information into xml format.
-  External SPI Delay module can now support 24 bit addressable SPI RAMs for ADAU145x.
-  Text In filter’s user control is updated

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.12.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Maximum and minimum values of Linear gain is now calculated depends on the type of core.
-  Compilation error in the NxM mixer for some values of N, M is fixed.
-  Bug in export for the NxM mixer is fixed. (ADAU145X)
-  Copy Paste bug in DC source is fixed.
-  Issue while creating a copy of the module which does not contain an algorithm, is fixed.
-  Misleading info in Combo: RMS + Peak module is corrected.
-  Issue while updating the parameter for High order shelving filter, is fixed.
-  T connection module is updated to restrict the connection between modules from different ICs.
-  Schematic status update is corrected for “Allow Realtime AB Testing” feature.
-  Issue with the FIR filter MIPS calculation is fixed for ADAU144x.

.. raw:: html

   </details>


Updates SigmaStudio 3.12.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  ADAU1372 has been added to the library.
-  New High Order Shelving filters for 3rd Generation Cores (ADAU144X, ADAU176X)
-  ParametricEQ now supports up to 192 kHz Fs GUI representation.
-  Hilbert Transform, Voice Activity Detector (VAD), Super Bass algorithms are implemented for ADAU145X processor.
-  New version of Dynamics Processors which outputs compressor gain is added
-  Linear Interpolator algorithm is implemented as a growable algorithm for ADAU145X and ADAU144X processors.
-  Support to directly switch the communication protocol from I2C to SPI for ADAU144x

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.12.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  ADAU145X, fix incorrect hold logic for “Max and Hold”, “Max Abs and Hold”, and “Min and Hold” blocks.
-  Reverb algorithm for AD1940.
-  ParametricEQ fixed for first order filter on ADAU145x.
-  Fixed transfer function calculation of Subtraction and Signal Invert modules for ADAU145x

.. raw:: html

   </details>


Updates SigmaStudio 3.12.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Save-restore support added for right-click context menu settings (e.g. slew-time, data-memory, block-size). This update supports preservation of the menu settings during copy/paste, undo/redo, project/cell “Settings”, scripting and “Control UI”.
-  “ADI Surround”, “Beam Forming (fixed)”, “Automatic EQ”, “Crossover Filter (double precision)”, “Pitch Transposer” and “GPIO Conditioning” algorithms implemented for ADAU145X processor
-  New ADAU145x Basic DSP Delay algorithm supports selection between the 2 data memories.
-  Arithmetic Shift operation added for ADAU145x
-  ADAU145x support for 32.0 (“RAW 32bit") format serial audio data, format option is located in right click context menu of inputs and outputs.
-  Holters filter with agnostic GUI.
-  ADAU1772 is SPI ready.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.12.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Mid EQ out of index issue caused by opening a SStudio v3.9 or older version project.
-  ADAU1450 register controls user interface fixed

.. raw:: html

   </details>


Updates SigmaStudio 3.12.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Support for multi-rate signal flow (multiple sampling rates or block-sizes in a single schematic design window).
-  Multi Tap Gain algorithm implemented for AD194x, ADAU170x, ADAU176x processors.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.12.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Level detector with output display for AD1940.
-  Standard RMS Compressor read back indicator worked for AD1940.
-  ADAU145x register window on the routing matrix and serial ports.
-  Parametric EQ cell, low pass and high pass first order filter selection.

.. raw:: html

   </details>


Updates SigmaStudio 3.11.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  SigmaStudio load time performance improvements for 64 bit OS
-  Added right click context menu for copy of “Output Window” text to clipboard
-  Presence of obsolete algorithm code in legacy projects indicated in assembler output window
-  Automatic Volume Control (AVC) implemented for ADAU145x processor
-  N-channel peak compressor implemented for ADAU145X processor
-  Multi Tap Gain algorithm implemented for ADAU145x processor

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.11.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Standard Peak Dynamic processor fix for ADAU145x to match full range -135dB to +21dB.
-  Memory error for large ADAU145x design using One Shot, Value Cross Detect, or DC Blocker
-  ADAU145x Logic “AB in CD out” condition fixed, GUI was not setting proper algorithm mode
-  Loading “hierarchy board” file caused mouse cursor to disappear

.. raw:: html

   </details>


Updates SigmaStudio 3.11.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Transfer function for the two way adder on the ADAU1772 is now implemented.
-  RealTimeDisplay cell now supports ADAU145x data format.
-  Added ADAU1452 NLMS filter algorithm.
-  Mono Dynamics Bass Boost and Adaptive Mixer Dual graph algorithms added for ADAU145x.
-  Configurable SPI memory erase cycle time to support large flash memories for ADAU145x.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.11.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  ADAU145x Linear interpolator now supports more than 128 points.
-  ADAU145x multiple instances of DC Blocker filter causes exception.
-  ADAU1451 register control routing matrix window fixed.
-  ADAU145x NxM Multiple Ctrl Mixer cell causes exception.
-  ADAU145x External Volume (HW Slew) slew control function and state save/restore fixed.
-  ADAU145x incorrect instruction cycle count estimate for large FIR filters
-  Selfboot EEPROM I2C device settings not compatible with ADAU1701/ADAU1772 eval boards.
-  ADAU1772 EEPROM write causes exception.
-  ADAU145x block processing context save/restore added for peripheral math accelerators.
-  ADAU145X rounding mode is now disabled (round to –inf) by default.

.. raw:: html

   </details>


Updates SigmaStudio 3.11.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Adding Advanced Pith Shifter DEMO algorithm
-  Adding single precision ParametricEQ.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.11.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Export files using CRC and clearing Program memory methods were missing.
-  Fixed the real delay wrong calculated of fractional delay.

.. raw:: html

   </details>


Updates SigmaStudio 3.10.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  New multi-tap delay mixer: AD194x, ADAU170x, ADAU176x, ADAU144x
-  New linear value NxM mixer (all processors).
-  ADAU145x algorithms: Standard Compressor, DC Blocking Filter, Pink Noise Filter, Lookup Table (8.24), Pulse Count, Timer, Stop Watch, Envelope, State Machine, MUX w/ slew, Voltage Controlled Delay, Multi-tap Delay, Fractional Delay, Max, Min, One Shot, Value Cross, Value Hold, Abs Max, Master Port Delay, Master Port Writer.
-  ADAU145X framework changes required for silicon Revision D support (backward compatible)

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.10.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Projects from version 3.5 or earlier would not open in version 3.10
-  Parametric EQ Index Selectable filter on IIR, now it displays correctly all the curves.
-  Fixed the interaction problem between different “OneShot Rise, Reset” block.
-  Fixed “Boost Min” save and restore issue on “General 2nd Order w var Param/Lookup/Slew”.
-  Fixed source-destination reversal of links and hierarchy board input/output distortion due to connections made in reverse direction.
-  Fixed Min and Hold and Max and Hold algorithms.
-  Sequence window, fixed corruption when editing data or bytes when data spans more than 1 line.
-  Fixed ADAU145x Linear Interpolator table not initialized correctly.
-  Fixed ADAU145x index selectable mux, demux and Look-up-table (LUT): offset value “out of range” error in large projects.
-  Fixed ADAU145X NxM mixer algorithm, gain values not downloaded
-  Fixed ADAU145X GPIO algorithm: interrupt protection required

.. raw:: html

   </details>


Updates SigmaStudio 3.10.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added multiple channels FIR and obsolete the old one.
-  Added lower range log look up table which ranged from -90dB to +6 dB.
-  ADAU145X framework updated
-  Added no MIPS and no Data usage switch for ADAU1761, ADAU1781 and ADAU144x.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.10.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Register window fixes for ADAU1772 on the PGA/ADC tab, all four pop suppression buttons. On Output/Serial Port tab, both the DAC0 and DAC1 gain sliders, and pop suppression buttons under “Headphone Control” section.
-  ADAU1772 Parametric EQ bug when used with a two way mixer.
-  “Export system files” capability for ADAU1772 is now fixed.
-  ADAU1701, ADAU1702, and ADAU1401 had a GPIO option on MP0 and MP6 of TDM8 in and TDM out respectively, which is no longer supported. The register window has been updated accordingly.
-  NxM mixer cell has been modified so that the export files avoid the address repetition.
-  ParametricEQ multiple filter bug for ADAU145x core.

.. raw:: html

   </details>


Updates SigmaStudio 3.10.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  New DC Input Entry and New Single Volume (Write to Selected parameter) with no MIPS and no Data usage for ADAU1761, ADAU1781 and ADAU144x.
-  Enable / Disable button got bigger for most filters. A new phase shift button was included on the filters.
-  Updated DSP Configuration Window for ADAU145x

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.10.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Hilbert Transform now works properly for ADAU1701 and AD1940.
-  VCO with phase reset is ready for ADAU1701 and AD1940.
-  Fixed the ADAU1461 I/O problem on digital input 9.
-  Fixed MidEQ Shelving filter downloading coefficients twice.

.. raw:: html

   </details>


Updates SigmaStudio 3.10.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  New ADAU145X processor
-  Add Standard Dynamics processors for ADAU1701 and AD1940.
-  New Real Time Display and Single Level detector with no MIPS and no Data usage for ADAU144x, and low power DSP.
-  New Stereo and Mono Peak Dynamics Processors with higher range (-90 dB, +24 dB) with and without external detect for ADAU1701 and AD1940.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.10.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  VCO with reset algorithm for ADAU1701 and AD1940 is fixed.

.. raw:: html

   </details>


Updates SigmaStudio 3.10.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  New dynamics interpolator with feed forward graph.
-  New no averaging level detectors with and inverse display and speed control.
-  New parameter read back block with no DATA instructions, for ADAU176x, ADAU1781 and ADAU144x.
-  New linear sweep blocks (2 externally triggered and 2 on/off switch).

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.10.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  SigmaStudio load time has been reduced.
-  Pulse generator approximates user’s duty cycle input.

.. raw:: html

   </details>


Updates SigmaStudio 3.9.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Export to Linux files now supports XML format. Implementation of Export to Linux files for ADAU1701.
-  Single band level detector supports linear display.
-  New peak dynamics processors with external detect (Mono/Stereo) that supports fast release for low frequencies.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.9.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

(None)

.. raw:: html

   </details>


Updates SigmaStudio 3.9.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Single band level detector has now a new graphic adjustable display.
-  Added All-pass selection to “First Order Filters” type in General (2nd Order) Filter
-  Added user selectable phase wrapped/un-wrapped and radians/degrees options in probe window

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.9.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  FIR Filter table is fixed, with all coefficients set to zero except the first.

.. raw:: html

   </details>


Updates SigmaStudio 3.9.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Extended probe window frequency axis to 96kHz maximum.
-  Added log lookup table for ADAU170x and ADAU144x.
-  Made simple sub-harmonic support ADAU176x, ADAU1781 and ADAU144x.
-  Added Quad VCO support ADAU1701 and AD1940.
-  Added VCO with flexible phase for ADAU170x and ADAU144x.
-  Added two externally triggered sweeps for ADAU170x and ADAU144x.
-  Added square root approximation for ADAU170x and ADAU144x.
-  Added peak compressor with zero cross for ADAU176x, ADAU1781 and ADAU144x.
-  Added elliptical interpolated IIR low pass filter for ADAU176x, ADAU1781 and ADAU144X.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.9.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Change schematic view mouse wheel zoom steps to match the zoom menu zoom step sizes.
-  Decrease font size and add tooltips in the ADAU144X register window to fix readability issues.
-  Optimized schematic linking reduces compile times for large projects

.. raw:: html

   </details>


Updates SigmaStudio 3.8.2
~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added optimized sine tone generator which used subroutine.
-  SigmaStudio application was not appearing in the toolbar at launch when opened with a project.
-  Sequence Window download operation was inserting read-back after each write, this is now a user option “Verify on Download” that is disabled by default.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.8.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Additional .dspproj file can now be opened from Windows Explorer when SigmaStudio is already running.
-  SigmaStudio application was not appearing in the toolbar at launch when opened with a project.
-  Sequence Window download operation was inserting read-back after each write, this is now a user option “Verify on Download“ that is disabled by default.

.. raw:: html

   </details>


Updates SigmaStudio 3.8.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added Virtual Control Interface, user customizable system tuning graphical interface.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.8.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fix duplicate parameter naming in “Export System Files” for the Pitch Transpose.
-  Certain projects were set as dirty (i.e. modified) immediately on file open.

.. raw:: html

   </details>


Updates SigmaStudio 3.7.7
~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Windows Administrator privileges are required for installation

   -  The option for installing as ‘All Users’ or ‘Just Me’ was removed.
   -  The default location of the Sample Scripts and Sample Schematics has changed

-  Automatic Add-Ins: at startup SigmaStudio will automatically scan all DLL files located in the SigmaStudio installation directly and enable them for use in SigmaStudio. The existing Tools \| Add-Ins Browser can still be used to add external libraries or disable a library.
-  The “Reverb” algorithm’s user interface has been visually redesigned.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.7.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Lookup table editor prevents the user to delete text lines accidentally.
-  The bypass and enable of ADAU1373’s PLLA and PLLB were inverted. N div was also inverted.
-  FIR filters now support copy/paste and Hierarchy board save/load. Existing Hierarchy board files must be resaved before the FIR settings will be restored when on hierarchy board load.
-  Hierarchy board load behavior changed to better support large hierarchy files. Loading a hierarchy board is now a destruction (non-undoable) operation.
-  SignalDetection decay time fixed for ADAU1701 and AD1940.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.7.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Knobs in SigmaStudio support click protection property, tooltip value indicator, and speed control. Value label indicators do not clutter anymore.
-  ADAU1772 included.
-  Added a Mono peak compressor with external detection.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.7.5 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The continuous read check box’s check status of RealTimeDisplay was disturbed.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.7.5 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added “Pulse Generator” for ADAU176x, ADAU1781, ADAU1701 and AD1940.
-  Made RealTimeDisplay work for the 1701 and 1940.
-  Gain Envelope algorithms moved from “ADI Algorithms” category to “Volume Controls”.
-  ADAU1772 DSP is now added into SigmaStudio environment.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.7.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Gen 2nd Order filter is fixed. This will prevent error for unsupported Q values.
-  Index Selectable Independent Multiple Band filter is fixed. Filter editor will now display all the controls in any row of the filter.
-  Index Selectable Independent Multiple Band filter and Index Selectable filters are fixed. The module will not show error message upon removing the last filter while in selected state.
-  Chime algorithm modulation issue. Now is fixed and output a full scale signal.
-  Modified “Pitch Transpose” using UIData serialization.
-  Copy/Paste of block hierarchy board is fixed. This will prevent boards containing block processing modules getting pasted in the sample processing design tab.
-  Copy/Paste of sample hierarchy board is fixed. This will prevent all sub-boards getting pasted in the main design tab.
-  Scripting interface is fixed. This will remove the restrictions in connecting 2 block processing modules using script.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.7.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Linear interpolator has added a GUI for intuitive usability.
-  Added “Fractional Delay” controls and algorithms both Voltage Controlled and User Controlled.
-  Added “Pitch Transpose” controls and algorithms both Voltage Controlled and User Controlled.
-  Added “Pulse Generator” for ADAU176x, ADAU1781, ADAU1701 and AD1940.
-  Added a “tiny circle” for “DSP Read Back” to control the cell start/stop continuous read back.
-  Filter stability criteria imposed on "State Variable Filter" controls.
-  More automation APIs added to SigmaStudioServer.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.7.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

(None)

.. raw:: html

   </details>


Enhancements SigmaStudio 3.7.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Add a mono super bass.
-  Add a gain output volume control.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.7.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  TreeToolbox multiple DSP crash fixed.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.7.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Sound String algorithm added.
-  Probe – Stimulus data flow efficiency enhanced.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.6.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemParametric EQ first order filter coefficients are now generated correctly.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.6.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Volume control has new min, max, and step limit values while using it in the linear scale.
-  The installer prompts the option to install as “All Users” or as an “Individual User”.
-  SigmaStudio will no longer use elevation to open.
-  TCP/IP implementation for ADAU1761.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.6.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemFilter table generator format fix. This will prevent the user to input an unsupported format.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.6.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemPolar plotter is now part of Basic DSP toolbox.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.6.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed bug in 8 channel cross mixer caused when growing the cell by more than one.
-  Export files naming issues on variable declarations were fixed.
-  Standard Dynamics processors attack and hold value issues fixed.
-  ADAU1x61 Signal Path registers had been corrected from a series of GUI components out of their place.

.. raw:: html

   </details>


Enhancements SigmaStudio 3.6.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Absolute Max Value, Max Value , and Min Value Algorithms added.
-  RMS table cell extends range from -93 to +3 dB. (Before was -93 to 0 dB).
-  RMS table cell has lower and upper limit. Upper limit output is mapped to the +3dB value and lower limit to the -93 dB.
-  Index Selectable EQ Cell enhanced its GUI: Now it only displays the row of filters that is selected. It updates the window when selecting different rows. The focus on the add, delete, and show buttons is selected as not focused after moving the mouse pointer away from them.
-  Read/Write and Sequencer window now updates the Register Window.

.. raw:: html

   </details>


SigmaStudio 3.5 Release
~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemIncludes all bug fixes and enhancements from previous SigmaStudio 3.5.x Beta

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.7 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Optimized filters transfer function is now fixed.
-  SigmaServer external interface fixed to support for Windows7

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.7 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Two Dimensional Lookup table algorithm has been added.
-  Support for SSM2529.
-  SSM2518 included.
-  ALT+Drag wiring mode, connects all pins in source black to all pins in destination block

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.6 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Low latency register excluded from sequence download for ADAU1x82
-  General 2nd Order with variable Parameter/Lookup/Slew serialization issue.
-  TreeToolBox Block Processing / Stream Data issue fixed.
-  Lookup Table does not allow empty strings in the table and will not increase the number of points of the system. The only way to increase the number of points is through the main control.
-  When saving as while on Block processing tab the Main form title now updates.
-  NumericTextBox enable/disable back color is now fixed.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.6 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Index Independent EQ has now a new control GUI. It depicts a clue description tooltip for each button. It has two extra buttons that adds and removes rows.
-  Lookup Table now is expressed on both linear and dB units.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.5 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed transfer function for subtraction library. The TF has it’s polarity inverted, The code was corrected.
-  ADAU1x61 register window added “User” preset on the ALC Presets, fixing a bug where the Left/Right input volumes were disabled.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.5 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added Hoffman Transform.
-  Added quadrature output VCO.
-  Added adaptive beam forming algorithm.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Change in b1 coefficient minimum value for the IIR control.
-  For the AD193x family, on PLL and Clock Control Register 1 the ADC Clock definition was swapped. Now it is reverted and working properly.
-  ADAU1x81 register 0x4010 bitfield [2] enable -> 0 and disable -> 1.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.4 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Real Time Display now supports Y-axis configuration and Format.
-  DB Volume and DB Volume "Compact" with subroutine algorithms for multiple input channels have been added.
-  Text-In and Index Selectable Multiple Band Filters now support Peaking Filter.
-  DC Block filter is now double precision.
-  Compiler Output information for multiple ICs.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemSequencer Output Export Files fixed and support for multiple IC sequences.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.3 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

(None)

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Unordered List ItemFix on the PARAMS.h file from the “Export Output Files” tool.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.2 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  No need to re-compile “Frozen” schematics. All the download information is stored in the schematic.
-  RMS Dynamics Processors: Capability to switch between Units from dB/s to milliseconds and vice versa.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

(None)

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.5.1 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Micro Controller output files will no longer show “NumBytes_IC_1.dat” or “TxBuffer_IC_1.dat” to reduce redundant output information.
-  All Filters have a new upper frequency limit of 96 kHz.

.. raw:: html

   </details>


Bug Fixes SigmaStudio 3.5.0 BETA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Made the following modules Obsolete: Optimized Single Precision Filter 2-Channel, Optimized Double Precision Filter 2-Channel.In previous versions these modules auto-assigned non-optimized code for less than 3 biquads in series. The modules were re-added to the library without this automatic feature and will always use the optimized code regardless of how many biquads are in series.
-  Enhancements in SigmaStudio 3.5.0 BETA
-  Adding new modules:

   -  Optimized Single Precision Filter 1-Channel (ADAU144x, ADAU176x, ADAU178x)
   -  Optimized Double Precision Filter 1-Channel (ADAU144x, ADAU176x, ADAU178x)

.. raw:: html

   </details>


SigmaStudio 3.4
~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed size of General 2nd Order Filters Frequency control to always display 5 digits and Tooltip
-  Incremented Chebyshev ripple from 5 to 10 on 2nd order filters.
-  Added multiply value to Real Time display to scale the signal read back from the DSP.
-  Parametric EQ IIR coefficient window bug fix.
-  Fixed the Hard Clip, Soft Clip, and Advanced Clip algorithms multiple parameter write upon algorithm growth
-  Added the following new algorithms/modules:

   -  Bitwise Logic (ADAU144x, ADAU176x, ADAU178x)

-  Unordered List ItemLinear Interpolator Block no longer supports invalid Number of Points in Table and Serialization fixed for Max/Min saving values when Min saved as 1.0
-  ParametricEQ:

   -  When disabling and enabling a filter, sometimes the Boost value goes to zero.
   -  Boost value now goes from +30 dB to -100 dB, before it went to -30 dB.

-  Unordered List ItemAdded the following new algorithms/modules:

   -  Single Band Level Detector Running Average (ADAU144x, ADAU176x, ADAU178x)
   -  Single Band Level Detector Direct Read (ADAU144x, ADAU176x, ADAU178x)

-  Added the Real Time Display algorithm, which is a graphical version of the Readback algorithm.
-  Added Signal Detect algorithm and cell
-  Fixed bug on non programmable IC’s (showing a communication error)
-  HW Configuration and Schematic Tabs are displayed as tabs and not as buttons.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.3.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Windows Vista and Windows 7 x64 support.
-  New installation process:

   -  Default Installation file path location for x64 architecture is Program Files (x64).
   -  Default SigmaStudio projects including the “Sample Schematics” path location is \\<users>\\Documents\\Analog Devices\\SigmaStudio <version>\\Projects.
   -  Addins.xml default path is AppData\\Roaming\\Analog Devices\\SigmaStudio <version>
   -  During installation process, the user will be prompted with an additional USBi installation. This is to install the right USBi drivers into the current machine and it only needs to be run once.

-  PLL wait command during “download-compile”.
-  Export uC files with the wait command. This includes Sequencer support on wait command.
-  Envelope time span from 10 ms to 4400 ms.
-  Peaking No Post Gain now supports full range (-90 dB -> +24 dB).
-  New SigmaDSP Gen3 volume controls (Linear Gain, RC Gain optimized, dB, and dB compact).
-  ADAU1701 Assembler modification to better display MIPS used at design time.
-  Additions and updates to Gen3 core assemblers.
-  Addition of NoiseReduction algorithm to standard library
-  Addition of SuperBass algorithm to standard library
-  Increase of Index Lookup Table size to 500 from 100

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  SigmaStudio toolbox were optimized and thus would open faster.
-  Tree Toolbox now displays Algorithm Description.
-  New Standard Peaking Dynamics Processors.
-  New Standard Independent Channel Linked/Unlinked Dynamics Processors.
-  Added the following new algorithms/modules

   -  Voice Activity Detector (VAD) Standard (ADAU144x, ADAU176x, ADAU178x)
   -  Voice Activity Detector (VAD) With Acceleration (ADAU144x, ADAU176x, ADAU178x)
   -  Endless Loop Chime (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
   -  Peak Envelope Ext. Decay (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)

-  SigmaStudio A/B comparison download time enhanced.
-  Implementation of CRC and Watchdog for ADAU144x.
-  Existing algorithms made available for ADAU178x platform:

   -  Division
   -  Multi-tap Voltage Controlled Decay
   -  Value Hold
   -  Absolute Value
   -  RMS Table
   -  Peak Envelope w/ External Decay Input
   -  Mono Peak Compressor (no External Detection Input)
   -  Mono RMS Compressor w/ External Detection (no Hold, no Decay, no Post Gain)
   -  Stereo RMS Compressor w/ External Detection (no Hold, no Decay, no Post Gain)
   -  Mono Full Range Compressor (no External Detection Input)
   -  N-Channel RMS Compressor
   -  Stereo Hi Resolution RMS Compressor
   -  Stereo Full Range RMS Compressor w/ External Detection Input)
   -  Stereo Full Range RMS Compressor (no External Detection Input)
   -  Counter
   -  Timer w/ External Reset
   -  Stop Watch w/ External Reset
   -  2-Channel Mixer
   -  3-Channel Mixer
   -  8-Channel Mixer
   -  DC block Filter
   -  De-emphasis Filter
   -  General 2nd Order Index Selectable (Double and Single Precision)
   -  General 2nd Order Lookup
   -  State Variable Filter
   -  State Variable Filter w/ Q Input
   -  Tracking Filter
   -  General 2nd Order w/ var Param/Lookup/Slew
   -  First order w/ var Param/Lookup/Slew
   -  Multiple Control Mixer (No Slew Standard)
   -  Multiple Conrtol Mixer (Clickless SW Slew)
   -  Single Control Mixer (No Slew Standard)
   -  Single Control Mixer (Clickless SW Slew)
   -  Single Control Splitter (No Slew Standard)
   -  Single Control Splitter (Clickless SW Slew)
   -  Multiple Control Splitter (No Slew Standard)
   -  Multiple Control Splitter (Clickless SW Slew)
   -  Stereo Mixer (No Slew Standard)
   -  Stereo Mixer (Clickless SW Slew)
   -  Index Selectable De-Multiplexer (Mono)
   -  Index Selectable De-Multiplexer (Stereo)
   -  Index Selectable Multiplexer w/ Slew (Mono)

-  New feature for supporting cell enable/disable with password upon right-click
-  New mouse icon change to indicate when cell is movable
-  Added AVC.dll to installer (not added to the auto addins file)
-  Added Pin name for some algorithms on tool-tip hover over pins
-  Added AllPass filter to the Index Selectable Multiple Filter Control
-  Micro Controller Enable/Disable Parameter Export for each individual control.
-  ADAU144x Register cleanup.
-  Chime algorithm cleanup.
-  Chime hierarchy modification on TreeToolbox. It belongs to “Sources” category.
-  Filter Q on some filters was limited to additional knob range. Bug Fix
-  Fixed internal hierarchy cell renaming bugs
-  Capture window and exported uC files display the algorithm hierarchical structure on parameters
-  Read back cell now has a variable timer for continuous reads.
-  Added base address, offset, and algorithm index to be used for report on selected ICs.

.. raw:: html

   </details>


SigmaStudio 3.2.0 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Label position bug on save/open fixed.
-  Addins Browser Installer error message upon adding a valid Dll fixed.
-  Chime time/frequency controls now update the algorithm slope.
-  Changed the Chime min and max time.
-  Compressor Graph UI serialization on first point fixed.
-  GUI add/remove drag-point errors were fixed for all chime and envelope algorithms. Misbehavior of the points was also fixed.
-  TreeToolBox “Unclassified” Folder with multiple listings issue was corrected.
-  Parametric EQ

   -  Additional Filter bug upon modifying X-min axis fixed.
   -  SpinText color upon bug on enable/disable fixed.

-  Dejitter window register bug fixed for ADAU1381, ADAU 178x and ADAU1x61
-  Standard Independent RMS Dynamics Processor Algorithm:

   -  Attack and Release controls now are updating its value every time they get modified.
   -  Compression Visualization issue fixed.

-  Mono MUX No Slew: Changed the algorithm numbering system to avoid duplicate addresses.
-  Sequencer Window Export Files: Exports files with the right number of address bytes for ICs that have address bytes different than two.
-  Register download sequence changed for all GEN3 cores to support Start Pulse Select/Sample Rate register before the DSP Core Run Bit to ensure beginning code being run upon multiple link/compile/downloads
-  Export micro controller files are saved on the assigned location.
-  Control’s Settings/Options bug fixed.
-  Hierarchy cell renaming fixes.
-  Filter Q maximum value bug fix.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added Self-boot EEPROM \*.hex file export to Sequence Window for custom self-boot configurations.
-  Re-introduce GPIO Conditioning “Up/Down control, index output” algorithm, useful when indexing multiple lookup tables from the same GPIO input.
-  Added a new Context Menu to the read back module that would allow continuous read back with a .5 seconds timer.
-  Fixed a bug found on the control that controls filter’s Q were it allowed values higher than 15 to be written were the application was throwing an exception.

.. raw:: html

   </details>


SigmaStudio 3.1.20 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Bug fix for the Running Average Algorithm running on GEN2 processors (AD1940, ADAU170x)
-  Fix ADAU144x Self-boot EEPROM file errors, missing start pulse and core enable registers.
-  Include “DSP Readback” algorithm’s parameter definitions in exported system header files.
-  Add ADAV46xx I2C interfaces for EVAL-ADUSB2 (USBi)

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added the following new algorithms/modules:

   -  Standard Independent RMS (ADAU144x, ADAU176x, ADAU178x)
   -  Standard RMS (ADAU144x, ADAU176x, ADAU178x)
   -  Value Cross Detection (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
   -  Pulse Counter (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
   -  Running Average Envelope (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)

-  Sequence Window: The ability to export independent files for each sequence mode for uC usage.
-  Filter Bypass added to MidEQ Filter

.. raw:: html

   </details>


SigmaStudio 3.1.9 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The Envelope Folder in Dynamics Processing was organized in the TreeToolBox to reflect proper naming match to algorithms. [Previously named “RMS” envelope is actually the square output of the RMS envelope – See the help file for more information]
-  Naming fixed for parameters in the Multiple Control mixer. This problem only exhibited itself when multiple instances and growths of the algorithm were present causing a naming conflict violation.
-  Chime GUI. An error occurred while the user put together two drag points. Each drag point will be separated to avoid this common error.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.8
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added the Index Selectable Independent Multiple Bi-quad Filter algorithm for GEN2

   -  1 Channel Single Precision
   -  1 Channel Double Precision
   -  2 Channel Single Precision
   -  2 Channel Double Precision

-  Added Beta version of Phase Response for Transfer Function Window using Probe/Stimuli

.. raw:: html

   </details>


SigmaStudio 3.1.8 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed Square Root algorithm bug for GEN2 parts.
-  Fixed Bug for ADAU170x projects when doing copy/paste operation on controls with parameters, whose new address did not exist in the address map
-  System Export Files bugs fixed, undefined registers and register name conflicts
-  SigmaStudio Script, “ObjectConnect()” function errors fixed.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added a filter bypass option on the control for the following filter cells:

   -  General (2nd Order)
   -  Text-In Filter
   -  General (1st Order)
   -  Parametric EQ
   -  Index Selectable Independent Multiple Band
   -  General 2nd Order Index Selectable

-  Added the Index Selectable Independent Multiple Biquad Filter algorithm for GEN

Note: This was incorrectly implemented in 3.1.7. This feature is available in version 3.1.8

.. raw:: html

   </details>


SigmaStudio 3.1.7 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed FIR Table Editor window from crashing upon initial open/close without modifying points
-  Fixed opacity Bug on Parametric EQ algorithm upon download

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  USBi support for the AD193x codecs (SPI: AD1938/AD1939, I2C: AD1937)
-  USBi support for ADAU1371 (I2C).
-  ADAU1371 Register window for Filter Coefficient calculation.
-  Standard RMS Dynamics Processor: Low Range (-90 - 6 dB); real time signal representation on the dynamic graph; Compressor and Expander Ratio slider; Attack, Hold, and Release are now displayed in milliseconds; and it is available only for Gen 3 DSPs.
-  Chime- Envelope with and without infinite loop.

.. raw:: html

   </details>


SigmaStudio 3.1.6 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Export System Files, fixed errors in (\*.h) header file register/param definitions.
-  Non-Modulo fix.

.. raw:: html

   </details>


SigmaStudio 3.1.5 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Disallow parameter download during project load
-  ADAU144x non-modulo size no longer fixed at 256 data values
-  Gain (RC slew) and 2Channel – Double Precision, Optimized algorithms updated to properly support all GEN3 parts

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added the following new algorithms/modules:

   -  SuperPhat Spatialization
   -  Offline Microphone Match
   -  Combo Peak/RMS Compressor

-  New Settings Toolbar feature added to support multiple coefficient parameter settings for a schematic project.

.. raw:: html

   </details>


SigmaStudio 3.1.4 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  USB Communication channel for ADAU170x fixed to allow proper communication for certain parameters.
-  The Link/Compile/Download sequence was modified to ensure the proper register sequence and sample rate is set for GEN3 ICs.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The entire library of filters, now support a lower limit center or cutoff frequency of 1Hz on all filter controls. Previous versions of SigmaStudio limited the lowest frequency value that could be entered, but now all filter controls allow values down to 1Hz.

.. raw:: html

   </details>


SigmaStudio 3.1.3 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The SW Clickless Mute algorithm was not working properly for the ADAU170x IC. A new method for downloading the proper mute coefficient was implemented to fix this issue.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added the following new algorithms/modules:

   -  Advanced Soft Clip
   -  Square Root (Standard)
   -  Square Root (Ultra Precision)

.. raw:: html

   </details>


SigmaStudio 3.1.2 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The beginning code for GEN3 cores was updated to reflect a new order of initialization for use with the DAGS. Any new ICs used in projects will have the updated code. Existing schematic projects will have the old default beginning code saved. In order to update to the newest beginning code, drop a new IC in the hardware window of the project schematic and copy the existing algorithms to the new IC.
-  The Parameter Index Lookup Filters have renamed coefficients to avoid a potential bug. This only exhibited itself with more than 10 instantiations of the algorithms each with 10 or more curves. The algorithms affected were:

   -  General (2nd Order/Lookup)
   -  General 2nd Order Index Selectable – Double and Single Precision
   -  General 2nd Order w var Param/Lookup/Slew

-  The Parameter Index Lookup Filter Cell had legacy code that downloaded incorrect filter values to the DSP. This mechanism was updated to ensure proper filter coefficient download.
-  Multiple Link/Compile/Download compilations for GEN3 projects using algorithm code with DAG updates cause intermittent behavior with coefficient download. A new register sequence is implemented for the Link/Compile/Download operation to ensure proper coefficient operation.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Added new algorithms to the Index Selectable Independent Multiple Band Filter

   -  2 Channel Single Precision
   -  1 Channel Double Precision
   -  1 Channel Single Precision

.. raw:: html

   </details>


SigmaStudio 3.1.1 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  The following GEN3 SW Slew Volume algorithms were fixed to support double precision volume handling for low signal levels.

   -  Gain (RC Slew)
   -  Growable Single Vol Ctrl

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.1.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Allow the creation of hierarchy board from a selection of multiple cells
-  Allow rapid Register Settings (same concept as copying Cell settings). This functionality can be found by right clicking the DSP and following the context menu)
-  Provide a file “Properties” Dialog.
-  Right clicking the schematic tab to open or get the path of current project files provides easier access to compiled output.
-  Added Index Selectable Stereo Biquad Filter with asymmetrical filter number selection.
-  Added Frequency chimes

   -  Linked Freq/Amp Sweep
   -  Distinct Freq/Amp Sweep
   -  Freq Sweep Full Scale

-  Added Register Sequencer functionality to Data Capture window
-  Added Parameter RAM visualization list to Data Capture window
-  Added new GPIO modules

   -  Push Button Volume
   -  Push Button Volume, Mute
   -  Rotary Volume
   -  Toggle On/Off
   -  Toggle Counter (Rising and Falling Edge algorithms)

-  Modified and improved 3rd generation compiler outputs to directly write into the output window to better show DSP resources
-  Added support for ADAU1761 and ADAU1361
-  Added support for ADAU1781 and ADAU1381
-  Added the following new modules

   -  Enhanced Stereo Capture
   -  Mono2Stereo
   -  Logic Buffer
   -  Zero Comparator
   -  One Shot Fall (with and without reset)
   -  One Shot Rise (with and without reset)
   -  Signal Subtract
   -  Data Controlled Clip
   -  Standard Cubic Soft Clip

.. raw:: html

   </details>


SigmaStudio 3.1.0 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Moved Standard Clip to be placed in new Tree Toolbox folder (Non Linear Processors)
-  “Soft” GPIO Read/Write interface blocks for the 3rd generation cores that do not have interface registers.
-  New Capture Window Read back implementation (Read Request + Read Result)
-  Updated “System Files”, C formatted header files which mimic SigmaStudio download. The sequencer window also exports to .h files
-  Change IC on board now properly applies to nested cells
-  Improved support for large font sizes
-  Updated SigmaServer automation/scripting interface (Improved Matlab interoperability)
-  USBi support for 1940 and ADAV46xx
-  Index Selectable Multiple Filter Bug fixes
-  Register Window ADAU1x61 update
-  White Noise Algorithm output was scaled down to be between ±1
-  Fixed the 1702 Maximum Memory of Parameter RAM to 1024
-  Fixed Index Selectable Filter for Chebyshev Filters

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.13
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  ADAU144x: SigmaDSP Digital Audio Processor with Flexible Audio Routing Matrix
-  Added MONO “Peaking Compressor” algorithm
-  Modified compressors to allow better precision when setting crossover points. This is now done by allowing right clicking on points.
-  Added linear interpolator block.
-  Improved Compiler output reporting for 3rd generation cores.
-  Modified and optimized White noise.
-  Modified 1936 data ram assignation to make better use of memory.
-  Modified Non Modulo Register assignation.
-  Increased maximum number of tabs available for FIR filters.

.. raw:: html

   </details>


SigmaStudio 3.0.13 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Microsoft .NET Framework 3.0/3.5 causing SigmaStudio crash at startup
-  SigmaStudio Sampling Rate, 11.025kHz instead of 11kHz, 22.05kHz instead of 22kHz
-  Feedback algorithm fixed for ADAU144x
-  ADAU1701/1401 register controls updated for compatibility with revised silicon

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.12
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Improved Index Selectable Filter: Maximum filter count increased to 100, optimized user interface response. Added First Order index selectable filter algorithm.
-  Algorithm optimizations for “General 1st/2nd Order w var Param/Lookup/Slew” and “Parameter Tone with Index Lookup Tables” blocks.
-  Improved Alias block, alias blocks share a common name for easier identification.

.. raw:: html

   </details>


SigmaStudio 3.0.12 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Mute block fixed, mute block might not function properly when two mute blocks use contiguous slew ram.
-  1st order High-Pass filter algorithm update, now has constant gain across all frequencies.
-  “On/Off Switch” source set to off on SigmaStudio download.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.11
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Add support for ADAV46xx products, Audio Processors for Advanced TV.

.. raw:: html

   </details>


SigmaStudio 3.0.11 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Prevent use of comma ‘,’ or space ‘ ‘ for numerical decimal place in non-English versions of Windows, only the period character ‘.’ is supported.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Capture window display mode of Address in hexadecimal format and Data in binary format.
-  User Comment font can be modified by right clicking the User Comment block.

.. raw:: html

   </details>


SigmaStudio 3.0.10 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Parametric EQ block did not support multi-channel input, the first input was processed and copied to all outputs. Any additional inputs were ignored.
-  Signal Merger and Signal Add blocks had the same algorithm name which introduced errors when using both blocks in the same schematic design. The Signal Merger’s algorithm has been renamed. This change should not affect legacy designs.
-  Alias Block caused errors when using Copy and Paste. Alias blocks could not be renamed.
-  General (2nd Order) “Tone Control” filter equations were not included in the Help file.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.9
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  It is no longer required to connect unused block output pin to the “Schematic Terminal” block. Linking will succeed with unconnected output pins.
-  USBSerialConverter (EVAL-ADUSB1) supports SPI communication with all SigmaDSP ICs; previously SPI was only available for AD1940.

.. raw:: html

   </details>


SigmaStudio 3.0.8 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fix ADAU1701/1702 safeload write for EVAL-ADUSB2 (USBi) interface.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.7
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  E2PROM download and read/write support added for EVAL-ADUSB2 (USBi) interface.

.. raw:: html

   </details>


SigmaStudio 3.0.7 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  “DSP Readback” block’s value can be incorrect when reading from a GPIO input.
-  ADAU1702 compiler has incorrect size of 512 for Parameter RAM, should be 1024.

.. raw:: html

   </details>


SigmaStudio 3.0.6 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed, unexpected error dialogs when compiling projects. Caused by Enhanced schematic status indicator introduced in 3.0.4.

.. raw:: html

   </details>


SigmaStudio 3.0.5 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed, mouse cursor could disappear in schematic window after compilation.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Improved low signal level performance for RMS Compressor blocks.
-  Enhanced schematic status indicator, now displays USB communication status. Refer to the “Link/Compile/Download” topic in the SigmaStudio Help for more information.

.. raw:: html

   </details>


SigmaStudio 3.0.4 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Fixed compressor Hold and Decay time-constant controls. In previous versions the TC calculation was incorrect, limiting the time-constants to a smaller range than is supported by the compressor algorithms. Depending on Hold and Decay settings, this fix may affect the system response in legacy designs utilizing RMS compressor blocks.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Parametric EQ: graphical adjustment of filter response, create complex responses using up to 15 cascaded 2nd order filters, available in the Toolbox’s “Filters” category.
-  Crossover: graphical design of 2-way and 3-way crossover filters, selectable crossover types (2nd-8th order Linkwitz-Riley, 2nd-4th order Butterworth, and 2nd-4th order Bessel) , available in the Toolbox’s “Filters” category.

.. raw:: html

   </details>


SigmaStudio 3.0.3 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Feedback blocks not functioning properly in some cases.
-  DC Input Entry range limited to -16.0 when set to 28.0 format, should be -(2^27).
-  Links (Wires) between hierarchy boards are not created during paste operation or board file loading.
-  "Delete" command missing in schematic right click menu.

.. raw:: html

   </details>


SigmaStudio 3.0.2 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Maximum delay value set to 1 sample on during cut/paste or undo/redo operation.
-  Default block name and block “Settings” set during copy/paste are not equivalent, this causes settings malfunction and name conflicts until the project is reloaded.

.. raw:: html

   </details>


SigmaStudio 3.0.1 Major Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  Deleting a hierarchy board’s input or output blocks can reset the control settings of blocks contained in the hierarchy board.
-  Edit Control drawing error when scrolling or displaying overlapped dialogs.
-  Probe Window "Always on top" behavior is unexpected.

.. raw:: html

   </details>


Enhancements in SigmaStudio 3.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. raw:: html

   <details><summary>Click for details</summary>

-  “General 2nd Order Index Selectable” filter with graphical adjustment of filter response.
-  Sawtooth, Square, and Triangle wave source algorithms.
-  Mux and Mixer algorithms with software slew.
-  Project and cell settings; State of all block/algorithm controls can be saved and recalled to/from “settings” files for a/b comparisons or re-using settings between projects.
-  “Tree Toolbox” window, design building blocks are functionally categorized for each IC in a tree view.
-  “Change IC”, change IC can be applied to a selection, assigning the IC for all selected block(s) and algorithm(s) in a single operation.
-  Hierarchy Files, Hierarchy boards can be saved as files and re-used in new designs.
-  Hierarchy Board “Hide”, Hierarchy board tabs can be hidden and optionally password protected to protect confidential design elements.
-  Hierarchy Board “Freeze”, Hierarchy boards can be individually frozen to prevent modifications.
-  Undo/Redo support, All design modification can be undone and re-done.
-  Cut/Copy/Paste support, schematic design blocks (blocks) can be copied and pasted, within a design and between project files.
-  Schematic Printing, schematic designs can be printed.
-  Enhanced capture window, communication capture window can be docked and customized.

.. raw:: html

   </details>


Bug Reports
-----------

If you experience something you think might be a bug in SigmaStudio, please report it by posting on the :ez:`SigmaDSP Community on EngineerZone <community/dsp/sigmadsp>`. Please describe what you did, what error resulted, the version of SigmaStudio, and include any error messages from SigmaStudio.

Unless additional information is needed, you will not receive a direct response.

Requests for Features
---------------------

If you have an idea or request for additional features or enhancements of SigmaStudio, your input is always welcome. Please submit any suggestions by posting them on the :ez:`SigmaDSP Community on EngineerZone <community/dsp/sigmadsp>`.

Legal Notices
-------------

SigmaStudio is a registered trademark of Analog Devices, Inc. All other trademarks are the property of their respective owners.

Analog Devices, Inc, One Technology Way, P.O. Box 9106, Norwood, MA 02062-9106, U.S.A. © 2015 Analog Devices, Inc. All rights reserved.
