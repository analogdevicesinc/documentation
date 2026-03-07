| :doc:`Click here to go back </wiki-migration/resources/tools-software/sigmastudiov2/targetintegration/commapi>`
| =====Communication library and interface header file details=====
| The communication library handles the parsing of the SPI packets received from the Host, handling SMAP, code and parameter download, parameter tuning, read-back communication etc.
| The SSn communication library for ADSP-SC5xx processors are listed below:
| \* "libadi_sigma_sharc_comm_SC57x_Core0.a" for ADSP-SC57x family of processors

-  "libadi_sigma_sharc_comm_SC58x_Core0.a" for ADSP-SC58x family of processors
-  "libadi_sigma_sharc_comm_SC59x_Core0.a" for ADSP-SC59x family of processors

| This is the Communication Library which is built to run on ARM core of ADSP-SC58x/ ADSP-SC57x/ ADSP-SC59x processors respectively.
| The SSn communication library for ADSP-215xx processors are listed below:
| \* libadi_sigma_sharc_comm_2156x_Core1.dlb

-  libadi_sigma_sharc_comm_2157x_Core1.dlb
-  libadi_sigma_sharc_comm_2158x_Core1.dlb
-  libadi_sigma_sharc_comm_2159x_Core1.dlb
-  libadi_sigma_sharc_comm_SC59x_Core1.dlb

| This is the Communication Library which is built to run on SHARC core of ADSP-SC57x/ADSP-SC58x/ADSP-SC59x and ADSP-2158x, ADSP-2157x, ADSP-2156x and ADSP-2159x processors respectively. This Library is generated with short Word Code (VISA) and byte-addressing mode.
| =====Include Files===== The include files required for integration of this library is :

::

    • adi_ss_communication.h

This public file contains interfaces for communication module (between Host and Target)

::

    • adi_ss_connection.h

This public file contains interfaces for physical SPI connection.

::

    • adi_ss_common.h. 

This is a common public header file which contains structures for memory definition.
