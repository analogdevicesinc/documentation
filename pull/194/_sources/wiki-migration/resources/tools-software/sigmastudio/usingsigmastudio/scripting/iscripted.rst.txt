:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

IScripted Interface
===================

| Analog.SStudioScripting.IScripted is contained in a .NET assembly, BaseLib.dll, installed in the SigmaStudio folder.
| Script window can be used to run scripts using the Iscripted interface. |image1|

Return Type
-----------

| The interface defines an integer return type, “HResult”, as follows:
| ``HResult.S_OK = 0
  HResult.E_FAILED = 1
  HResult.E_INVALID_ARGS = 2
  HResult.E_EXCEPTION = 3``

Project File Interface
----------------------

| The following functions can be used to interface with a project file.
| ====Create==== Create a new project file

.. code:: csharp

   HResult ProjectNew();

| The function takes no parameter
| ====Open==== Open a project file from disk

.. code:: csharp

   HResult ProjectOpen( string filename );

| <fc #cd5c5c>\ *filename*\ </fc> -> A fully qualified file path
| ====Save/Save As==== Save the Active project file

.. code:: csharp

   HResult ProjectSave();

| The function takes no parameter
| Save a specific project file

.. code:: csharp

   HResult ProjectSave( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| Save as the Active project file

.. code:: csharp

   HResult ProjectSaveAs( string saveAsFilename );

| <fc #cd5c5c>\ *saveAsFilename*\ </fc> -> A new file name or fully qualified path
| Save as a specific project file

.. code:: csharp

   HResult ProjectSaveAs( string projectName, string saveAsFilename );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *saveAsFilename*\ </fc> -> The new file name or fully qualified path
| ====Close==== Close the Active project file

.. code:: csharp

   HResult ProjectClose();

| 
| Close a specific project file

.. code:: csharp

   HResult ProjectClose( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| ====Set Project as active==== Set a project as the active project

.. code:: csharp

   HResult ProjectSetActive( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| ====Link==== Link the active Schematic

.. code:: csharp

   HResult ProjectLink();

| The function takes no parameter
| Link and compile the active Schematic

.. code:: csharp

   HResult ProjectLinkCompile();

| The function takes no parameter
| Link and compile the active Schematic

.. code:: csharp

   HResult ProjectLinkCompile( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| Link, compile and download the active Schematic

.. code:: csharp

   HResult ProjectLinkCompileDownload();

| The function takes no parameter
| Link, compile and download a specific project file

.. code:: csharp

   HResult ProjectLinkCompileDownload( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| ====Others==== Set the "New Item Sample Rate" (Schematic Sampling Rate) for the active project

.. code:: csharp

   HResult DesignSetSamplingRate( int samplingRate );

| 
| Propagate Schematic Sampling Rate

.. code:: csharp

   HResult DesignPropagateSamplingRate();

| The function takes no parameter
| Toggle Schematic Freeze On/Off

.. code:: csharp

   HResult DesignToggleSchematicFreeze( string password );

| <fc #cd5c5c>\ *password*\ </fc> -> Schematic freeze password
| Set the activate hierarchy board in the current Schematic

.. code:: csharp

   HResult DesignSetActiveBoard( string boardName );

| <fc #cd5c5c>\ *boardName*\ </fc> -> Board name in the active Schematic
| Export the system files of the active Schematic

.. code:: csharp

   HResult ProjectExportSystemFiles ( string fullyQualifiedFileName );

| <fc #cd5c5c>\ *fullyQualifiedFileName*\ </fc> -> fully qualified path of the system file without the extension
| Build Plug-In DLL using Algorithm Designer

.. code:: csharp

   HResult BuildExternalModule ( string ICName, string fullyQualifiedProjectName, string fullyQualifiedLibraryName );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) for example "IC 1" or "IC 2"
| <fc #cd5c5c>\ *fullyQualifiedProjectName*\ </fc> -> fully qualified path of designer project file
| <fc #cd5c5c>\ *fullyQualifiedLibraryName*\ </fc> -> fully qualified path of the output DLL
| Note: The DSP IC has to be there in new schematic window before calling this API.
| For example,
| HResult eResult = HResult.S_OK;
| sigmastudio.ProjectNew();
| sigmastudio.ObjectInsert( "ADSP-214xx" );
| eResult = sigmastudio.BuildExternalModule("IC 1", "C:\\\\Analog Devices\\\\SoftwareModules\\\\SigmaStudioForSHARC-SH-Rel2.2.0\\\\Target\\\\ExtModules\\\\Biquad\\\\adi_Biquad.ssg", "C:\\\\Analog Devices\\\\SoftwareModules\\\\SigmaStudioForSHARC-SH-Rel2.2.0\\\\Target\\\\ExtModules\\\\Biquad\\\\adi_biquad.dll");
| Set the “Schematic Block Size” of IC and Algorithms belonging to the IC for the active project

.. code:: csharp

   HResult DesignSetBlockSize(string ICName, int nSize);

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC)
| <fc #cd5c5c>\ *nSize*\ </fc> -> The Schematic Block Size given as ‘nSize’ will be set to all Modules/Algorithms belonging to the IC corresponding to the ‘ICName’. The Schematic Block Size (nSize) should be greater than 8 and a multiple of 8.
| =====Register/Parameter Interface===== Functions for working with the registers and parameters are listed below.
| ====Register Write==== Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( int numOfBytesToWrite, byte[] dataToWrite, int protocol, int chipAddress, int writeAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

| <fc #cd5c5c>\ *numOfBytesToWrite*\ </fc> -> Number of bytes in 'dataToWrite' to write to the dsp
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> The data to write, byte array of length numOfBytesToWrite
| <fc #cd5c5c>\ *protocol*\ </fc> -> The protocol to transfer the data, SPI = 1 and I2C = 0
| <fc #cd5c5c>\ *chipAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The register address to write
| <fc #cd5c5c>\ *addressWidth*\ </fc> -> The width of the register address to write
| <fc #cd5c5c>\ *registerByteLength*\ </fc> -> The byte length of the register to write
| <fc #cd5c5c>\ *communicationChannel*\ </fc> -> The interface for communication, USBI = 0 and AARDVARK = 1
| <fc #cd5c5c>\ *ICType*\ </fc> -> The type of the IC, ADAU145x/ADAU146x = 0, ADSP-214xx = 1, ADSP-SC5xx/ADSP-215xx = 2
| Note :- Refer this link for example script :doc:`/wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/iscripted_samples`
| Write data to a register

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int writeAddress,int writeNumberBytes, long dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The register address to write
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Number of bytes in 'dataToWrite' to write to the dsp
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> The data to write (long == 64bit max data)
| Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int deviceAddress, int writeAddress, int writeNumberBytes, long dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC)
| <fc #cd5c5c>\ *deviceAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The register address to write
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Number of bytes in 'dataToWrite' to write to the dsp
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> The data to write (long == 64bit max data)
| Write data to a register, data specified as a byte array

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int writeAddress,int writeNumberBytes, byte[] dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The register address to write
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Number of bytes in 'dataToWrite' to write to the dsp
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> The data to write, byte array of length writeNumberBytes
| Write data to a register, specific device address

.. code:: csharp

   HResult ICRegisterWrite( string ICName, int deviceAddress, int writeAddress,int writeNumberBytes, byte[] dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC)
| <fc #cd5c5c>\ *deviceAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The register address to write
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Number of bytes in 'dataToWrite' to write to the dsp
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> The data to write, byte array of length writeNumberBytes
| Write safeload register

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int safeloadRegister,long dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| "safeloadRegister” = Regsiter address to safeload
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> Data to write to the safeload register (5Bytes)
| Write multiple contiguous safeload registers

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int safeloadRegister,int writeNumberBytes, Byte[] dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *safeloadRegister*\ </fc> -> Regsiter address to safeload
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Number of data bytes in dataToWrite
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> Data to write to the safeload register (5Bytes)
| Write multiple safeload registers

.. code:: csharp

   HResult ICRegisterSafeload( string ICName, int[] writeAddresses,int[] writeNumberBytes, byte[] dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddresses*\ </fc> -> Array of addresses to safeload
| <fc #cd5c5c>\ *writeNumberBytes*\ </fc> -> Write bytes per address (for each writeAddresses entry)
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> Data array to write to the safeload registers

Register Read
~~~~~~~~~~~~~

Read data to a register from specific device address

.. code:: csharp

   HResult ICRegisterRead( int numOfBytesToRead, byte[] dataRead, int protocol, int chipAddress, int readAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

| <fc #cd5c5c>\ *numOfBytesToRead*\ </fc> -> Number of bytes to read from the dsp
| <fc #cd5c5c>\ *dataRead*\ </fc> -> Read the data from register
| <fc #cd5c5c>\ *protocol*\ </fc> -> The protocol to transfer the data, SPI = 1 and I2C = 0
| <fc #cd5c5c>\ *chipAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The address of register to read the data
| <fc #cd5c5c>\ *addressWidth*\ </fc> -> The width of the register address to write
| <fc #cd5c5c>\ *registerByteLength*\ </fc> -> The byte length of the register to write
| <fc #cd5c5c>\ *communicationChannel*\ </fc> -> The interface for communication, USBI = 0 and AARDVARK = 1
| <fc #cd5c5c>\ *ICType*\ </fc> -> The type of the IC, ADAU145x/ADAU146x = 0, ADSP-214xx = 1, ADSP-SC5xx/ADSP-215xx = 2
| Note :- Refer this link for example script :doc:`/wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting/iscripted_samples`
| Read data from a register, read value returned in method parameter

.. code:: csharp

   HResult ICRegisterRead( string ICName, int readAddress, int readNumberBytes,out long bytesRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| <fc #cd5c5c>\ *bytesRead*\ </fc> -> Return data if read is successful
| Read data from a register, specific device address

.. code:: csharp

   HResult ICRegisterRead( string ICName, int deviceAddress, int readAddress, int readNumberBytes, out long bytesRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC)
| <fc #cd5c5c>\ *deviceAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| <fc #cd5c5c>\ *bytesRead*\ </fc> -> Return data if read is successful
| Read data from a register, data as byte array

.. code:: csharp

   HResult ICRegisterRead( string ICName, int readAddress, int readNumberBytes, ref byte[] bytesRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| <fc #cd5c5c>\ *bytesRead*\ </fc> -> Return data if read is successful
| Read data from a register, specific device address

.. code:: csharp

   HResult ICRegisterRead( string ICName, int deviceAddress, int readAddress, int readNumberBytes, ref byte[] bytesRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC)
| <fc #cd5c5c>\ *deviceAddress*\ </fc> -> I2C or SPI address
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| <fc #cd5c5c>\ *bytesRead*\ </fc> -> Return data if read is successful
| Read data from a register, read value is return type

.. code:: csharp

   long ICRegisterRead( string ICName, int readAddress, int readNumberBytes );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| Read buffer of data from a register, read value array returned

.. code:: csharp

   byte[] ICRegisterRead( string ICName, int readAddress, int readNumberBytes, ref bool bRet );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The register address to read
| <fc #cd5c5c>\ *readNumberBytes*\ </fc> -> Number of bytes to read
| <fc #cd5c5c>\ *ret*\ </fc> -> Did the read succeed

Parameter Write
~~~~~~~~~~~~~~~

Write parameter data, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Write parameter data, specifying target fixed-point format and parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string icName, string paramName, int intbits, int fracbits, float valToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *paramName*\ </fc> -> The parameter name to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Write parameter data array, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int intbits, int fracbits, int writeNumParams, float[] valsToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valsToWrite*\ </fc> -> Parameter data values to write
| Write parameter data array, specifying target fixed-point format and parameter name instead of parameter address.

.. code:: csharp

    HResult ICParameterWrite(string icName, string paramName, int intbits, int fracbits, int writeNumParams, float[] valsToWrite)

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *paramName*\ </fc> -> The parameter name to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valsToWrite*\ </fc> -> Parameter data values to write
| Write parameter data, floating point value

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, float valToWrite )

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Write parameter data as floating point value using parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string ICName, string paramName, float valToWrite )

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *paramName*\ </fc> -> The parameter name to begin writing data
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Write multiple contiguous parameters, floating point value.

.. code:: csharp

   HResult ICParameterWrite( string ICName, int writeAddress, int writeNumParams, float[] valsToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valsToWrite*\ </fc> -> Parameter data values to write
| Write multiple contiguous parameters as floating point value using parameter name instead of parameter address.

.. code:: csharp

   HResult ICParameterWrite( string ICName, string paramName, int writeNumParams, float[] valsToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *paramName*\ </fc> -> The parameter name to begin writing data
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valsToWrite*\ </fc> -> Parameter data values to write
| Safeload parameter data, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Safeload parameter data array, specifying target fixed-point format

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int intbits, int fracbits, int writeNumParams, float[] dataToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *dataToWrite*\ </fc> -> Parameter data values to write
| Write parameter data via safeload, floating point value

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, float valToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valToWrite*\ </fc> -> Parameter data value to write
| Write multiple parameters via safeload, floating point values

.. code:: csharp

   HResult ICParameterSafeload( string ICName, int writeAddress, int writeNumParams, float[] valsToWrite );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| <fc #cd5c5c>\ *writeNumParams*\ </fc> -> Number of values in valsToWrite
| <fc #cd5c5c>\ *valsToWrite*\ </fc> -> Parameter data values to write
| Load comma-delineated byte data from a text file at a particular parameter/parameter

.. code:: csharp

   HResult ICLoadDataFile( string ICName, string filename, int writeAddress );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to write to
| <fc #cd5c5c>\ *filename*\ </fc> -> fully qualified filename of data file to load
| <fc #cd5c5c>\ *writeAddress*\ </fc> -> The parameter address to begin writing data
| ====Parameter Read==== Read fixed-point parameter data, read value returned as float

.. code:: csharp

   float ICParameterRead( string ICName, int readAddress, int intbits, int fracbits );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The parameter address to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| Read fixed-point parameter data using parameter name, read value returned as float

.. code:: csharp

   float ICParameterRead( string ICName, string paramName, int intbits, int fracbits );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *paramName*\ </fc> -> The name of the parameter to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| Read data from a parameter, data returned as float

.. code:: csharp

   HResult ICParameterRead( string ICName, int readAddress, int intbits,int fracbits, out float valRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The parameter address to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *valRead*\ </fc> -> returned read value
| Read fixed-point parameter data array, read values returned as float[]

.. code:: csharp

   float[] ICParameterRead( string ICName, int readAddress, int intbits, int fracbits, int readNumParams, ref bool bRet );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The parameter address to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *readNumParams*\ </fc> -> Number of values to read
| <fc #cd5c5c>\ *bRet*\ </fc> -> result, true if read was successful asdf
| Read fixed-point parameter data array using the parameter name, read values returned as float[]

.. code:: csharp

   float[] ICParameterRead( string ICName, string paramName, int intbits, int fracbits, int readNumParams, ref bool bRet );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *paramName*\ </fc> -> The name of the parameter to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *readNumParams*\ </fc> -> Number of values to read
| <fc #cd5c5c>\ *bRet*\ </fc> -> result, true if read was successful asdf
| Read fixed-point parameter data array, read values returned in float[]

.. code:: csharp

   HResult ICParameterRead( string ICName, int readAddress, int intbits, int fracbits, int readNumParams, ref float[] valsRead );

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *readAddress*\ </fc> -> The parameter address to read
| <fc #cd5c5c>\ *intbits*\ </fc> = number of integer (magnitude) bits <fc #cd5c5c>\ *fracbits*\ </fc> -> number of fraction bits
| <fc #cd5c5c>\ *readNumParams*\ </fc> -> Number of values to read
| <fc #cd5c5c>\ *valsRead*\ </fc> -> returned read values
| ====Parameter Address==== API returns all the parameters' name and addresses for a IC in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, out string[] names, out int[] addresses);

| <fc #cd5c5c>\ *icName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *names*\ </fc> -> Returns the array of parameters for the IC in the current schematic.
| <fc #cd5c5c>\ *addresses*\ </fc> Returns the array of parameter addresses corresponding to names[].
| API returns all the parameters' name and addresses for a cell/module in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, string cellName, out string[] names, out int[] addresses);

| <fc #cd5c5c>\ *icName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *cellName*\ </fc> -> Cell/Module's name in the schematic.
| <fc #cd5c5c>\ *names*\ </fc> -> Returns the array of parameters for the IC in the current schematic.
| <fc #cd5c5c>\ *addresses*\ </fc> Returns the array of parameter addresses corresponding to names[].
| API returns all the parameters' name and addresses for a cell/module in the current schematic.

.. code:: csharp

   HResult ICGetParamNamesAndAddresses(string icName, object cellObject, out string[] names, out int[] addresses);

| <fc #cd5c5c>\ *icName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *cellObject*\ </fc> -> Cell/Module's object.
| <fc #cd5c5c>\ *names*\ </fc> -> Returns the array of parameters for the IC in the current schematic.
| <fc #cd5c5c>\ *addresses*\ </fc> Returns the array of parameter addresses corresponding to names[].
| API returns the parameter's address for given parameter name

.. code:: csharp

   HResult ICGetParamAddress(string icName, string paramName, out int address);

| <fc #cd5c5c>\ *icName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *paramName*\ </fc> -> Parameter name.
| <fc #cd5c5c>\ *address*\ </fc> -> Returns the address of the parameter.
| API returns the parameter's name for given parameter address

.. code:: csharp

   HResult ICGetParamName(string icName, int address, out string paramName);

| <fc #cd5c5c>\ *icName*\ </fc> -> Friendly name of DSP(IC) to read from
| <fc #cd5c5c>\ *address*\ </fc> -> Parameter address.
| <fc #cd5c5c>\ *paramName*\ </fc> -> Returns the name of the parameter.

Insert
------

| The functions listed below are used to insert Schematic objects into a board.
| Insert an object into the active project, returns object reference

.. code:: csharp

   object ObjectInsert( string typeName );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| Insert an object into a specific open project, returns object reference

.. code:: csharp

   object ObjectInsert( string projectName, string typeName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| Insert an object into the active project at a specific position

.. code:: csharp

   object ObjectInsert( string typeName, Point pointInsert );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *pointInsert*\ </fc> -> System.Drawing.Point Schematic screen position
| Insert an object into a specific open project, at a specific position

.. code:: csharp

   object ObjectInsert( string projectName, string typeName, Point point );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *point*\ </fc> -> System.Drawing.Point Schematic screen coordinates
| Insert an object into the active project at a specific position

.. code:: csharp

   object ObjectInsert( string typeName, int X, int Y );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *X" & "Y*\ </fc> -> Schematic x- and y- coordinates to position the object
| Insert an object into a specific open project, at a specific position

.. code:: csharp

   object ObjectInsert( string projectName, string typeName, int X, int Y );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *X" & "Y*\ </fc> -> Schematic x- and y- coordinates to position the object
| Insert an object into the active project, returns an HResult

.. code:: csharp

   HResult ObjectInsert( string typeName, out string objectName );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object, null if insertion fails
| Insert an object into a specific open project, returns an HResult

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName,out string objectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object, null if insertion fails
| Insert an object into the active project at a specific position

.. code:: csharp

   HResult ObjectInsert( string typeName, Point point, out string objectName );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *point*\ </fc> -> System.Drawing.Point Schematic screen coordinates
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object, null if insertion fails
| Insert an object into a specific open project, at a specific position

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName,Point point, out string objectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *point*\ </fc> -> System.Drawing.Point Schematic screen coordinates
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object or null if insertion fails
| Insert an object into the active project at a specific position

.. code:: csharp

   HResult ObjectInsert( string typeName, int X, int Y, out string objectName );

| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *X" & "Y*\ </fc> -> Schematic x- and y- coordinates to position the object
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object, null if insertion fails
| Insert an object into a specific open project, at a specific position

.. code:: csharp

   HResult ObjectInsert( string projectName, string typeName, int X, int Y,out string objectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> an open project file’s name or fully qualified path
| <fc #cd5c5c>\ *typeName*\ </fc> -> object description (toolbox name)
| <fc #cd5c5c>\ *X" & "Y*\ </fc> -> Schematic x- and y- coordinates to position the object
| <fc #cd5c5c>\ *objectName*\ </fc> -> return name of inserted object, null if insertion fails
| NOTE: Schematic objects are inserted into the currently selected hierarchy board of ‘Schematic’ tab by default. Use ‘BlockObjectInsert’ function instead of ‘ObjectInsert’ function to insert Schematic objects into the ‘Block Schematic’ tab.
| =====Remove===== The functions below are used to remove objects from projects.
| Delete an object in the active project

.. code:: csharp

   HResult ObjectRemove( string objectName );

| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of object to delete
| Delete an object from a specific open project

.. code:: csharp

   HResult ObjectRemove( string projectName, string objectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of object to delete
| Delete an object in the active project

.. code:: csharp

   HResult ObjectRemove( object object );

| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to delete
| Delete an object from a specific open project

.. code:: csharp

   HResult ObjectRemove( string projectName, object object );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to delete
| =====Connection===== Use the functions below for connecting an object’s input and output in a project.
| Connect a pair of objects’ output to input in the active project

.. code:: csharp

   HResult ObjectConnect( string fromName, int fromOutPinIndex,string toName, int toInPinIndex );

| <fc #cd5c5c>\ *fromName*\ </fc> -> Name of object to connect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to connect FROM (zero-based)
| <fc #cd5c5c>\ *toName*\ </fc> -> Name of object to connect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to connect TO (zero-based)
| Connect a pair of objects’ outputs to inputs in a specific open project

.. code:: csharp

   HResult ObjectConnect( string projectName, string fromName,int fromOutPinIndex, string toName, int toInPinIndex);

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *fromName*\ </fc> -> Name of object to connect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to connect FROM (zero-based)
| <fc #cd5c5c>\ *toName*\ </fc> -> Name of object to connect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to connect TO (zero-based)
| Connect a pair of objects’ output to input in the active project

.. code:: csharp

   HResult ObjectConnect( object fromObject, int fromOutPinIndex,object toObject, int toInPinIndex );

| <fc #cd5c5c>\ *fromObject*\ </fc> -> Reference to object to connect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to connect FROM (zero-based)
| <fc #cd5c5c>\ *toObject*\ </fc> -> Reference to object to connect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to connect TO (zero-based)
| Connect a pair of objects’ output to input in a specific open project

.. code:: csharp

   HResult ObjectConnect( string projectName, object fromObject,int fromOutPinIndex, object toObject, int toInPinIndex );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *fromObject*\ </fc> -> Reference to object to connect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to connect FROM (zero-based)
| <fc #cd5c5c>\ *toObject*\ </fc> -> Reference to object to connect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to connect TO (zero-based)
| =====Disconnect===== The functions below are used to disconnect input and output from objects in a project.
| Disconnect output from input of a pair of objects in the active project

.. code:: csharp

   HResult ObjectDisconnect( string fromName, int fromOutPinIndex,string toName, int toInPinIndex );

| <fc #cd5c5c>\ *fromName*\ </fc> -> Name of object to disconnect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to disconnect FROM (zero-based)
| <fc #cd5c5c>\ *toName*\ </fc> -> Name of object to disconnect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to disconnect TO (zero-based)
| Disconnect output from input of a pair of objects in a specific open project

.. code:: csharp

   HResult ObjectDisconnect( string projectName, string fromName,int fromOutPinIndex, string toName, int toInPinIndex );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *fromName*\ </fc> -> Name of object to disconnect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to disconnect FROM (zero-based)
| <fc #cd5c5c>\ *toName*\ </fc> -> Name of object to disconnect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to disconnect TO (zero-based)
| Disconnect output from input of a pair of objects in the active project

.. code:: csharp

   HResult ObjectDisconnect( object fromObject, int fromOutPinIndex,object toObject, int toInPinIndex );

| <fc #cd5c5c>\ *fromObject*\ </fc> -> Reference to object to disconnect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to disconnect FROM (zero-based)
| <fc #cd5c5c>\ *toObject*\ </fc> -> Reference to object to disconnect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to disconnect TO (zero-based)
| Disconnect output from input of a pair of objects in a specific open project

.. code:: csharp

   HResult ObjectDisconnect( string projectName, object fromObject,int fromOutPinIndex, object toObject, int toInPinIndex );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *fromObject*\ </fc> -> Reference to object to disconnect FROM
| <fc #cd5c5c>\ *fromOutPinIndex*\ </fc> -> Output pin index to disconnect FROM (zero-based)
| <fc #cd5c5c>\ *toObject*\ </fc> -> Reference to object to connect TO
| <fc #cd5c5c>\ *toInPinIndex*\ </fc> -> Input pin index to disconnect TO (zero-based)
| =====Console/ File IO===== The following functions print any message given to the output window in the script editor.

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

| The functions below may be used to manage object properties.
| Manipulate an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectSetProperties( string opcode, string objectName, params object[] propertyParams );

| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to update
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Manipulate an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectSetProperties( string opcode, object object, params object[] propertyParams );

| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to update
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Manipulate an object's properties or parameters in a specific open project

.. code:: csharp

   HResult ObjectSetProperties( string projectName, string opcode, string objectName, params object[] propertyParams );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to update
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Manipulate an object's properties or parameters in a specific open project

.. code:: csharp

   HResult ObjectSetProperties( string projectName, string opcode, object object, params object[] propertyParams );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to update
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string opcode, string objectName, out object[] getPropVal,params object[] propertyParams );

| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to update
| <fc #cd5c5c>\ *getPropVal*\ </fc> -> Fetched property or parameters
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string opcode, object object, out object[] getPropVal, params object[] propertyParams );

| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to update
| <fc #cd5c5c>\ *getPropVal*\ </fc> -> Fetched property or parameters
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string projectName, string opcode, string objectName,out object[] getPropVal, params object[] propertyParams );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to update
| <fc #cd5c5c>\ *getPropVal*\ </fc> -> Fetched property or parameters
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| Fetch an object's properties or parameters in the active project

.. code:: csharp

   HResult ObjectGetProperties( string projectName, string opcode, object object, out object[] getPropVal,params object[] propertyParams );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *object*\ </fc> -> Reference to object to update
| <fc #cd5c5c>\ *getPropVal*\ </fc> -> Fetched property or parameters
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| The property interfaces require an opcode (Operation Code), which specifies the type of operation to be performed. Relevant opcodes depend on the type of object. Some opcodes apply to all objects (e.g. setPosition and setName); others are specific to particular object categories. Essential opcodes are listed in the table below:
| ^ Opcode ^ Type ^ PropertyParams^

+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setPosition*\ </fc>            | 1. System.Drawing.Point    | Screen position at which to centre the object |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setName*\ </fc>                | 1. System.String           | New name for object (must be unique)          |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *changeIC*\ </fc>               | 1. System.String           | Name of IC to associate with the Algorithm    |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. int (optional)          | Index of Algorithm to change                  |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *addAlgorithm*\ </fc>           | 1. Sytem.String (optional) | New name for object (must be unique)          |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. Sytem.String (optional) | Name of Algorithm to add                      |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *removeAlgorithm*\ </fc>        | NONE                       |                                               |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *growAlgorithm*\ </fc>          | 1. int                     | Index of Algorithm to grow                    |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. int                     | Amount to grow Algorithm                      |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *reduceAlgorithm*\ </fc>        | 1. int                     | Index of Algorithm to reduce                  |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. int                     | Amount to reduce Algorithm                    |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setSamplingRate*\ </fc>        | 1. int                     | New Module Sampling Rate                      |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setBlockSize*\ </fc>           | 1. int                     | New Source Module Block Size                  |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setControlValue*\ </fc>        | 1. int                     | Index of Algorithm                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. int                     | Repeat Index (Grow index)                     |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 3. System.String           | Control value name**\*                        |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 4. System.object           | Value to set                                  |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setBlockSize*\ </fc>           | 1. int                     | New Source Module Block Size                  |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setOutputBufferSize*\ </fc>    | 1. int                     | New Output Buffer Size in bytes               |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *setPCMxOutputBlockSize*\ </fc> | 1. int                     | New PCMx Output Module Block Size             |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *getBlockSize*\ </fc>           | 1. None                    | NA                                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *getSamplingRate*\ </fc>        | 1. None                    | NA                                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *getControlValue*\ </fc>        | 1. int                     | Index of Algorithm                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 2. int                     | Repeat Index (Grow index)                     |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
|                                               | 3. System.String           | Control value name                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+
| <fc #cd5c5c>\ *getCurrentGrowth*\ </fc>       | 1. int                     | Index of Algorithm                            |
+-----------------------------------------------+----------------------------+-----------------------------------------------+

| 
| Table 2: Opcode and Property Parameters
| NOTE: Control value names can be viewed as tooltip information. Please refer :doc:`Viewing Control Parameter Names . </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/paramuidataname>`
| =====Reflection Support===== The functions below may be used to access methods, properties and fields from SigmaStudio object using C# reflection.
| There are two kinds of object used in the SigmaStudio schematic modules. Cell Object and Algorithm Object. Cell object contains the GUI related information. Algorithm object contains algorithm related information. There can be multiple algorithm objects in a single cell object.

.. code:: csharp

   object GetCellObject(string objectName);
   object[] GetAlgorithmObjects(string objectName);

| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the Cell object.
| API uses the Reflection's GetProperty() method and returns the PropertyInfo for the module with the name 'objectName in the schematic. ObjectGetProperties() retuns all the public properties in the object.

.. code:: csharp

   PropertyInfo ObjectGetProperty(string objectName, string propertyName);
   PropertyInfo[] ObjectGetProperties(string objectName);

| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to get the properties info
| <fc #cd5c5c>\ *propertyName*\ </fc> -> Name of the property to get from the object.
| API uses the Reflection's GetField() method and returns the FieldInfo for the module with the name 'objectName in the schematic. ObjectGetFields() retuns all the public fields in the object.

.. code:: csharp

   FieldInfo ObjectGetField(string objectName, string fieldName);
   FieldInfo [] ObjectGetFields(string objectName);

| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to get the fields info
| <fc #cd5c5c>\ *fieldName*\ </fc> -> Name of the field to get from the object.
| API uses the Reflection's GetMethod() method and returns the MethodInfo for the module with the name 'objectName in the schematic. ObjecMethodss() returns all the public methods in the object.

.. code:: csharp

   MethodInfo ObjectGetMethod(string objectName, string methodName);
   MethodInfo [] ObjectGetMethods(string objectName);

| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to get the methods info
| <fc #cd5c5c>\ *methodName*\ </fc> -> Name of the method to get from the object.
| ====Examples==== The following shows an example of how to access the Checkbox in the mute module using refection.

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

| The function below may be used to manage SigmaStudio settings.
| Manipulate SigmaStudio settings in the active project

.. code:: csharp

   HResult DesignSettings(string cmd, params object[] arg);

| <fc #cd5c5c>\ *cmd*\ </fc> -> Command opcode of setting to modify
| <fc #cd5c5c>\ *arg*\ </fc> -> Modified value of the setting. This should be of string datatype
| ^ Command ^ Argument^

+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *XMLOnly*\ </fc>      | 1. "true" – Only XML file will get generated upon exporting                                                                                                                                                                                     |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     | 2. ”false” – Non XML system files will also get generated upon exporting                                                                                                                                                                        |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *SchematicTag*\ </fc> | “String” tag to be associated with the Schematic xml file. e.g. “SigmaStudioforSHARC - Version x_y_z1”                                                                                                                                          |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *Pre-build*\ </fc>    | The command to be executed before the Schematic is compiled.. e.g. “ssTestSettings.bat arg1”                                                                                                                                                    |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *Post-build*\ </fc>   | The command to be executed after the Schematic is compiled. e.g. “ssTestSettings.bat arg1”                                                                                                                                                      |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *Pre-export*\ </fc>   | The command to be executed before the export of a Schematic. e.g.“ssTestSettings.bat arg1”                                                                                                                                                      |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *Post-export*\ </fc>  | The command to be executed after the export of a Schematic. e.g.“ssTestSettings.bat arg1”                                                                                                                                                       |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *Auto-export*\ </fc>  | 1. ”false”, “D:\\\\test\\\\autoexport” – Auto export of system files after compile is disabled. The second string is the path where the export files should be generated. The path entered should be a valid one                                |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                     | 2. "true", “D:\\\\test\\\\autoexport” – Auto export of system files after compile is disabled. The second string is the path where the export files should be generated. The path entered should be a valid one.                                |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| <fc #cd5c5c>\ *ToolSel*\ </fc>      | This should be the full name of the tool- chain (as available in the Tools -> Settings -> SHARC -> Tool-chain list) to be used for Schematic compilation. e.g.“CrossCore Embedded Studio for Analog Devices Processors v1.0.3”“VisualDSP++ 5.1” |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

| 
| Table 3: Command and Arguments for Settings API
| 1 x.y.z denotes the version of SigmaStudio for SHARC. Refer Release Notes for version information of SigmaStudio for SHARC
| Manipulate properties in the IC Control window

.. code:: csharp

   HResult SetICControlProperties(string ICName, string cmd, object arg);

| <fc #cd5c5c>\ *ICName*\ </fc> -> Friendly name of DSP(IC) to be modified
| <fc #cd5c5c>\ *cmd*\ </fc> -> Command opcode of property to modify
| <fc #cd5c5c>\ *arg*\ </fc> -> Modified value of the setting
| ^ Command ^ Type ^ Argument ^

+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *MaxInChannels*\ </fc>   | int    | Number of input channels                            |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *MaxOutChannels*\ </fc>  | int    | Number of output channels                           |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *MasterBypass*\ </fc>    | bool   | true - Master Bypass enabled                        |
+----------------------------------------+--------+-----------------------------------------------------+
|                                        |        | false - Master Bypass disabled                      |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *DefaultCore*\ </fc>     | bool   | true - Core 1 enabled                               |
+----------------------------------------+--------+-----------------------------------------------------+
|                                        |        | false - Core 2 enabled                              |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *TargetBuildMode*\ </fc> | bool   | true - Debug mode enabled                           |
+----------------------------------------+--------+-----------------------------------------------------+
|                                        |        | false – Release mode enabled                        |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *BlockSize*\ </fc>       | int    | Blocksize value (8 or multiple of 8)                |
+----------------------------------------+--------+-----------------------------------------------------+
| <fc #cd5c5c>\ *LoadAppDXE*\ </fc>      | string | The Application DXE, to be selected, with full path |
+----------------------------------------+--------+-----------------------------------------------------+

| Table 4: Command and Argument for Modify IC Control Window Properties API
| =====Plug-Ins===== The function given below may be used to manipulate Plug-Ins.
| Enable or disable a Plug-In added to the SigmaStudio Add-Ins window

.. code:: csharp

   HResult ModifyPlugInState ( string plugin, bool state);

| <fc #cd5c5c>\ *plugin*\ </fc> -> name of the Plug-In as string
| <fc #cd5c5c>\ *state*\ </fc> -> “True” or “False” indicating whether to ‘enable’ or ‘disable’ Plug-In
| The first argument, which is the name of the Plug-In, can either be the full path of the Plug-In DLL as listed in the Add-Ins list or only the file name of the Plug-In DLL. SigmaStudio will first try to match the argument string against full path of the Plug-Ins in the Add-Ins list. If a match is not found, the string is matched against the file name of the Plug-Ins. If multiple Plug-Ins with the name passed as argument are present in the Add-Ins list, only the first occurrence in the list is modified by this function. The Plug-In name is case insensitive.
| =====Float Packets Interface=====

ICParameterSafeload
~~~~~~~~~~~~~~~~~~~

| 
| The function has two overloaded methods as shown in prototype-1 and prototype-2 given below.
| This is an API to handle floating point packets and hence is applicable for SHARC only.
| ===Prototype-1===

.. code:: csharp

   HResult ICParameterSafeload ( string ICname, int32 WriteAddress, single DataToWrite)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method sends a parameter data to the address specified by the write address for the specified IC. The parameters will be loaded to the target using the “Safeload” mechanism.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC to which data is to be sent
| Name:WriteAddress
| Type:int32
| Description:Offset address location to which the parameter needs to be written
| Name:DataToWrite
| Type:Single
| Description:Single precision floating point parameter value to be written to target memory.
| ===Prototype-2===

.. code:: csharp

   HResult ICParameterSafeload ( string ICname, int32 WriteAddress, int32 WriteNumParams, single[] DataToWrite)

| <fc #6495ed>\ *Description*\ </fc>
| The method sends an array of parameter data of size “WriteNumParams” to the address specified by the write address for the specified IC. The parameters will be loaded to the target using the “Safeload” mechanism.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC to which data is to be sent
| Name:WriteAddress
| Type:int32
| Description:Offset address location to which the parameter needs to be written
| Name:WriteNumParams
| Type:int32
| Description:Number of parameters to be written to target parameter memory
| Name:DataToWrite
| Type:Single
| Description:Single precision floating point array of parameter values to be written to target parameter memory.
| ====ICParameterWrite====
| The function has two overloaded methods as shown in prototype-1 and prototype-2 given below.
| This is an API to handle floating point packets and hence is applicable for SHARC only.
| ===Prototype-1===

.. code:: csharp

   HResult ICParameterWrite ( string ICname, int32 WriteAddress, single DataToWrite)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method sends a parameter data to the address specified by the write address for the specified IC. The parameters will be loaded to the target without “Safeload” mechanism.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC to which data is to be sent
| Name:WriteAddress
| Type:int32
| Description:Offset address location to which the parameter needs to be written
| Name:DataToWrite
| Type:Single
| Description:Single precision floating point parameter value to be written to target memory.
| ===Prototype-2===

.. code:: csharp

   HResult ICParameterWrite ( string ICname, int32 WriteAddress, int32 WriteNumParams, single[] DataToWrite)

| <fc #6495ed>\ *Description*\ </fc>
| The method sends an array of parameter data of size “WriteNumParams” to the address specified by the write address for the specified IC. The parameters will be loaded to the target as a block without using the “Safeload” mechanism.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC to which data is to be sent
| Name:WriteAddress
| Type:int32
| Description:Offset address location to which the parameter needs to be written
| Name:WriteNumParams
| Type:int32
| Description:Number of parameters to be written to target parameter memory
| Name:DataToWrite
| Type:Single
| Description:Single precision floating point array of parameter values to be written to target parameter memory.
| ====ICParameterRead====
| This is an API to handle floating point packets and hence is applicable for SHARC only.
| ===Prototype===

.. code:: csharp

   float ICParameterRead ( string ICname, int32 readAddress)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method reads a parameter data from the address specified by the read address for the specified IC.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC from which data is to be read
| Name:readAddress
| Type:int32
| Description:Offset address location from parameter memory from where the parameter needs to be read
| =====SHARCTargetBoot=====
| This is applicable only for the SHARC target, where booting using a Loader File is applicable.
| ===Prototype===

.. code:: csharp

   HResult SHARCTargetBoot (string ICName, string fileName, ArrayList bootArgs)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method is used to boot the SHARC Target with a Loader File.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC which should be booted
| Name:Filename
| Type:String
| Description:Full path of the LDR file
| Name:bootArgs
| Type:ArrayList
| Description:Arguments for boot configuration ArrayList with the boot option (2, 3, 4, 5 or 10) as the first entry 2: Analog-In 3: Digital-In 4: Digital-Out alone 5: Analog\\Digital Co-existence 10: Analog\\Digital Co-existence (Digital Clock)
| =====SHARCReadMIPS=====
| This API is applicable only for the SHARC target, to get the MIPS information from the target.
| ===Prototype===

.. code:: csharp

   float SHARCReadMIPS (string ICName)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Read MIPS consumed by the SHARC Target hardware.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC from which to read the MIPS
| =====SHARCReadLibVersion=====
| This API is applicable for SHARC target only, to fetch the target library version from the target.
| ===Prototype===

.. code:: csharp

   uint SHARCReadLibVersion (string ICName)

| 
| <fc #6495ed>\ *Description*\ </fc>
| The method is used to read version number of the Target Library running on SHARC Target processor.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: ICname
| Type: String
| Description:Name of the IC from which the version should be obtained

General Functions
-----------------

| A list of general functions and their prototypes are given below.
| ====Undo==== Undo an action in active project file

.. code:: csharp

   HResult ScriptUndo();

| 
| Undo an action in specific project file

.. code:: csharp

   HResult ScriptUndo( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| ====Redo==== Redo an action in active project file

.. code:: csharp

   HResult ScriptRedo();

Redo an action in specific project file

.. code:: csharp

   HResult ScriptRedo( string projectName );

| <fc #cd5c5c>\ *projectName*\ </fc> -> An open project file’s name or fully qualified path
| ====Pause==== Pause script execution for delay Milliseconds

.. code:: csharp

   HResult ScriptDelay( int delayMilliseconds );

| <fc #cd5c5c>\ *delayMilliseconds*\ </fc> -> Amount of delay in milliseconds
| ====Run==== Run script

.. code:: csharp

   HResult ScriptRun( string script );

| <fc #cd5c5c>\ *script*\ </fc> -> script code as a System.String
| Run script file

.. code:: csharp

   HResult ScriptRunFile( string scriptFilename );


   | <fc #cd5c5c>\ *scriptFilename*\ </fc> -> The fully qualified script file name

Pause and Resume Options
~~~~~~~~~~~~~~~~~~~~~~~~

|

| =====USBiReset=====

.. code:: csharp

   HResult ResetUSBInterface();

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Reset the USBi interface
| =====GetIcNames=====

.. code:: csharp

   ArrayList GetIcNames();

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Gets IcName in the schematic
| =====Selfboot Options=====

Selfboot Port settings
^^^^^^^^^^^^^^^^^^^^^^

.. code:: csharp

   SELFBOOT_PORT_SETTINGS(string cellName, int[] values);

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to settings the E2prom port through server/script
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: Cellname
| Type: String
| <fc #6495ed>\ *Description*\ </fc>
| Cell name of SigmaDSP IC example: "IC 1"
| Name: PORT_SETTINGS
| Type: int

Example for Python :
""""""""""""""""""""

| 
| PORT_SETTINGS = VARIANT(pythoncom.VT_ARRAY\| pythoncom.VT_I4, [1048576,0x03,0x02,0x03,0x06,0xc7,10,10000,256,1,0])
| ==Example for .sss:==
| System.Collections.Generic.List<int> PORT_SETTINGS = new System.Collections.Generic.List<int>();
| PORT_SETTINGS.Add(1048576);
| PORT_SETTINGS.Add(0x03);
| PORT_SETTINGS.Add(0x02);
| PORT_SETTINGS.Add(0x03);
| PORT_SETTINGS.Add(0x06);
| PORT_SETTINGS.Add(0xc7);
| PORT_SETTINGS.Add(10);
| PORT_SETTINGS.Add(10000);
| PORT_SETTINGS.Add(256);
| PORT_SETTINGS.Add(1);
| PORT_SETTINGS.Add(0);

Selfboot write
^^^^^^^^^^^^^^

.. code:: csharp

   SELFBOOTWRITE(string cellName, string writeThrough);

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to write through "DSP" or "USB" (USB currently not supported)

Selfboot Export
^^^^^^^^^^^^^^^

.. code:: csharp

   EXPORT_SELFBOOT_DATA(bool readThroughDSP, string fullyQualifiedFileName);

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Export the Selfboot data from E2PROM.
| <fc #6495ed>\ *Parameters*\ </fc>
| Name: projectexportFile
| Type: String
| <fc #6495ed>\ *Description*\ </fc>
| stored the .Hex file on this path

Selfboot Erase
^^^^^^^^^^^^^^

.. code:: csharp

   SELFBOOTERASE(string cellName);

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Erase the E2PROM.
| ====Examples====

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

| <fc #6495ed>\ *Description*\ </fc>
| The method is used to Write / from Read the values of the parameter to/from IPAT Address.
| <fc #6495ed>\ *<fc #6495ed>Parameters</fc>*\ </fc>
| Type & Name: int numOfBytesToWrite
| <fc #6495ed>\ *Description*\ </fc>
| Number of bytes in 'dataToWrite' to write to the dsp
| Type & Name: int writeToData
| <fc #6495ed>\ *Description*\ </fc>
| The data to write
| Type & Name: int ipatWriteAddress
| <fc #6495ed>\ *Description*\ </fc>
| Indirect address of the parameter to be load
| Type & Name: int \_numOfLoadsAndTriggers
| <fc #6495ed>\ *Description*\ </fc>
| Number of consecutive loads
| Type & Name: int protocol
| <fc #6495ed>\ *Description*\ </fc>
| Serial prorotcol to transfer the data
| Type & Name: int chipAddress
| <fc #6495ed>\ *Description*\ </fc>
| I2C - Load Address, SPI - Address is zero
| Type & Name: int addressOfStartAddress
| <fc #6495ed>\ *Description*\ </fc>
| Address of the IPAT StartAddress
| Type & Name: int addressWidth
| <fc #6495ed>\ *Description*\ </fc>
| The width of address
| Type & Name: int registerByteLength
| <fc #6495ed>\ *Description*\ </fc>
| address increment
| Type & Name: int communicationChannel
| <fc #6495ed>\ *Description*\ </fc>
| The commumnication channel USBi/AARDVARK
| Type & Name: int ICType

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/scripting/script1.jpg
   :width: 400px
