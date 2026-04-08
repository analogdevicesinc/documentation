AD9144 Evaluation Boards
========================

There are currently :adi:`AD9144` evaluation boards that support either the DPG3
Pattern Generator Platform or the ADS7 FMC-compatible Pattern Generator. These
board variants are listed below in the table.

The AD9144 DPG3 and ADS7 DAC-only evaluation boards are also compatible and
supported by new SPI programming software called ACE (Analysis \| Control \|
Evaluate). This software can be downloaded from the ACE Wiki site under
"Resources" (:dokuwiki:`/resources/tools-software/ace`) and is also included in
the DVD that is shipped as part of the evaluation board kit. Please refer to the
Quick Start Guide Using ACE for details on how to use the new SPI GUI software.

Documentation and software updates for using High-Speed DAC Evaluation Boards
are included in individual, self-extracting update files.

Files included in the AD9144 Update:
------------------------------------

-  SPI Application
-  DPGDownloader Panel
-  :adi:`AD9144 Data Sheet <static/imported-files/data_sheets/AD9144.pdf>`
-  :adi:`IBIS Model <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9144.ibs>`

.. list-table::
   :header-rows: 1

   * - Item
     - AD9144-EBZ
     - AD9144-M6720-EBZ
     - AD9144-FMC-EBZ
   * - Quick Start (SPIPro)
     - :doc:`ad9144-ebz <ad9144-ebz>`
     - :doc:`ad9144-adrf6720-ebz <ad9144-adrf6720-ebz>`
     - :doc:`ad9144-fmc-ebz <ad9144-fmc-ebz>`
   * - Quick Start (ACE)
     - :doc:`ace_ad9144-ebz <ace_ad9144-ebz>`
     - Not Currently Supported
     - :doc:`ace_ad9144-fmc-ebz <ace_ad9144-fmc-ebz>`
   * - Schematics
     - :download:`RevA <../resources/ad9144-ebz_reva_schematic.pdf>`
     - :download:`RevC <../resources/ad9144-adrf6720-ebz_revc_schematic.pdf>`
     - :download:`RevB <../resources/ad9144-fmc-ebz_revb_schematic.pdf>`
   * - Bill of Materials
     - :download:`RevA <../resources/ad9144-ebz_reva_bom.xls>`
     - Unavailable
     - :download:`RevB <../resources/ad9144-fmc-ebz_revb_bom.xls>`
   * - PCB Gerber Files
     - :download:`RevA <../resources/ad9144-ebz_reva_gerber_files.zip>`
     - :download:`RevC <../resources/ad9144-adrf6720-ebz_revc_gerber_files.zip>`
     - :download:`RevB <../resources/ad9144-fmc-ebz_revb_gerber_files.zip>`
   * - PCB BRD File
     - :download:`RevA <../resources/ad9144-ebz_reva.zip>`
     - :download:`RevC <../resources/ad9144-adrf6720-ebz_revc.zip>`
     - :download:`RevB <../resources/ad9144-fmc-ebz_revb.zip>`
   * - PCB Layout PDF
     - :download:`RevA <../resources/ad9144-ebz_reva_layout.pdf>`
     - :download:`RevC <../resources/ad9144-adrf6720-ebz_revc_layout.pdf>`
     - :download:`RevB <../resources/ad9144-fmc-ebz_revb_layout.pdf>`

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
