EVAL-ADIN1100FMCZ User Guide
============================

FEATURES
--------

-  Operates from a single, external 5-30 V supply or from USB
-  On-board ARM Cortex ADuCM4050 microcontroller
-  FMC connector for MII/RMII interface, MDIO signals, and status signals
-  Flexible MDIO interface options
-  Accessible hardware configuration pin switches

EVALUATION KIT CONTENTS
-----------------------

-  Two EVAL-ADIN1100FMCZ evaluation boards
-  Two mini USB cables

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02-063798-01-b_board.jpg

General Description
-------------------

The EVAL-ADIN1100FMZ allows a simplified evaluation of the key features of the :adi:`ADIN1100` robust, industrial, low power 10BASE-T1L Ethernet physical layer (PHY). The EVAL-ADIN1100FMCZ is powered by a single, external, 5-30 V BOARD_PWR supply rail that can be supplied either via the P1 connector or via the P2 plug. Alternatively, the board can be powered from USB via the P5 connector or from the 12V FMC supply. See P4 connector in the schematic.

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/02-063798-01-b_p4.jpg

All :adi:`ADIN1100` supplies are regulated from the BOARD_PWR rail, providing supply rails required for AVDD_H, AVDD_L, VDDIO, and DVDD_1P1.

The P3 field-programmable gate array (FPGA) mezzanine connector (FMC) connector is provided for connection to a master FPGA system for the media access control (MAC) interface and management data input/output (MDIO) control. The P12 connector and :adi:`ADuCM4050` provide two alternative means for MDIO control. The EVAL-ADIN1100FMCZ is fitted with a 25 MHz crystal (Y3).

For more details about the hardware, go to `EVAL-ADIN1100FMCZ Hardware Guide <https://wiki.analog.com/.adin_1100/eval_hw>`__.

For the software details, go to :doc:`EVAL-ADIN1100FMCZ Software Guide </wiki-migration/resources/eval/user-guides/adin_1100/eval_sw>`

For the Linux Driver details, go to :doc:`ADIN1100 10BASE-T1L PHY Linux Driver </wiki-migration/resources/tools-software/linux-drivers/net-phy/adin1100>`

For complete specifications for the :adi:`ADIN1100` device, see the :adi:`ADIN1100` data sheet, which must be consulted in conjunction with this user guide when using the EVAL-ADIN1100FMCZ.
