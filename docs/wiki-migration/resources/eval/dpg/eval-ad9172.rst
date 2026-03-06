AD9171/AD9172/AD9173/AD9174/AD9175/AD9176 Evaluation Board
==========================================================

The :adi:`AD9171`, :adi:`AD9172`, :adi:`AD9173`, :adi:`AD9174`, :adi:`AD9175` and :adi:`AD9176` evaluation board is an FMC form-factor board with FMC connector that complies to the Vita 57.1 standard. The FMC board uses a Mini-Circuits balun on the DAC output.

To operate the evaluation board, the user must attach the board to a compatible FMC carrier board, such as those provided by FPGA vendors. Analog Devices produces an FPGA carrier called the ADS7-V2, which serves as a digital pattern generator or data source as well as the power supply for the boards. The AD917x board has an option to be powered from a lab power supply when used in a special NCO-only mode. This operation is described in more detail in the User's Guide. The user must be able to observe the DAC output on a spectrum analyzer. A low noise clock source is provided on the evaluations boards, the HMC7044 clock synthesizer, and an option exists for the user to supply a low jitter external sine or square wave clock as a clock source instead. The evaluation board comes with software, called ACE, which allows the user to program the SPI port. Via the SPI port, the DUT (and clock circuitry) can be programmed into any of its various operating modes. It also comes with the DAC Software Suite which includes the DPGDownloader for vector generation, download, and transmission to the evaluation board when using the ADS7-V2.

Documentation and software updates for using High-Speed DAC Evaluation Boards are included in individual, self-extracting update files. The latest DPG Downloader software can be downloaded from here: :doc:`High-Speed DAC Software Suite </wiki-migration/resources/eval/dpg/dacsoftwaresuite>`. The latest ACE software can be downloaded from here: :doc:`Analysis \| Control \| Evaluation (ACE) Software </wiki-migration/resources/tools-software/ace>`. The plugins for this board can be downloaded from the plugin manager in the ACE software.

Files included in the AD9171, AD9172, AD9173, AD9174, AD9175, AD9176 Update:
----------------------------------------------------------------------------

-  SPI Application
-  DPGDownloader Panel
-  :adi:`AD9171 Data Sheet <media/en/technical-documentation/data-sheets/AD9171.pdf>`
-  :adi:`AD9172 Data Sheet <media/en/technical-documentation/data-sheets/AD9172.pdf>`
-  :adi:`AD9173 Data Sheet <media/en/technical-documentation/data-sheets/AD9173.pdf>`
-  :adi:`AD9174 Data Sheet <media/en/technical-documentation/data-sheets/AD9174.pdf>`
-  :adi:`AD9175 Data Sheet <media/en/technical-documentation/data-sheets/AD9175.pdf>`
-  :adi:`AD9176 Data Sheet <media/en/technical-documentation/data-sheets/AD9176.pdf>`

+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Item              | AD917(1,2,3,4,5,6)-FMC-EBZ                                                                                                                 |
+===================+============================================================================================================================================+
| User Guide        | :doc:`AD917x User Guide </wiki-migration/resources/eval/dpg/ad917x-fmc-ebz>`                                                               |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Schematics        | `AD917x-FMC-EBZ Schematic <https://wiki.analog.com/_media/resources/eval/dpg/ad9172-fmc-ebz_revc_schematic.pdf>`__                         |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Layout            | `AD917x-FMC-EBZ Layout <https://wiki.analog.com/_media/resources/eval/dpg/ad9172-fmc-ebz_revc_layout.pdf>`__                               |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| Bill of Materials | `AD917x-FMC-EBZ BOM <https://wiki.analog.com/_media/resources/eval/dpg/ad9172-fmc-ebz_revc_bom.zip>`__                                     |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| PCB Gerber Files  | `AD917x-FMC-EBZ Gerber Files <https://wiki.analog.com/_media/resources/eval/dpg/ad9172-fmc-ebz_revc_gerber_files.zip>`__                   |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| PCB BRD File      | `AD917x-FMC-EBZ Board File <https://wiki.analog.com/_media/resources/eval/dpg/ad9172-fmc-ebz_revc.zip>`__                                  |
+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: https://wiki.analog.com/_media/section>resources/eval/dpg#Data Pattern Generator&nofooter&noindent
   :alt: dpg#Data Pattern Generator&nofooter&noindent
