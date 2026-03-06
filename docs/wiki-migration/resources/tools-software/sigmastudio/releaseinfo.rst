:doc:`Click here to return to the SigmaStudio and SigmaDSP Documentation top page. </wiki-migration/resources/tools-software/sigmastudio>`

Release Information
===================

This section contains the details of enhancements and bug fixes done in various releases.

4.7 Release (18-Apr-2022)
-------------------------

ADAU145x/ADAU146x
~~~~~~~~~~~~~~~~~

-  Checksum error when Version control enabled in ADAU-145x/146x is resolved.
-  Issue with operation of up sampling and down sampling algorithm is resolved.
-  Issue with schematic compilation when HW Slew NxM Mixers and Multiple Control Mixer Modules are present in the schematic, is resolved.
-  Complex Division module functionality issue with growth resolved.
-  The exception issue with the schematics created in SigmaStudio 4.5 is resolved.
-  Issue in copy and paste of General EQ (2nd order) Slew Ex filter is resolved.
-  Issue in Hilbert Transform module functionality is resolved.
-  Block Signal Mixer compilation issue when there is growth more than 4, is resolved.
-  The Safe load functionality issue in Register Read Write window is resolved.
-  Compilation errors on using the DM delay modules is resolved.
-  Exception issue with Delay block is resolved.
-  No audio output with oscillator modules is resolved.
-  Parametric EQ GUI issue for Boost parameter is resolved.
-  State Variable Filter instability issue with change in frequency resolved.
-  Kill core register support added for ADAU146x IC.
-  Level Detector no MIPS module added for ADAU145x and ADAU146x.
-  12kHz and 24kHz sample rate options added for ADAU145x and ADAU146x IC.

ADAU178x
~~~~~~~~

-  Issues with header file export is resolved.

Scripting
~~~~~~~~~

-  New scripting API interfaces added for A2B 19.4.3 release.

4.6 Release (24-Dec-2020)
-------------------------

.. _adau145xadau146x-1:

ADAU145x/ADAU146x
~~~~~~~~~~~~~~~~~

-  Invalid section growth options in Parametric EQ is removed.
-  Multiple issues with the CrossFade algorithm are resolved.
-  LPF option is removed in the down sampling/up sampling module. LPF can be done outside the modules now.
-  An issue with Audio Signal router modules which causing the modules not to work for some IO combinations is resolved.
-  An issue with the DSP calculation General second order filter which causing the boost to be wrong is resolved.
-  Pitch Transposer delay memory can be chosen between DM0, DM1 or PM now.
-  Assembler error caused in mute module when the parameter is allocated in DM0/DM1 page 2 is resolved. (ADAU146x).
-  Parameter write issue with the Advanced Clip module is resolved
-  Issues with Framework overrun monitor for ADAU146x is resolved
-  NxM mixer accepts gain between -128 to 127.99 now.
-  An issue with AutoEQ which causing the high frequencies roll off is resolved.
-  Assembler errors in Fractional Delay module are resolved
-  Export issue with the AVC modules are resolved.
-  Issue with the invert functionality of the crossover filter is

resolved

-  Issue with Block framework MIPS reporting is resolved
-  Add algorithm option is removed form the Fractional delay
-  Issue with the CheckSum module when multiple ADAU145x/ADAU146x ICs are used in a single project is resolved.
-  Malloc and free code are optimized for code size
-  Issues with NxM mixer which is causing some IO option to fail are resolved.
-  Issues in the Schematic Version control are resolved.

ADAU170x
~~~~~~~~

-  Issues with the Algorithm version history for ‘Index Selectable Filter’ is resolved.
-  Wrong parameter addresses in Multi-tap Delay are fixed.

Export
~~~~~~

-  Issues with the Type field in export XML is resolved.
-  Export now supports relative path from the schematic file.
-  Issues with Address Increment field in the export for ADAU1761 is resolved.
-  Issues with the data length field of the Sequence Window export are resolved.

User Interface
~~~~~~~~~~~~~~

-  Issues in Standard RMS compressor GUI is resolved.
-  UI issue with the Nth Order filter module which causing the coefficients to change is resolved.
-  An issue with ‘Resize View’ option which causing the module labels to become empty is resolved.
-  Issues with the timestamp field in the capture window are resolved.
-  Issues with Holders EQ/ High order shelving filters which causing the SigmaStudio project file not to open in some cases resolved.
-  Issues with the Level detector which causing the update not to happen in some cases are resolved.
-  Module labels are maintained unique when hierarchy boards are copied and pasted within the schematic.
-  Scrollbars are now visible in the AD193x codec configurations.

.. _scripting-1:

Scripting
~~~~~~~~~

-  Indirect Parameter table values can be written from the scripting now.
-  Load and design filters options in AutoEQ modules can be done through script now.
-  Writing the self-boot image of ADAU145x/ADAU146x schematic can be done using script now.

4.5 Release (11-Nov-2019)
-------------------------

.. _user-interface-1:

User Interface:
~~~~~~~~~~~~~~~

-  Serialization Issue with the Gain and Pulse with Dynamic duty cycle modules are resolved.
-  Copy/paste issue with Nth Order filter is resolved.
-  RMS Compressor backward compatibility issue is resolved

.. _scripting-2:

Scripting:
~~~~~~~~~~

-  ICRegisterRead API issue with Aardvark is resolved.
-  Issues in RMS Compressor, Peak Compressor and Delay Block are resolved.

.. _adau145xadau146x-2:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  Option to access checksum variables and all parameters of Wav Player(Internal) , GainEnvelope modules through IPAT is added
-  Wav Player output distortion issue for fractional pitch factors is resolved.
-  ADAU146x Compiler Issue is resolved.
-  ADAU1462 Compiler error related to Page Size is resolved.
-  Issue with runtime I2C Read for addresses beyond 0x7FFF is resolved.
-  Issue in High pass first order filter coefficient generation is resolved for the following modules

   -  General Eq (2nd order) Single Precision- Clickless HW Slew/ No Slew/ Clickless SW Slew

      -  General Eq (2nd order) Double Precision- Clickless HW Slew/ No Slew/ Clickless SW Slew
      -  Parametric EQ-Double Precision

4.4 Release (9-Jul-2019)
------------------------

.. _user-interface-2:

User Interface:
~~~~~~~~~~~~~~~

-  A new window to display what is new in the recent SigmaStudio release is added.
-  Issue with the Gain module in dB for negative gain is resolved.
-  UI issue with the scrolling which accidently changed the parameters are resolved.
-  Lookup Table has now an update option to update the parameter.
-  Issue with FIR filter enable/disable option is resolved.
-  Issue with the multiple short-keys in the SigmaStudio is resolved.

.. _scripting-3:

Scripting:
~~~~~~~~~~

-  New Scripting APIs ICRegisterRead and ICRegisterWrite are added for reading and writing IC registers without the IC Name as the parameter.
-  Pause and Resume and Halt options are added in SigmaStudio scripting.
-  Issues in RMS Compressor modules which caused the ObjectGetProperties() API not to work properly are resolved.

.. _adau145xadau146x-3:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  Biquads with the HW slew is added.
-  There is a new option to monitor MIPS overrun in the framework now.
-  Compiler errors caused when using the multi-rate blocks are resolved.
-  Multiple issues with the Flash programmer module are resolved.
-  TCP IP communication channel is supported for ADAU146x now.
-  Export issues with AVC is resolved.
-  Now the export for ADAU146x will contain the page information.
-  Compiler error in the SRC module is resolved.
-  Now pitch shifting factor in the Wav player is accessible through the IPAT.
-  Issue with Analysis and the Synthesis window share coefficient option is resolved.
-  Export issues with the multiple compressors are resolved.
-  Issue with the bypass option in the index selectable filter is resolved.
-  A new option is added to optimize the DM0 and DM1 packs by removing zeros.
-  An issue with the checksum module during the selfboot is resolved.
-  Minor issues with IPAT is resolved.

ADAU144x/ADAU176x:
~~~~~~~~~~~~~~~~~~

-  An issue with the Index Controlled RMS Compressor is resolved.
-  Issue with external controlled fractional delay is resolved.

4.3.3 Beta (21-May-2019)
------------------------

-  SigmaStudio support for ADAU1787 is added.
-  SigmaStudio support for ADAU7118 is added.

4.2 Release (26-Sep-2018)
-------------------------

General:
~~~~~~~~

-  Third-party algorithms developed for SigmaStudio can easily be downloaded now using ‘Manage Downloadable Add-Ins’ option in the Tools menu.

.. _adau145xadau146x-4:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  Multiple versions of Dynamic EQ are added (Single Blend EQ, RMS Blend EQ, Single Blend EQ with External Blend ).
-  Delay, Multi-tap voltage control delay module now supports the program memory to be used for the delay line.
-  A new option is added to map the delay line with input/output pins in FIR Filter pool module.
-  Compilation speed is now improved significantly.
-  Keyboard up down arrow keys can be used now to select the parameters in the Indirect Parameter Access table.
-  An exception caused by FIR filter Transfer function is fixed.
-  RMS Limiter tool tip is corrected.
-  Wrong labels in the panic manager is corrected.
-  Parameter changes are now shown in the capture window for High Order Shelving filters.
-  An issue with ‘Loudness Low & Hi’ external is resolved.
-  Wav player removes the header for all the files now when multiple files are selected using a single instance.
-  T-Connection is made obsolete for block schematic as Splitter module does the same functionality.
-  A bug in framework initialization which overrides DM is resolved.
-  Unused PM can be cleared during the initialization in the framework now.
-  Analysis and Synthesis window can share the coefficients across instances now.
-  An issue with real FFT which caused compiler error when the buffers are mapped to different DMs is resolved.
-  Schematic Export is working when the ‘Master Control Port run time module is present.
-  Safeload addresses are now included in the export for ADAU146x.
-  Checksum can be used to verify the transaction for DM0, DM1, and PM packs during download.
-  Flash programmer can now support Start Address for each file.

.. _adau170x-1:

ADAU170x:
~~~~~~~~~

-  A GUI issue with the GPIO selection is resolved.

.. _user-interface-3:

User Interface:
~~~~~~~~~~~~~~~

-  Now modules’ labels in the schematic can be copied with Ctrl+C short key.
-  An exception caused while Zoom In/Zoom out is resolved.
-  Serialization issue with the Peak envelope is resolved.
-  Serialization issue with the tracking filter is resolved.
-  A bug in the DC Hex option is resolved.
-  Obsolete algorithms in the block schematic is displayed in output window now.
-  User is notified to save the schematic now when the freeze schematic is enabled and not saved.
-  Linear Gain now has an option to display the gain in dB.
-  An GUI issue in real time display is resolved.
-  A bug caused the schematics with add algorithm not to open is resolved.
-  GUI Issue with the volume control in linear mode is resolved.

.. _scripting-4:

Scripting:
~~~~~~~~~~

-  ObjectGetProperty() IScripted API and GET_OBJECT_PROPERTY() SigmaServer API support an option to get the current growth.

4.1 Release (5-Jun-2018)
------------------------

Communication Channels:
~~~~~~~~~~~~~~~~~~~~~~~

-  An issue which causes the USBi not to respond when the USBi is connected to USB3.0 port with Windows 10 OS is resolved.

.. _adau145xadau146x-5:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  FFT, IFFT, Real FFT and Real IFFT algorithms are optimized for cycles.
-  Compatibility with Real FFT output is added for Complex Magnitude, Complex Multiplication, Complex Conjugate Multiplication and Complex Divide.
-  A bug in sine tone oscillator when the growth is more than 4 is resolved.
-  A bug in block division is resolved.
-  Coefficients used in Analysis and Synthesis window is configurable now.
-  Transfer function related issues are resolved in multiple filters.
-  A UI issue in Digital Mic is resolved.
-  Multiple issues in Master Control port modules are resolved for SPI.
-  Flash programmer now supports an option to specify the starting address to program.
-  WavPlayer supports up to 16 files in a single instance.
-  Compiler issues where the size of DM reported wrongly for ADAU146x is resolved.

Others:
~~~~~~~

-  Now the short parameter name feature supports cells with multiple algorithms.
-  Sequence file generated from sequence window can save the address in the hexadecimal format now

4.0 Release (22-Mar-2018)
-------------------------

.. _adau145xadau146x-6:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  Modified Filtered- X LMS algorithm is added.
-  Real FFT and Real IFFT algorithms are added in the block domain.
-  WavPlayer using internal memory is added.
-  A bug in export issues for General 2nd Order Filter with Slew is resolved.
-  A new option is added to enable ‘Indirect Parameter Table Access’ and other framework features in the older schematics.
-  Panic Error set due to Program memory is resolved.
-  FlashProgrammer now supports up to 32 files.
-  Support for ‘Block Protection Unlock’ SPI command is added to FlashProgrammer module.
-  Transfer function related bug in General 2nd Order filter DP is resolved.

.. _adau170x-2:

ADAU170x:
~~~~~~~~~

-  A bug in Hard Clipper is resolved.

SigmaStudio Scripting:
~~~~~~~~~~~~~~~~~~~~~~

-  The following new APIs are added.

   -  API to get all the DSP parameter's name and address in the schematic

      -  API to write/read to any DSP parameter using the DSP parameter name

.. _communication-channels-1:

Communication Channels:
~~~~~~~~~~~~~~~~~~~~~~~

-  Now Multiple AARDVARK devices can be connected to a single SigmaStudio instance.

3.17 Release (13-Feb-2018)
--------------------------

No new features have been added to this release. The following changes are applicable to this release:

-  A few corrections relating to documentation
-  Code refactoring

3.16 Release (21-Dec-2017)
--------------------------

User Interface Changes:

-  SigmaStudio is upgraded to use .NET 4.7
-  A bug in Auto EQ filter which causes an exception during the download is resolved.

ADAU145x/ADAU146x:

-  SRC module to convert the sample rate between 44.1kHZ and 48kHZ is added.
-  DSP Parameter Read module is added to readback parameters periodically and store in files.
-  General EQ Blend and General EQ with external blend algorithms are added
-  More options are added in the Indirect Parameter Access Table UI.
-  Multiple instance is now supported by WavPlayer.
-  Pitch Shifting and Loopback options are added for WavPlayer
-  The following block processing algorithms are added.

   -  Signal Divide

      -  Signal Invert

         -  Min/Max

            -  Min and Max Limit
            -  Min/Max Limit
            -  Max and Hold
            -  Min and Hold
            -  Feedback
            -  Scalar Addition
            -  Scalar Multiplication

-  FIR Filter pool is optimized for MIPS. User can choose between optimize for MIPS/Memory.
-  A bug in Audio Signal router parameter tuning for ADAU146x family is resolved.
-  Issue in Safeload write for ADAU1450 is resolved.
-  An issue in Sine tone growth option is resolved.
-  Standard dynamic Processor threshold resolution is reduced to 0.1 dB.
-  Compiler error created in Master Control port SPI Mode 0 is resolved.
-  A bug which is causing inconsistence code generation between multiple Link Compile Download is resolved.
-  Multiple bugs in Complex-Real multiplication block is resolved.

Other SigmaDSPs:

-  An issue in ADAU144x parameter update module which caused corruption in other modules in the schematic is resolved.
-  A bug in Sequence window which caused the Safeload to fail is resolved.

SigmaStudio Scripting:

-  New SigmaStudio Server API and IScripted interface APIs are added to get parameter values.
-  A new option is added to find the parameter name to use in the SigmaStudio scripting.

Export:

-  A new option is added to shorten the parameter names in the PARAM.h export files.

3.16.1 Beta (3-Nov-2017)
------------------------

-  Interpolator module is added for ADAU1777.
-  SSM3525 is supported now.

3.15 Release (29-Sep-2017)
--------------------------

.. _user-interface-4:

User Interface:
~~~~~~~~~~~~~~~

-  Version control is maintained for algorithms obsoleted from release 3.15 onwards.
-  An issue with ‘Resize View’ is resolved.

ADAU146x:
~~~~~~~~~

-  A bug in block processing framework is resolved.
-  Issues with GPIO IN and GPIO Out is resolved for ADAU1467 and ADAU1463.
-  Missing AUX ADCs are added for ADAU1467/63.

.. _adau145xadau146x-7:

ADAU145x/ADAU146x:
~~~~~~~~~~~~~~~~~~

-  Anti-Aliasing/Interpolation filter is added as part of down sampling/up sampling modules.
-  Single precision 4-band version of Multiband compressor algorithm is added.
-  The following modules are added in the block processing mode.

   -  Block Subtraction

      -  Block Multiplication

         -  Block T Connection

            -  Block Square Root
            -  Complex- Real Multiplication
            -  Complex Conjugate
            -  Complex – Complex Conjugate Multiplication
            -  Magnitude of Complex number

-  Issue with hierarchy board in block schematic is resolved.
-  An issue in data controlled Asymmetrical soft clipper is resolved.
-  Issue with Self-Boot EEPROM speed configuration is resolved.
-  A bug in Flash programmer which causes an exception during the link compile download is resolved.
-  An issue in xml export for Indirect Parameter access table is resolved.
-  An issue with parameter address for multiple control mixer is resolved.
-  PLL CTRL0 is added to download sequence before enabling the PLL.
-  Parameter address for Level detectors output now available in PARAM.h export file.
-  A backward compatibility issue with audio signal router is resolved.
-  A bug causing a noise in Advanced Clipper and Data Controller is resolved.
-  A bug RMS (No Post) External Detect External gain output is fixed.
-  Panic Error caused by NxM Mixer is resolved.
-  Compiler error occurred when using 44.1 kHz signal chain in block processing is resolved.
-  Issues in self boot with 512kB/16-bit addressable SPI EEPROM is resolved.
-  Butterworth filter is added as an option for Loudness module. Butterworth reduces the deviation in frequency response for this module between different sample rates.

ADAU144x/ ADAU176x:
~~~~~~~~~~~~~~~~~~~

-  Eight order shelving filters which were available for ADAU1761 are now available for ADAU144x also.
-  A bug in FIR filter length parameter is resolved.
-  Communication Error created when FIR bypass is enabled is resolved.
-  Issue with ISF filter is resolved. Now it supports up to 46 slew points.

ADAU1777/72:
~~~~~~~~~~~~

-  Backward compatibility issue with older schematics is resolved
-  An exception occurred when multiple Parametric EQ is resolved.
-  Issue with the frequency response for filters are resolved.

.. _sigmastudio-scripting-1:

SigmaStudio Scripting:
~~~~~~~~~~~~~~~~~~~~~~

-  New APIs are added for Reflection support.
-  Now parameters can be read from file and configured through scripts.
-  Print API is added to print debug messages from the script.

.. _others-1:

Others:
~~~~~~~

-  A security issue in hierarchy board with respect to linker window and compiler output is resolved.

3.15.2 Beta (29-Jun-2017)
-------------------------

Support Added for the following ICs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ADAU1462, ADAU1463, ADAU1466, ADAU1467

ADAU145x
~~~~~~~~

-  Master Control Port Runtime Sequential Write and Master Control Port Boot time I/O now supports SPI protocol along with I2C.
-  Minor bugs in One shot Fall Reset, One Shot Rise and One shot Rise Reset algorithms are resolved.
-  Audio Signal Router Maximum channel is improved to 34 channels.
-  Parameters can be added to Indirect Parameter Access table by right click option from the module.
-  Issue with Loudness block which created noise in the output is resolved.
-  A bug in assembler which caused multiple modules to fail during the multi-rate processing is resolved.
-  Complex Subtract, Complex Multiply, Complex Divide, Complex Merger , Complex Readback, DC Source, Complex DC Source, and Complex Splitter algorithms are added in block processing mode.
-  Real Time Variant module is added.
-  A bug in NxM mixer with HW slew which caused the mixer to fail when grown to multiple channels is resolved.
-  A bug in export for NxM mixer and Nth order filter modules are resolved.
-  FIR filer pool algorithm is added to the module library.
-  Multi-tap Multi-channel delay is added to the module library.
-  Bugs in Audio Signal Router Transfer function is fixed.
-  Inconsistencies in the SPI slave select for Flash Programmer and External SPI delay are resolved.
-  Wav Player supports upto 16MB now.
-  An issue with External SPI delay which was not allowing maximum delay more than 48000 is resolved.
-  Slew version of Index Selectable Independent Filter is created to avoid click noises.
-  A minor bug in up sampler/down sampler is resolved.
-  Multiple Control Adjustable Gain and Multiple Control Mute algorithms are added.
-  Register Read and Register Write modules are added to read/Write registers.
-  Bugs in transfer function for Parameter EQ filter is resolved
-  Number of channels can be increased for output module now.
-  Growable 2 channel adder module is implemented.
-  ASRC In, FIR, Delay modules are optimized for MIPS.
-  A new version of ASRC In is added which applies gain to the input.
-  A bug in Master Control Port interface read is resolved.
-  SPI is now supported by Master control port interface read/write.
-  Growable version of 2x1, 3x1 and 4x1 mixers are added.
-  HW Slew mode is configurable through GUI now

ADAU144x
~~~~~~~~

-  Parameters can be added to Indirect Parameter Access table by right click option from the module.
-  Bugs in Audio Signal Router Transfer function is fixed.
-  Export issue in Nth order filter is resolved.

.. _communication-channels-2:

Communication Channels
~~~~~~~~~~~~~~~~~~~~~~

-  Aardvark I2C/SPI is now supported for ADAU145x, ADAU144x family of SigmaDSPs.
-  Issue with "Single Level Detector w Numerical Display" during TCP/IP communication is resolved.

.. _user-interface-5:

User Interface
~~~~~~~~~~~~~~

-  Counterpart of the Alias will be highlighted when an alias is selected.
-  A security issue with the hierarchy boards’ password is resolved.
-  A bug in hierarchy board which cause the project file to corrupt is resolved.
-  New Zooming options are added (Zoom to Fit, Zoom to selection)
-  All the Level Detectors and the Readback modules can be switched on/off from the menu option.
-  Now Level Detectors and Readback module shall be inactive when not visible in the schematic.
-  ‘DC Input Entry’ modules can accept and display value in Hex now.
-  Multiple bugs in sequence file generation is resolved.
-  Icons are improved for communication channels.
-  UI improvement is done for Copy pasting data to Audio Signal router.
-  GUI exception in Index Selectable Independent filter is resolved.
-  An issue in FIR filter GUI which caused the parameter update not to happen for the first time download is resolved.

.. _others-2:

Others
~~~~~~

-  Mistakes in I2C addresses are corrected for ADAU1966

3.15.1 Beta
-----------

-  A bug in ADAU1777 Parameter EQ is fixed
-  ADAU1777 parameter EQ supports sample rate up to 768 kHz.

3.14 Release (23-Dec-2016)
--------------------------

-  TCP/IP Channel support is added for ADAU145x and ADAU144x
-  Wav Player algorithm is added for ADAU145x.
-  Asymmetric Soft Clippers modules are added for ADAU145x.
-  General FIR filter algorithm is added for ADAU145x.
-  IIR with slew is added for ADAU145x.
-  Loading from file option is added in index selectable filter.
-  Various bugs in 2nd Order filter Coefficient calculation is fixed for ADAU145x.
-  Critical bug in Mux and De-mux switches are addressed for ADAU145x.
-  Bug in SigmaStudioServer.dll which caused the MATLAB interface to fail is addressed.
-  Bug in pulse block is fixed for ADAU145x.
-  A minor bug in freeze schematic feature is addressed.
-  A bug in feedback cell addressed for AD71096.
-  Copy/paste functionality is improved.

.. _beta-1:

3.14.1 Beta
-----------

-  Support for :adi:`ADAU1777 <en/products/audio-video/audio-codecs/adau1777.html>` is added in SigmaStudio

3.13 Release
------------

Enhancements
^^^^^^^^^^^^

-  :doc:`Log2 </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/log2>` and Log10 is added for ADAU144X and ADAU170X, ADAU176X family of processors.
-  Biquad Filter Pool is added for ADAU145x.
-  :doc:`Nth Order Filter </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/nthorderfilter>` is added for ADAU145X.
-  :doc:`Level Detector Designer </wiki-migration/resources/tools-software/sigmastudio/toolbox/leveldetectorslookuptables/leveldetectordesigner>` is added for ADAU145X.
-  :doc:`Audio Signal Router </wiki-migration/resources/tools-software/sigmastudio/toolbox/mixerssplitters/audiosignalrouter>` now supports 32 channels. The input/output labels are editable.
-  :doc:`Indirect Parameter Access Table </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/indirectparamaccess>` is added for ADAU145X and ADAU144X.
-  :doc:`‘Parameter Update’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/basicdsp/parameterupdate>` module is added which updates coefficients with the external data though input pin.
-  :doc:`‘Filtered-x LMS’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/filters/filterednlmsfilter>` algorithm is added for ADAU145X.
-  :doc:`‘Up Sampling’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/multirateprocessing/upsampling>` and :doc:`‘Down Sampling’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/multirateprocessing/downsampling>` modules are added for ADAU145X.
-  :doc:`‘Interface Read’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/inferfaceread>` and :doc:`‘Interface Write’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/io/inferfacewrite>` modules which uses the master control port (I2C) to write back interface values are added for ADAU145X.
-  :doc:`‘Master Control Port Status’ </wiki-migration/resources/tools-software/sigmastudio/toolbox/mastercontrolport/mastercontrolportstatus>` module in ADAU145X reports I2C error as well.
-  External memory post program modification capability via GPIO pins and Master Port at self-boot time.

Bug Fixes
^^^^^^^^^

-  SafeLoad registers are mapped to the start of the DM1 for ADAU145X processers. These registers’ addresses will be available in the export files.
-  A bug in Index Selectable multiband filter which caused the SigmaStudio to crash is resolved.
-  A bug in Standard Resolution compressor which caused the SigmaStudio to crash when changing expander ratio and input gain is resolved.
-  A bug in Linear Interpolator which caused the SigmaStudio to crash is resolved.
-  A bug in Loudness algorithm which does not set the output to zero when the input is zero is resolved for ADAU145X.
-  Bug in transfer function for ‘Gain- No slew’ module is resolved.
-  A bug in EEPROM programming for ADAU144X which caused the ‘Compare Latest Compilation with EEPROM’ feature to fail is resolved.
-  Bugs in real time display module are resolved.
-  A Bug in loudness module which caused the step value not to be stored while saving is resolved.
-  Zoom Shortcut bug is resolved. Delete ToolbarLayout.dat from (%APPDATA%/Analog Devices/SigmaStudio 3.13) for the shortcut to work.

.. _beta-2:

3.13.1 Beta
-----------

.. _enhancements-1:

Enhancements
^^^^^^^^^^^^

-  External memory post program modification capability via GPIO pins and Master Port at self-boot time.
-  Now the schematics can be copied as a bitmap image.
-  A feature to maintain firmware version is added for ADAU145X.
-  Master Control port libraries now supports runtime I2C Read/write for multiple slaves. (ADAU145X)
-  DM0, DM1 memory section option is added to the voltage controlled delay algorithm (ADAU145X)
-  Voltage Controlled External SPI delay algorithm is added to the toolbox. (ADAU145X)

.. _bug-fixes-1:

Bug Fixes
^^^^^^^^^

-  Mistakes in algorithm names for various dynamic processors algorithms are corrected.
-  A bug in ADI Virtual down mix which caused the multiple instances of this algorithm to fail is addressed.
-  A bug in ‘Change-IC’ option for Mono-Slew Mux is fixed.
-  Bug in Sequence Window edit which caused the multiple row data to be cleared is fixed.
-  A bug in FIR filter which caused the coefficient load to take significant time is fixed.
-  Bug in ADAU145X RMS table algorithm which caused the value at index 1 to correct is fixed.

3.12.4 Beta/ 3.12 Release
-------------------------

.. _enhancements-2:

Enhancements
^^^^^^^^^^^^

-  Text In filter contains All-Pass, Notch, Band-Pass and Band-Stop filter options.
-  Standard look up tables can be grown for multiple inputs.
-  Standard look up tables input and output formats can be changed either to fractional or integer.
-  High order shelving optimized filter with external and internal gain can accept values lower than -16 dB when using the scaled gain option.
-  Multiple channel signal envelope generator (up to 8 channels) with code optimization.
-  Gain and Initial phase parameters added for Sine Tone, Sawtooth wave, Square wave and triangle wave
-  Value Hold module allows growing the number of channels.
-  Standard Peak compressor with the external detect is added for ADAU145X.
-  Audio signal routers GUI performance is improved when multiple tabs are created.
-  New module is added to read multiple I2C slaves for ADAU145X.
-  Phat-Stereo module is added for ADAU145X
-  A new filter module which does the coefficient calculation in the DSP is added for General Highpass, Lowpass, Bandpass and BandStop (ADAU145X).

.. _bug-fixes-2:

Bug Fixes
^^^^^^^^^

-  Issue with the parameter generation while exporting the system files, for first order filter is fixed.
-  Compiler error created during multiple instance of ‘VAD Accel’ for ADAU145x is corrected.
-  A bug which restricts the DC value to 16 is corrected for floating point processors.
-  Table interpolator copy/paste made the upper value go to 1.01.
-  Table interpolator algorithm did not have an upper or lower limit, resulting in non-desirable output data when out of bounds.
-  EEPROM Properties window now saves parameters and does not ignore them when flashing the EEPROM.
-  EEPROM flashing for ADAU145x now can program I2C memories to addresses at and beyond 0x8000.
-  Corrected mistake in the Peaking Compressors algorithms’ names
-  A bug which creates an exception when First Order is mode is used in the Index Selectable Filter is resolved.
-  Stimulus bug on General 2nd order filter for ADAU145x is resolved.
-  A bug in SuperBass algorithm which causes the output to saturate is resolved for ADAU145x.

.. _beta-3:

3.12.3 Beta
-----------

.. _enhancements-3:

Enhancements
^^^^^^^^^^^^

-  Initial phase can be configured now in Sin, Square, Triangle and Sawtooth wave oscillators for ADAU145x.
-  Audio signal router algorithms are added.
-  ‘Value Hold’ algorithm can hold multiple input channels for ADAU145x.
-  ‘Export System Files’ generates the Netlist information into xml format.
-  External SPI Delay module can now support 24 bit addressable SPI RAMs for ADAU145x.
-  Text In filter’s user control is updated

.. _bug-fixes-3:

Bug Fixes
^^^^^^^^^

-  Maximum and minimum values of linear gain is now calculated depends on the type of core.
-  Compilation error in the NxM mixer for some values of N, M is fixed.
-  Bug in export for the NxM mixer is fixed. (ADAU145X)
-  Copy Paste bug in DC source is fixed.
-  Issue while creating a copy of the module which does not contain an algorithm, is fixed.
-  Misleading info in Combo: RMS + Peak module is corrected.
-  Issue while updating the parameter for High order shelving filter, is fixed.
-  T connection module is updated to restrict the connection between modules from different ICs.
-  Schematic status update is corrected for “Allow Realtime AB Testing” feature.
-  Issue with the FIR filter MIPS calculation is fixed for ADAU144x.

.. _beta-4:

3.12.2 Beta
-----------

.. _enhancements-4:

Enhancements
^^^^^^^^^^^^

-  ADAU1372 has been added to the library.
-  New High Order Shelving filters for 3rd Generation Cores (ADAU144X, ADAU176X)
-  ParametricEQ now supports up to 192 kHz Fs GUI representation.
-  Hilbert Transform, Voice Activity Detector (VAD), Super Bass algorithms are implemented for ADAU145X processor.
-  New version of Dynamics Processors which outputs compressor gain is added
-  Linear Interpolator algorithm is implemented as a growable algorithm for ADAU145X and ADAU144X processors.
-  Support to directly switch the communication protocol from I2C to SPI for ADAU144x

.. _bug-fixes-4:

Bug Fixes
^^^^^^^^^

-  ADAU145X, fix incorrect hold logic for “Max and Hold”, “Max Abs and Hold”, and “Min and Hold” blocks.
-  Reverb algorithm for AD1940.
-  ParametricEQ fixed for first order filter on ADAU145x.
-  Fixed transfer function calculation of Subtraction and Signal Invert modules for ADAU145x

.. _beta-5:

3.12.1 Beta
-----------

.. _enhancements-5:

Enhancements
^^^^^^^^^^^^

-  Save-restore support added for right-click context menu settings (e.g. slew-time, data-memory, and block-size). This update supports preservation of the menu settings during copy/paste, undo/redo, project/cell “Settings”, scripting and “Control UI”.
-  “ADI Surround”, “Beam Forming (fixed)”, “Automatic EQ”, “Crossover Filter (double precision)”, “Pitch Transposer” and “GPIO Conditioning” algorithms implemented for ADAU145X processor
-  New ADAU145x Basic DSP Delay algorithm supports selection between the 2 data memories.
-  Arithmetic Shift operation added for ADAU145x
-  ADAU145x support for 32.0 (“RAW 32bit") format serial audio data, format option is located in right click context menu of inputs and outputs.
-  Holters filter with agnostic GUI.
-  ADAU1772 is SPI ready.

.. _bug-fixes-5:

Bug Fixes
^^^^^^^^^

-  Mid EQ out of index issue caused by opening an SStudio v3.9 or older version project.
-  ADAU1450 register controls user interface fixed

.. _beta-6:

3.12.0 Beta
-----------

.. _enhancements-6:

Enhancements
^^^^^^^^^^^^

-  Support for multi-rate signal flow (multiple sampling rates or block-sizes in a single schematic design window).
-  Multi Tap Gain algorithm implemented for AD194x, ADAU170x, ADAU176x processors.

.. _bug-fixes-6:

Bug Fixes
^^^^^^^^^

-  Level detector with output display for AD1940.
-  Standard RMS Compressor read back indicator worked for AD1940.
-  ADAU145x register window on the routing matrix and serial ports.
-  Parametric EQ cell, low pass and high pass first order filter selection.

3.11.2 Beta/ 3.11 Release
-------------------------

.. _enhancements-7:

Enhancements
^^^^^^^^^^^^

-  SigmaStudio load time performance improvements for 64 bit OS
-  Added right click context menu for copy of “Output Window” text to clipboard
-  Presence of obsolete algorithm code in legacy projects indicated in assembler output window
-  Automatic Volume Control (AVC) implemented for ADAU145x processor
-  N-channel peak compressor implemented for ADAU145X processor
-  Multi Tap Gain algorithm implemented for ADAU145x processor

.. _bug-fixes-7:

Bug Fixes
^^^^^^^^^

-  Standard Peak Dynamic processor fix for ADAU145x to match full range -135dB to +21dB.
-  Memory error for large ADAU145x design using One Shot, Value Cross Detect, or DC Blocker
-  ADAU145x Logic “AB in CD out” condition fixed, GUI was not setting proper algorithm mode
-  Loading “hierarchy board” file caused mouse cursor to disappear

.. _beta-7:

3.11.1 Beta
-----------

.. _enhancements-8:

Enhancements
^^^^^^^^^^^^

-  Transfer function for the two way adder on the ADAU1772 is now implemented.
-  RealTimeDisplay cell now supports ADAU145x data format.
-  Added ADAU1452 NLMS filter algorithm.
-  Mono Dynamics Bass Boost and Adaptive Mixer Dual graph algorithms added for ADAU145x.
-  Configurable SPI memory erase cycle time to support large flash memories for ADAU145x.

.. _bug-fixes-8:

Bug Fixes
^^^^^^^^^

-  ADAU145x Linear interpolator now supports more than 128 points.
-  ADAU145x multiple instances of DC Blocker filter causes exception.
-  ADAU1451 register control routing matrix window fixed.
-  ADAU145x NxM Multiple Ctrl Mixer cell causes exception.
-  ADAU145x External Volume (HW Slew) slew control function and state save/restore fixed.
-  ADAU145x incorrect instruction cycle count estimate for large FIR filters
-  Self boot EEPROM I2C device settings not compatible with ADAU1701/ADAU1772 eval boards.
-  ADAU1772 EEPROM write causes exception.
-  ADAU145x block processing context save/restore added for peripheral math accelerators.
-  ADAU145X rounding mode is now disabled (round to –inf) by default.

.. _beta-8:

3.11.0 Beta
-----------

.. _enhancements-9:

Enhancements
^^^^^^^^^^^^

-  Adding Advanced Pith Shifter DEMO algorithm
-  Adding single precision ParametricEQ.

.. _bug-fixes-9:

Bug Fixes
^^^^^^^^^

-  Export files using CRC and clearing Program memory methods were missing.
-  Fixed the real delay wrong calculated of fractional delay.

3.10.4 Beta / 3.10 Release
--------------------------

.. _enhancements-10:

Enhancements
^^^^^^^^^^^^

-  New multi-tap delay mixer: AD194x, ADAU170x, ADAU176x, ADAU144x
-  New linear value NxM mixer (all processors).
-  ADAU145x algorithms: Standard Compressor, DC Blocking Filter, Pink Noise Filter, Lookup Table (8.24), Pulse Count, Timer, Stop Watch, Envelope, State Machine, MUX w/ slew, Voltage Controlled Delay, Multi-tap Delay, Fractional Delay, Max, Min, One Shot, Value Cross, Value Hold, Abs Max, Master Port Delay, Master Port Writer.
-  ADAU145X framework changes required for silicon Revision D support (backward compatible)

.. _bug-fixes-10:

Bug Fixes
^^^^^^^^^

-  Projects from version 3.5 or earlier would not open in version 3.10
-  Parametric EQ Index Selectable filter on IIR, now it displays correctly all the curves.
-  Fixed the interaction problem between different “One-shot Rise, Reset” block.
-  Fixed “Boost Min” save and restore issue on “General 2nd Order w var Param/Lookup/Slew”.
-  Fixed source-destination reversal of links and hierarchy board input/output distortion due to connections made in reverse direction.
-  Fixed Min and Hold and Max and Hold algorithms.
-  Sequence window, fixed corruption when editing data or bytes when data spans more than 1 line.
-  Fixed ADAU145x Linear Interpolator table not initialized correctly.
-  Fixed ADAU145x index selectable mux, demux and Look-up-table (LUT): offset value “out of range” error in large projects.
-  Fixed ADAU145X NxM mixer algorithm, gain values not downloaded
-  Fixed ADAU145X GPIO algorithm: interrupt protection required

.. _beta-9:

3.10.3 Beta
-----------

.. _enhancements-11:

Enhancements
^^^^^^^^^^^^

-  Added multiple channels FIR and obsolete the old one.
-  Added lower range log look up table which ranged from -90dB to +6 db.
-  ADAU145X framework updated
-  Added no MIPS and no Data usage switch for ADAU1761, ADAU1781 and ADAU144x.

.. _bug-fixes-11:

Bug Fixes
^^^^^^^^^

-  Register window fixes for ADAU1772 on the PGA/ADC tab, all four pop suppression buttons. On Output/Serial Port tab, both the DAC0 and DAC1 gain sliders, and pop suppression buttons under “Headphone Control” section.
-  ADAU1772 Parametric EQ bug when used with a two way mixer.
-  “Export system files” capability for ADAU1772 is now fixed.
-  ADAU1701, ADAU1702, and ADAU1401 had a GPIO option on MP0 and MP6 of TDM8 in and TDM out respectively, which is no longer supported. The register window has been updated accordingly.
-  NxM mixer cell has been modified so that the export files avoid the address repetition.
-  ParametricEQ multiple filter bug for ADAU145x core.

.. _beta-10:

3.10.2 Beta
-----------

.. _enhancements-12:

Enhancements
^^^^^^^^^^^^

-  New DC Input Entry and New Single Volume (Write to Selected parameter) with no MIPS and no Data usage for ADAU1761, ADAU1781 and ADAU144x.
-  Enable / Disable button got bigger for most filters. A new phase shift button was included on the filters.
-  Updated DSP Configuration Window for ADAU145x

.. _bug-fixes-12:

Bug Fixes
^^^^^^^^^

-  Hilbert Transform now works properly for ADAU1701 and AD1940.
-  VCO with phase reset is ready for ADAU1701 and AD1940.
-  Fixed the ADAU1461 I/O problem on digital input 9.
-  Fixed MidEQ Shelving filter downloading coefficients twice.

.. _beta-11:

3.10.1 Beta
-----------

.. _enhancements-13:

Enhancements
^^^^^^^^^^^^

-  New ADAU145X processor
-  Add Standard Dynamics processors for ADAU1701 and AD1940.
-  New Real Time Display and Single Level detector with no MIPS and no Data usage for ADAU144x, and low power DSP.
-  New Stereo and Mono Peak Dynamics Processors with higher range (-90 dB, +24 dB) with and without external detect for ADAU1701 and AD1940.

.. _bug-fixes-13:

Bug Fixes
^^^^^^^^^

-  VCO with reset algorithm for ADAU1701 and AD1940 is fixed.

.. _beta-12:

3.10.0 Beta
-----------

.. _enhancements-14:

Enhancements
^^^^^^^^^^^^

-  New dynamics interpolator with feed forward graph.
-  New no averaging level detectors with and inverse display and speed control.
-  New parameter read back block with no DATA instructions, for ADAU176x, ADAU1781 and ADAU144x.
-  New linear sweep blocks (2 externally triggered and 2 on/off switch).

.. _bug-fixes-14:

Bug Fixes
^^^^^^^^^

-  SigmaStudio load time has been reduced.
-  Pulse generator approximates user’s duty cycle input.

3.9.2 Beta / 3.9 Release
------------------------

.. _enhancements-15:

Enhancements
^^^^^^^^^^^^

-  Export to Linux files now supports XML format. Implementation of Export to Linux files for ADAU1701.
-  Single band level detector supports linear display.
-  New peak dynamics processors with external detect (Mono/Stereo) that supports fast release for low frequencies.

.. _bug-fixes-15:

Bug Fixes
^^^^^^^^^

-  N/A

.. _beta-13:

3.9.1 Beta
----------

.. _enhancements-16:

Enhancements
^^^^^^^^^^^^

-  Single band level detector has now a new graphic adjustable display.
-  Added All-pass selection to “First Order Filters” type in General (2nd Order) Filter
-  Added user selectable phase wrapped/un-wrapped and radians/degrees options in probe window

.. _bug-fixes-16:

Bug Fixes
^^^^^^^^^

-  FIR Filter table is fixed, with all coefficients set to zero except the first.

.. _beta-14:

3.9.0 Beta
----------

.. _enhancements-17:

Enhancements
^^^^^^^^^^^^

-  Extended probe window frequency axis to 96 kHz maximum.
-  Added log lookup table for ADAU170x and ADAU144x.
-  Made simple sub-harmonic support ADAU176x, ADAU1781 and ADAU144x.
-  Added Quad VCO support ADAU1701 and AD1940.
-  Added VCO with flexible phase for ADAU170x and ADAU144x.
-  Added two externally triggered sweeps for ADAU170x and ADAU144x.
-  Added square root approximation for ADAU170x and ADAU144x.
-  Added peak compressor with zero cross for ADAU176x, ADAU1781 and ADAU144x.
-  Added elliptical interpolated IIR low pass filter for ADAU176x, ADAU1781 and ADAU144X.

.. _bug-fixes-17:

Bug Fixes
^^^^^^^^^

-  Change schematic view mouse wheel zoom steps to match the zoom menu zoom step sizes.
-  Decrease font size and add tooltips in the ADAU144X register window to fix readability issues.
-  Optimized schematic linking reduces compile times for large projects

.. _release-1:

3.8.2 / 3.8 Release
-------------------

.. _enhancements-18:

Enhancements
^^^^^^^^^^^^

-  Added optimized sine tone generator which used subroutine.
-  SigmaStudio application was not appearing in the toolbar at launch when opened with a project.
-  Sequence Window download operation was inserting read-back after each write, this is now a user option “Verify on Download” that is disabled by default.

.. _bug-fixes-18:

Bug Fixes
^^^^^^^^^

-  Additional .dspproj file can now be opened from Windows Explorer when SigmaStudio is already running.
-  SigmaStudio application was not appearing in the toolbar at launch when opened with a project.
-  Sequence Window download operation was inserting read-back after each write, this is now a user option “Verify on Download“that is disabled by default.

.. _beta-15:

3.8.1 Beta
----------

.. _enhancements-19:

Enhancements
^^^^^^^^^^^^

-  Added Virtual Control Interface, user customizable system tuning graphical interface.

.. _bug-fixes-19:

Bug Fixes
^^^^^^^^^

-  Fix duplicate parameter naming in “Export System Files” for the Pitch Transpose.
-  Certain projects were set as dirty (i.e. modified) immediately on file open.

3.7.7
-----

.. _enhancements-20:

Enhancements
^^^^^^^^^^^^

-  Windows Administrator privileges are required for installation
-  The option for installing as ‘All Users’ or ‘Just Me’ was removed.
-  The default location of the Sample Scripts and Sample Schematics has changed
-  Automatic Add-Ins: at start-up SigmaStudio will automatically scan all DLL files located in the SigmaStudio installation directly and enable them for use in SigmaStudio. The existing Tools \| Add-Ins Browser can still be used to add external libraries or disable a library.
-  The “Reverb” algorithm’s user interface has been visually redesigned.

.. _bug-fixes-20:

Bug Fixes
^^^^^^^^^

-  Lookup table editor prevents the user to delete text lines accidentally.
-  The bypass and enable of ADAU1373’s PLLA and PLLB were inverted. N div was also inverted.
-  FIR filters now support copy/paste and Hierarchy board save/load. Existing Hierarchy board files must be resaved before the FIR settings will be restored when on hierarchy board load.
-  Hierarchy board load behaviour changed to better support large hierarchy files. Loading a hierarchy board is now a destruction (non-undoable) operation.
-  SignalDetection decay time fixed for ADAU1701 and AD1940.

.. _section-1:

3.7.6
-----

.. _enhancements-21:

Enhancements
^^^^^^^^^^^^

-  Knobs in SigmaStudio support click protection property, tooltip value indicator, and speed control. Value label indicators do not clutter anymore.
-  ADAU1772 included.
-  Added a Mono peak compressor with external detection.

.. _bug-fixes-21:

Bug Fixes
^^^^^^^^^

-  The continuous read check box’s check status of RealTimeDisplay was disturbed.

.. _beta-16:

3.7.5 Beta
----------

.. _enhancements-22:

Enhancements
^^^^^^^^^^^^

-  Added “Pulse Generator” for ADAU176x, ADAU1781, ADAU1701 and AD1940.
-  Made RealTimeDisplay work for the 1701 and 1940.
-  Gain Envelope algorithms moved from “ADI Algorithms” category to “Volume Controls”.
-  ADAU1772 DSP is now added into SigmaStudio environment.

.. _bug-fixes-22:

Bug Fixes
^^^^^^^^^

-  Gen 2nd Order filter is fixed. This will prevent error for unsupported Q values.
-  Index Selectable Independent Multiple Band filter is fixed. Filter editor will now display all the controls in any row of the filter.
-  Index Selectable Independent Multiple Band filter and Index Selectable filters are fixed. The module will not show error message upon removing the last filter while in selected state.
-  Chime algorithm modulation issue. Now is fixed and output a full scale signal.
-  Modified “Pitch Transpose” using UIData serialization.
-  Copy/Paste of block hierarchy board is fixed. This will prevent boards containing block processing modules getting pasted in the sample processing design tab.
-  Copy/Paste of sample hierarchy board is fixed. This will prevent all sub-boards getting pasted in the main design tab.
-  Scripting interface is fixed. This will remove the restrictions in connecting 2 block processing modules using script.

.. _beta-17:

3.7.4 Beta
----------

.. _enhancements-23:

Enhancements
^^^^^^^^^^^^

-  Linear interpolator has added a GUI for intuitive usability.
-  Added “Fractional Delay” controls and algorithms both Voltage Controlled and User Controlled.
-  Added “Pitch Transpose” controls and algorithms both Voltage Controlled and User Controlled.
-  Added a “tiny circle” for “DSP Read Back” to control the cell start/stop continuous read back.
-  Added a “tiny circle” for “FIR Filter” to bypass or enable the filter.
-  Filter stability criteria imposed on "State Variable Filter" controls.
-  More automation APIs added to SigmaStudioServer.
-  Peaking filter boost value of zero (0) automatically zeros filter coefficients; this can now be disabled by defining the following ‘appSettings’ tag in the Application Configuration File:

<appSettings><add key="Disable-Boost-Bypass" value="1" /></appSettings>

.. _bug-fixes-23:

Bug Fixes
^^^^^^^^^

-  N/A

.. _beta-18:

3.7.3 Beta
----------

.. _enhancements-24:

Enhancements
^^^^^^^^^^^^

-  Add a mono super bass.
-  Add a gain output volume control.

.. _bug-fixes-24:

Bug Fixes
^^^^^^^^^

-  TreeToolbox multiple DSP crash fixed.

.. _beta-19:

3.7.2 Beta
----------

.. _enhancements-25:

Enhancements
^^^^^^^^^^^^

-  Sound String algorithm added.
-  Probe – Stimulus data flow efficiency enhanced.

.. _bug-fixes-25:

Bug Fixes
^^^^^^^^^

-  Parametric EQ first order filter coefficients are now generated correctly.

.. _beta-20:

3.6.3 Beta
----------

.. _enhancements-26:

Enhancements
^^^^^^^^^^^^

-  Volume control has new min, max, and step limit values while using it in the linear scale.
-  The installer prompts the option to install as “All Users” or as an “Individual User”.
-  SigmaStudio will no longer use elevation to open.
-  TCP/IP implementation for ADAU1761.

.. _bug-fixes-26:

Bug Fixes
^^^^^^^^^

-  Filter table generator format fix. This will prevent the user to input an unsupported format.

.. _beta-21:

3.6.2 Beta
----------

.. _enhancements-27:

Enhancements
^^^^^^^^^^^^

-  Polar plotter is now part of Basic DSP toolbox.

.. _bug-fixes-27:

Bug Fixes
^^^^^^^^^

-  Fixed bug in 8 channel cross mixer caused when growing the cell by more than one.
-  Export files naming issues on variable declarations were fixed.
-  Standard Dynamics processors attack and hold value issues fixed.
-  ADAU1x61 Signal Path registers had been corrected from a series of GUI components out of their place.

.. _beta-22:

3.6.1 Beta
----------

.. _enhancements-28:

Enhancements
^^^^^^^^^^^^

-  Absolute Max Value, Max Value, and Min Value Algorithms added.
-  RMS table cell extends range from -93 to +3 db. (Before was -93 to 0 dB).
-  RMS table cell has lower and upper limit. Upper limit output is mapped to the +3dB value and lower limit to the -93 db.
-  Index Selectable EQ Cell enhanced its GUI: Now it only displays the row of filters that is selected. It updates the window when selecting different rows. The focus on the add, delete, and show buttons is selected as not focused after moving the mouse pointer away from them.
-  Read/Write and Sequencer window now updates the Register Window.

SigmaStudio 3.5 Release

-  Includes all bug fixes and enhancements from previous SigmaStudio 3.5.x Beta

.. _bug-fixes-28:

Bug Fixes
^^^^^^^^^

-  Optimized filters transfer function is now fixed.
-  SigmaServer external interface fixed to support for Windows7

.. _beta-23:

3.5.7 Beta
----------

.. _enhancements-29:

Enhancements
^^^^^^^^^^^^

-  Two Dimensional Lookup table algorithm has been added.
-  Support for SSM2529.
-  SSM2518 included.
-  ALT+Drag wiring mode, connects all pins in source black to all pins in destination block

.. _bug-fixes-29:

Bug Fixes
^^^^^^^^^

-  Low latency register excluded from sequence download for ADAU1x82
-  General 2nd Order with variable Parameter/Lookup/Slew serialization issue.
-  TreeToolBox Block Processing / Stream Data issue fixed.
-  Lookup Table does not allow empty strings in the table and will not increase the number of points of the system. The only way to increase the number of points is through the main control.
-  When saving as while on Block processing tab the Main form title now updates.
-  NumericTextBox enable/disable back color is now fixed.

.. _beta-24:

3.5.6 Beta
----------

.. _enhancements-30:

Enhancements
^^^^^^^^^^^^

-  Index Independent EQ has now a new control GUI. It depicts a clue description tooltip for each button. It has two extra buttons that adds and removes rows.
-  Lookup Table now is expressed on both linear and dB units.

.. _bug-fixes-30:

Bug Fixes
^^^^^^^^^

-  Fixed transfer function for subtraction library. The TF has its polarity inverted, the code was corrected.
-  ADAU1x61 register window added “User” pre-set on the ALC Pre-sets, fixing a bug where the Left/Right input volumes were disabled.

.. _beta-25:

3.5.5 Beta
----------

.. _enhancements-31:

Enhancements
^^^^^^^^^^^^

-  Added Hoffman Transform.
-  Added quadrature output VCO.
-  Added adaptive beam forming algorithm.

.. _bug-fixes-31:

Bug Fixes
^^^^^^^^^

-  Change in b1 coefficient minimum value for the IIR control.
-  For the AD193x family, on PLL and Clock Control Register 1 the ADC Clock definition was swapped. Now it is reverted and working properly.
-  ADAU1x81 register 0x4010 bit field [2] enable  0 and disable  1.

.. _beta-26:

3.5.4 Beta
----------

.. _enhancements-32:

Enhancements
^^^^^^^^^^^^

-  Real Time Display now supports Y-axis configuration and Format.
-  DB Volume and DB Volume "Compact" with subroutine algorithms for multiple input channels have been added.
-  Text-In and Index Selectable Multiple Band Filters now support Peaking Filter.
-  DC Block filter is now double precision.
-  Compiler Output information for multiple ICs.

.. _section-2:

3.5.4
-----

.. _bug-fixes-32:

Bug Fixes
^^^^^^^^^

-  Sequencer Output Export Files fixed and support for multiple IC sequences.

.. _beta-27:

3.5.2 Beta
----------

.. _enhancements-33:

Enhancements
^^^^^^^^^^^^

-  No need to re-compile “Frozen” schematics. All the download information is stored in the schematic.
-  RMS Dynamics Processors: Capability to switch between Units from dB/s to milliseconds and vice versa.

.. _bug-fixes-33:

Bug Fixes
^^^^^^^^^

-  Fix on the PARAMS.h file from the “Export Output Files” tool.

.. _beta-28:

3.5.1 Beta
----------

.. _enhancements-34:

Enhancements
^^^^^^^^^^^^

-  Micro Controller output files will no longer show “NumBytes_IC_1.dat” or “TxBuffer_IC_1.dat” to reduce redundant output information.
-  All Filters have a new upper frequency limit of 96 kHz.

.. _bug-fixes-34:

Bug Fixes
^^^^^^^^^

-  Made the following modules Obsolete: Optimized Single Precision Filter 2-Channel, Optimized Double Precision Filter 2-Channel.In previous versions these modules auto-assigned non-optimized code for less than 3 biquads in series. The modules were re-added to the library without this automatic feature and will always use the optimized code regardless of how many biquads are in series.

.. _beta-29:

3.5.0 Beta
----------

.. _enhancements-35:

Enhancements
^^^^^^^^^^^^

-  Adding new modules:
-  Optimized Single Precision Filter 1-Channel (ADAU144x, ADAU176x, ADAU178x)
-  Optimized Double Precision Filter 1-Channel (ADAU144x, ADAU176x, ADAU178x)

.. _section-3:

3.4
---

.. _enhancements-36:

Enhancements
^^^^^^^^^^^^

-  Fixed size of General 2nd Order Filters Frequency control to always display 5 digits and Tooltip
-  Incremented Chebyshev ripple from 5 to 10 on 2nd order filters.
-  Added multiply value to Real Time display to scale the signal read back from the DSP.
-  Parametric EQ IIR coefficient window bug fix.
-  Fixed the Hard Clip, Soft Clip, and Advanced Clip algorithms multiple parameter write upon algorithm growth
-  Added the following new algorithms/modules:
-  Bitwise Logic (ADAU144x, ADAU176x, ADAU178x)
-  Linear Interpolator Block no longer supports invalid Number of Points in Table and Serialization fixed for Max/Min saving values when Min saved as 1.0
-  ParametricEQ:
-  When disabling and enabling a filter, sometimes the Boost value goes to zero.
-  Boost value now goes from +30 dB to -100 dB, before it went to -30 db.
-  Added the following new algorithms/modules:
-  Single Band Level Detector Running Average (ADAU144x, ADAU176x, ADAU178x)
-  Single Band Level Detector Direct Read (ADAU144x, ADAU176x, ADAU178x)
-  Added the Real Time Display algorithm, which is a graphical version of the Readback algorithm.
-  Added Signal Detect algorithm and cell
-  Fixed bug on non-programmable IC’s (showing a communication error)
-  HW Configuration and Schematic Tabs are displayed as tabs and not as buttons.

.. _section-4:

3.3.0
-----

.. _enhancements-37:

Enhancements
^^^^^^^^^^^^

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

.. _section-5:

3.2.0
-----

.. _enhancements-38:

Enhancements
^^^^^^^^^^^^

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
-  Capture window and exported uC files display the algorithm hierarchical structure on parameters
-  Read back cell now has a variable timer for continuous reads.
-  Added base address, offset, and algorithm index to be used for report on selected ICs.

.. _bug-fixes-35:

Bug Fixes
^^^^^^^^^

-  Label position bug on save/open fixed.
-  Addins Browser Installer error message upon adding a valid Dll fixed.
-  Chime time/frequency controls now update the algorithm slope.
-  Changed the Chime min and max time.
-  Compressor Graph UI serialization on first point fixed.
-  GUI add/remove drag-point errors were fixed for all chime and envelope algorithms. Misbehaviour of the points was also fixed.
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

.. _section-6:

3.1.20
------

.. _enhancements-39:

Enhancements
^^^^^^^^^^^^

-  Added Self-boot EEPROM \*.hex file export to Sequence Window for custom self-boot configurations.
-  Re-introduce GPIO Conditioning “Up/Down control, index output” algorithm, useful when indexing multiple lookup tables from the same GPIO input.
-  Added a new Context Menu to the read back module that would allow continuous read back with a .5 seconds timer.
-  Fixed a bug found on the control that controls filter’s Q were it allowed values higher than 15 to be written were the application was throwing an exception.

.. _bug-fixes-36:

Bug Fixes
^^^^^^^^^

-  Bug fix for the Running Average Algorithm running on GEN2 processors (AD1940, ADAU170x)
-  Fix ADAU144x Self-boot EEPROM file errors, missing start pulse and core enable registers.
-  Include “DSP Readback” algorithm’s parameter definitions in exported system header files.
-  Add ADAV46xx I2C interfaces for EVAL-ADUSB2 (USBi)

.. _section-7:

3.1.9
-----

.. _enhancements-40:

Enhancements
^^^^^^^^^^^^

-  Added the following new algorithms/modules:
-  Standard Independent RMS (ADAU144x, ADAU176x, ADAU178x)
-  Standard RMS (ADAU144x, ADAU176x, ADAU178x)
-  Value Cross Detection (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
-  Pulse Counter (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
-  Running Average Envelope (AD1940, ADAU170x, ADAU144x, ADAU176x, ADAU178x)
-  Sequence Window: The ability to export independent files for each sequence mode for uC usage.
-  Filter Bypass added to MidEQ Filter

.. _bug-fixes-37:

Bug Fixes
^^^^^^^^^

-  The Envelope Folder in Dynamics Processing was organized in the TreeToolBox to reflect proper naming match to algorithms. [Previously named “RMS” envelope is actually the square output of the RMS envelope – See the help file for more information]
-  Naming fixed for parameters in the Multiple Control mixer. This problem only exhibited itself when multiple instances and growths of the algorithm were present causing a naming conflict violation.
-  Chime GUI. An error occurred while the user put together two drag points. Each drag point will be separated to avoid this common error.

.. _section-8:

3.1.8
-----

.. _enhancements-41:

Enhancements
^^^^^^^^^^^^

-  Added the Index Selectable Independent Multiple Bi-quad Filter algorithm for GEN2
-  1 Channel Single Precision
-  1 Channel Double Precision
-  2 Channel Single Precision
-  2 Channel Double Precision
-  Added Beta version of Phase Response for Transfer Function Window using Probe/Stimuli

SigmaStudio 3.1.8

-  Fixed Square Root algorithm bug for GEN2 parts.
-  Fixed Bug for ADAU170x projects when doing copy/paste operation on controls with parameters, whose new address did not exist in the address map
-  System Export Files bugs fixed, undefined registers and register name conflicts
-  SigmaStudio Script, “ObjectConnect()” function errors fixed.

.. _section-9:

3.1.7
-----

.. _enhancements-42:

Enhancements
^^^^^^^^^^^^

-  Added a filter bypass option on the control for the following filter cells:
-  General (2nd Order)
-  Text-In Filter
-  General (1st Order)
-  Parametric EQ
-  Index Selectable Independent Multiple Band
-  General 2nd Order Index Selectable
-  Added the Index Selectable Independent Multiple Biquad Filter algorithm for GEN

Note: This was incorrectly implemented in 3.1.7. This feature is available in version 3.1.8

.. _bug-fixes-38:

Bug Fixes
^^^^^^^^^

-  Fixed FIR Table Editor window from crashing upon initial open/close without modifying points
-  Fixed opacity Bug on Parametric EQ algorithm upon download

.. _section-10:

3.1.6
-----

.. _enhancements-43:

Enhancements
^^^^^^^^^^^^

-  USBi support for the AD193x codecs (SPI: AD1938/AD1939, I2C: AD1937)
-  USBi support for ADAU1371 (I2C).
-  ADAU1371 Register window for Filter Coefficient calculation.
-  Standard RMS Dynamics Processor: Low Range (-90 - 6 dB); real time signal representation on the dynamic graph; Compressor and Expander Ratio slider; Attack, Hold, and Release are now displayed in milliseconds; and it is available only for Gen 3 DSPs.
-  Chime- Envelope with and without infinite loop.

.. _bug-fixes-39:

Bug Fixes
^^^^^^^^^

-  Export System Files, fixed errors in (\*.h) header file register/param definitions.
-  Non-Modulo fix.

.. _section-11:

3.1.5
-----

.. _bug-fixes-40:

Bug Fixes
^^^^^^^^^

-  Disallow parameter download during project load
-  ADAU144x non-modulo size no longer fixed at 256 data values
-  Gain (RC slew) and 2Channel – Double Precision, Optimized algorithms updated to properly support all GEN3 parts

.. _section-12:

3.1.4
-----

.. _enhancements-44:

Enhancements
^^^^^^^^^^^^

-  Added the following new algorithms/modules:
-  SuperPhat Spatialization
-  Offline Microphone Match
-  Combo Peak/RMS Compressor
-  New Settings Toolbar feature added to support multiple coefficient parameter settings for a schematic project.

SigmaStudio 3.1.4

-  USB Communication channel for ADAU170x fixed to allow proper communication for certain parameters.
-  The Link/Compile/Download sequence was modified to ensure the proper register sequence and sample rate is set for GEN3 ICs.

.. _section-13:

3.1.3
-----

.. _enhancements-45:

Enhancements
^^^^^^^^^^^^

-  The entire library of filters, now support a lower limit center or cutoff frequency of 1Hz on all filter controls. Previous versions of SigmaStudio limited the lowest frequency value that could be entered, but now all filter controls allow values down to 1Hz.

.. _bug-fixes-41:

Bug Fixes
^^^^^^^^^

-  The SW Clickless Mute algorithm was not working properly for the ADAU170x IC. A new method for downloading the proper mute coefficient was implemented to fix this issue.

.. _section-14:

3.1.2
-----

.. _enhancements-46:

Enhancements
^^^^^^^^^^^^

-  Added the following new algorithms/modules:
-  Advanced Soft Clip
-  Square Root (Standard)
-  Square Root (Ultra Precision)

.. _bug-fixes-42:

Bug Fixes
^^^^^^^^^

-  The beginning code for GEN3 cores was updated to reflect a new order of initialization for use with the DAGS. Any new ICs used in projects will have the updated code. Existing schematic projects will have the old default beginning code saved. In order to update to the newest beginning code, drop a new IC in the hardware window of the project schematic and copy the existing algorithms to the new IC.
-  The Parameter Index Lookup Filters have renamed coefficients to avoid a potential bug. This only exhibited itself with more than 10 instantiations of the algorithms each with 10 or more curves. The algorithms affected were:
-  General (2nd Order/Lookup)
-  General 2nd Order Index Selectable – Double and Single Precision
-  General 2nd Order w var Param/Lookup/Slew
-  The Parameter Index Lookup Filter Cell had legacy code that downloaded incorrect filter values to the DSP. This mechanism was updated to ensure proper filter coefficient download.
-  Multiple Link/Compile/Download compilations for GEN3 projects using algorithm code with DAG updates cause intermittent behaviour with coefficient download. A new register sequence is implemented for the Link/Compile/Download operation to ensure proper coefficient operation.

.. _section-15:

3.1.1
-----

.. _enhancements-47:

Enhancements
^^^^^^^^^^^^

-  Added new algorithms to the Index Selectable Independent Multiple Band Filter
-  2 Channel Single Precision
-  1 Channel Double Precision
-  1 Channel Single Precision

.. _bug-fixes-43:

Bug Fixes
^^^^^^^^^

-  The following GEN3 SW Slew Volume algorithms were fixed to support double precision volume handling for low signal levels.
-  Gain (RC Slew)
-  Growable Single Vol Ctrl

.. _section-16:

3.1.0
-----

.. _enhancements-48:

Enhancements
^^^^^^^^^^^^

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

.. _bug-fixes-44:

Bug Fixes
^^^^^^^^^

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

.. _section-17:

3.0.13
------

.. _enhancements-49:

Enhancements
^^^^^^^^^^^^

-  ADAU144x: SigmaDSP Digital Audio Processor with Flexible Audio Routing Matrix
-  Added MONO “Peaking Compressor” algorithm
-  Modified compressors to allow better precision when setting crossover points. This is now done by allowing right clicking on points.
-  Added linear interpolator block.
-  Improved Compiler output reporting for 3rd generation cores.
-  Modified and optimized White noise.
-  Modified 1936 data ram assignation to make better use of memory.
-  Modified Non Modulo Register assignation.
-  Increased maximum number of tabs available for FIR filters.

.. _bug-fixes-45:

Bug Fixes
^^^^^^^^^

-  Microsoft .NET Framework 3.0/3.5 causing SigmaStudio crash at start-up
-  SigmaStudio Sampling Rate, 11.025kHz instead of 11kHz, 22.05kHz instead of 22kHz
-  Feedback algorithm fixed for ADAU144x
-  ADAU1701/1401 register controls updated for compatibility with revised silicon

.. _section-18:

3.0.12
------

.. _enhancements-50:

Enhancements
^^^^^^^^^^^^

-  Improved Index Selectable Filter: Maximum filter count increased to 100, optimized user interface response. Added First Order index selectable filter algorithm.
-  Algorithm optimizations for “General 1st/2nd Order w var Param/Lookup/Slew” and “Parameter Tone with Index Lookup Tables” blocks.
-  Improved Alias block, alias blocks share a common name for easier identification.

.. _bug-fixes-46:

Bug Fixes
^^^^^^^^^

-  Mute block fixed, mute block might not function properly when two mute blocks use contiguous slew ram.
-  1st order High-Pass filter algorithm update, now has constant gain across all frequencies.
-  “On/Off Switch” source set to off on SigmaStudio download.

.. _section-19:

3.0.11
------

.. _enhancements-51:

Enhancements
^^^^^^^^^^^^

-  Add support for ADAV46xx products, Audio Processors for Advanced TV.

.. _bug-fixes-47:

Bug Fixes
^^^^^^^^^

-  Prevent use of comma ‘,’ or space ‘ ‘for numerical decimal place in non-English versions of Windows, only the period character ‘.’ is supported.

.. _section-20:

3.0.10
------

.. _enhancements-52:

Enhancements
^^^^^^^^^^^^

-  Capture window display mode of Address in hexadecimal format and Data in binary format.
-  User Comment font can be modified by right clicking the User Comment block.

.. _bug-fixes-48:

Bug Fixes
^^^^^^^^^

-  Parametric EQ block did not support multi-channel input, the first input was processed and copied to all outputs. Any additional inputs were ignored.
-  Signal Merger and Signal Add blocks had the same algorithm name which introduced errors when using both blocks in the same schematic design. The Signal Merger’s algorithm has been renamed. This change should not affect legacy designs.
-  Alias Block caused errors when using Copy and Paste. Alias blocks could not be renamed.
-  General (2nd Order) “Tone Control” filter equations were not included in the Help file.

.. _section-21:

3.0.9
-----

.. _enhancements-53:

Enhancements
^^^^^^^^^^^^

-  It is no longer required to connect unused block output pin to the “Schematic Terminal” block. Linking will succeed with unconnected output pins.
-  USBSerialConverter (EVAL-ADUSB1) supports SPI communication with all SigmaDSP ICs; previously SPI was only available for AD1940.

.. _bug-fixes-49:

Bug Fixes
^^^^^^^^^

-  Fix ADAU1701/1702 safeload write for EVAL-ADUSB2 (USBi) interface.

.. _section-22:

3.0.7
-----

.. _enhancements-54:

Enhancements
^^^^^^^^^^^^

-  E2PROM download and read/write support added for EVAL-ADUSB2 (USBi) interface.

.. _bug-fixes-50:

Bug Fixes
^^^^^^^^^

-  “DSP Readback” block’s value can be incorrect when reading from a GPIO input.
-  ADAU1702 compiler has incorrect size of 512 for Parameter RAM, should be 1024.

.. _section-23:

3.0.6
-----

.. _bug-fixes-51:

Bug Fixes
^^^^^^^^^

-  Fixed, unexpected error dialogs when compiling projects. Caused by Enhanced schematic status indicator introduced in 3.0.4.

.. _section-24:

3.0.5
-----

.. _bug-fixes-52:

Bug Fixes
^^^^^^^^^

-  Fixed, mouse cursor could disappear in schematic window after compilation.

.. _section-25:

3.0.4
-----

.. _enhancements-55:

Enhancements
^^^^^^^^^^^^

-  Improved low signal level performance for RMS Compressor blocks.
-  Enhanced schematic status indicator, now displays USB communication status. Refer to the “Link/Compile/Download” topic in the SigmaStudio Help for more information.

.. _bug-fixes-53:

Bug Fixes
^^^^^^^^^

-  Fixed compressor Hold and Decay time-constant controls. In previous versions the TC calculation was incorrect, limiting the time-constants to a smaller range than is supported by the compressor algorithms. Depending on Hold and Decay settings, this fix may affect the system response in legacy designs utilizing RMS compressor blocks.

.. _section-26:

3.0.3
-----

.. _enhancements-56:

Enhancements
^^^^^^^^^^^^

-  Parametric EQ: graphical adjustment of filter response, create complex responses using up to 15 cascaded 2nd order filters, available in the Toolbox’s “Filters” category.
-  Crossover: graphical design of 2-way and 3-way crossover filters, selectable crossover types (2nd-8th order Linkwitz-Riley, 2nd-4th order Butterworth, and 2nd-4th order Bessel) , available in the Toolbox’s “Filters” category.

.. _bug-fixes-54:

Bug Fixes
^^^^^^^^^

-  Feedback blocks not functioning properly in some cases.
-  DC Input Entry range limited to -16.0 when set to 28.0 format, should be - (2^27).
-  Links (Wires) between hierarchy boards are not created during paste operation or board file loading.
-  "Delete" command missing in schematic right click menu.

.. _section-27:

3.0.2
-----

.. _bug-fixes-55:

Bug Fixes
^^^^^^^^^

-  Maximum delay value set to 1 sample on during cut/paste or undo/redo operation.
-  Default block name and block “Settings” set during copy/paste are not equivalent, this causes settings malfunction and name conflicts until the project is reloaded.

.. _section-28:

3.0.1
-----

.. _bug-fixes-56:

Bug Fixes
^^^^^^^^^

-  Deleting a hierarchy board’s input or output blocks can reset the control settings of blocks contained in the hierarchy board.
-  Edit Control drawing error when scrolling or displaying overlapped dialogs.
-  Probe Window "Always on top" behaviour is unexpected.

.. _section-29:

3.0.0
-----

.. _enhancements-57:

Enhancements
^^^^^^^^^^^^

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
