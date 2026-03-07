:doc:`Click here to return to 'SigmaStudio Scripting' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/scripting>`

SigmaStudioServer
=================

| An automation client can be used to access the objects, properties, methods, and events associated with the SigmaStudioServer interface. SigmaStudioServer is a .NET server as well as an ActiveX server.
| To access the server interface, SigmaStudio and the client application have to be launched on the same PC, and then the client application has to point to the Analog.SigmaStudioServer.dll which is installed alongside SStudio.exe in the SigmaStudio program folder.
| =====SigmaStudioServer Commands (ISigmaStudioServer)===== Once the server interface is launched, the following commands are available for use.
| ====NEW_PROJECT==== Start a new SigmaStudio project

.. code:: csharp

   bool NEW_PROJECT();

| 
| ====OPEN_PROJECT==== Open a SigmaStudio project file (\*.dspproj)

.. code:: csharp

   Bool OPEN_PROJECT( string fullyQualifiedFileName );

| 
| ====COMPILE_PROJECT==== Compile (compile,link,download) the active SigmaStudio project

.. code:: csharp

   bool COMPILE_PROJECT();

| 
| ====LINK==== Link the active SigmaStudio project

.. code:: csharp

   bool LINK();

| 
| ====COMPILE==== Compile the active SigmaStudio project

.. code:: csharp

   bool COMPILE();

| 
| ====DOWNLOAD==== Download the active SigmaStudio project

.. code:: csharp

   bool DOWNLOAD();

| 
| ====COMPILE_PROJECT_NAME==== Link/Compile/Download the SigmaStudio project, specified as an .NET CLR compatible System.String

.. code:: csharp

   bool COMPILE_PROJECT_NAME( string projectName );

| 
| ====CLOSE_PROJECT==== Close the active SigmaStudio project

.. code:: csharp

   bool CLOSE_PROJECT();

| 
| ====CLOSE_PROJECT_NAME==== Close SigmaStudio project by project name

.. code:: csharp

   bool CLOSE_PROJECT_NAME( string projectName );

| 
| ====SAVE_PROJECT==== Save the active SigmaStudio project

.. code:: csharp

   bool SAVE_PROJECT();

| 
| ====SAVEAS_PROJECT==== Save the active SigmaStudio project under the mentioned name

.. code:: csharp

   bool SAVEAS_PROJECT( string saveAsFileName );

| 
| ====SAVE_PROJECT_NAME==== Save a SigmaStudio project to file

.. code:: csharp

   bool SAVE_PROJECT_NAME( string projectName );

| 
| ====SAVEAS_PROJECT_NAME==== Save a SigmaStudio project under the mentioned name

.. code:: csharp

   bool SAVEAS_PROJECT_NAME( string projectName, string saveAsFileName );

| 
| ====SET_ACTIVE_PROJECT==== Set a specified SigmaStudio project as the active project

.. code:: csharp

   bool SET_ACTIVE_PROJECT( string projectName );

| 
| ====SET_ACTIVE_BOARD==== Set a specified SigmaStudio board as the active board

.. code:: csharp

   bool SET_ACTIVE_BOARD( string boardName );

| 
| ====SET_SAMPLING_RATE==== Set Schematic Sampling Rate for the SigmaStudio project

.. code:: csharp

   bool SET_SAMPLING_RATE( int samplingRate );

| 
| ====PROPAGATE_SAMPLING_RATE==== Propagate the Schematic Sampling Rate across the Schematic

.. code:: csharp

   bool PROPAGATE_SAMPLING_RATE();

| 
| ====SET_BLOCK_SIZE==== Set Block Size for the SigmaStudio project

.. code:: csharp

   bool SET_BLOCK_SIZE ( string ICname, int nSize );

| 
| ====TOGGLE_FREEZE_SCHEMATIC==== Toggle the Freeze/Unfreeze state of the schametic

.. code:: csharp

   bool TOGGLE_FREEZE_SCHEMATIC( string password );

| 
| ====DELAY_SCRIPT==== Delay a SigmaStudio script for period specified as an argument

.. code:: csharp

   bool DELAY_SCRIPT( int delayMilliseconds );

| 
| ====SET_TIMEOUT==== Set SigmaStudio Server API wait timeout for the script. The default timeout set as 30 sec.

.. code:: csharp

   bool   SET_TIMEOUT( int timeOutSeconds );

| 
| ====REGISTER_WRITE_BYTES==== Write bytes to IC register(s) (active project must be compiled and downloaded)

.. code:: csharp

   bool REGISTER_WRITE_BYTES(int numOfBytesToWrite, byte[] writeToData, int protocol, int chipAddress, int writeAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

| 
| ====REGISTER_WRITE==== Write to IC register (active project must be compiled and downloaded)

.. code:: csharp

   bool REGISTER_WRITE( string ICName, int writeAddess, int numBytesToWrite, int dataToWrite );

| 
| ====REGISTER_WRITE_ARRAY==== Write data array to IC regster(s)

.. code:: csharp

   bool REGISTER_WRITE_ARRAY( string ICName, int writeAddress, int numBytesToWrite, byte[] aDataToWrite );

| 
| ====REGISTER_READ_BYTES==== Read bytes of data from an IC register(s) (active project must be compiled and downloaded)

.. code:: csharp

   byte[] REGISTER_READ_BYTES(int numOfBytesToRead, int protocol, int chipAddress, int readAddress, int addressWidth, int registerByteLength, int communicationChannel, int ICType);

| 
| ====REGISTER_READ==== Read from an IC register (active project must be compiled and downloaded)

.. code:: csharp

   long REGISTER_READ( string ICName, int readAddess, int readNumberBytes );

| 
| ====REGISTER_READ_ARRAY==== Read array of data from an IC register(s)

.. code:: csharp

   byte[] REGISTER_READ_ARRAY( string ICName, int readAddress, int readNumberBytes );

| 
| ====REGISTER_SAFELAOD_WRITE==== Safeload write data to IC register

.. code:: csharp

   bool REGISTER_SAFELAOD_WRITE( string ICName, int writeAddress, int numBytesToWrite, int dataToWrite );

| 
| ====REGISTER_SAFELAOD_ARRAY==== Safeload write data array to IC regster(s)

.. code:: csharp

   bool REGISTER_SAFELAOD_ARRAY( string ICName, int writeAddress, int numBytesToWrite, byte[] aDataToWrite );

| 
| ====PARAMETER_WRITE==== Write value to a Parameter, SStudio handles conversion

.. code:: csharp

   bool PARAMETER_WRITE( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

| 
| ====PARAMETER_WRITE_USING_NAME==== Write value to a Parameter using the parameter's name, SStudio handles conversion

.. code:: csharp

   bool PARAMETER_WRITE_USING_NAME(string icName, string paramName, int intbits, int fracbits, float dataToWrite);

| 
| ====PARAMETER_WRITE_ARRAY==== Write parameters values, SStudio handles conversion

.. code:: csharp

   bool PARAMETER_WRITE_ARRAY( string ICName, int writeAddress, int intbits, int fracbits, int numValsToWrite, float[] aValsToWrite );

| 
| ====PARAMETER_WRITE_ARRAY_USING_NAME==== Write parameters values, SStudio handles conversion

.. code:: csharp

   bool PARAMETER_WRITE_ARRAY_USING_NAME( string ICName, string paramName, int intbits, int fracbits, int numValsToWrite, float[] aValsToWrite );

| 
| ====PARAMETER_WRITE_FLOAT==== Write value to a Parameter as float

.. code:: csharp

   bool PARAMETER_WRITE_FLOAT( string ICName, int writeAddress, float valToWrite );

| 
| ====PARAMETER_WRITE_FLOAT_USING_NAME==== Write value to a Parameter as float using the parameter name instaed of the parameter address.

.. code:: csharp

   bool PARAMETER_WRITE_FLOAT_USING_NAME( string ICName, string paramName, float valToWrite );

| 
| ====PARAMETER_WRITE_ARRAY_FLOAT==== Write parameter values as float

.. code:: csharp

   bool PARAMETER_WRITE_ARRAY_FLOAT( string ICName, int writeAddress, int numValsToWrite, float[] aValsToWrite );

| 
| ====PARAMETER_WRITE_ARRAY_FLOAT_USING_NAME==== Write parameter values as float using the parameter name

.. code:: csharp

   bool PARAMETER_WRITE_ARRAY_FLOAT_USING_NAME( string ICName, string paramName, int numValsToWrite, float[] aValsToWrite );

| 
| ====PARAMETER_READ==== Read parameter value from a register

.. code:: csharp

   float PARAMETER_READ( string ICName, int readAddress, int intbits, int fracbits );

| 
| ====PARAMETER_READ_USING_NAME==== Read parameter value from a register

.. code:: csharp

   float PARAMETER_READ( string ICName, string paramName, int intbits, int fracbits );

| 
| ====PARAMETER_READ_FLOAT==== Read float parameter value from a register

.. code:: csharp

   float PARAMETER_READ_FLOAT( string ICName, int readAddress );

| 
| ====PARAMETER_READ_FLOAT_USING_NAME==== Read float parameter value from a register using the paramete name

.. code:: csharp

   float PARAMETER_READ_FLOAT_USING_NAME( string ICName, string paramName);

| 
| ====PARAMETER_READ_ARRAY==== Read array of parameters

.. code:: csharp

   float[] PARAMETER_READ_ARRAY( string ICName, int readAddress, int intbits, int fracbits, int numValsToRead );

| 
| ====PARAMETER_READ_ARRAY_USING_NAME==== Read array of parameters

.. code:: csharp

   float[] PARAMETER_READ_ARRAY_USING_NAME( string ICName, string paramName, int intbits, int fracbits, int numValsToRead );

| 
| ====PARAMETER_SAFELAOD_WRITE==== Write parameter value via safeload

.. code:: csharp

   bool PARAMETER_SAFELAOD_WRITE( string ICName, int writeAddress, int intbits, int fracbits, float valToWrite );

| 
| ====PARAMETER_SAFELAOD_ARRAY==== Write data to parameters via safeload

.. code:: csharp

   bool PARAMETER_SAFELAOD_ARRAY( string ICName, int writeAddress, int intbits, int fracbits, int numValsToWrite, float[] aValsToWrite );

| 
| ====PARAMETER_SAFELOAD_WRITE_FLOAT==== Write parameter value via safeload as float

.. code:: csharp

   bool PARAMETER_SAFELOAD_WRITE_FLOAT( string ICName, int writeAddress, float valToWrite );

| 
| ====PARAMETER_SAFELOAD_ARRAY_FLOAT==== Write data to parameters via safeload as float

.. code:: csharp

   bool PARAMETER_SAFELOAD_ARRAY_FLOAT( string ICName, int writeAddress, int numValsToWrite, float[] aValsToWrite );

| 
| ====RUN_SCRIPT==== Run SigmaStudio script

.. code:: csharp

   bool RUN_SCRIPT( string script );

| 
| ====RUN_SCRIPT_FILE==== Open and Run SigmaStudio script file

.. code:: csharp

   bool RUN_SCRIPT_FILE( string fullyQualifiedFileName );

| 
| ====UNDO_SCRIPT==== Undo the last operation performed on active SigmaStudio project

.. code:: csharp

   bool UNDO_SCRIPT();

| 
| ====REDO_SCRIPT==== Redo the last operation on active SigmaStudio project

.. code:: csharp

   bool REDO_SCRIPT();

| 
| ====UNDO_SCRIPT_PROJECT==== Undo the last operation performed on SigmaStudio project

.. code:: csharp

   bool UNDO_SCRIPT_PROJECT( string projectName );

| 
| ====REDO_SCRIPT_PROJECT==== Redo the last operation on SigmaStudio project

.. code:: csharp

   bool REDO_SCRIPT_PROJECT( string projectName );

| 
| ====SET_LOGGING_MODE==== Auto dismiss all error,warning, and notifications and log messages to a file

.. code:: csharp

   bool SET_LOGGING_MODE( bool enabled );

| 
| ====INSERT_OBJECT==== Insert an object to Schematic

.. code:: csharp

   bool INSERT_OBJECT( string objectTypeName );

| 
| ====INSERT_OBJECT_POINT==== Insert an object to Schematic at specified location

.. code:: csharp

   bool INSERT_OBJECT_POINT( string objectTypeName, int pointX, int pointY );

| 
| ====INSERT_BLOCKOBJECT==== Insert a block object to Schematic

.. code:: csharp

   bool INSERT_BLOCKOBJECT( string objectTypeName );

| 
| ====INSERT_BLOCKOBJECT_POINT==== Insert a block object to Schematic at specified location

.. code:: csharp

   bool INSERT_BLOCKOBJECT_POINT( string objectTypeName, int pointX, int pointY );

| 
| ====REMOVE_OBJECT==== Remove an object from a Schematic

.. code:: csharp

   bool REMOVE_OBJECT( string objectName );

| 
| ====CONNECT_OBJECT==== Establish connection betweenn pins belonging to two objects

.. code:: csharp

   bool CONNECT_OBJECT( string fromObjectName, int fromOutPinIndex, string toObjectName, int toInPinIndex );

| 
| ====DISCONNECT_OBJECT==== Remove a connection betweenn two objects

.. code:: csharp

   bool DISCONNECT_OBJECT( string fromObjectName, int fromOutPinIndex, string toObjectName, int toInPinIndex);

| 
| ====SET_OBJECT_PROPERTY==== Manage the properties of the objects on the active praoject

.. code:: csharp

   bool SET_OBJECT_PROPERTY( string opcode, string objectName, params object[] propertyParams);

| 
| ====EXPORT_SYSTEM_FILES==== Export the system files of the active project

.. code:: csharp

   bool EXPORT_SYSTEM_FILES( string fullyQualifiedFileName );

| 
| ====BUILD_DESIGNER_DLL==== Generate SigmaStudio plugin using Algorithm Designer

.. code:: csharp

   bool BUILD_DESIGNER_DLL( string ICName, string fullyQualifiedProjectName, string fullyQualifiedLibraryName );

| 
| ====BOOT_SHARC==== Boot SHARC with a loader (\*.ldr) file

.. code:: csharp

   bool BOOT_SHARC( string ICName, string fullyQualifiedFileName );

| 
| ====READ_MIPS_SHARC==== Read MIPS consumed by the Target SHARC hardware

.. code:: csharp

   float READ_MIPS_SHARC( string ICName );

| 
| ====READ_VERSION_SHARC==== Read version number of the software running on target SHARC processor

.. code:: csharp

   uint READ_VERSION_SHARC( string ICName );

| 
| ====MODIFY_DESIGN_SETTINGS==== Modify SigmaStudio settings

.. code:: csharp

   bool MODIFY_DESIGN_SETTINGS ( string cmd, params object[] arg );

| 
| ====MODIFY_IC_CONTROL_PROPERTIES==== Modify IC Control window properties

.. code:: csharp

   bool MODIFY_IC_CONTROL_PROPERTIES ( string ICName, string cmd, object arg );

| 
| ====MODIFY_PLUGIN_STATUS==== Enable or Disable a Plug-In in the Add-Ins Window

.. code:: csharp

   bool MODIFY_PLUGIN_STATUS ( string plugin, bool state );

| 
| ====GET_OBJECT_PROPERTY==== Fetch the properties of the objects on the active project\ ``bool GET_OBJECT_PROPERTY(string opcode, string objectName, out object[] getPropVal, params object[] propertyParams)``
| <fc #cd5c5c>\ *opcode*\ </fc> -> Opcode of function to perform (see below)
| <fc #cd5c5c>\ *objectName*\ </fc> -> Name of the object to update
| <fc #cd5c5c>\ *getPropVal*\ </fc> -> Fetched property or parameters
| <fc #cd5c5c>\ *propertyParams*\ </fc> -> Parameters associated with the specified opcode
| The property interface require an opcode (Operation Code), which specifies the type of operation to be performed. Essential opcodes are listed in the table below:
| ^ Opcode ^ Type ^ PropertyParams^

+-----------------------------------------+------------------+---------------------------+
| <fc #cd5c5c>\ *getBlockSize*\ </fc>     | 1. None          | NA                        |
+-----------------------------------------+------------------+---------------------------+
| <fc #cd5c5c>\ *getSamplingRate*\ </fc>  | 1. None          | NA                        |
+-----------------------------------------+------------------+---------------------------+
| <fc #cd5c5c>\ *getControlValue*\ </fc>  | 1. int           | Index of Algorithm        |
+-----------------------------------------+------------------+---------------------------+
|                                         | 2. int           | Repeat Index (Grow index) |
+-----------------------------------------+------------------+---------------------------+
|                                         | 3. System.String | Control value name        |
+-----------------------------------------+------------------+---------------------------+
| <fc #cd5c5c>\ *getCurrentGrowth*\ </fc> | 1. int           | Index of Algorithm        |
+-----------------------------------------+------------------+---------------------------+

**NOTE:** Control value names can be viewed as tooltip information. Please refer :doc:`Viewing Control Parameter Names . </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/paramuidataname>`
