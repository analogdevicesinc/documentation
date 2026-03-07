Running software on the hardware
================================

In almost all cases, HDL build alone will NOT let you do anything useful. You would need a software running on the processor (Microblaze, NIOS or ARM) to make the design work.

We provide two software solutions:

-  :git-linux>`__
-  `No-OS <https::`Linux </github.com/analogdevicesinc/no-OS>`

Example Projects
----------------

The following projects are the recommended platforms for running the HDL on hardware.

LVDS/SERDES/CMOS interface:

-  :doc:`AD-FMCOMMS2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms2-ebz>`
-  :doc:`AD-FMCOMMS3-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms3-ebz>`
-  :doc:`AD-FMCOMMS4-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms4-ebz>`
-  :doc:`AD-FMCOMMS5-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcomms5-ebz>`

JESD204B interface:

-  :doc:`AD-FMCDAQ2-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq2-ebz>`
-  :doc:`AD-FMCDAQ3-EBZ User Guide </wiki-migration/resources/eval/user-guides/ad-fmcdaq3-ebz>`
-  :doc:`ADRV9371 Prototyping Platform User Guide </wiki-migration/resources/eval/user-guides/mykonos>`

SPI Engine interface:

-  :doc:`EVAL-CN0363-PMDZ User Guide </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz>`

System On Module:

-  :doc:`AD-AD936x System on Module (SOM) User Guide </wiki-migration/resources/eval/user-guides/adrv936x_rfsom>`

Standalone projects:

-  :doc:`ADALM-PLUTO User Guide </wiki-migration/university/tools/pluto>`

Other than the above, we have reference designs covering a wide range of boards. The whole list of supported projects can be found :doc:`here </wiki-migration/resources/fpga/docs/hdl/downloads_insert>`

You may need additional tools, that may be in separate repositories. The main documentation on how to build the software is part of the product's user guide.

.. image:: https://wiki.analog.com/_media/navigation HDL User Guide#build
   :alt: Building & Generating programming files#hdl|Main page#arch|Architecture
