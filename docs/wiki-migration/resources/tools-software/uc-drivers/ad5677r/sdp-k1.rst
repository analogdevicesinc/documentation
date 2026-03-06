AD5677R Evaluation Board and SDP-K1
===================================

Hardware setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/ad5677r/ad5677r_eval_board_chain_with_sdp-k1.png
   :align: center
   :width: 600px

-  Connect the :adi:`EVAL-AD5677R evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5677R.html>` to the :adi:`SDP-K1 controller board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>`.
-  Connect the :adi:`SDP-K1 controller board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/sdp-k1.html>` to your computer over USB.

Software setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_software_layers.jpg
   :align: center
   :width: 250px

-  Make sure you have the `Mbed Online Compiler <https://ide.mbed.com/compiler>`__ installed.
-  Download the `EVAL-AD568x-AD569x <https://os.mbed.com/teams/AnalogDevices/code/EVAL-AD568x-AD569x/>`__ driver. Despite its name, this driver library does support the AD5677R.
-  This driver defaults to supporting the AD5686R. To change to the AD5677R, edit the app_config.h file.
-  Follow the quick start instructions in :doc:`Mbed: User Guide for SDP-K1 </wiki-migration/resources/tools-software/mbed>`
-  Start up a serial terminal emulator (e.g. Tera Term)
-  Find the com-port your controller board is connected on and select it.
-  Set the baud-rate for 115200
-  Reset the controller board and connect.
-  Use the menu provided over the terminal window to access the evaluation board.
