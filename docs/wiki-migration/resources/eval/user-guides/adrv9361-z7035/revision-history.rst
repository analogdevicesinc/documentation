ADRV936x SOM Revision History
=============================

This page contains revision details for the ADRV936x SOM boards.

ADRV9361-Z7035
--------------

Revision F
~~~~~~~~~~

This is the current shipping version.

.. admonition:: Download
   :class: download

   
   -  `Rev F Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv9361-z7035/02-038702-01-f2.pdf>`__
   -  `BOM (7 zipped) <https://wiki.analog.com/_media/resources/eval/user-guides/adrv9361-z7035/05-038702-01-f2.7z>`__
   -  `Allegro brd file (7 zipped) <https://wiki.analog.com/_media/resources/eval/user-guides/adrv9361-z7035/08_038702f.7z>`__
   


-  Changes from Rev E to Rev F:

   -  The schematic did not change. We only made an adjustment to the layout.
   -  The RF traces were modified to improve the insertion loss and the return loss as well as the EVM.
   -  For some unknown reason the rev is "F2" not just "F"

Revision E
~~~~~~~~~~

.. admonition:: Download
   :class: download

   
   -  `Rev E Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035_reve.pdf>`__
   -  `Rev E BOM <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/05_038702-e.xlsx>`__
   -  `Rev E Allegro Board File <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/08_038702e.zip>`__ (This file is `compressed <http://www.7-zip.org/7z.html>`__). Get the `Allegro FREE Physical Viewer <https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-downloads-start.html>`__ (You need 16.6 or higher).
   


Revision D
~~~~~~~~~~

-  Changes from Rev C to Rev D:

   -  Moved all (4) GTX ports from Bank 111 to Bank 112 on the Zynq SoC in order to be in compliance with Xilinx recommended PCIe design rules. Functionally equivalent to Rev C.

      -  The GTX signal assignments at the JX micro headers were unchanged in order to maintain compatibility with existing carrier boards.

   -  Added revision and part number to the silkscreen and copper.
   -  The LED (D3), used to illuminate when PG_MODULE is asserted, now has its anode connected to the 3V3_I2C supply (formerly connected to 3.3V supply). This was done to allow the LED to be used as a visual state indicator during SOM power up, reflecting different states of the ADM1166 sequencer. In addition, the ADM1166 firmware was updated to include LED toggling (slow/fast), corresponding to specific power up states.
   -  Improved the power structure and increased the 0.95V current from 2A to 6A
   -  Added a `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`__ option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
   -  Improved the layout to accommodate the power changes.

Revision C (First publicly available revision)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first publicly available revision.

.. admonition:: Download
   :class: download

   
   -  `Rev C Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9361-z7035.pdf>`__
   


ADRV9364-Z7020 Hardware
-----------------------

.. _revision-d-1:

Revision D
~~~~~~~~~~

This is the current shipping version.

-  Changes from Rev C to Rev D

   -  Improved the power structure and increased the 1V current from 2A to 4A
   -  Improved the layout to accommodate the power changes.
   -  Added a `1000BASE-KX <https://en.wikipedia.org/wiki/Gigabit_Ethernet#1000BASE-KX>`__ option for the Ethernet Phy (Ethernet Operation over Electrical Backplanes)
   -  Improved the RF traces to have better insertion loss and return loss.

.. admonition:: Download
   :class: download

   
   -  `Rev D1 Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revd-1.pdf>`__
   
      -  There was a small typo in the rev D0 of the schematics (below), the net named ``*_EN_AGC``, was tied to the ``ENABLE`` pin, and the net called ``*_ENABLE`` was tied to the ``EN_AGC`` pin. This is fixed/updated in this schematic. copper/layout does not change, only the designation on the wire (for clarity).
   
   -  `Rev D Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revd.pdf>`__
   
      -  This has the notation error described above.
   


.. _revision-c-first-publicly-available-revision-1:

Revision C (First publicly available revision)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first publicly available revision.

.. admonition:: Download
   :class: download

   
   -  `Rev C Schematics <https://wiki.analog.com/_media/resources/eval/user-guides/adrv936x_rfsom/adrv9364-z7020_revc.pdf>`__
   


Support
-------

Please refer to :ez:`EngineerZone <community/fpga>` with questions on hardware/schematics/or using the ADRV936x RF SOMs.
