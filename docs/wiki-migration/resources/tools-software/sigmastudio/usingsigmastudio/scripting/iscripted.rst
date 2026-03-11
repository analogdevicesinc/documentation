:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

IScripted Interface
===================

Analog.SStudioScripting.IScripted is contained in a .NET assembly, BaseLib.dll, installed in the SigmaStudio folder.

Script window can be used to run scripts using the Iscripted interface.


|image1|

Return Type
-----------

The interface defines an integer return type, “HResult”, as follows:

.. code:: csharp

   HResult.S_OK = 0
   HResult.E_FAILED = 1
   HResult.E_INVALID_ARGS = 2
   HResult.E_EXCEPTION = 3

Project File Interface
----------------------

The following functions can be used to interface with a project file.

Create
~~~~~~

Create a new project file

.. code:: csharp

   HResult ProjectNew();

The function takes no parameter

Open
~~~~

Open a project file from disk

.. code:: csharp

   HResult ProjectOpen( string filename );

*filename* -> A fully qualified file path

Save/Save As
~~~~~~~~~~~~

Save the Active project file

.. code:: csharp

   HResult ProjectSave();

The function takes no parameter

Save a specific project file

.. code:: csharp

   HResult ProjectSave( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Save as the Active project file

.. code:: csharp

   HResult ProjectSaveAs( string saveAsFilename );

*saveAsFilename* -> A new file name or fully qualified path

Save as a specific project file

.. code:: csharp

   HResult ProjectSaveAs( string projectName, string saveAsFilename );

*projectName* -> An open project file’s name or fully qualified path

*saveAsFilename* -> The new file name or fully qualified path

Close
~~~~~

Close the Active project file

.. code:: csharp

   HResult ProjectClose();

Close a specific project file

.. code:: csharp

   HResult ProjectClose( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Set Project as active
~~~~~~~~~~~~~~~~~~~~~

Set a project as the active project

.. code:: csharp

   HResult ProjectSetActive( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Link
~~~~

Link the active Schematic

.. code:: csharp

   HResult ProjectLink();

The function takes no parameter

Link and compile the active Schematic

.. code:: csharp

   HResult ProjectLinkCompile();

The function takes no parameter

Link and compile the active Schematic

.. code:: csharp

   HResult ProjectLinkCompile( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Link, compile and download the active Schematic

.. code:: csharp

   HResult ProjectLinkCompileDownload();

The function takes no parameter

Link, compile and download a specific project file

.. code:: csharp

   HResult ProjectLinkCompileDownload( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Others
~~~~~~

Set the "New Item Sample Rate" (Schematic Sampling Rate) for the active project

.. code:: csharp

   HResult DesignSetSamplingRate( int samplingRate );

Propagate Schematic Sampling Rate

.. code:: csharp

   HResult DesignPropagateSamplingRate();

The function takes no parameter

Toggle Schematic Freeze On/Off

.. code:: csharp

   HResult DesignToggleSchematicFreeze( string password );

*password* -> Schematic freeze password

Set the activate hierarchy board in the current Schematic

.. code:: csharp

   HResult DesignSetActiveBoard( string boardName );

*boardName* -> Board name in the active Schematic

Export the system files of the active Schematic

.. code:: csharp

   HResult ProjectExportSystemFiles ( string fullyQualifiedFileName );

*fullyQualifiedFileName* -> fully qualified path of the system file without the extension

Build Plug-In DLL using Algorithm Designer

.. code:: csharp

   HResult BuildExternalModule ( string ICName, string fullyQualifiedProjectName, string fullyQualifiedLibraryName );

*ICName* -> Friendly name of DSP(IC) for example "IC 1" or "IC 2"

*fullyQualifiedProjectName* -> fully qualified path of designer project file

*fullyQualifiedLibraryName* -> fully qualified path of the output DLL

Note: The DSP IC has to be there in new schematic window before calling this API.

For example,

HResult eResult = HResult.S_OK;

sigmastudio.ProjectNew();

sigmastudio.ObjectInsert( "ADSP-214xx" );

eResult = sigmastudio.BuildExternalModule("IC 1", "C:\\\\Analog Devices\\\\SoftwareModules\\\\SigmaStudioForSHARC-SH-Rel2.2.0\\\\Target\\\\ExtModules\\\\Biquad\\\\adi_Biquad.ssg", "C:\\\\Analog Devices\\\\SoftwareModules\\\\SigmaStudioForSHARC-SH-Rel2.2.0\\\\Target\\\\ExtModules\\\\Biquad\\\\adi_biquad.dll");

Set the “Schematic Block Size” of IC and Algorithms belonging to the IC for the active project

.. code:: csharp

   HResult DesignSetBlockSize(string ICName, int nSize);

*ICName* -> Friendly name of DSP(IC)

*nSize* -> The Schematic Block Size given as ‘nSize’ will be set to all Modules/Algorithms belonging to the IC corresponding to the ‘ICName’. The Schematic Block Size (nSize) should be greater than 8 and a multiple of 8.

Register/Parameter Interface
----------------------------

Functions for working with the registers and parameters are listed below.

Register Write
~~~~~~~~~~~~~~

Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( int numOfBytesToWrite, byte[] dataToWrite, int protocol, int chipAddress, int writeAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

*numOfBytesToWrite* -> Number of bytes in 'dataToWrite' to write to the dsp

*dataToWrite* -> The data to write, byte array of length numOfBytesToWrite

*protocol* -> The protocol to transfer the data, SPI = 1 and I2C = 0

*chipAddress* -> I2C or SPI address

*writeAddress* -> The register address to write

*addressWidth* -> The width of the register address to write

*registerByteLength* -> The byte length of the register to write

*communicationChannel* -> The interface for communication, USBI = 0 and AARDVARK = 1

*ICType* -> The type of the IC, ADAU145x/ADAU146x = 0, ADSP-214xx = 1, ADSP-SC5xx/ADSP-215xx = 2

Note :- Refer this link for example script :doc:`/wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/iscripted_samples`

Write data to a register

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int writeAddress,int writeNumberBytes, long dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The register address to write

*writeNumberBytes* -> Number of bytes in 'dataToWrite' to write to the dsp

*dataToWrite* -> The data to write (long == 64bit max data)

Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int deviceAddress, int writeAddress, int writeNumberBytes, long dataToWrite );

*ICName* -> Friendly name of DSP(IC)

*deviceAddress* -> I2C or SPI address

*writeAddress* -> The register address to write

*writeNumberBytes* -> Number of bytes in 'dataToWrite' to write to the dsp

*dataToWrite* -> The data to write (long == 64bit max data)

Write data to a register, data specified as a byte array

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int writeAddress,int writeNumberBytes, byte[] dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The register address to write

*writeNumberBytes* -> Number of bytes in 'dataToWrite' to write to the dsp

*dataToWrite* -> The data to write, byte array of length writeNumberBytes

Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int deviceAddress, int writeAddress,int writeNumberBytes, byte[] dataToWrite );

*ICName* -> Friendly name of DSP(IC)

*deviceAddress* -> I2C or SPI address

*writeAddress* -> The register address to write

*writeNumberBytes* -> Number of bytes in 'dataToWrite' to write to the dsp

*dataToWrite* -> The data to write, byte array of length writeNumberBytes

Write safeload register

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int safeloadRegister,long dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

"safeloadRegister” = Regsiter address to safeload

*dataToWrite* -> Data to write to the safeload register (5Bytes)

Write multiple contiguous safeload registers

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int safeloadRegister,int writeNumberBytes, Byte[] dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*safeloadRegister* -> Regsiter address to safeload

*writeNumberBytes* -> Number of data bytes in dataToWrite

*dataToWrite* -> Data to write to the safeload register (5Bytes)

Write multiple safeload registers

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int[] writeAddresses,int[] writeNumberBytes, byte[] dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddresses* -> Array of addresses to safeload

*writeNumberBytes* -> Write bytes per address (for each writeAddresses entry)

*dataToWrite* -> Data array to write to the safeload registers

Register Read
~~~~~~~~~~~~~

Read data to a register from specific device address

.. code:: csharp

   HResult ICRegisterRead( int numOfBytesToRead, byte[] dataRead, int protocol, int chipAddress, int readAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

*numOfBytesToRead* -> Number of bytes to read from the dsp

*dataRead* -> Read the data from register

*protocol* -> The protocol to transfer the data, SPI = 1 and I2C = 0

*chipAddress* -> I2C or SPI address

*readAddress* -> The address of register to read the data

*addressWidth* -> The width of the register address to write

*registerByteLength* -> The byte length of the register to write

*communicationChannel* -> The interface for communication, USBI = 0 and AARDVARK = 1

*ICType* -> The type of the IC, ADAU145x/ADAU146x = 0, ADSP-214xx = 1, ADSP-SC5xx/ADSP-215xx = 2

Note :- Refer this link for example script :doc:`/wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/iscripted_samples`

Read data from a register, read value returned in method parameter

.. code:: csharp

   HResult ICRegisterRead( string ICName, int readAddress, int readNumberBytes,out long bytesRead );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

*bytesRead* -> Return data if read is successful

Read data from a register, specific device address

.. code:: csharp

   HResult ICRegisterRead( string ICName, int deviceAddress, int readAddress, int readNumberBytes, out long bytesRead );

*ICName* -> Friendly name of DSP(IC)

*deviceAddress* -> I2C or SPI address

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

*bytesRead* -> Return data if read is successful

Read data from a register, data as byte array

.. code:: csharp

   HResult ICRegisterRead( string ICName, int readAddress, int readNumberBytes, ref byte[] bytesRead );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

*bytesRead* -> Return data if read is successful

Read data from a register, specific device address

.. code:: csharp

   HResult ICRegisterRead( string ICName, int deviceAddress, int readAddress, int readNumberBytes, ref byte[] bytesRead );

*ICName* -> Friendly name of DSP(IC)

*deviceAddress* -> I2C or SPI address

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

*bytesRead* -> Return data if read is successful

Read data from a register, read value is return type

.. code:: csharp

   long ICRegisterRead( string ICName, int readAddress, int readNumberBytes );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

Read buffer of data from a register, read value array returned

.. code:: csharp

   byte[] ICRegisterRead( string ICName, int readAddress, int readNumberBytes, ref bool bRet );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The register address to read

*readNumberBytes* -> Number of bytes to read

*ret* -> Did the read succeed

Parameter Write
~~~~~~~~~~~~~~~

Write parameter data, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*valToWrite* -> Parameter data value to write

Write parameter data, specifying target fixed-point format and parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string icName, string paramName, int intbits, int fracbits, float valToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*paramName* -> The parameter name to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*valToWrite* -> Parameter data value to write

Write parameter data array, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int intbits, int fracbits, int writeNumParams, float[] valsToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*writeNumParams* -> Number of values in valsToWrite

*valsToWrite* -> Parameter data values to write

Write parameter data array, specifying target fixed-point format and parameter name instead of parameter address.

.. code:: csharp

    HResult ICParameterWrite(string icName, string paramName, int intbits, int fracbits, int writeNumParams, float[] valsToWrite)

*ICName* -> Friendly name of DSP(IC) to write to

*paramName* -> The parameter name to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*writeNumParams* -> Number of values in valsToWrite

*valsToWrite* -> Parameter data values to write

Write parameter data, floating point value

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, float valToWrite )

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*valToWrite* -> Parameter data value to write

Write parameter data as floating point value using parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string ICName, string paramName, float valToWrite )

*ICName* -> Friendly name of DSP(IC) to write to

*paramName* -> The parameter name to begin writing data

*valToWrite* -> Parameter data value to write

Write multiple contiguous parameters, floating point value.

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int writeNumParams, float[] valsToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*writeNumParams* -> Number of values in valsToWrite

*valsToWrite* -> Parameter data values to write

Write multiple contiguous parameters as floating point value using parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string ICName, string paramName, int writeNumParams, float[] valsToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*paramName* -> The parameter name to begin writing data

*writeNumParams* -> Number of values in valsToWrite

*valsToWrite* -> Parameter data values to write

Safeload parameter data, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*valToWrite* -> Parameter data value to write

Safeload parameter data array, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int intbits, int fracbits, int writeNumParams, float[] dataToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*writeNumParams* -> Number of values in valsToWrite

*dataToWrite* -> Parameter data values to write

Write parameter data via safeload, floating point value

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, float valToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*writeNumParams* -> Number of values in valsToWrite

*valToWrite* -> Parameter data value to write

Write multiple parameters via safeload, floating point values

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int writeNumParams, float[] valsToWrite );

*ICName* -> Friendly name of DSP(IC) to write to

*writeAddress* -> The parameter address to begin writing data

*writeNumParams* -> Number of values in valsToWrite

*valsToWrite* -> Parameter data values to write

Load comma-delineated byte data from a text file at a particular parameter/parameter

.. code:: csharp

   HResult ICLoadDataFile( string ICName, string filename, int writeAddress );

*ICName* -> Friendly name of DSP(IC) to write to

*filename* -> fully qualified filename of data file to load

*writeAddress* -> The parameter address to begin writing data

Parameter Read
~~~~~~~~~~~~~~

Read fixed-point parameter data, read value returned as float

.. code:: csharp

   float ICParameterRead( string ICName, int readAddress, int intbits, int fracbits );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The parameter address to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

Read fixed-point parameter data using parameter name, read value returned as float

.. code:: csharp

   float ICParameterRead( string ICName, string paramName, int intbits, int fracbits );

*ICName* -> Friendly name of DSP(IC) to read from

*paramName* -> The name of the parameter to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

Read data from a parameter, data returned as float

.. code:: csharp

   HResult ICParameterRead( string ICName, int readAddress, int intbits,int fracbits, out float valRead );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The parameter address to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*valRead* -> returned read value

Read fixed-point parameter data array, read values returned as float[]

.. code:: csharp

   float[] ICParameterRead( string ICName, int readAddress, int intbits, int fracbits, int readNumParams, ref bool bRet );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The parameter address to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*readNumParams* -> Number of values to read

*bRet* -> result, true if read was successful asdf

Read fixed-point parameter data array using the parameter name, read values returned as float[]

.. code:: csharp

   float[] ICParameterRead( string ICName, string paramName, int intbits, int fracbits, int readNumParams, ref bool bRet );

*ICName* -> Friendly name of DSP(IC) to read from

*paramName* -> The name of the parameter to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*readNumParams* -> Number of values to read

*bRet* -> result, true if read was successful asdf

Read fixed-point parameter data array, read values returned in float[]

.. code:: csharp

   HResult ICParameterRead( string ICName, int readAddress, int intbits, int fracbits, int readNumParams, ref float[] valsRead );

*ICName* -> Friendly name of DSP(IC) to read from

*readAddress* -> The parameter address to read

*intbits* = number of integer (magnitude) bits *fracbits* -> number of fraction bits

*readNumParams* -> Number of values to read

*valsRead* -> returned read values

Parameter Address
~~~~~~~~~~~~~~~~~

API returns all the parameters' name and addresses for a IC in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, out string[] names, out int[] addresses);

*icName* -> Friendly name of DSP(IC) to read from

*names* -> Returns the array of parameters for the IC in the current schematic.

*addresses* Returns the array of parameter addresses corresponding to names[].

API returns all the parameters' name and addresses for a cell/module in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, string cellName, out string[] names, out int[] addresses);

*icName* -> Friendly name of DSP(IC) to read from

*cellName* -> Cell/Module's name in the schematic.

*names* -> Returns the array of parameters for the IC in the current schematic.

*addresses* Returns the array of parameter addresses corresponding to names[].

API returns all the parameters' name and addresses for a cell/module in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, object cellObject, out string[] names, out int[] addresses);

*icName* -> Friendly name of DSP(IC) to read from

*cellObject* -> Cell/Module's object.

*names* -> Returns the array of parameters for the IC in the current schematic.

*addresses* Returns the array of parameter addresses corresponding to names[].

API returns the parameter's address for given parameter name

.. code:: csharp

   HResult ICGetParamAddress(string icName, string paramName, out int address);

*icName* -> Friendly name of DSP(IC) to read from

*paramName* -> Parameter name.

*address* -> Returns the address of the parameter.

API returns the parameter's name for given parameter address

.. code:: csharp

   HResult ICGetParamName(string icName, int address, out string paramName);

*icName* -> Friendly name of DSP(IC) to read from

*address* -> Parameter address.

*paramName* -> Returns the name of the parameter.

Insert
------

The functions listed below are used to insert Schematic objects into a board.

Insert an object into the active project, returns object reference

.. code:: csharp

   object ObjectInsert( string typeName );

*typeName* -> object description (toolbox name)

Insert an object into a specific open project, returns object reference

.. code:: csharp

   object ObjectInsert( string projectName, string typeName );

*projectName* -> An open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

Insert an object into the active project at a specific position

.. code:: csharp

   object ObjectInsert( string typeName, Point pointInsert );

*typeName* -> object description (toolbox name)

*pointInsert* -> System.Drawing.Point Schematic screen position

Insert an object into a specific open project, at a specific position

.. code:: csharp

   object ObjectInsert( string projectName, string typeName, Point point );

*projectName* -> An open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

*point* -> System.Drawing.Point Schematic screen coordinates

Insert an object into the active project at a specific position

.. code:: csharp

   object ObjectInsert( string typeName, int X, int Y );

*typeName* -> object description (toolbox name)

*X" & "Y* -> Schematic x- and y- coordinates to position the object

Insert an object into a specific open project, at a specific position

.. code:: csharp

   object ObjectInsert( string projectName, string typeName, int X, int Y );

*projectName* -> An open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

*X" & "Y* -> Schematic x- and y- coordinates to position the object

Insert an object into the active project, returns an HResult

.. code:: csharp

   HResult ObjectInsert( string typeName, out string objectName );

*typeName* -> object description (toolbox name)

*objectName* -> return name of inserted object, null if insertion fails

Insert an object into a specific open project, returns an HResult

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName,out string objectName );

*projectName* -> An open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

*objectName* -> return name of inserted object, null if insertion fails

Insert an object into the active project at a specific position

.. code:: csharp

   HResult ObjectInsert( string typeName, Point point, out string objectName );

*typeName* -> object description (toolbox name)

*point* -> System.Drawing.Point Schematic screen coordinates

*objectName* -> return name of inserted object, null if insertion fails

Insert an object into a specific open project, at a specific position

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName,Point point, out string objectName );

*projectName* -> An open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

*point* -> System.Drawing.Point Schematic screen coordinates

*objectName* -> return name of inserted object or null if insertion fails

Insert an object into the active project at a specific position

.. code:: csharp

   HResult ObjectInsert( string typeName, int X, int Y, out string objectName );

*typeName* -> object description (toolbox name)

*X" & "Y* -> Schematic x- and y- coordinates to position the object

*objectName* -> return name of inserted object, null if insertion fails

Insert an object into a specific open project, at a specific position

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName, int X, int Y,out string objectName );

*projectName* -> an open project file’s name or fully qualified path

*typeName* -> object description (toolbox name)

*X" & "Y* -> Schematic x- and y- coordinates to position the object

*objectName* -> return name of inserted object, null if insertion fails

NOTE: Schematic objects are inserted into the currently selected hierarchy board of ‘Schematic’ tab by default. Use ‘BlockObjectInsert’ function instead of ‘ObjectInsert’ function to insert Schematic objects into the ‘Block Schematic’ tab.

Remove
------

The functions below are used to remove objects from projects.

Delete an object in the active project

.. code:: csharp

   HResult ObjectRemove( string objectName );

*objectName* -> Name of object to delete

Delete an object from a specific open project

.. code:: csharp

   HResult ObjectRemove( string projectName, string objectName );

*projectName* -> An open project file’s name or fully qualified path

*objectName* -> Name of object to delete

Delete an object in the active project

.. code:: csharp

   HResult ObjectRemove( object object );

*object* -> Reference to object to delete

Delete an object from a specific open project

.. code:: csharp

   HResult ObjectRemove( string projectName, object object );

*projectName* -> An open project file’s name or fully qualified path

*object* -> Reference to object to delete

Connection
----------

Use the functions below for connecting an object’s input and output in a project.

Connect a pair of objects’ output to input in the active project

.. code:: csharp

   HResult ObjectConnect( string fromName, int fromOutPinIndex,string toName, int toInPinIndex );

*fromName* -> Name of object to connect FROM

*fromOutPinIndex* -> Output pin index to connect FROM (zero-based)

*toName* -> Name of object to connect TO

*toInPinIndex* -> Input pin index to connect TO (zero-based)

Connect a pair of objects’ outputs to inputs in a specific open project

.. code:: csharp

   HResult ObjectConnect( string projectName, string fromName,int fromOutPinIndex, string toName, int toInPinIndex);

*projectName* -> An open project file’s name or fully qualified path

*fromName* -> Name of object to connect FROM

*fromOutPinIndex* -> Output pin index to connect FROM (zero-based)

*toName* -> Name of object to connect TO

*toInPinIndex* -> Input pin index to connect TO (zero-based)

Connect a pair of objects’ output to input in the active project

.. code:: csharp

   HResult ObjectConnect( object fromObject, int fromOutPinIndex,object toObject, int toInPinIndex );

*fromObject* -> Reference to object to connect FROM

*fromOutPinIndex* -> Output pin index to connect FROM (zero-based)

*toObject* -> Reference to object to connect TO

*toInPinIndex* -> Input pin index to connect TO (zero-based)

Connect a pair of objects’ output to input in a specific open project

.. code:: csharp

   HResult ObjectConnect( string projectName, object fromObject,int fromOutPinIndex, object toObject, int toInPinIndex );

*projectName* -> An open project file’s name or fully qualified path

*fromObject* -> Reference to object to connect FROM

*fromOutPinIndex* -> Output pin index to connect FROM (zero-based)

*toObject* -> Reference to object to connect TO

*toInPinIndex* -> Input pin index to connect TO (zero-based)

Disconnect
----------

The functions below are used to disconnect input and output from objects in a project.

Disconnect output from input of a pair of objects in the active project

.. code:: csharp

   HResult ObjectDisconnect( string fromName, int fromOutPinIndex,string toName, int toInPinIndex );

*fromName* -> Name of object to disconnect FROM

*fromOutPinIndex* -> Output pin index to disconnect FROM (zero-based)

*toName* -> Name of object to disconnect TO

*toInPinIndex* -> Input pin index to disconnect TO (zero-based)

Disconnect output from input of a pair of objects in a specific open project

.. code:: csharp

   HResult ObjectDisconnect( string projectName, string fromName,int fromOutPinIndex, string toName, int toInPinIndex );

*projectName* -> An open project file’s name or fully qualified path

*fromName* -> Name of object to disconnect FROM

*fromOutPinIndex* -> Output pin index to disconnect FROM (zero-based)

*toName* -> Name of object to disconnect TO

*toInPinIndex* -> Input pin index to disconnect TO (zero-based)

Disconnect output from input of a pair of objects in the active project

.. code:: csharp

   HResult ObjectDisconnect( object fromObject, int fromOutPinIndex,object toObject, int toInPinIndex );

*fromObject* -> Reference to object to disconnect FROM

*fromOutPinIndex* -> Output pin index to disconnect FROM (zero-based)

*toObject* -> Reference to object to disconnect TO

*toInPinIndex* -> Input pin index to disconnect TO (zero-based)

Disconnect output from input of a pair of objects in a specific open project

.. code:: csharp

   HResult ObjectDisconnect( string projectName, object fromObject,int fromOutPinIndex, object toObject, int toInPinIndex );

*projectName* -> An open project file’s name or fully qualified path

*fromObject* -> Reference to object to disconnect FROM

*fromOutPinIndex* -> Output pin index to disconnect FROM (zero-based)

*toObject* -> Reference to object to connect TO

*toInPinIndex* -> Input pin index to disconnect TO (zero-based)

Console/ File IO
----------------

The following functions print any message given to the output window in the script editor.

.. code:: csharp

   HResult Print( string message);
   HResult PrintLine( string message);

The following sample code shows how to read parameters from a file using C# file IO.

.. code:: csharp

   // #LANGUAGE# C#
   // Get Cell object

   ss.ProjectLinkCompileDownload();
   object obj = ss.GetCellObject("Gain1");
   System.Reflection.FieldInfo[] memberInfos = ss.ObjectGetFields(obj);
   System.Collections.ArrayList arr1 = null;
   foreach (System.Reflection.FieldInfo memberInfo in memberInfos)
   {
       if (memberInfo.Name == "controlarr")
       {
           arr1  = (System.Collections.ArrayList)memberInfo.GetValue(obj);
           break;
       }
   }
   System.Reflection.PropertyInfo prop = ss.ObjectGetProperty(arr1[0], "LGain");

   string pathSource = @"D:\testdata.txt";
   FileStream fsSource = new FileStream(pathSource, FileMode.Open, FileAccess.Read);
   System.IO.StreamReader sr = new System.IO.StreamReader(fsSource, System.Text.Encoding.ASCII);

   while (!sr.EndOfStream)
   {
       string myString = sr.ReadLine();
           float fval = 0;
       float.TryParse(myString, out fval);
       prop.SetValue(arr1[0], (double) fval, null);
       System.Threading.Thread.Sleep(2000);
   }
   fsSource.Dispose();

   // #LANGUAGE# C#

Properties
----------

The functions below may be used to manage object properties.

Manipulate an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectSetProperties( string opcode, string objectName, params object[] propertyParams );

*opcode* -> Opcode of function to perform (see below)

*objectName* -> Name of the object to update

*propertyParams* -> Parameters associated with the specified opcode

Manipulate an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectSetProperties( string opcode, object object, params object[] propertyParams );

*opcode* -> Opcode of function to perform (see below)

*object* -> Reference to object to update

*propertyParams* -> Parameters associated with the specified opcode

Manipulate an object's properties or parameters in a specific open project

.. code:: csharp

   HResult ObjectSetProperties( string projectName, string opcode, string objectName, params object[] propertyParams );

*projectName* -> An open project file’s name or fully qualified path

*opcode* -> Opcode of function to perform (see below)

*objectName* -> Name of the object to update

*propertyParams* -> Parameters associated with the specified opcode

Manipulate an object's properties or parameters in a specific open project

.. code:: csharp

   HResult ObjectSetProperties( string projectName, string opcode, object object, params object[] propertyParams );

*projectName* -> An open project file’s name or fully qualified path

*opcode* -> Opcode of function to perform (see below)

*object* -> Reference to object to update

*propertyParams* -> Parameters associated with the specified opcode

Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string opcode, string objectName, out object[] getPropVal,params object[] propertyParams );

*opcode* -> Opcode of function to perform (see below)

*objectName* -> Name of the object to update

*getPropVal* -> Fetched property or parameters

*propertyParams* -> Parameters associated with the specified opcode

Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string opcode, object object, out object[] getPropVal, params object[] propertyParams );

*opcode* -> Opcode of function to perform (see below)

*object* -> Reference to object to update

*getPropVal* -> Fetched property or parameters

*propertyParams* -> Parameters associated with the specified opcode

Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string projectName, string opcode, string objectName,out object[] getPropVal, params object[] propertyParams );

*projectName* -> An open project file’s name or fully qualified path

*opcode* -> Opcode of function to perform (see below)

*objectName* -> Name of the object to update

*getPropVal* -> Fetched property or parameters

*propertyParams* -> Parameters associated with the specified opcode

Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string projectName, string opcode, object object, out object[] getPropVal,params object[] propertyParams );

*projectName* -> An open project file’s name or fully qualified path

*opcode* -> Opcode of function to perform (see below)

*object* -> Reference to object to update

*getPropVal* -> Fetched property or parameters

*propertyParams* -> Parameters associated with the specified opcode

The property interfaces require an opcode (Operation Code), which specifies the type of operation to be performed. Relevant opcodes depend on the type of object. Some opcodes apply to all objects (e.g. setPosition and setName); others are specific to particular object categories. Essential opcodes are listed in the table below:

+--------------------------+----------------------------+-----------------------------------------------+
| Opcode                   | Type                       | PropertyParams                                |
+==========================+============================+===============================================+
| *setPosition*            | 1. System.Drawing.Point    | Screen position at which to centre the object |
+--------------------------+----------------------------+-----------------------------------------------+
| *setName*                | 1. System.String           | New name for object (must be unique)          |
+--------------------------+----------------------------+-----------------------------------------------+
| *changeIC*               | 1. System.String           | Name of IC to associate with the Algorithm    |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. int (optional)          | Index of Algorithm to change                  |
+--------------------------+----------------------------+-----------------------------------------------+
| *addAlgorithm*           | 1. Sytem.String (optional) | New name for object (must be unique)          |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. Sytem.String (optional) | Name of Algorithm to add                      |
+--------------------------+----------------------------+-----------------------------------------------+
| *removeAlgorithm*        | NONE                       |                                               |
+--------------------------+----------------------------+-----------------------------------------------+
| *growAlgorithm*          | 1. int                     | Index of Algorithm to grow                    |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. int                     | Amount to grow Algorithm                      |
+--------------------------+----------------------------+-----------------------------------------------+
| *reduceAlgorithm*        | 1. int                     | Index of Algorithm to reduce                  |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. int                     | Amount to reduce Algorithm                    |
+--------------------------+----------------------------+-----------------------------------------------+
| *setSamplingRate*        | 1. int                     | New Module Sampling Rate                      |
+--------------------------+----------------------------+-----------------------------------------------+
| *setBlockSize*           | 1. int                     | New Source Module Block Size                  |
+--------------------------+----------------------------+-----------------------------------------------+
| *setControlValue*        | 1. int                     | Index of Algorithm                            |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. int                     | Repeat Index (Grow index)                     |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 3. System.String           | Control value name**\*                        |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 4. System.object           | Value to set                                  |
+--------------------------+----------------------------+-----------------------------------------------+
| *setBlockSize*           | 1. int                     | New Source Module Block Size                  |
+--------------------------+----------------------------+-----------------------------------------------+
| *setOutputBufferSize*    | 1. int                     | New Output Buffer Size in bytes               |
+--------------------------+----------------------------+-----------------------------------------------+
| *setPCMxOutputBlockSize* | 1. int                     | New PCMx Output Module Block Size             |
+--------------------------+----------------------------+-----------------------------------------------+
| *getBlockSize*           | 1. None                    | NA                                            |
+--------------------------+----------------------------+-----------------------------------------------+
| *getSamplingRate*        | 1. None                    | NA                                            |
+--------------------------+----------------------------+-----------------------------------------------+
| *getControlValue*        | 1. int                     | Index of Algorithm                            |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 2. int                     | Repeat Index (Grow index)                     |
+--------------------------+----------------------------+-----------------------------------------------+
|                          | 3. System.String           | Control value name                            |
+--------------------------+----------------------------+-----------------------------------------------+
| *getCurrentGrowth*       | 1. int                     | Index of Algorithm                            |
+--------------------------+----------------------------+-----------------------------------------------+

| 
| Table 2: Opcode and Property Parameters

NOTE: Control value names can be viewed as tooltip information. Please refer :doc:`Viewing Control Parameter Names . </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/paramuidataname>`

Reflection Support
------------------

The functions below may be used to access methods, properties and fields from SigmaStudio object using C# reflection.

There are two kinds of object used in the SigmaStudio schematic modules. Cell Object and Algorithm Object. Cell object contains the GUI related information. Algorithm object contains algorithm related information. There can be multiple algorithm objects in a single cell object.

.. code:: csharp

   object GetCellObject(string objectName);
   object[] GetAlgorithmObjects(string objectName);

*objectName* -> Name of the Cell object.

API uses the Reflection's GetProperty() method and returns the PropertyInfo for the module with the name 'objectName in the schematic. ObjectGetProperties() retuns all the public properties in the object.

.. code:: csharp

   PropertyInfo ObjectGetProperty(string objectName, string propertyName);
   PropertyInfo[] ObjectGetProperties(string objectName);

*objectName* -> Name of the object to get the properties info

*propertyName* -> Name of the property to get from the object.

API uses the Reflection's GetField() method and returns the FieldInfo for the module with the name 'objectName in the schematic. ObjectGetFields() retuns all the public fields in the object.

.. code:: csharp

   FieldInfo ObjectGetField(string objectName, string fieldName);
   FieldInfo [] ObjectGetFields(string objectName);

*objectName* -> Name of the object to get the fields info

*fieldName* -> Name of the field to get from the object.

API uses the Reflection's GetMethod() method and returns the MethodInfo for the module with the name 'objectName in the schematic. ObjecMethodss() returns all the public methods in the object.

.. code:: csharp

   MethodInfo ObjectGetMethod(string objectName, string methodName);
   MethodInfo [] ObjectGetMethods(string objectName);

*objectName* -> Name of the object to get the methods info

*methodName* -> Name of the method to get from the object.

Examples
~~~~~~~~

The following shows an example of how to access the Checkbox in the mute module using refection.

.. code:: csharp

   object obj = ss.GetCellObject("Mute1");
   System.Reflection.FieldInfo[] memberInfos = ss.ObjectGetFields(obj);
   System.Collections.ArrayList arr = null;
   ss.PrintLine("Mute fields are received ");
   foreach (System.Reflection.FieldInfo memberInfo in memberInfos)
   {
           // control array contains all the Controls in the module.
       if (memberInfo.Name == "controlarr")
       {
               arr  = (System.Collections.ArrayList)memberInfo.GetValue(obj);
           break;
       }
   }

   System.Reflection.PropertyInfo[] props = ss.ObjectGetProperties(arr[0]);
   foreach (System.Reflection.PropertyInfo prop in props)
   {
      ss.PrintLine(prop.Name);
      if (prop.Name == "IsChecked")
      {
           // Set the Checkbox status to true
       prop.SetValue(arr[0], true, null);
      }
   }

   // Wait for 5s
   System.Threading.Thread.Sleep(5000);

   // Set the checkbox to false
   System.Reflection.PropertyInfo propInfo = ss.ObjectGetProperty(arr[0],"IsChecked");
   propInfo.SetValue(arr[0], false, null);

The following example calls the 'PackDataAllControls' method from the cell object. This method downloads all the parameters from the module.

.. code:: csharp

   object obj = ss.GetCellObject("Mute1");

   // Print all the methods
   System.Reflection.MethodInfo[] memberInfos = ss.ObjectGetMethods(obj);
   foreach (System.Reflection.MethodInfo memberInfo in memberInfos)
   {
      ss.PrintLine(memberInfo.Name);
   }

   // Get Pack All Controls method and call it.
   System.Reflection.MethodInfo methodInfo = ss.ObjectGetMethod(obj, "PackDataAllControls");
   ss.PrintLine(methodInfo.Name);
   methodInfo.Invoke(obj, new object[]{});

Settings
--------

The function below may be used to manage SigmaStudio settings.

Manipulate SigmaStudio settings in the active project

.. code:: csharp

   HResult DesignSettings(string cmd, params object[] arg);

*cmd* -> Command opcode of setting to modify

*arg* -> Modified value of the setting. This should be of string datatype

+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Command        | Argument                                                                                                                                                                                                                                        |
+================+=================================================================================================================================================================================================================================================+
| *XMLOnly*      | 1. "true" – Only XML file will get generated upon exporting                                                                                                                                                                                     |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                | 2. ”false” – Non XML system files will also get generated upon exporting                                                                                                                                                                        |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *SchematicTag* | “String” tag to be associated with the Schematic xml file. e.g. “SigmaStudioforSHARC - Version x_y_z1”                                                                                                                                          |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Pre-build*    | The command to be executed before the Schematic is compiled.. e.g. “ssTestSettings.bat arg1”                                                                                                                                                    |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Post-build*   | The command to be executed after the Schematic is compiled. e.g. “ssTestSettings.bat arg1”                                                                                                                                                      |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Pre-export*   | The command to be executed before the export of a Schematic. e.g.“ssTestSettings.bat arg1”                                                                                                                                                      |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Post-export*  | The command to be executed after the export of a Schematic. e.g.“ssTestSettings.bat arg1”                                                                                                                                                       |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *Auto-export*  | 1. ”false”, “D:\\\\test\\\\autoexport” – Auto export of system files after compile is disabled. The second string is the path where the export files should be generated. The path entered should be a valid one                                |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                | 2. "true", “D:\\\\test\\\\autoexport” – Auto export of system files after compile is disabled. The second string is the path where the export files should be generated. The path entered should be a valid one.                                |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| *ToolSel*      | This should be the full name of the tool- chain (as available in the Tools -> Settings -> SHARC -> Tool-chain list) to be used for Schematic compilation. e.g.“CrossCore Embedded Studio for Analog Devices Processors v1.0.3”“VisualDSP++ 5.1” |
+----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| Table 3: Command and Arguments for Settings API

1 x.y.z denotes the version of SigmaStudio for SHARC. Refer Release Notes for version information of SigmaStudio for SHARC

Manipulate properties in the IC Control window

.. code:: csharp

   HResult SetICControlProperties(string ICName, string cmd, object arg);

*ICName* -> Friendly name of DSP(IC) to be modified

*cmd* -> Command opcode of property to modify

*arg* -> Modified value of the setting

+-------------------+--------+-----------------------------------------------------+
| Command           | Type   | Argument                                            |
+===================+========+=====================================================+
| *MaxInChannels*   | int    | Number of input channels                            |
+-------------------+--------+-----------------------------------------------------+
| *MaxOutChannels*  | int    | Number of output channels                           |
+-------------------+--------+-----------------------------------------------------+
| *MasterBypass*    | bool   | true - Master Bypass enabled                        |
+-------------------+--------+-----------------------------------------------------+
|                   |        | false - Master Bypass disabled                      |
+-------------------+--------+-----------------------------------------------------+
| *DefaultCore*     | bool   | true - Core 1 enabled                               |
+-------------------+--------+-----------------------------------------------------+
|                   |        | false - Core 2 enabled                              |
+-------------------+--------+-----------------------------------------------------+
| *TargetBuildMode* | bool   | true - Debug mode enabled                           |
+-------------------+--------+-----------------------------------------------------+
|                   |        | false – Release mode enabled                        |
+-------------------+--------+-----------------------------------------------------+
| *BlockSize*       | int    | Blocksize value (8 or multiple of 8)                |
+-------------------+--------+-----------------------------------------------------+
| *LoadAppDXE*      | string | The Application DXE, to be selected, with full path |
+-------------------+--------+-----------------------------------------------------+

Table 4: Command and Argument for Modify IC Control Window Properties API

Plug-Ins
--------

The function given below may be used to manipulate Plug-Ins.

Enable or disable a Plug-In added to the SigmaStudio Add-Ins window

.. code:: csharp

   HResult ModifyPlugInState ( string plugin, bool state);

*plugin* -> name of the Plug-In as string

*state* -> “True” or “False” indicating whether to ‘enable’ or ‘disable’ Plug-In

The first argument, which is the name of the Plug-In, can either be the full path of the Plug-In DLL as listed in the Add-Ins list or only the file name of the Plug-In DLL. SigmaStudio will first try to match the argument string against full path of the Plug-Ins in the Add-Ins list. If a match is not found, the string is matched against the file name of the Plug-Ins. If multiple Plug-Ins with the name passed as argument are present in the Add-Ins list, only the first occurrence in the list is modified by this function. The Plug-In name is case insensitive.

Float Packets Interface
-----------------------

ICParameterSafeload
~~~~~~~~~~~~~~~~~~~

The function has two overloaded methods as shown in prototype-1 and prototype-2 given below.

This is an API to handle floating point packets and hence is applicable for SHARC only.

Prototype-1
^^^^^^^^^^^

.. code:: csharp

   HResult ICParameterSafeload ( string ICname, int32 WriteAddress, single DataToWrite)

*Description*

The method sends a parameter data to the address specified by the write address for the specified IC. The parameters will be loaded to the target using the “Safeload” mechanism.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC to which data is to be sent

Name:WriteAddress

Type:int32

Description:Offset address location to which the parameter needs to be written

Name:DataToWrite

Type:Single

Description:Single precision floating point parameter value to be written to target memory.

Prototype-2
^^^^^^^^^^^

.. code:: csharp

   HResult ICParameterSafeload ( string ICname, int32 WriteAddress, int32 WriteNumParams, single[] DataToWrite)

*Description*

The method sends an array of parameter data of size “WriteNumParams” to the address specified by the write address for the specified IC. The parameters will be loaded to the target using the “Safeload” mechanism.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC to which data is to be sent

Name:WriteAddress

Type:int32

Description:Offset address location to which the parameter needs to be written

Name:WriteNumParams

Type:int32

Description:Number of parameters to be written to target parameter memory

Name:DataToWrite

Type:Single

Description:Single precision floating point array of parameter values to be written to target parameter memory.

ICParameterWrite
~~~~~~~~~~~~~~~~

The function has two overloaded methods as shown in prototype-1 and prototype-2 given below.

This is an API to handle floating point packets and hence is applicable for SHARC only.

Prototype-1
^^^^^^^^^^^

.. code:: csharp

   HResult ICParameterWrite ( string ICname, int32 WriteAddress, single DataToWrite)

*Description*

The method sends a parameter data to the address specified by the write address for the specified IC. The parameters will be loaded to the target without “Safeload” mechanism.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC to which data is to be sent

Name:WriteAddress

Type:int32

Description:Offset address location to which the parameter needs to be written

Name:DataToWrite

Type:Single

Description:Single precision floating point parameter value to be written to target memory.

Prototype-2
^^^^^^^^^^^

.. code:: csharp

   HResult ICParameterWrite ( string ICname, int32 WriteAddress, int32 WriteNumParams, single[] DataToWrite)

*Description*

The method sends an array of parameter data of size “WriteNumParams” to the address specified by the write address for the specified IC. The parameters will be loaded to the target as a block without using the “Safeload” mechanism.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC to which data is to be sent

Name:WriteAddress

Type:int32

Description:Offset address location to which the parameter needs to be written

Name:WriteNumParams

Type:int32

Description:Number of parameters to be written to target parameter memory

Name:DataToWrite

Type:Single

Description:Single precision floating point array of parameter values to be written to target parameter memory.

ICParameterRead
~~~~~~~~~~~~~~~

This is an API to handle floating point packets and hence is applicable for SHARC only.

Prototype
^^^^^^^^^

.. code:: csharp

   float ICParameterRead ( string ICname, int32 readAddress)

*Description*

The method reads a parameter data from the address specified by the read address for the specified IC.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC from which data is to be read

Name:readAddress

Type:int32

Description:Offset address location from parameter memory from where the parameter needs to be read

SHARCTargetBoot
---------------

This is applicable only for the SHARC target, where booting using a Loader File is applicable.

Prototype
~~~~~~~~~

.. code:: csharp

   HResult SHARCTargetBoot (string ICName, string fileName, ArrayList bootArgs)

*Description*

The method is used to boot the SHARC Target with a Loader File.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC which should be booted

Name:Filename

Type:String

Description:Full path of the LDR file

Name:bootArgs

Type:ArrayList

Description:Arguments for boot configuration ArrayList with the boot option (2, 3, 4, 5 or 10) as the first entry 2: Analog-In 3: Digital-In 4: Digital-Out alone 5: Analog\\Digital Co-existence 10: Analog\\Digital Co-existence (Digital Clock)

SHARCReadMIPS
-------------

This API is applicable only for the SHARC target, to get the MIPS information from the target.

Prototype
~~~~~~~~~

.. code:: csharp

   float SHARCReadMIPS (string ICName)

*Description*

The method is used to Read MIPS consumed by the SHARC Target hardware.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC from which to read the MIPS

SHARCReadLibVersion
-------------------

This API is applicable for SHARC target only, to fetch the target library version from the target.

Prototype
~~~~~~~~~

.. code:: csharp

   uint SHARCReadLibVersion (string ICName)

*Description*

The method is used to read version number of the Target Library running on SHARC Target processor.

*Parameters*

Name: ICname

Type: String

Description:Name of the IC from which the version should be obtained

General Functions
-----------------

A list of general functions and their prototypes are given below.

Undo
~~~~

Undo an action in active project file

.. code:: csharp

   HResult ScriptUndo();

Undo an action in specific project file

.. code:: csharp

   HResult ScriptUndo( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Redo
~~~~

Redo an action in active project file

.. code:: csharp

   HResult ScriptRedo();

Redo an action in specific project file

.. code:: csharp

   HResult ScriptRedo( string projectName );

*projectName* -> An open project file’s name or fully qualified path

Pause
~~~~~

Pause script execution for delay Milliseconds

.. code:: csharp

   HResult ScriptDelay( int delayMilliseconds );

*delayMilliseconds* -> Amount of delay in milliseconds

Run
~~~

Run script

.. code:: csharp

   HResult ScriptRun( string script );

*script* -> script code as a System.String

Run script file

.. code:: csharp

   HResult ScriptRunFile( string scriptFilename );

*scriptFilename* -> The fully qualified script file name

Pause and Resume Options
~~~~~~~~~~~~~~~~~~~~~~~~

USBiReset
---------

.. code:: csharp

   HResult ResetUSBInterface();

*Description*

The method is used to Reset the USBi interface

GetIcNames
----------

.. code:: csharp

   ArrayList GetIcNames();

*Description*

The method is used to Gets IcName in the schematic

Selfboot Options
----------------

Selfboot Port settings
~~~~~~~~~~~~~~~~~~~~~~

.. code:: csharp

   SELFBOOT_PORT_SETTINGS(string cellName, int[] values);

*Description*

The method is used to settings the E2prom port through server/script

*Parameters*

Name: Cellname

Type: String

*Description*

Cell name of SigmaDSP IC example: "IC 1"

Name: PORT_SETTINGS

Type: int

Example for Python :
^^^^^^^^^^^^^^^^^^^^

PORT_SETTINGS = VARIANT(pythoncom.VT_ARRAY\| pythoncom.VT_I4, [1048576,0x03,0x02,0x03,0x06,0xc7,10,10000,256,1,0])

Example for .sss:
^^^^^^^^^^^^^^^^^

System.Collections.Generic.List<int> PORT_SETTINGS = new System.Collections.Generic.List<int>();

PORT_SETTINGS.Add(1048576); PORT_SETTINGS.Add(0x03); PORT_SETTINGS.Add(0x02); PORT_SETTINGS.Add(0x03); PORT_SETTINGS.Add(0x06); PORT_SETTINGS.Add(0xc7); PORT_SETTINGS.Add(10); PORT_SETTINGS.Add(10000); PORT_SETTINGS.Add(256); PORT_SETTINGS.Add(1); PORT_SETTINGS.Add(0);

Selfboot write
~~~~~~~~~~~~~~

.. code:: csharp

   SELFBOOTWRITE(string cellName, string writeThrough);

*Description*

The method is used to write through "DSP" or "USB" (USB currently not supported)

Selfboot Export
~~~~~~~~~~~~~~~

.. code:: csharp

   EXPORT_SELFBOOT_DATA(bool readThroughDSP, string fullyQualifiedFileName);

*Description*

The method is used to Export the Selfboot data from E2PROM.

*Parameters*

Name: projectexportFile

Type: String

*Description*

stored the .Hex file on this path

Selfboot Erase
~~~~~~~~~~~~~~

.. code:: csharp

   SELFBOOTERASE(string cellName);

*Description*

The method is used to Erase the E2PROM.

Examples
~~~~~~~~

The following shows an example of how to using Selfboot .

.. code:: csharp

   rom  win32com.client.dynamic import Dispatch
   from win32com.client import VARIANT
   import pythoncom
   import sys

   try:
       import clr
   except:
       import pip
       pip.main(['install', 'pythonnet'])
       import clr

   clr.AddReference('System.Collections')
   from System.Collections.Generic import List

   PORT_SETTINGS = VARIANT(pythoncom.VT_ARRAY| pythoncom.VT_I4, [1048576,0x03,0x02,0x03,0x06,0xc7,10,10000,256,1,0])

   ## This program is designed to test SigmaStudio scripting from Python.
   if __name__ == "__main__":

       server = Dispatch('Analog.SigmaStudioServer.SigmaStudioServer')
       print('Running')

       projectexportFile= "C:\Work\Test\Python1\SelfBootWrite_export" # Needs update
       projectexporteraseFile= "C:\Work\Test\Python1\SelfBootErase_export"  # Needs update
       Cellname = 'IC 1'
       SelfbootThrough = 'DSP'

       status = server.SET_TIMEOUT(120) # 2 Min Needs update if erase or export of complete EEPROM
       print('set_timeout..')
       server.COMPILE_PROJECT

       print('Selfboot Port settings')
       # Arg1 - Cell name of SigmaDSP IC example: "IC 1"
       # Arg2 - EEPROM port settings
       server.SELFBOOT_PORT_SETTINGS(Cellname, PORT_SETTINGS)

       print('Selfboot write')
       # Arg1 - Cell name of SigmaDSP IC example: "IC 1"
       # Arg2 - write through "DSP" or "USB" (USB currently not supported)
       server.SELFBOOTWRITE(Cellname, SelfbootThrough)

       print('Selfboot Export')
       # Arg1 - True for DSP, False for USB (USB currently not supported)
       # Arg2 - Export file path
       server.EXPORT_SELFBOOT_DATA(True, projectexportFile)

       print('Selfboot Erase')
       # Arg1 - Cell name of SigmaDSP IC example: "IC 1"
       server.SELFBOOTERASE(Cellname);

       server.EXPORT_SELFBOOT_DATA(True, projectexporteraseFile)

       server.SAVE_PROJECT

IPAT Options
------------

Write
~~~~~

.. code:: csharp

   HResult IPATParamWrite(int numOfBytesToWrite, byte[] dataToWrite, int ipatWriteAddress, int _numOfLoadsAndTriggers, int protocol, int chipAddress, int addressOfStartAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

Read
~~~~

.. code:: csharp

   HResult IPATParamRead(int numberBytesToRead, out byte[] dataRead, int protocol, int chipAddress, int ipatReadAddress, int AddressWidth, int RegisterByteLength, int communicationChannel, int ICType);

*Description*

The method is used to Write / from Read the values of the parameter to/from IPAT Address.

*Parameters*

Type & Name: int numOfBytesToWrite

*Description*

Number of bytes in 'dataToWrite' to write to the dsp

Type & Name: int writeToData

*Description*

The data to write

Type & Name: int ipatWriteAddress

*Description*

Indirect address of the parameter to be load

Type & Name: int \_numOfLoadsAndTriggers

*Description*

Number of consecutive loads

Type & Name: int protocol

*Description*

Serial prorotcol to transfer the data

Type & Name: int chipAddress

*Description*

I2C - Load Address, SPI - Address is zero

Type & Name: int addressOfStartAddress

*Description*

Address of the IPAT StartAddress

Type & Name: int addressWidth

*Description*

The width of address

Type & Name: int registerByteLength

*Description*

address increment

Type & Name: int communicationChannel

*Description*

The commumnication channel USBi/AARDVARK

Type & Name: int ICType

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/script1.jpg
   :width: 400px
