FPGAs inside of ADI
===================

`Fpga <https://en.wikipedia.org/wiki/Fpga>`__'s are in wide use across various ADI groups, for three main purposes:

-  device validation (pre tapeout). Typically ADI's customers never see these, or they are lent to our large customers for pre-tapeout system verification.
-  device verification (post tapeout). Typically used on bench evaluation boards and ATE hardware. Used for device verification, evaluation and characterization from first silicon to manufacturing release. Also used in production test. ADI customers can use the bench evaluation hardware and are sometimes given access to source code (see next item).
-  as a complementary product to ADI's devices, (where ADI's end customers connect our product to the FPGA, and desire help/assistance in doing so). These systems can typically be obtained by our customers easily, and sometimes even include the entire design package (schematics, gerbers, BOM, firmware, software, HDL) which allows the customer to replicate pieces in their end product. These can be either part of a silicon evaluation platform, or a subsystem demonstration platform.

This page is to allow internal developers of FPGA's (for either platform) to better understand the uses of FPGAs inside of ADI, and to share what they are doing - as to increase re-use of any FPGA platforms (either Hardware or HDL code) inside the company, not only allowing you and others to do their jobs faster, but to provide a standard, unified deliverable of HDL (when that is delivered to the customer).

Vendors & Tools
---------------

`Xilinx <xilinx>>`__ and `Altera <http://www.altera.com/>`__ are the current FPGA market leaders and long-time industry rivals. Together, they control over 80 percent of the market (Depending on who's numbers you believe). Both Xilinx and Altera provide free Windows and Linux design software, and both are used within ADI.

-  More information about Xilinx (and Xilinx partner programs) inside of ADI, including where to get tools can be found :doc:`Here </wiki-migration/internal_only/fpga/xilinx>`
-  More information about Altera inside of ADI, including where to get tools can be found :doc:`Here </wiki-migration/internal_only/fpga/altera>`

`Aldec <http://www.aldec.com/>`__ - Is this a relevant tool supplier for FPGA or ASIC design and verification tools? New product release - "VHDL and Verilog Design Rule Checker"

Many Xilinx platforms use the "FMC" connector defined by ANSI/VITA 57.1 specification. `VITA's website for FMC <http://www.vita.com/fmc>`__ has a list of vendors who develop FMC boards. The current specification for VITA 57.1 is:

-  `FMC Spec, 2010 version <https://wiki.analog.com/_media/internal_only/av57dot1.pdf>`__
-  `FMC+ Spec, 2018 <https://wiki.analog.com/_media/internal_only/av57.4-2018.pdf>`__
-  `FMC Spec, 2019 version <https://wiki.analog.com/_media/internal_only/av57dot1-2019_errata.pdf>`__

Platforms
---------

There are many FPGA platforms around ADI. Here is a quick list with responsible contacts. Please feel free to add your platform to the list:

+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Platform     | Customer facing | Description                                                                                                                                                                                   | Contact                                                                                 |
+==============+=================+===============================================================================================================================================================================================+=========================================================================================+
| DPG I/O      | Yes             | :adi:`ad-dpgioz`                                                                                                                                                                              | `jason.coutermarsh@analog.com <https://wiki.analog.com/jason.coutermarsh@analog.com>`__ |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| DPG2         | Yes             | Virtex-4, DDR2 SDRAM, Cypress USB                                                                                                                                                             | `jason.coutermarsh@analog.com <https://wiki.analog.com/jason.coutermarsh@analog.com>`__ |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| DPG3         | Yes             | Stratix-4, DDR3 SDRAM, Blackfin USB                                                                                                                                                           | `jason.coutermarsh@analog.com <https://wiki.analog.com/jason.coutermarsh@analog.com>`__ |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| DN7002K10MEG | No              | http://www.dinigroup.com/new/DN7002k10MEG.html                                                                                                                                                | `Gordon Sterling <https://wiki.analog.com/gordon.sterling@analog.com>`__                |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| FIFO5        | Yes             | :adi:`Virtex-4, SRAM, Cypress USB <en/other-products/multi-chip/ad13280/products/evaluation-boardstools/CU_High-Speed_ADC_FIFO_evaluation_tools/resources/fca.html#FPGA>`                     | `mike.hughes@analog.com <https://wiki.analog.com/mike.hughes@analog.com>`__             |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| FIFO503D     | Yes             | :adi:`Stratix II GX, SRAM, Cypress USB <static/imported-files/eval_boards/AD9239_AD9639_data_capture_bd.pdf>`                                                                                 | `mike.hughes@analog.com <https://wiki.analog.com/mike.hughes@analog.com>`__             |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| FIFO_V5      | No              | Virtex-5, SRAM, Cypress USB                                                                                                                                                                   | `mike.hughes@analog.com <https://wiki.analog.com/mike.hughes@analog.com>`__             |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| CED          | Yes             | :adi:`Cyclone I, SRAM, Cypress USB <en/analog-to-digital-converters/ad-converters/eval-ced/products/product.html>`                                                                            | `mick.mccarthy@analog.com <https://wiki.analog.com/mick.mccarthy@analog.com>`__         |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| UFG1         | Yes             | ARM7, Stratix II, DDR2 SDRAM, Cypress USB (USB Frame Grabber Platform for CCD Sensors with AFETGs)                                                                                            | `johnny-y.huang@analog.com <https://wiki.analog.com/johnny-y.huang@analog.com>`__       |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| UFG2         | Yes             | Nios II, Stratix II, DDR2 SDRAM, Cypress USB (USB Frame Grabber Platform for CCD/CMOS Sensors with AFETGs)                                                                                    | `johnny-y.huang@analog.com <https://wiki.analog.com/johnny-y.huang@analog.com>`__       |
+--------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

Please include links to block diagrams, schematics, layout files, software and other details of platform.

Is SDP going up here?

Platforms in Development, Schedules/Status
------------------------------------------

Keep other teans up-to-date on your FPGA-related projects.

Calls, Meetings, Workshops Schedule
-----------------------------------

:doc:`March 1-3, 2011 FPGA Workshop in Boston </wiki-migration/internal_only/fpga/march1-3>`

:doc:`March 28 week, GTC Follow-up Meeting </wiki-migration/internal_only/fpga/gtcmeeting>`

:doc:`Synplicity lunch and learn, Wilm6-Faneuil Hall - March 22nd, 11:30 - 1:00 </wiki-migration/internal_only/fpga/synplicity>`

ADI Working Groups, Members
---------------------------

Add the working teams as they are formed. Individuals include information on your group, needs

Please add your name and details :doc:`here </wiki-migration/internal_only/fpga/people>`:

RTL Coding Style Working Group : Jason Coutermarsh, Mark Cox, Mick McCarthy, Steve Harston, Russ Stop. For more see :doc:`here </wiki-migration/internal_only/fpga/rtlcodingstyle>`:

Training
--------

For general FPGA and Xilinx-specific training, please visit the :doc:`Hardent </wiki-migration/internal_only/hardent>` page.
