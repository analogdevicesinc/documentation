.. _eval-ad9154:

AD9154 Evaluation Boards
========================

The :adi:`AD9154` evaluation boards are available in multiple form factors for
different evaluation setups.

Documentation and software updates for using High-Speed DAC Evaluation Boards
are included in individual, self-extracting update files.

Files included in the AD9154 Update:
------------------------------------

-  SPI Application
-  DPGDownloader Panel
-  :adi:`AD9154 Data Sheet <static/imported-files/data_sheets/AD9154.pdf>`
-  :adi:`IBIS Model <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9154.ibs>`

.. list-table::
   :header-rows: 1

   * - Item
     - AD9154-EBZ
     - AD9154-ADRF6720-EBZ
     - AD9154-FMC-EBZ
   * - Quick Start (SPIPro)
     - :doc:`ad9154-ebz <ad9154-ebz>`
     - :doc:`ad9154-adrf6720-ebz <ad9154-adrf6720-ebz>`
     - :doc:`ad9154-fmc-ebz <ad9154-fmc-ebz>`
   * - Quick Start (ACE)
     - :doc:`ad9154-ace-ebz <ad9154-ace-ebz>`
     - :doc:`ad9154-m6720-ebz <ad9154-m6720-ebz>`
     - :doc:`ad9154-ace-fmc-ebz <ad9154-ace-fmc-ebz>`
   * - Schematics
     - :dokuwiki:`RevD <_media/resources/eval/dpg/ad9154-ebz_revd_schematic.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-adrf6720-ebz_reva_schematic.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-fmc-ebz_reva_schematic.pdf>`
   * - Bill of Materials
     - :dokuwiki:`RevD <_media/resources/eval/dpg/ad9154-ebz_revd_bom.xls>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-adrf6720-ebz_reva_bom.xls>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-fmc-ebz_reva_bom.xls>`
   * - PCB Gerber Files
     - :dokuwiki:`RevD <_media/resources/eval/dpg/ad9154-ebz_revd_gerber_files.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-adrf6720-ebz_reva_gerber_files.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-fmc-ebz_reva_gerber_files.zip>`
   * - PCB BRD File
     - :dokuwiki:`RevD <_media/resources/eval/dpg/ad9154-ebz_revd.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-adrf6720-ebz_reva.zip>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-fmc-ebz_reva.zip>`
   * - PCB Layout PDF
     - :dokuwiki:`RevD <_media/resources/eval/dpg/ad9154-ebz_revd_layout.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-adrf6720-ebz_reva_layout.pdf>`
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9154-fmc-ebz_reva_layout.pdf>`

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
