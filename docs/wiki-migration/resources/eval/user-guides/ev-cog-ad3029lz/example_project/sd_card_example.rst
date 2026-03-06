SDHC card Interfacing with EV-COG-AD3029LZ
==========================================

Introduction
------------

This document explains about the hardware and software setup, which is required to interface the SDHC memory card to the EV-COG-AD3029LZ through SPI Interface.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/introductio_bgw.png
   :width: 600px

The hardware details covers the pin mapping between the SDHC memory card and EV-COG-AD3029LZ along with useful links that provides more details for EV-COG-AD3029LZ and SDHC memory card . The software details covers the software development kit required to interface the SDHC memory card with EV-COG-AD3029LZ and the software architecture.

Boards and Accessories required
-------------------------------

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/things_needed_all.png

a.) EV-GEAR-EXPANDER1Z (left) b.) EV-COG-AD3029LZ (middle) c.) SDHC card (right)

Hardware interface
------------------

SPI interface
~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/block_diagram.png
   :align: center

Schematic of SDHC card slot (P2) in expander gear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/sdcardinterface.png

Steps
~~~~~

1. Connect the EV-GEAR-EXPANDER1Z via it’s Cog connectors to the EV-COG-AD3029LZ’s expansion connectors.


|image1|

2. Insert the SDHC card into the SDHC slot (P2) of the expander gear as shown in the figure below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/capture4-bgw.png

Software Details
----------------

A modular implementation of FatFs library called Elm-Chan FatFs library is provided for using SD card with Fat file system

The example software provided consists of these packs

-  Example application code.
-  Elm-Chan’s FatFs C library- This pack is required for the implementation of FAT file system on SD card.

\* The index of API’s provided by Elm-Chan’s FatFs C library and their description can be found in this `Link <http://elm-chan.org/fsw/ff/00index_e.html>`__

\* The driver version used is -> ADuCM302x-Rel1.0.6

Software Architecture
~~~~~~~~~~~~~~~~~~~~~

The software architecture for the SDHC application along with the FATFS is depicted below.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/ev-cog-ad3029lz/example_project/software_flow_v1.png

The Application level software handles file management tasks such as create, read /write ,edit files.

The Files in the FSFAT folder provides the Elm-Chan FATFS API calls. The files under HAL folder provides the SPI interface port for the ADuCM3029 Controller.

Raw I/O without FatFs
~~~~~~~~~~~~~~~~~~~~~

If raw read/write access to SD card at sector level is needed in the user application without the FATFS then the user can only use the files in HAL folder.

To do the above, remove the static keyword from the declaration and definition of the functions that the user needs to use from the SD.C and SD.h files. After doing the changes user can add SD.h in their application code.

.. important::

   While using with FatFs library the user application should not call the low level functions (in HAL).Doing so may crash the library and lead to errors.


SD Card Example Application
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. admonition:: Download
   :class: download

   :git-EV-COG-AD3029LZ:`SD Card With EV-COG_AD3029LZ <SDCARD%20EXAMPLE%20PROJECT/SD_CARD_SPI_3029_V1.0>`


:doc:`Back </wiki-migration/resources/eval/user-guides/ev-cog-ad3029lz>`

*End of Document*

.. |image1| image:: https://wiki.analog.com/_media/ resources/eval/user-guides/ev-cog-ad3029lz/example_project/cog_expan_connector.png
   :width: 800px
