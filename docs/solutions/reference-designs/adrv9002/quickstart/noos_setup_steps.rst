Follow the steps in this order, to avoid damaging the components:

#. Connect the :adi:`{{ eval_board }}` FMC board to the
   FPGA carrier
#. Configure :xilinx:`ZedBoard` for JTAG boot mode (mode MIO[5:2] jumpers in
   the position **0,0,0,0**)
#. Connect USB UART J83 (Micro USB) to your host PC
#. Connecy USB JTAG (Micro USB) to your host PC
#. (Optional) Connect a monitor to the FPGA by HDMI, and a mouse and a keyboard
#. Turn on the power switch on the FPGA board
#. Build and run the project using the steps shown in
   :external+no-OS:doc:`here <projects/rf-transceiver/adrv9001>`.
#. Observe console output messages on your terminal (use the first ttyUSB or
   COM port registered)
