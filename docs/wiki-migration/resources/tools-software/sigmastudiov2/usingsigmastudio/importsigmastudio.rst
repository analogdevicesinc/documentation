| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`
| ====== Import SigmaStudio Projects ======

.. important::

   It is recommended to apply **SigmaStudio+ 2.2.0.2 update** before using the 'Import SigmaStudio Project' feature. This update can be applied only if SigmaStudio+ 2.2.0 is installed. Launch 'Update Manager' from the 'Help' menu to apply this update


This feature is used to convert a SigmaStudio project into a SigmaStudio+ project. The SigmaStudio project is opened in SigmaStudio and system files are generated. These system files are then imported in SigmaStudio+ using "Import SigmaStudio Projects" from the 'Action' menu. SigmaStudio+ will reconstruct the SigmaStudio project in SigmaStudio+ based on the information present in the imported system files.

.. note::

   For migrating A2B projects on SigmaStudio to SigmaStudio+, refer :doc:`A2B Project Migration </wiki-migration/resources/tools-software/a2bv2/a2bssplususerguide/projectmigration>`


1. Export System Files in SigmaStudio
=====================================

| 
| Follow the steps given below to generate system files of the SigmaStudio project:

-  Launch SigmaStudio 4.6 or later version
-  Open the SigmaStudio project to be converted as SigmaStudio+ project
-  Link-Compile-Download
-  Use "Export System Files" from the 'Action' menu to generate the system files.

.. note::

   SigmaStudio 4.6 or later version is required. SigmaStudio+ project conversion will be incomplete if earlier versions are used


2. Import SigmaStudio System Files in SigmaStudio+
==================================================

| 
| Follow the steps given below to reconstruct SigmaStudio project in SigmaStudio+ using the system files:

-  Click "Import SigmaStudio Projects" from the 'Action' menu
-  In the File Open Dialog window that appears, select the exported XML file. There will be two XML files: <export name>.xml and <export name>_Netlist.xml. Select <export name>.xml and click 'Open'.
-  The SigmaStudio+ project will be constructed based on the information parsed from the exported files. Make the require manual modifications, if any, and save.
-  The summary report of the project migration will be displayed on the Output Window of SigmaStudio+. Report is generated as <export name>_MigrationLog.txt in the same folder from which system files were imported. Controls and settings on the module which could not be applied on the reconstructed project will be detailed in the summary report. These changes should be manually applied. A summary of such settings is listed in :doc:`Post-Import Manual Changes </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/importsigmastudio/manualimportsettings>`

.. note::

   If SigmaStudio+ could not identify an equivalent module for any given module in SigmaStudio, a dummy module is inserted


.. note::

   Connections found distorted in the imported project will be auto corrected once the newly created project is saved and reopened


.. note::

   Migration handles only signal flow and SigmaDSP register window settings reproduction in this version of SigmaStudio+. Other settings should be manually applied in the reconstructed project

