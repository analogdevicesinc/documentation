Hardware Setup for Analog Devices Precision Toolbox
===================================================

For each of the converters supported by the Precision Toolbox, the hardware setup steps are outlined below. The steps detail the hardware and the configurations needed to get the Precision Toolbox to communicate with the converter evaluation board. ‎ ‎

AD4630-24, AD4630-16, AD4030-24
-------------------------------

You will require: SD-Card, Digilent Zedboard with 12 V wall-adapter power supply, PC running Windows 10.

-  Insert the SD card provided with the evaluation board into J12 on the ZedBoard
-  Connect the Evaluation board to the FMC connector of the ZedBoard.
-  Connect the provided power supplies to J20 on the ZedBoard.
-  Connect the USB cable to the USB OTG (J13) on the ZedBoard and to the computer
-  Connect the desired input signal to the appropriate input on the evaluation board (J2-J5)
-  Move SW8 to the ON position to start the ZedBoard

‎Refer to the :doc:`AD4630/AD4030 Evaluation Board User Guide </wiki-migration/resources/eval/ad4630-24-eval-board>` for more information.

‎

AD7768, AD7768-1
----------------

You will require: SD-Card, Digilent Zedboard with 12 V wall-adapter power supply, PC running Windows 10.

-  Use the latest release of the ADI Kuiper Linux image with support for evaluation `from here <:doc:`/wiki-migration/resources/tools-software/linux-software/adi-kuiper_images_for_ace`>`__, and configure your SD card to boot with correct project `using this guide <:doc:`/wiki-migration/resources/tools-software/linux-software/kuiper-linux`>`__
-  Insert the SD card into J12 on the ZedBoard
-  Connect the Evaluation board to the FMC connector of the ZedBoard.
-  Connect the provided power supplies to J20 on the ZedBoard.
-  Connect an Ethernet cable to J11 on the ZedBoard and the other end to your PC or a router on the same network as your PC, so that the ZedBoard is discoverable by the PC.
-  Connect the desired input signal to the appropriate input on the evaluation board
-  Move SW8 to the ON position to start the ZedBoard

‎

AD7380
------

You will require: SD-Card, Digilent Zedboard with 12 V wall-adapter power supply, PC running Windows 10.

-  Build the HDL, Zynq kernel and device tree for imaging the SD Card, targeting the AD7380, by following `this guide <:doc:`/wiki-migration/resources/tools-software/linux-software/kuiper-linux`>`__.
-  Insert the SD card into J12 on the ZedBoard
-  Connect the Evaluation board to the FMC connector of the ZedBoard.
-  Connect the provided power supplies to J20 on the ZedBoard.
-  Connect an Ethernet cable to J11 on the ZedBoard and the other end to your PC or a router on the same network as your PC, so that the ZedBoard is discoverable by the PC.
-  Connect the desired input signal to the appropriate input on the evaluation board
-  Connect the power supply to J1 or J3 on the evaluation board
-  Move SW8 to the ON position to start the ZedBoard
