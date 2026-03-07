:doc:`Click here to return to the A2B Raspberry Pi User Guide homepage </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi>`

Migrating Latest A2B stack
==========================

Migration to the latest A2B stack can be done by referring to the following link: :doc:`A2B Stack Migration </wiki-migration/resources/tools-software/a2bv2/a2bstackmigrationtolinux_qnx>`

After migrating to the latest A2B stack, export the adi_a2b_busconfig.c file from the respective SigmaStudio/SigmaStudio+ version (compiled with the A2B stack) and paste it into the appropriate location in the Raspberry Pi application. Then, clean and build the application, and run it as explained in :doc:`Build kernel and Run application </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/buildingkernel>`.

.. note::

   If build errors occur, they can be resolved by making the necessary changes to the source code.


**PREV :** :doc:`DTS Overlay </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/dtsoverlay>` **NEXT :** :doc:`SigmaStudioPlus Example Schematic for 242x </wiki-migration/resources/tools-software/a2bv2/a2braspberrypi/schematic242x>`
