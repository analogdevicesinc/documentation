Advanced Framework Configurations (ADAU145x/ADAU146x)
=====================================================

| :doc:`Click here to return to the Using SigmaStudio page </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio>`
| Advanced framework configurations can be accessed by right-clicking on the IC as shown below. This window provides various advanced options to modify the framework. The feature is supported starting with "SigmaStudio 4.0 Release" or above. it is currently supported only for ADAU145x/ADAU146x family of SigmaDSPs. |image1|
| This feature allows the user to select the framework configuration as shown below |image2|

Options
-------

Enable Indirect Parameter Access Table and Fixed SafeLoad Address (From SigmaStudio 3.13)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Users can enable the Indirect Parameter Access table in the older schematics by selecting this option. By default, this is disabled for the schematics created in "SigmaStudio 3.12 Release" or below. This is enabled for the schematics created from "SigmaStudio 3.13 Release" or above. If the feature is enabled, the context menu in IC shows the option for 'Indirect Parameter Access Table.
| |image3|
| ==== Enable malloc and free modifications in the block processing mode (From SigmaStudio 3.15)==== Enabling this solves issues in the malloc routine in the block processing mode. This feature is disabled by default for the schematics created in "SigmaStudio 3.13 Release" or below and enabled by default from "SigmaStudio 3.14 Release" or above.

Clear the unused PM, DM0 and DM1 during initialization (From SigmaStudio 4.3)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Enabling this to clear the unused PM, DM0, and DM1 locations during the framework initialization. This is disabled by default.
| ==== Enable modification in the framework initialization (From SigmaStudio 4.2) ==== There was an issue in the framework initialization which was corrupting the DM in some corner cases when block processing is used. Enabling this option will enable the fix. This is disabled by default for the schematics created in SigmaStudio 4.1 or below and enabled by default from "SigmaStudio 4.2 Release" or above.
| ==== Capture memory allocation details in the compiler output file (From SigmaStudio 4.2) ==== By enabling this option user can see the memory map details in the 'compiler_output.log' generated during the link compile download. Please note that enabling this option will make the compilation slower. This is disabled by default.
| ==== monitor the overrun errors and free cycles in the framework (From SigmaStudio 4.3) ====
| ==== Reduce the size of DM0 and DM1 download packets by removing zero initializations (From SIgmaStudio 4.3) ==== Enabling this option will remove the heap and state buffers data from DM0 and DM1 download packets during link compile download. The heap and state buffers clear will be done during the framework initialization. By default this is disabled.
| ==== Indirect Parameter Access Table to handle the multiple memory pages (SigmaStudio 4.3) ====
| ==== Clear the state buffers before calculating the checksum during initialization (SigmaStudio 4.4) ==== If DSP is booted through Selfboot, the state buffers have not cleared this results the wrong result in the checksum calculation. By enabling this option, the state buffers have cleared during the framework initialization. This feature is disabled by default for the schematics created in "SigmaStudio 4.3 Release" or below and enabled by default from "SigmaStudio 4.4 Release" or above.
| ==== Enable Optimization in malloc and free modifications in block processing (SigmaSudio 4.6) ==== By enabling this option will optimize the code memory(Program memory) when a project has Block processing modules. By default this option is enabled for schematics created from SS4.6 or above. This option will be disabled automatically if 'Enable malloc and free modifications in the block processing mode (From SigmaStudio 3.15)' is disabled.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/advancefwconfig.png
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/advancedframeworkconfig_malloc_free.jpg
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudio/usingsigmastudio/advancefwconfigipat.png
