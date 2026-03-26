Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`EVAL-ADRV9002` FMC board to the FPGA carrier FMC socket.
#. On the FMC card, set the switch to select clock source between:

  - an on-board 38.4 MHz VCTCXO (default)
  - external (via J501) 10 MHz to 1000 MHz / +13 dBm

#. Connect the UART port of ZedBoard (J14) to a PC via Micro-USB.
#. Insert the SD card into the slot (J12), located on the underside of
   ZedBoard.
#. Configure ZedBoard for SD BOOT: boot (JP7-JP11) and MIO0 (JP6) jumpers set
   to SD card mode, ,in accordance with the picture shown below.

      .. image:: ../images/jumper_config.png
        :align: center
        :width: 500

#. Connect 12V power supply to barrel jack (J20).
#. Turn on the power switch (SW8) on the FPGA board. Green Power LED (LD13)
   should illuminate.
#. Wait approximately 15 seconds. The blue Done LED (LD12) should illuminate.
#. Observe kernel and serial console messages on your terminal.


