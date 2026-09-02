.. _eval-ad9136:

AD9136 & AD9135 Evaluation Boards
=================================

The :adi:`AD9136` and :adi:`AD9135` evaluation boards follow the same design as
the AD9144 evaluation board. They share the same PCBs. The BOM & schematics
below reflect the differences in board components and assembly.

The AD9136 & AD9135 DPG3 and ADS7 evaluation boards are also compatible and
supported by new SPI programming software called ACE (Analysis \| Control \|
Evaluate). This software can be downloaded from the ACE Wiki site under
"Resources" (:dokuwiki:`/resources/tools-software/ace`) and is also
included in the DVD that is shipped as part of the evaluation board kit. Please
refer to the Quick Start Guide Using ACE for details on how to use the new SPI
GUI software.

Documentation and software updates for using High-Speed DAC Evaluation Boards
are included in the :dokuwiki:`DAC Software Suite <resources/eval/dpg/dacsoftwaresuite>`
and below. Follow the link to the Quick Start Guides below for information on
both the AD9136 and AD9135.

Files
-----

-  :adi:`AD9136 & AD9135 Data Sheet <static/imported-files/data_sheets/AD9135_9136.pdf>`
-  :adi:`IBIS Model <Analog_Root/static/techSupport/designTools/ibisModels/license/ibis_general.html?ibs=AD9144.ibs>`

.. list-table::
   :header-rows: 1

   * - Item
     - AD9136-EBZ & AD9135-EBZ
     - AD9136-FMC-EBZ & AD9135-FMC-EBZ
   * - Quick Start Guide
     - :doc:`ACE <ace_ad9136-ebz>` / :doc:`SPIPro <ad9136-ebz>`
     - :doc:`ACE <ad9136-fmc-ebz>`
   * - Schematics
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9144-ebz_reva_schematic.pdf>`
     - :dokuwiki:`AD9135-FMC-EBZ <_media/resources/eval/dpg/ad9135-fmc-ebz_revb_schematic.pdf>` /
       :dokuwiki:`AD9136-FMC-EBZ <_media/resources/eval/dpg/ad9136-fmc-ebz_revb_schematic.pdf>`
   * - Bill of Materials
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9144-ebz_reva_bom.xls>`
     - :dokuwiki:`AD9135-FMC-EBZ <_media/resources/eval/dpg/ad9135-fmc-ebz_revb_bom_customer.xlsx>` /
       :dokuwiki:`AD9136-FMC-EBZ <_media/resources/eval/dpg/ad9136-fmc-ebz_revb_bom_customer.xls>`
   * - PCB Gerber Files
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9144-ebz_reva_gerber_files.zip>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9144-fmc-ebz_revb_gerber_files.zip>`
   * - PCB BRD File
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9144-ebz_reva.zip>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9144-fmc-ebz_revb.zip>`
   * - PCB Layout PDF
     - :dokuwiki:`RevA <_media/resources/eval/dpg/ad9144-ebz_reva_layout.pdf>`
     - :dokuwiki:`RevB <_media/resources/eval/dpg/ad9144-fmc-ebz_revb_layout.pdf>`

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
