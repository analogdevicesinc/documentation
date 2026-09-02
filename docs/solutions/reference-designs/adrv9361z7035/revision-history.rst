.. _adrv9361z7035 revision_history:

ADRV936x SOM Revision History
=============================

This page contains revision details for the ADRV936x SOM boards.

ADRV9361-Z7035
--------------

Revision F
~~~~~~~~~~

This is the current shipping version.

..
   TODO: The following resource files have been removed and need to be
   re-hosted or replaced:
   -  Rev F Schematics (02-038702-01-f2.pdf)
   -  BOM, 7 zipped (05-038702-01-f2.7z)
   -  Allegro brd file, 7 zipped (08_038702f.7z)

- Changes from Rev E to Rev F:

   -  The schematic did not change. We only made an adjustment to the layout.
   -  The RF traces were modified to improve the insertion loss and the return
      loss as well as the EVM.
   -  For some unknown reason the rev is "F2" not just "F"

Revision E
~~~~~~~~~~

..
   TODO: The following resource files have been removed and need to be
   re-hosted or replaced:
   -  Rev E Schematics (adrv9361-z7035_reve.pdf)
   -  Rev E BOM (05_038702-e.xlsx, was in images/)
   -  Rev E Allegro Board File (08_038702e.zip)

Revision D
~~~~~~~~~~

- Changes from Rev C to Rev D:

   -  Moved all (4) GTX ports from Bank 111 to Bank 112 on the Zynq SoC in order
      to be in compliance with Xilinx recommended PCIe design rules.
      Functionally equivalent to Rev C.

      -  The GTX signal assignments at the JX micro headers were unchanged in
         order to maintain compatibility with existing carrier boards.

   -  Added revision and part number to the silkscreen and copper.
   -  The LED (D3), used to illuminate when PG_MODULE is asserted, now has its
      anode connected to the 3V3_I2C supply (formerly connected to 3.3V supply).
      This was done to allow the LED to be used as a visual state indicator
      during SOM power up, reflecting different states of the ADM1166 sequencer.
      In addition, the ADM1166 firmware was updated to include LED toggling
      (slow/fast), corresponding to specific power up states.
   -  Improved the power structure and increased the 0.95V current from 2A to 6A
   -  Added a `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`_
      option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
   -  Improved the layout to accommodate the power changes.

Revision C (First publicly available revision)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first publicly available revision.

..
   TODO: The following resource file has been removed and needs to be
   re-hosted or replaced:
   -  Rev C Schematics (adrv9361-z7035.pdf)

ADRV9364-Z7020 Hardware
-----------------------

Revision D
~~~~~~~~~~

This is the current shipping version.

- Changes from Rev C to Rev D

   -  Improved the power structure and increased the 1V current from 2A to 4A
   -  Improved the layout to accommodate the power changes.
   -  Added a `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`_
      option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
   -  Improved the RF traces to have better insertion loss and return loss.

..
   TODO: The following resource files have been removed and need to be
   re-hosted or replaced:
   -  Rev D1 Schematics (adrv9364-z7020_revd-1.pdf)
   -  Rev D Schematics (adrv9364-z7020_revd.pdf)

-  There was a small typo in the rev D0 of the schematics, the net
   named ``*_EN_AGC``, was tied to the ``ENABLE`` pin, and the net called
   ``*_ENABLE`` was tied to the ``EN_AGC`` pin. This is fixed/updated in
   the D1 revision. Copper/layout does not change, only the designation on
   the wire (for clarity).

Revision C (First publicly available revision)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first publicly available revision.

..
   TODO: The following resource file has been removed and needs to be
   re-hosted or replaced:
   -  Rev C Schematics (adrv9364-z7020_revc.pdf)

Support
-------

Please refer to :ez:`EngineerZone <community/fpga>` with questions on
hardware/schematics/or using the ADRV936x RF SOMs.
