.. _eval-ad9152:

AD9152 Evaluation Board
=======================

The :adi:`AD9152` evaluation boards follow the same design principles and are
available in multiple form factors for different evaluation setups.

Documentation and software updates for using High-Speed DAC Evaluation Boards
are included in individual, self-extracting update files.

Files included in the AD9152 Update:
------------------------------------

-  SPI Application
-  DPGDownloader Panel
-  :adi:`AD9152 Data Sheet <static/imported-files/data_sheets/AD9152.pdf>`
-  :adi:`IBIS Model <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9152.ibs>`

.. list-table::
   :header-rows: 1

   * - Item
     - AD9152-EBZ
     - AD9152-ADRF6720-EBZ
     - AD9152-FMC-EBZ
   * - Quick Start
     - :doc:`ad9152-ebz <ad9152-ebz>`
     - :doc:`ad9152-adrf6720-ebz <ad9152-adrf6720-ebz>`
     - :doc:`ad9152-fmc-ebz <ad9152-fmc-ebz>`
   * - Schematics
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-ebz_revb_schematic.pdf>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-adrf6720-ebz_revb_schematic.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_schematic.pdf>`
   * - Bill of Materials
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-ebz_revb_bom.xlsx>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-adrf6720-ebz_revb_bom.xlsx>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_bom.xlsx>`
   * - PCB Gerber Files
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-ebz_revb_gerber_files.zip>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-adrf6720-ebz_revb_gerber_files.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_gerber_files.zip>`
   * - PCB BRD File
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-ebz_revb.zip>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-adrf6720-ebz_revb.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva.zip>`
   * - PCB Layout PDF
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-ebz_revb_layout.pdf>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9152-adrf6720-ebz_revb_layout.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9152-fmc-ebz_reva_layout.pdf>`

Data Pattern Generator
----------------------

The Data Pattern Generator (DPG) is a bench-top instrument for driving vectors
into high-speed digital-to-analog converters. The DPG connects to a USB on a PC
and allows a user to download a vector from the PC into the internal memory of
the DPG. Once downloaded, the vector can be played out to an attached evaluation
board for a specific DAC at full speed. This allows for rapid evaluation of the
DAC with both generic and custom-generated test data.

For more information on the DPG line of pattern generators and software:

- :dokuwiki:`DAC Software Suite <resources/eval/dpg/dacsoftwaresuite>`
- :dokuwiki:`DPG Lite <resources/tools-software/ace/dpg-lite>`
- :dokuwiki:`Analysis | Control | Evaluation (ACE) Software <resources/tools-software/ace>`
- :dokuwiki:`ADS7 <resources/eval/dpg/ads7>`
