EVAL-ADPAQ3029 - First application [RGB LED]
============================================

-  Setup the hardware as shown :doc:`here. </wiki-migration/resources/eval/user-guides/eval-adpaq3029/hw_setup>`
-  Make sure to use Dev module with LED. Here is the schematics for one such board - `Nexpaq_Glue_Micro_Dev_Board. <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/dev_board.pdf>`_
-  Download the following projects from the :doc:`resources </wiki-migration/resources/eval/user-guides/eval-adpaq3029/resources>` section.

   -  Bootloader
   -  MDK source code

-  Download firmware and Tile application from below

.. admonition:: Download
   :class: download

   \ `RGB led Firmware <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/ledapp.zip>`_

   
   `Tile GUI application <https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/moduware.tile.example-led-rgb.zip>`_\


-  The mapping of the RGB LED with the ADPAQ GPIOs is given below

.. container:: round box

   
   ========= ==============
   LED color GPIO port used
   ========= ==============
   Red       P1_08
   Green     P0_14
   Blue      P1_09
   ========= ==============
   


-  Launch the CCES IDE and import the first 3 projects into CCES as explained :doc:`here </wiki-migration/resources/eval/user-guides/eval-adpaq3029/fw_dev/import_prj>`.
-  Build and flash the firmware binary (\*.bin) as explained :doc:`here </wiki-migration/resources/eval/user-guides/eval-adpaq3029/fw_dev>`
-  Deploy the tile application as explained\ :doc:`here </wiki-migration/resources/eval/user-guides/eval-adpaq3029/tile_dev>`
-  Launch the ``Moduware`` app and pair to the gateway (Mini Dev board)
-  Now you should be able to see tile with ``DevMod``.\ `image <https://wiki.analog.com/resources/eval/user-guides/eval-adpaq3029/tile5.png>`_
-  Long Press on the ``DevMod`` Tile. Select the ``RGB LED`` tile. `image <https://wiki.analog.com/resources/eval/user-guides/eval-adpaq3029/app1.png>`_
-  The tile of the RGBLED app which was uploaded earlier will appear as shown in the image.\

|image1|

-  Test the application using GUI, by pressing R, G and B color buttons to observe change in the LED color in ADPAQ Dev module.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adpaq3029/app2.png
   :width: 400px
