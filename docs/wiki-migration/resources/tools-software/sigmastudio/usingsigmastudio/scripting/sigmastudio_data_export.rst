`Click here to return to 'SigmaStudio for SHARC Host Controller' page. <https://wiki.analog.com/resources/tools-software/sigmastudio/usingsigmastudio/ss4shhostcontroller>`__

SigmaStudio Data Export
=======================

| The SigmaStudio Host application can export the code and parameters that are to be sent to the SHARC Target once it is booted. This section describes how to export and use the system files.
| =====Export Settings===== The export related settings can be configured through the SigmaStudio Settings window. The “Settings” window can be launched by selecting Tools  Settings.
| ====Export Mode==== The user can select whether, on export, all files are to be generated or only the XML file is to be generated. ‘Export Mode’ is present in the ‘System Files Export’ tab of the Settings window. If ‘XML Only’ is checked, only the XML file is generated on export. Otherwise, all export system files including the XML file are generated.
| ====Auto Export Mode==== Export files can be automatically generated after a successful ‘Link-Compile-Download’ by enabling ‘Auto Export System Files’ in the SigmaStudio settings window.
| =====Exporting System Files===== The system files can be exported after a Schematic is successfully compiled. Once the ‘Link-Compile-Download’ action is complete, the system files can be exported by selecting Action  Export System Files.
| Note: The Action  Export System Files menu item is inactive if the Schematic is not compiled after any modifications.
| The name of system files and the folder to which it can be saved is to be decided by the user. The files contain code, parameter and version information to be sent to the SHARC Target. The files should be freshly generated every time the Schematic is modified.
| =====System File Contents and Usage===== Examples of the content of the exported files and associated descriptions are given in this section. Files that are named by the user are named “xxx” for ease of representation. The file name also contains information on the IC used and has a text of form “\_IC_1” for IC-1. The name can be modified by the user. For ease of representation this is indicated by “\_IC_y” in the document.
| ====defines.h==== Example Contents

.. code:: csharp

   #define BufferSize_IC_1 9792
   #define NumTransactions_IC_1 4

| Description
| The file contains definitions for the size of data in the system files. The macro BufferSize_IC_y gives the total size in bytes of reset, version, code and parameter data. Related data can be found in the file TxBuffer_IC_y.dat. The macro NumTransactions_IC_y contains the size of the data contained in NumBytes_IC_y.dat.
