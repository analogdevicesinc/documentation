:doc:`Return to the specifications page </wiki-migration/resources/tools-software/sigmastudiov2/specifications>`

Export System Files
===================

Refer to :doc:`SigmaStudio+ Settings </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/settings>` for details on the export file naming convention.

``SigmaStudioFW.h``: This file contains user-editable functions to communicate with the DSP. This file is required by SigmaStudio+ export files.

Following are the SigmaStudio+ export files:

-  ``<naming convention>.h``: Contains default control register addresses and values, as well the default_download() function used to program the DSP. The default_download() function executes the exact same flow as “Link-Compile-Download” in SigmaStudio+.
-  ``<naming convention>.param``: Lists all schematic algorithm parameters names, memory addresses, and values.
-  ``<naming convention>_Defines.h``: Contains pre-compiler definitions related to the download packets.
-  ``<naming convention>_NumBytes.dat``: Lists the size (number of bytes) of control registers and default_download() functions used to program the DSP.
-  ``<naming convention>_PARAM.h``: Contains useful information about algorithm parameters including 'Default values', 'Addresses', Which memory page the parameter is on (for ADAU146x) etc.
-  ``<naming convention>_REG.h``: Contains similar information to the \_PARAM.h file above, but for control registers instead of algorithm parameters.
-  ``<naming convention>_TxBuffer.dat``: Lists all the buffer raw byte values in hexadecimal format
-  ``<naming convention>_TxMetaBuffer.dat``: Contains similar information to the \_TxBuffer.dat file above, however with additional parameter metadata information.
-  ``<processor name>_NetList.xml``: Contains details regarding how different modules are linked in the signal-flow

diagram.

-  ``<processor name>.xml``: Contains the details of modules and their parameters present in the signal-flow diagram.
-  ``<processor name>_Target.xml``: This is similar to the above xml file. However, the data buffers are updated with the protocol packetizations, if applicable, as written to the target.
-  ``<processor name>.json``: Contains the details of modules and their parameters present in the signal-flow diagram in JSON format.

| 
| ===== Netlist File ===== <IC> is the root element of the Netlist file.

<IC>
----

-  **name** - name of the IC.
-  **partnumber** - part number of the IC.
-  **<Core>** - one or more <Core> elements each representing the processing cores within the processor/IC.

<Core>
------

-  **name** - unique id of the core.
-  **coreid** - core id
-  **<Schematic>** - one or more <Schematic> elements each representing the signal flow diagram executing on the core.

<Schematic>
-----------

-  **name** - unique id of the schematic.
-  **<Algorithm>** - one or more <Algorithm> elements each representing the connected algorithm modules in the schematic.

<Algorithm>
-----------

-  **name** - unique id of the algorithm.
-  **friendlyname** - description of the algorithm.
-  **<Link>** - one or more <Link> elements each representing the input or output connections of the module.

<Link>
------

-  **pin** - name of the pin.
-  **dir** - indicates whether this is input or output pin.
-  **link** - name of the link.
-  **id** - unique id of the link.

| 
| ===== XML File ===== <IC> is the root element of the XML file.

.. _ic-1:

<IC>
----

-  **<Name>** - name of the IC
-  **<PartNumber>** - part number of the IC
-  **<Core>** - cores within the IC/processor.

.. _core-1:

<Core>
------

-  **<Name>** - unique id of the core.
-  **<CoreID>** - core id.
-  **<Schematic>** - schematics within the core.

.. _schematic-1:

<Schematic>
-----------

-  **<Name>** - unique id of the schematic.
-  **<Meta>** - metadata buffers of the schematic.
-  **<Register>** - registers writes.
-  **<Program>** - program buffer.
-  **<Parameter>** - parameter buffer.
-  **<Module>** - modules present in the schematic.

<Meta>
------

-  **<Name>** - name of the meta-data buffer.
-  **<AddrIncr>** - register byte length.
-  **<Size>** - size of data in bytes.
-  **<Data>** - data represented in hexadecimal format.

<Register>
----------

-  **<Name>** - name of the register.
-  **<Address>** - address of the register. 0 in case of Delay.
-  **<AddrIncr>** - register length. 0 in case of Delay.
-  **<Size>** - size of data in bytes.
-  **<Data>** - data represented in hexadecimal format.

<Program>
---------

-  **<Name>** - name of the program buffer.
-  **<Address>** - address of the program buffer.
-  **<AddrIncr>** - word length in bytes.
-  **<Size>** - size of the program buffer in bytes.
-  **<Data>** - program data represented in hexadecimal format.

<Parameter>
-----------

-  **<Name>** - name of the parameter buffer.
-  **<Address>** - address of the parameter buffer.
-  **<AddrIncr>** - word length in bytes.
-  **<Size>** - size of the parameter buffer in bytes
-  **<Data>** - parameter data represented in hexadecimal format.

<Module>
--------

-  **<Algorithm>** - algorithm (typically only one) within the graphical module block.

.. _algorithm-1:

<Algorithm>
-----------

-  **<AlgoName>** - unique id of the algorithm.
-  **<DetailedName>** - full plugin name of the algorithm.
-  **<Description>** - detailed description of the algorithm.
-  **<Address>** - parameter offset of the algorithm within the parameter buffer.
-  **<AbstractParameter>** - abstract parameters (UI parameters) of the module.
-  **<ModuleParameter>** - module parameters (target parameters) of the module.

<AbstractParameter>
-------------------

-  **<Name>** - name of the parameter.
-  **<Type>** - type of the parameter (Numeric, Boolean, NumericArray, List etc.).
-  **<Value>** - Abstract value of the parameter.

<ModuleParameter>
-----------------

-  **<Name>** - name of the parameter.
-  **<Type>** - type of the parameter (Numeric or NumericArray).
-  **<DataType>** - data type (floating point, fixed point format etc.).
-  **<Offset>** - offset of the parameter within the modules' parameter memory.
-  **<SafeloadGroup>** - safeload group name in case of safeload parameters. Safeload parameters within a group are written to the target as a group.
-  **<Value>** - value of the parameter (applicable only in case of numeric parameter).
-  **<Size>** - size of the parameter in bytes.
-  **<Data>** - data bytes represented in hexadecimal.

| 
| ===== JSON File ===== This file is similar to the XML file described above but generated in JSON format.
