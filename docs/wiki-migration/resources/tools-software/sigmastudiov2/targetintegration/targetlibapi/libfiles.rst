| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/targetlibapi>`
| =====Target Library and Header Files=====
| The SS+ target library for ADSP-SC5xx processors is
| • libadi_sigma_sharc_SC5xx.dlb: SHARC Target Library generated with Short Word Code (VISA) and byte-addressing

::

     mode for ADSP-SC5xx processors.

| 
| The SS+ target library for ADSP-215xx processors is
| • libadi_sigma_sharc_215xx.dlb: SHARC Target Library generated with Short Word Code (VISA) and byte-addressing

::

     mode for ADSP-215xx processors.

| 
| Note: The Framework Source files, which are available in Target/Framework/Source and Target/Sys/Source can be used along with the libraries, to create a whole Application.
| Include Files
| The include files required for integration of this library is
| • adi_ss_ssn.h This public file contains all the API definitions, structures and macros of the SSn target library.

::

   • adi_ss_common.h. This public file contains structures for memory definition.

| 
| Linker Files
| The linker files required to be used along with this library is

::

   • adi_ss_app.ldf: This .ldf file should be used along with the application .ldf file. This .ldf file reserves 
   sections for GMAP and for IPC.

| 
