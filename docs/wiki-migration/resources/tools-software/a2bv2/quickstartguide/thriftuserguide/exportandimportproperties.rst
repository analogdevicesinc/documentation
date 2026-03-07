:doc:`Click here to return to Thrift User Guide Homepage </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide>`

List of API in Export and Import Properties
===========================================

-  :doc:`Export Commandlist.xml File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export Commandlist.h File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export Busconfig.c File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export Busconfig.xml File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export A2b_System_AutoConfig.xml File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export A2b_System_Autoconfig.dat File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`
-  :doc:`Export MergedBranch.xml File </wiki-migration/resources/tools-software/a2bv2/quickstartguide/thriftuserguide/exportandimportproperties>`

| 
| ====Export Commandlist.xml File==== This API is used for Exporting Commandlist.xml file . It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal); SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  TxtFilePathCLxml – To export Commandlist.xml

-   “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty and UpdateBooleanProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty and UpdateBooleanProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "TxtFilePathCLxml", @"C:\\Thrift\\a2bcommandlist.xml");

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkIncludeModA2BRegistersCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkIncludePeripeheralConfigCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkGenerateforBusSelfCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "Export", true);

**Python Example:**

::

   ssp_result = client.UpdateStringProperty("A2B_0", "TxtFilePathCLxml", "C:\\Thrift\\a2bcommandlist.xml")    
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkIncludeModA2BRegistersCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkIncludePeripeheralConfigCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkGenerateforBusSelfCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "Export", "True")

| 
| ====Export Commandlist.h File==== This API is used for Exporting Commandlist.h file . It takes element Uid and property name and property value as arguments and returns SSPResult.

**API:** SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal); SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  TxtFilePathCLh– To export Commandlist.h

-   “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty and UpdateBooleanProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty and UpdateBooleanProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "TxtFilePathCLh", @"C:\\Thrift\\a2b_Commandlist.h");

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkIncludeModA2BRegistersCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkIncludePeripeheralConfigCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkGenerateforBusSelfCL", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "Export", true);

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "TxtFilePathCLh", "C:\\\\Thrift\\\\a2b_Commandlist.h")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkIncludeModA2BRegistersCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkIncludePeripeheralConfigCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkGenerateforBusSelfCL", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "Export", "True")

| 
| ====Export Busconfig.c File==== This API is used for Exporting Busconfig.c file . It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal); SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  TxtFilePathBCc– To export Busconfig.c

-   “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty and UpdateBooleanProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty and UpdateBooleanProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "TxtFilePathBCc", @"C:\\Thrift\\a2b_busconfig.c");

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "Export", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileBCFMerge", true);
   _sspresult = client.UpdateBooleanProperty("A2B_0", "ChkEnableCompressionBCFMerge", true);

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "TxtFilePathBCc", "C:\\\\Thrift\\\\a2b_busconfig.c")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "Export", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkOptimizeexprtfileBCFMerge", "True")
   ssp_result = client.UpdateBooleanProperty("A2B_0", "ChkEnableCompressionBCFMerge", "True")

| 
| ====Export Busconfig.xml File==== This API is used for Exporting Busconfig.xml file . It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal); SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  TxtFilePathBCxml– To export Busconfig.xml

-  “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty and UpdateBooleanProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty and UpdateBooleanProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "TxtFilePathBCxml", @"C:\\Thrift\\a2b_busconfig.xml");

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "Export", true);

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "TxtFilePathBCxml", "C:\\\\Thrift\\\\a2b_busconfig.xml")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "Export", "True")

| 
| ====Export A2b_System_AutoConfig.xml File==== This API is used for Exporting a2b_system_autoconfig.xml file. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal);

**Arguments:**

-  “elementUid” = UID of the A2B Channel
-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  XMLDumpPath – Path to export a2b_system_autoconfig.xml

      -  DumpXML - To export a2b_system_autoconfig.xml

-   “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "XMLDumpPath", @"C:\\Thrift\\adi_a2b_system_autoconfig.xml");

::

   _sspresult = client.UpdateStringProperty("A2B_0", "DumpXML", @"C:\Thrift\adi_a2b_system_autoconfig.xml");

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "XMLDumpPath", "C:\\\\Thrift\\\\adi_a2b_system_autoconfig.xml")

::

   ssp_result = client.UpdateStringProperty("A2B_0", "DumpXML", "C:\\Thrift\\adi_a2b_system_autoconfig.xml")

| 
| ====Export A2b_System_Autoconfig.dat File==== This API is used for Exporting a2b_system_autoconfig.dat file. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  DatDumpPath– Path to export a2b_system_autoconfig.dat

      -  DumpDat- To export a2b_system_autoconfig.dat

-   “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "DatDumpPath", @"C:\\Thrift\\adi_a2b_system_autoconfig.dat");

::

   _sspresult = client.UpdateBooleanProperty("A2B_0", "CanIncludeStreamInformationToDatFile", true);
   _sspresult = client.UpdateStringProperty("A2B_0", "DumpDat", @"C:\Thrift\adi_a2b_system_autoconfig.dat");

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "DatDumpPath", "C:\\\\Thrift\\\\adi_a2b_system_autoconfig.dat")

::

   ssp_result = client.UpdateBooleanProperty("A2B_0", "CanIncludeStreamInformationToDatFile", "True")
   ssp_result = client.UpdateStringProperty("A2B_0", "DumpDat", "C:\\Thrift\\adi_a2b_system_autoconfig.dat")

| 
| ====Export MergedBranch.xml File==== This API is used for ExportingMergedBranch.xml file. It takes element Uid and property name and property value as arguments and returns SSPResult.

| **API:**
| SSPResult UpdateStringProperty(string elementUid, string propertyName, string propertyVal); SSPResult UpdateBooleanProperty(string elementUid, string propertyName, bool propertyVal);

| **Arguments:**
| \* “elementUid” = UID of the A2B Channel

-  “propertyName” = Name of the action property. Some of the property name examples are listed below

   -  PrimaryBranchxml– Path to PrimaryBranch.xml

      -  SecondaryBranchxml - Path to SecondaryBranch.xml
      -  MergedBranchxml – Path to MergedBranch.xml

-  “PropertyValue” = Export Path in string.

| **Result:**
| SSPResult contains 'IsSuccess' flag and 'Message' information of UpdateStringProperty and UpdateBooleanProperty action.

-  IsSuccess is set to 'True' if the UpdateStringProperty and UpdateBooleanProperty was successful else 'False'.
-  Message contains the Success/Failure information in the form of list of string.

| **Csharp Example:**
| \_sspresult = client.UpdateStringProperty("A2B_0", "PrimaryBranchxml", @"C:\\Thrift\\a2b_primarybranch.xml");

::

   _sspresult = client.UpdateStringProperty("A2B_0", "SecondaryBranchxml", @"C:\Thrift\a2b_SecondaryBranchxml.xml");
   _sspresult = client.UpdateNumericProperty("A2B_0", "CntSubNodeId", 1.0);
   _sspresult = client.UpdateStringProperty("A2B_0", "MainI2CAddress", "0x6A");
   _sspresult = client.UpdateStringProperty("A2B_0", "MergedBranchxml", @"C:\Thrift\a2b_MergedBranchxml.xml");
   _sspresult = client.UpdateBooleanProperty("A2B_0", "Export", true);

| **Python Example:**
| ssp_result = client.UpdateStringProperty("A2B_0", "PrimaryBranchxml", "C:\\\\Thrift\\\\a2b_primarybranch.xml")

::

   ssp_result = client.UpdateStringProperty("A2B_0", "SecondaryBranchxml", "C:\\Thrift\\a2b_SecondaryBranchxml.xml")
   ssp_result = client.UpdateNumericProperty("A2B_0", "CntSubNodeId", float(1.0))
   ssp_result = client.UpdateStringProperty("A2B_0", "MainI2CAddress", "0x6A")
   ssp_result = client.UpdateStringProperty("A2B_0", "MergedBranchxml", "C:\\Thrift\\a2b_MergedBranchxml.xml")
   ssp_result = client.UpdateBooleanProperty( "A2B_0", "Export", "True")

.. tip::

   For more information about exporting A2B system configuration files, you can refer to the :doc:`A2B Plugin for SigmaStudio+ User Guide </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/exportinga2bsystemconfigurationfiles>`.

