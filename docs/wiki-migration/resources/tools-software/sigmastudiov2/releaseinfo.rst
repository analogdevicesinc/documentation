| :doc:`Return to the parent page </wiki-migration/resources/tools-software/sigmastudiov2>`
| ======Release Information======

3.3.0
=====

Features
--------

-  Adds software support for ADSP-2183x/ADSP-SC83x series of processors from the SHARC-FX processor family.
-  Absorbs all SigmaStudio+ 2.3.0.4 patch changes.
-  New ADSP-2183x/ADSP-SC83x features:

   -  Improves the performance of critical DSP modules.
   -  Introduces first set of interleaved DSP modules designed to enhance optimization for larger channel counts.
   -  Introduces simultaneous execution of sample and block processing for control and audio data respectively.
   -  Supports external MCU host packetization APIs for parameter write and read.
   -  Improves SS+ MIPS profiling experience by providing a .csv export option and supporting easy navigation from profiling table to schematic modules through double-click.

-  Misc. Features:

   -  Updates the Algorithm Designer workflow to a new User Interface.
   -  Upgrades the EVAL-A2B-USBi settings page to a new User Interface.
   -  Provides graphical CMD4 packetization support for SigmaStudio+ SHARC execution.
   -  Supports runtime multi-schematic download for ADSP-21569 and ADSP-21593 library integration projects.
   -  Supports MIPS reset option in all ADSP-215xx/SC5xx library integration projects.
   -  Adds easy navigation from memory window to modules in the schematic through double-click.
   -  Improves general user interface issues.

-  Adds new SigmaStudio modules:

   -  External Volume Control (with Dual slew) for ADSP-215xx/SC5xx and ADSP-2183x/SC83x family of processors.
   -  Wav Player support for ADSP-215xx/SC5xx family of processors

| 
| =====2.4.0=====

.. _features-1:

Features
--------

-  Introduces a new user interface for SigmaStudio+

   -  Offers both dark and light application themes for user preference.
   -  Redesigns UI controls with accessibility considerations and enhanced user experience.
   -  Optimizes DSP module layout for better canvas space utilization.
   -  Implements performance enhancements for a smoother user experience.

-  Adds the EVAL-A2B-USBi software support.
-  Adds SigmaStudio T connector.
-  Adds new features to ADSP-215xx/SC5xx

   -  Linear Slew Gain module.
   -  Advanced Delay Pool with memory selection.
   -  Voltage Controlled Delay with memory selection.
   -  External SPI Delay (only on ADSP-21568).
   -  Schematic by-pass feature.

Bug Fixes
---------

-  Fixes in SigmaDSP ADAU145x/ADAU146x registers and EEPROM functionality.
-  Fixes in hierarchy board for pin-re-arrangement during load and save shape feature.
-  Corrects issues related to slider controls found in earlier versions.
-  User experience improvements added while opening huge projects and performing UI operations on huge projects
-  Addresses other miscellaneous bugfixes.

| 
| =====2.3.0=====

.. _features-2:

Features
--------

-  Supports new ADSP-215xx/SC5xx platforms – ADSP-21568 processor using EV-21568-SOM board and ADZS-SC589-MINI (SAM) platform.
-  Enables A2B patch updates in SS+ Update Manager.
-  Support for SigmaDSP self-boot over I2C.
-  Supports scripting Thrift compatibility with 0.20.0 version.
-  Provision to drag and drop the .ssprj file into SS+ application to open the project.
-  Misc. Features

   -  Introduction of Home Page in SS+.
   -  Enhancements to SS+ Add-ins Browser – enables product and version level selection for SS+ compatible products.
   -  Provision to force the safe-load of parameters onto the target.
   -  Enhancements to 2D LUT module and comment box control.
   -  Provision to include or exclude platforms from download.
   -  Provision to set the scripting port number via command line switch or environment variable.
   -  Additional APIs supported for Sequence Window operations in scripting interface.
   -  Support for Code B in SHARC demo microcontroller mode application.
   -  Improves SS+ console command interface with additional commands.

.. _bug-fixes-1:

Bug Fixes
---------

-  Delay while loading SS+ File Explorers during New project, Open Project etc. resolved.
-  Resolves the shrinking of connectors issue when multiple shapes and connectors are selected moved across the canvas.
-  Enhancements to SigmaDSP self-boot operations.
-  Corrects Sequence Window download over SPI using SpiCmd fields.
-  Addresses locked modules canvas operations.
-  Addresses multi-instance SHARC MIPS read issues.
-  Addresses SigmaStudio migration related issues.
-  Addresses blind A/B comparison issues.
-  Fix for slower link compile and download operation for huge schematics.
-  Re-enables the connector context menu to align the connected modules, knob and slider controls.
-  Enhances general user interface for SS+ Update Manager

| 
| =====2.2.0=====

.. _features-3:

Features
--------

-  Support for Pitch Shifter module for ADSP-SC5xx family of processors
-  Link Compile Connect feature.
-  Provision to configure export files naming convention.
-  Enhances sequence window operations. Refer to sequence window wiki page for more information
-  Misc. Features

   -  Provision to store the output links of a module and restore them to another module.
   -  Multiple notification control.
   -  Highlights selected link between two modules in a different color compared to others.
   -  Enhancements to table control.
   -  Logging feature for output and capture window.
   -  More detailed compilation result in output window

.. _bug-fixes-2:

Bug Fixes
---------

-  Improves hierarchy board tool tip between connections.
-  Selection of modules to be retained after copy paste operation.
-  Addresses sequence window issues for I2C protocol with respect to data width field.
-  Corrects A2B tab names reverting to old labels.
-  Allows expansion and text trimming on Data column of capture window.
-  Addresses copy, paste issues related to IO modules.
-  Addresses generic undo, redo related issues.
-  Ensures shape labels are unique.
-  Migrates SigmaDSP configurations from SigmaStudio completely to SigmaStudio+.
-  Addresses graphical parametric filter modules issues.
-  Addresses generic alias pin issues

| 
| =====2.1.0=====

.. _features-4:

Features
--------

-  Support for ADSP-SC596 and ADSP-SC598
-  Provision to define new standard platforms using existing platforms
-  Additional APIs supported in scripting interface
-  Lock any platform/process/transceiver/module using password
-  Migration of SigmaStudio A2B projects to SigmaStudio+
-  Misc. Features

   -  Network bus length modification from the system view
   -  Context menu enhancements for ease of access of canvas and settings window
   -  Support for multiple communication protocol between communication device and platform
   -  Auto scroll while expanding in project window and toolbox entries
   -  Double click on a SigmaStudio+ project file to launch SigmaStudio+ and load the project

.. _bug-fixes-3:

Bug Fixes
---------

-  Added Copy/Paste functionality in the system level and addressed other Copy/Paste issues
-  Addressed distortions/overlapping of connections while re-opening the project and moving multiple shapes
-  Addressed Save Shape and Load Shape issues
-  Addressed pin related issues while closing and reopening of projects
-  Addressed issues related to Undo-Redo of platforms
-  Addressed issues in Thrift scripting APIs
-  Addressed issues in SigmaStudio project migration
-  Addressed linking and connection issues in Alias pin and Hierarchy boards
-  Addressed slow response or crash while opening a canvas with large number of shapes and connectors
-  Addressed the Update manager failure under certain networks
-  Addressed application freeze issue while performing copy-paste or move shape operations
-  Addressed issues related to inconsistent update on Project tree view or Tab header while editing the shape label
-  Fix in SPORT Configuration while updating the processor
-  Addressed compilation and migration issue on non-English language machines
-  Addressed the issue of not able to close or move undocked windows on top of application title bar
-  Miscellaneous fixes in module UI

| 
| =====2.0.0=====

.. _features-5:

Features
--------

-  Support for Networks and Network View
-  Provision to store multiple alternate canvases and set one of the canvases as the active canvas for processing
-  Enhanced project navigation
-  Misc. Features

   -  Migration of ADAU145x/146x register settings from SigmaStudio projects

.. _bug-fixes-4:

Bug Fixes
---------

-  TCPIP readback for ADSP-SC5xx/215xx
-  Misc. fixes in ADAU145x/ADAU146x and ADSP-SC5xx/215xx modules
-  Fixes in checksum, self-boot features
-  Misc. user interface improvements

| 
| =====1.3.0 Eval=====

.. _features-6:

Features
--------

-  Support for ADSP-21593 and ADSP-SC594 processors
-  Support for S/PDIF transmitter in default framework
-  Undo-Redo Window
-  Register read option in SigmaDSP Register Windows
-  Addins Browser Window to add Plugins
-  Integrated Examples
-  Misc. Features

   -  Zoom-in/out supported in settings window
   -  Provision to reset and disable shape resize
   -  Auto save and restore unsaved changes
   -  Port configuration for scripting
   -  Ctrl+ Drag option to create a copy of shape

.. _bug-fixes-5:

Bug Fixes
---------

-  Enhancements in capture and sequence windows
-  Fixes in hierarchy board creation
-  Fix in I2C register read
-  Fix in Address Abstraction Metadata file
-  Fix in communication check for SigmaDSP
-  Enhancements to Alias Pin
-  Enhancements to Copy-Paste operation

| 
| =====1.2.0 Eval=====

.. _features-7:

Features
--------

-  Inbuilt Software Update
-  Downloadable Plugin Management
-  Command line execution of SigmaStudio+
-  Multi-channel Audio Streaming **:math:`**  * MATLAB Integration **`**
-  Remote execution of SigmaStudio+ using Scripting APIs and TCP/IP communication
-  Additional modules for ADSP-215xx/ADSP-SC5xx

   -  Solo
   -  Generic Balance Fader

-  Misc. Features

   -  Split canvas and settings windows horizontally and vertically
   -  Align to Source Pin and Destination Pin
   -  Target verification after download
   -  Plugin Version Management
   -  Save-Load Shapes
   -  While background for canvas

.. _bug-fixes-6:

Bug Fixes
---------

-  Rotation of Shapes not happening on canvas
-  Group selection and Copy-Paste
-  Connectors and shapes are not rendered properly while loading a saved board
-  Fixes in Multi-channel Multi-tap Delay, Log Look-up Table, 2D Look-up Table, Parametric EQ, Index Selectable Delay, Level Detector, General Second Order Filter
-  Exceptions while performing Copy-Paste of Hierarchy Boards
-  Faster loading of SigmaStudio+ and faster rendering of schematic canvases
-  Application layout optimized for more canvas space

| 
| **$**: Available as separate add-on package
| =====1.1.0 Beta=====

.. _features-8:

Features
--------

-  Project Migration from SigmaStudio to SigmaStudio+
-  Additional modules for ADSP-215xx/ADSP-SC5xx

   -  Log Lookup table
   -  Pinking Filter
   -  Standard Independent RMS Compressor
   -  Index Selectable Delay
   -  Parameter Read
   -  Parameter Write

-  Framework Config File generation for ADSP-SC5xx/ADSP-215xx target framework
-  Support for ADAU145x and ADAU146x processors with a comprehensive algorithm toolbox comprising of 250+ modules for evaluation and early engagement
-  TCP/IP Communication

.. _bug-fixes-7:

Bug Fixes
---------

-  Error in SPORT Configuration while using non-default number of sources and sinks
-  Wiring distortion in the canvas when a project is saved and reopened
-  Delay in opening Table control when the table size is large
-  Issues with channel assignment when output modules are copy-pasted
-  Module library filter for ADSP-214xx
-  Improvements in module UIs

| 
| =====1.0.1 Beta=====

.. _features-9:

Features
--------

-  A/B Preset Testing
-  Instant Transfer Function Display
-  Support for ADSP-215xx SOM platform
-  Support for the following new block processing modules has been added in this release

   -  Automatic Speaker Equalization
   -  2 Power x
   -  RMS Ip Average /Max Compressor
   -  Compressor Core
   -  Non-Bare Filter
   -  Pink Noise
   -  Trigonometry
   -  Multiplier
   -  Tracking Filter
   -  Pooled Delay

-  Evaluation restriction has been removed for the following modules and features.

   -  Algorithm Designer
   -  Scripting
   -  Fixed Address Mode
   -  Advanced Modules
   -  Frequency Domain Operations
   -  Sample Rate Converters
   -  Dynamic Bass Enhancement
   -  Loudness
   -  Gala Gain
   -  Effects - Reverb, Phat Stereo
   -  Advanced Filters – NLMS, Parametric EQ

.. _bug-fixes-8:

Bug Fixes
---------

-  Multi-instance schematic download issue has been resolved.
-  Issue in modifying the number of audio sources and sinks used in target framework has ben resolved.
-  Miscellaneous module UI issues have been addressed.

| 
| =====1.0.0 Alpha=====

.. _features-10:

Features
--------

-  Design systems having one or more platforms belonging to ADSP-214xx, ADSP-SC5xx and ADSP-215xx family of SHARC processors
-  Realtime parameter tuning using graphical controls
-  Modern UI and controls with zoom, rotate, resize, undo-redo. Customizable application layout with one click layout restore.
-  Comprehensive algorithm toolbox, with 140+ optimized algorithms from the following category:

   -  Filters
   -  Dynamic Processors
   -  Mixers and Splitters
   -  Volume Control/Gain
   -  Arithmetic Operations
   -  Logic Operations
   -  Multiplexers and Demultiplexers
   -  Generators
   -  Readback and Level Detectors
   -  Delays
   -  Dynamic Bass Enhancements
   -  Loudness
   -  Audio Effects
   -  Frequency Domain Operations
   -  Sample Rate Converters
   -  Clippers
   -  Signal Detection
   -  Stop Watches and Counters

-  Generation of system files and header file for microcontroller code implementation
-  Algorithm Designer for implementing new SigmaStudio modules
-  Scripting support for automation
-  Search and object highlighting for ease of navigation through toolbox and schematic.
-  Tuning features like algorithm bypass, tuning presets etc.
-  Schematic design features like hierarchy boards (with password lock), algorithm version control etc.

.. _bug-fixes-9:

Bug Fixes
---------

-  None. This is the first version.

| 
