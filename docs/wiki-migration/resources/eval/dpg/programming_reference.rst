Programming Reference
=====================

All the functions of a DPG can be accessed through a set of Dynamic-Link Library (DLL) functions. These functions can be accessed via two different Windows® software interface standards:

-  Component Object Model (COM)
-  .NET Framework

When possible, the .NET version should be used instead of the COM version. It provides a more efficient and robust interface.

Class Organization
------------------

The following chart describes the organization of the various interfaces and classes used. A Hardware Interface (sometimes referred to as a "driver") implements the code required to communicate with a specific model of hardware. The Interface which describes what functions these drivers will implement is the `#ihardwareinterface <https://wiki.analog.com/>`_ interface. For each device that is currently connected, a Hardware Device object is created. This object is used to communicate with a specific, physical device. All of these Hardware Device objects abide by the `#ihardwaredevice <https://wiki.analog.com/>`_ interface.

.. image:: https://wiki.analog.com/_media/resources/eval/dpg/class_diagram.png
   :align: center

To connect to a DPG, an instance of the correct Hardware Interface must be created. This instance will provide an array of IHardwareDevice's corresponding to all the attached devices.

Getting Started with COM
------------------------

Unlike the .NET interface, you must connect directly to the appropriate Hardware Interface for the type of hardware you are connecting to. The individual hardware interfaces are registered with COM when the DAC Software Suite is installed. The ProgID of each interface is in the form "AnalogDevices.x", where x is the name of the hardware type. For example, the DPG2 Hardware Interface is registered with COM as AnalogDevices.DPG2.

Once the hardware interface is opened, all the functions listed in the `#ihardwareinterface <https://wiki.analog.com/>`_ interface can be used, as well as the functions in `#ihardwaredevice <https://wiki.analog.com/>`_ for any devices returned by the interface. Additional functions specific to the current hardware may also be available. Using these functions will limit the application to the current device type.

Getting Started with .NET
-------------------------

The AnalogDevices.DPG.Interfaces assembly provides the starting point for communicating with a DPG. This assembly exposes a number of interfaces, as well as the AnalogDevices.DPG.PluginFinder namespace.

The AnalogDevices.DPG.PluginFinder Namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This namespace provides a mechanism for locating the various hardware drivers that might be present on a user's PC. It should generally be used instead of a direct link to the hardware driver, to allow for future expansion.

Two methods are exposed, which both search for hardware drivers:

.. code:: csharp

   IHardwareInterface[] FindPlugins()

This will return an array of all the available Hardware Interfaces (drivers) on the current PC.

.. code:: csharp

   IHardwareInterface[] FindPluginsFiltered(string filter)

This function returns a list of the available Hardware Interfaces whose name matches the filter. For example, to search for only the DPG2 driver, the filter would be set to "DPG2". Using this function with a filter of "\*" is identical to just calling FindPlugins().

IHardwareInterface
------------------

This interface defines the properties and methods that a particular hardware driver will support.

COM Guid:C18A8C19-4DE7-4b2f-9A7F-91AF8BE9C2BD

Properties
~~~~~~~~~~

.. code:: csharp

   string FriendlyName

This property returns a human-readable string describing the hardware driver. It is commonly used when presenting the user with a list of available interfaces to choose from. *Read-Only.*

.. code:: csharp

   IHardwareDevice[] AttachedDevices

AttachedDevices returns an array of Hardware Device objects. Each object corresponds to exactly one physically connected device. If no devices are connected, an array of length zero will be returned. *Read-Only.*

IHardwareDevice
---------------

This interface describes the basic functions that all Hardware Device drivers will support.

COM Guid:108DE7EA-B745-4b45-A90C-0533998CACBD

.. _properties-1:

Properties
~~~~~~~~~~

.. code:: csharp

   int DeviceIndex

The Device Index differentiates between multiple devices of the same type which are connected to the same PC at the same time. For some devices, such as the DPG2, this value is also displayed on the hardware itself. Setting this value is not recommended. The driver will automatically assign indexes as new devices are attached. Note that the indexes are not guaranteed to be the same each time the device is connected, nor are the indexes guaranteed to be sequential. *Read/Write.*

.. code:: csharp

   DataAlignmentE DataAlignment

Specifies if the data presented is MSB aligned or LSB aligned. If the data is LSB aligned, no alignment processing is performed on the data. If the data is MSB aligned, the data is shifted to the left by 16-*DataWidth* bits. *Read/Write.*

.. code:: csharp

   int DataWidth

Specifies the width (resolution) of the data, in bits. *Read/Write.*

.. code:: csharp

   string[] AvailableConfigurations

Lists the names of the available standard configurations for the connected DPG. When using one of the *DownloadConfiguration* methods, the *config* string should exactly match one of the values from this list. *Read-Only.*

.. code:: csharp

   string CurrentConfiguration

Returns the name of the configuration currently loaded into the attached DPG. *Read-Only.*

.. code:: csharp

   double DownloadAsyncProgress

Returns the progress of an asynchronous vector download, as a percentage (0-100). *Read-Only.*

.. code:: csharp

   bool DownloadAsyncComplete

Indicates if an asynchronous vector download is still in progress. *Read-Only.*

.. code:: csharp

   SynchronizationModeE SynchronizationMode

Sets or returns if the attached DPG is set up for multi-DPG synchronization. *Read/Write.*

.. code:: csharp

   PlayModeE PlayMode

Sets or returns if the DPG should continuously loop its vector upon playback, or only play back the vector *PlayCount* times. *Read/Write.*

.. code:: csharp

   ulong PlayCount

When *PlayMode*\ =Count, this value determines how many loops the playback will perform before stopping. *Read/Write.*

.. code:: csharp

   ulong PlayStartAddress

Determines the address in which the vector playback will begin from. Defaults to 0 (beginning of the vector). *Read/Write.*

.. code:: csharp

   ulong PlayCurrentAddress

Indicates the current position of the playback. Note that due to numerous delays inherent in the system, this value should not be used for any synchronization purposes. *Read-Only.*

.. code:: csharp

   ulong PlayLength

Sets or returns the number of points to playback in each loop. This is set automatically when a vector is loaded. *Read/Write.*

.. code:: csharp

   PlayStatusE PlayStatus

Indicates if the DPG is currently playing a vector, or is paused/stopped. *Read-Only.*

.. code:: csharp

   Version ConfigurationVersion

Returns the dotted-decimal version number of the configuration file currently loaded into the DPG. Only valid after a DPG has been configured. *Read-Only.*

.. code:: csharp

   DateTime ConfigurationBuildDate

Returns the build date of the configuration file currently loaded into the DPG. Only valid after a DPG has been configured. *Read-Only.*

.. code:: csharp

   HardwareIdlePattern IdlePattern

Returns a reference to the HardwareIdlePattern object, which is used for altering the idle pattern. *Read-Only.*

.. code:: csharp

   bool DataClockDetected

Indicates if a data clock was detected. *Read-Only.*

.. code:: csharp

   double DataClockFrequency

Indicates the current measured data clock, in hertz (Hz). *Read-Only.*

.. code:: csharp

   HardwareSPIport[] SPIports

Returns an array of HardwareSPIport objects, used to communicate through a SPI port on the DPG. *Read-Only.*

.. code:: csharp

   JESD204Interface JESD204

Returns an object which allows access to JESD204-related functions. Only available on pattern generators which support JESD204, and only when a JESD204 image is loaded into the DPG. *Read-Only.*

Methods
~~~~~~~

.. code:: csharp

   IndividualUnitControl UnitControl(void)

Returns a GUI control which can control all aspects of the DPG. This is the same as what is displayed in DPGDownloader.

.. code:: csharp

   bool DownloadConfiguration(string config)

Downloads a configuration file into the FPGA of the attached DPG. *config* can be either the name of a standard configuration (as provided by *AvailableConfigurations*), or can be the full path to a custom configuration file. This function will not return until the download is complete (blocking call).

.. code:: csharp

   void DownloadConfigurationAsync(string config)

Asynchronously downloads a configuration file into the FPGA of the attached DPG. *config* can be either the name of a standard configuration (as provided by *AvailableConfigurations*), or can be the full path to a custom configuration file. This function will return immediately (non-blocking call).

.. code:: csharp

   bool DownloadConfigurationBytes(byte[] config)

Downloads configuration data into the FPGA of the attached DPG. *config* is an array of bytes, representing the configuration data that should be downloaded. If the data is already in a file, it is recommended that the *DownloadConfiguration* method be used instead. This function will not return until the download is complete (blocking call).

.. code:: csharp

   void DownloadConfigurationBytesAsync(byte[] config)

Asynchronously downloads configuration data into the FPGA of the attached DPG. *config* is an array of bytes, representing the configuration data that should be downloaded. If the data is already in a file, it is recommended that the *DownloadConfigurationAsync* method be used instead. This function will return immediately (non-blocking call).

.. code:: csharp

   void DownloadConfigurationAsyncCancel(void)

Cancels the current asynchronous configuration download.

.. code:: csharp

   bool DownloadDataVectorInt2D(int[,] data, bool ShowProgress)

Downloads a 2D array of integers. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadDataVectorDouble2D(double[,] data, bool ShowProgress)

Downloads a 2D array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadDataVectorInt1D(int[] data, bool ShowProgress)

Downloads an array of integers. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadDataVectorDouble1D(double[] data, bool ShowProgress)

Downloads an array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadInterleavedVectorInt1D(int[] data, int channels, bool ShowProgress)

Downloads an interleaved array of integers. Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadInterleavedVectorInt2D(int[,] data, int channels, bool ShowProgress)

Downloads an interleaved array of integers (only the first column/row of data is considered). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadInterleavedVectorDouble1D(double[] data, int channels, bool ShowProgress)

Downloads an interleaved array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   bool DownloadInterleavedVectorDouble2D(double[,] data, int channels, bool ShowProgress)

Downloads an interleaved array of doubles (only the first column/row of data is considered). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will not return until the download is complete (blocking call).

.. code:: csharp

   void DownloadDataVectorAsyncInt2D(int[,] data, bool ShowProgress)

Asynchronously downloads a 2D vector of integers. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadDataVectorAsyncDouble2D(double[,] data, bool ShowProgress)

Asynchronously downloads a 2D array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadDataVectorAsyncInt1D(int[] data, bool ShowProgress)

Asynchronously downloads an array of integers. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadDataVectorAsyncDouble1D(double[] data, bool ShowProgress)

Asynchronously downloads an array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadInterleavedVectorAsyncInt1D(int[] data, int channels, bool ShowProgress)

Asynchronously downloads an interleaved array of integers. Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadInterleavedVectorAsyncInt2D(int[,] data, int channels, bool ShowProgress)

Asynchronously downloads an interleaved array of integers (only the first column/row of data is considered). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadInterleavedVectorAsyncDouble1D(double[] data, int channels, bool ShowProgress)

Asynchronously downloads an interleaved array of doubles. If all the values of the array are less than 1, each value will be multiplied by the digital full-scale value (computed from *DataWidth*). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadInterleavedVectorAsyncDouble2D(double[,] data, int channels, bool ShowProgress)

Asynchronously downloads an interleaved array of doubles (only the first column/row of data is considered). Every *channels*-th point will be sent to the first data port on the DPG, every (*channels*\ +1)-th point will be sent to the second data port, and so on. Setting *ShowProgress* to true will show a pop-up progress bar during the download. This method will return immediately (non-blocking call).

.. code:: csharp

   void DownloadDataVectorAsyncCancel(void)

Cancels an in-progress asynchronous vector download.

.. code:: csharp

   double[,] UploadDataVector(int points)

Reads *points* points from the DPG's memory, and returns a 2D array of double. This is intended as a debug function and may not function as expected.

.. code:: csharp

   void StartPlayback(void)

Begins playback of the data vector.

.. code:: csharp

   void PausePlayback(void)

Pauses playback of the data vector. When started again with *StartPlayback*, playback will resume at the point in which it was stopped.

.. code:: csharp

   void StopPlayback(void)

Stops playback. When playback is started again with *StartPlayback*, playback will begin from *PlayStartAddress*.

Events
~~~~~~

.. code:: csharp

   DownloadConfigurationAsyncCompleted

This event is fired when an asynchronous configuration download has completed.

.. code:: csharp

   DownloadConfigurationStatusUpdate

This event is fired when the status (percent complete) of an asynchronous configuration download changes.

.. code:: csharp

   DownloadDataVectorAsyncCompleted

This event is fired when an asynchronous data vector download has completed.

.. code:: csharp

   DownloadDataVectorStatusUpdate

This event is fired when the status (percent complete) of an asynchronous data vector download changes.

.. code:: csharp

   DownloadDataVectorError

This event is fired when an error occurs during data vector download.

IHardwareIdlePattern
--------------------

This interface describes the properties and methods used to read, alter, and enable the Idle Pattern feature of the DPG.

COM Guid: 2EB6E57E-DCC1-4f48-B0CC-4FDD8E28759A

.. _properties-2:

Properties
~~~~~~~~~~

.. code:: csharp

   bool Enabled

This property enables or disables the Idle Pattern. When enabled (Enabled = true), the Idle Pattern will be played while the DPG isn't playing a vector. The Idle Pattern itself can be set regardless of the value of this property. *Read/Write.*

.. code:: csharp

   int[] Pattern

The Idle Pattern is set or retrieved as an array of integer values. When enabled, the Idle Pattern feature will loop through these values while the DPG is not playing out a vector. *Read/Write.*

.. _methods-1:

Methods
~~~~~~~

.. code:: csharp

   void SetPatternInt1D(int[] pattern)

This method is identical to setting the property Pattern. It is provided for use in applications which cannot set array properties.

.. code:: csharp

   void SetPatternInt2D(int[,] pattern)

This method is identical to setting the property Pattern. It is provided for use in applications which cannot set array properties.

JESD204Interface
----------------

Provides access to the JESD204 capabilities of a pattern generator.

.. _properties-3:

Properties
~~~~~~~~~~

.. code:: csharp

   int FramerCount

Gets or sets the number of framers in the current DPG setup.

.. code:: csharp

   JESD204Framer[] Framers

Returns an array of JESD204Framer objects, which is the primary interface to the hardware framers inside the DPG.

.. code:: csharp

   int LaneCount

Gets or sets the maximum number of lanes that can be utilized in this setup across all framers.

.. code:: csharp

   JESD204Lane[] Lanes

Returns an array of JESD204Lane objects, which provides access to individual lane features.

JESD204Framer
-------------

Provides access to one (of one or more) JESD204 framers inside the DPG.

Enumerations
~~~~~~~~~~~~

================ ==== ==================================================
eJESD204Revision      
================ ==== ==================================================
\                PreA The original revision of the JESD204 specification
\                A    The JESD204A revision
\                B    The JESD204B revision
================ ==== ==================================================

+-----------+-----------+--------------------------------------------------------+
| eSubclass |           |                                                        |
+===========+===========+========================================================+
|           | Subclass0 | JESD204B Subclass 0 (No deterministic latency)         |
+-----------+-----------+--------------------------------------------------------+
|           | Subclass1 | JESD204B Subclass 1 (High-Speed Deterministic Latency) |
+-----------+-----------+--------------------------------------------------------+
|           | Subclass2 | JESD204B Subclass 2 (Low-Speed Deterministic Latency)  |
+-----------+-----------+--------------------------------------------------------+

.. _properties-4:

Properties
~~~~~~~~~~

.. code:: csharp

   eJESD204Revision JESD204Revision

Gets or sets the revision of the JESD204 specification to use. *Read-Write.*

.. code:: csharp

   eSubclass Subclass

Gets or sets the JESD204B subclass used. *Read-Write.*

.. code:: csharp

   int L

Gets or sets the JESD204 parameter L *Read-Write.*

.. code:: csharp

   int F

Gets or sets the JESD204 parameter F *Read-Write.*

.. code:: csharp

   int K

Gets or sets the JESD204 parameter K *Read-Write.*

.. code:: csharp

   int N

Gets or sets the JESD204 parameter N *Read-Write.*

.. code:: csharp

   int Np

Gets or sets the JESD204 parameter Np *Read-Write.*

.. code:: csharp

   int M

Gets or sets the JESD204 parameter M *Read-Write.*

.. code:: csharp

   int S

Gets or sets the JESD204 parameter S *Read-Write.*

.. code:: csharp

   bool HD

Gets or sets the JESD204 parameter HD *Read-Write.*

.. code:: csharp

   bool Scrambling

Turns on or off JESD204 scrambling *Read-Write.*

.. _methods-2:

Methods
~~~~~~~

.. code:: csharp

   void DownloadDataAsync(UInt16[][] DataVectors, bool ShowProgress)

Downloads data asynchronously to the memory in the pattern generator for playback to the framer. The first dimension of DataVectors should be M long. ShowProgress indicates if a status bar should be displayed during the download process.

.. code:: csharp

   void DownloadData(UInt16[][] DataVectors, bool ShowProgress)

Downloads data synchronously to the memory in the pattern generator for playback to the framer. The first dimension of DataVectors should be M long. ShowProgress indicates if a status bar should be displayed during the download process.

JESD204Lane
-----------

Provides access to one (of one or more) JESD204 physical lanes inside the DPG.

.. _properties-5:

Properties
~~~~~~~~~~

.. code:: csharp

   bool InvertPolarity

When true, the polarity of the differential pair is reversed (effectively swapping P and N) *Read-Write.*

AnalogDevices.DPG.Interfaces.HardwareTypes Namespace
----------------------------------------------------

.. _enumerations-1:

Enumerations
~~~~~~~~~~~~

+-----------+-------+-----------------------------------------------------------------+
| PlayModeE |       |                                                                 |
+===========+=======+=================================================================+
|           | Loop  | The data vector will be looped continuously.                    |
+-----------+-------+-----------------------------------------------------------------+
|           | Count | The data vector will only be played a specific number of times. |
+-----------+-------+-----------------------------------------------------------------+

+-------------+---------+--------------------------------------------------------------------------------------+
| PlayStatusE |         |                                                                                      |
+=============+=========+======================================================================================+
|             | Stopped | The playback is stopped or paused. If enabled, the idle vector is currently playing. |
+-------------+---------+--------------------------------------------------------------------------------------+
|             | Playing | The data vector in the DPG's memory is currently being played.                       |
+-------------+---------+--------------------------------------------------------------------------------------+

+----------------------+--------+-----------------------------------------------------------------------+
| SynchronizationModeE |        |                                                                       |
+======================+========+=======================================================================+
|                      | Single | Do not synchronize to other DPGs.                                     |
+----------------------+--------+-----------------------------------------------------------------------+
|                      | Master | This DPG generates timing signals, to be received by other DPGs.      |
+----------------------+--------+-----------------------------------------------------------------------+
|                      | Slave  | This DPG will wait for timing signals to be received from the Master. |
+----------------------+--------+-----------------------------------------------------------------------+

+----------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| DataAlignmentE |             |                                                                                                                                                          |
+================+=============+==========================================================================================================================================================+
|                | MSB_Aligned | The MSB of the data is always positioned at the MSB of the data port. Data which is less than the width of the port will be left-shifted.                |
+----------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
|                | LSB_Aligned | The LSB of the data is always at the LSB of the data port (bit 0). Data which is less than the width of the port will have 0s placed in any unused bits. |
+----------------+-------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

DPG2-Specific Features
----------------------

Default Configurations
~~~~~~~~~~~~~~~~~~~~~~

The following are the default configurations that ship with the DPG2:

+-------------------+-----------------------------------------------------------------------------------------+
| Name              | Description                                                                             |
+===================+=========================================================================================+
| LVDS (DCO)        | LVDS Signaling, Data Clock provided to DPG2 via main connector (Extended Voltage Swing) |
+-------------------+-----------------------------------------------------------------------------------------+
| LVDS (DCO) Std.   | LVDS Signaling, Data Clock provided to DPG2 via main connector (Standard Voltage Swing) |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-3.3V (SMA) | 3.3V LVCMOS Signaling, Data Clock provided to DPG2 via SMA jacks                        |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-2.5V (SMA) | 2.5V LVCMOS Signaling, Data Clock provided to DPG2 via SMA jacks                        |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-1.8V (SMA) | 1.8V LVCMOS Signaling, Data Clock provided to DPG2 via SMA jacks                        |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-3.3V (DCO) | 3.3V LVCMOS Signaling, Data Clock provided to DPG2 via main connector                   |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-2.5V (DCO) | 2.5V LVCMOS Signaling, Data Clock provided to DPG2 via main connector                   |
+-------------------+-----------------------------------------------------------------------------------------+
| LVCMOS-1.8V (DCO) | 1.8V LVCMOS Signaling, Data Clock provided to DPG2 via main connector                   |
+-------------------+-----------------------------------------------------------------------------------------+

.. _properties-6:

Properties
~~~~~~~~~~

.. code:: csharp

   eFrameSyncMode FrameSyncMode

This property determines what the second data clock input (DCI) line will be. Under normal operation (FrameSyncMode=None), the second DCI is the normal data clock. When FrameSyncMode is any other mode, the second DCI is a divided-down version of the data clock, suitable for use as a frame sync signal for some parts. *Read/Write.*

.. _enumerations-2:

Enumerations
~~~~~~~~~~~~

+----------------+----------+----------------------------------------------------------------------------------+
| eFrameSyncMode |          |                                                                                  |
+================+==========+==================================================================================+
|                | None     | The second DCI line will be a standard clock signal.                             |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_2    | The second DCI line will be the DCO clock divided by 2                           |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_4    | The second DCI line will be the DCO clock divided by 4                           |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_8    | The second DCI line will be the DCO clock divided by 8                           |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_16   | The second DCI line will be the DCO clock divided by 16                          |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_32   | The second DCI line will be the DCO clock divided by 32                          |
+----------------+----------+----------------------------------------------------------------------------------+
|                | DCI_64   | The second DCI line will be the DCO clock divided by 64                          |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot1 | The second DCI line will be asserted for 1 DCO cycle after playback is started.  |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot2 | The second DCI line will be asserted for 2 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot3 | The second DCI line will be asserted for 3 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot4 | The second DCI line will be asserted for 4 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot5 | The second DCI line will be asserted for 5 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot6 | The second DCI line will be asserted for 6 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+
|                | OneShot7 | The second DCI line will be asserted for 7 DCO cycles after playback is started. |
+----------------+----------+----------------------------------------------------------------------------------+

DPG3-Specific Features
----------------------

QBF (Implementation of JESD204Framer)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the base implementation of JESD204Framer, this class also exposes:

.. _enumerations-3:

Enumerations
^^^^^^^^^^^^

+-------------+----------+----------------------------------------------------------------+
| eSyncSelect |          |                                                                |
+=============+==========+================================================================+
|             | Internal | Drive Sync from an internal data bit                           |
+-------------+----------+----------------------------------------------------------------+
|             | External | Use the Sync line provided from the connected evaluation board |
+-------------+----------+----------------------------------------------------------------+

.. _properties-7:

Properties
^^^^^^^^^^

.. code:: csharp

   bool Reset

Holds the framer in reset when true *Read-Write.*

.. code:: csharp

   eSyncSelect SyncSelect

Selects between the external (hardware) Sync line, or an internally generated sync state. *Read-Write.*
