:doc:`Click here to return to 'SigmaStudio for SHARC - Quick start guide' page. </wiki-migration/resources/tools-software/sigmastudio/usingsigmastudio/ss4shquickstartguide>`

Utility for formatting Exported data from SigmaStudio
=====================================================

| The ARM as microcontroller application requires the exported data from SigmaStudio to be formatted in a specific way so that the exported information can be used as ‘.c’ arrays within the application. A utility is provided with the installer to do this formatting. The ‘exportCodeParam’ utility is located in “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\utilities\\exportCodeParam”.
| Follow the steps below to format the exported data from SigmaStudio using the ‘exportCodeParam’ utility
| \* Copy all the SigmaStudio exported files into “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\utilities\\exportCodeParam” folder.

-  Open ‘cmd’ prompt and change the working directory to “< Software Modules folder >\\SigmaStudioForSHARC-SH-Rel3.9.0\\Target\\utilities\\exportCodeParam” folder.
-  Run the utility as below:

| exportCodeParam.exe <Visa> <Export File Name> <IC_name>
| For e.g. exportCodeParam.exe "SWC" "Volume_Mute_Block_SC5xx" "IC_1"
| This generates C formatted source and header file in the same folder.
| This utility has to be run multiple times corresponding to the number of ICs within the schematic. For schematics using the ‘Dual Core’ option, the SMAP, code and parameters for each of the SHARC cores are located in a single ‘.c’ and ‘.h’ file.
