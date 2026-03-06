.. _ad-fmclidar1-ebz-quickstart:

Kit Contents and System Setup
=============================

Kit Contents
------------

The development kit is delivered with an SD card containing the evaluation
software and a set of accessories required to assemble the system:

- 8 x SMA cables to connect the AFE and Laser boards analog output signals to
  the DAQ board ADC inputs
- 2 x ribbon cables to connect the AFE and Laser boards digital signals to the
  DAQ board
- 12 V at 4 A power supply for the Laser board and power cables
- `Plano-Convex Lens, 1", f = 25.4 mm, AR Coating: 650-1050 nm <https://www.thorlabs.com/thorproduct.cfm?partnumber=LA1951-B>`__
- `SM1 Lens Tube, 1.50" Thread Depth <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1L15>`__
- `SM1 Lens Tube, 1" Thread Depth <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1L10>`__
- `Retaining Ring for stackable lens mount <https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1RR>`__
- SD card with the evaluation software for the supported FPGA carrier boards

System Setup
------------

To get the system up and running:

#. Connect the DAQ board to the FMC HPC connector on the FPGA carrier board.
#. Connect the ribbon cables between the DAQ board and the Laser and AFE
   boards. The DAQ board has silkscreen labels next to the AFE and Laser board
   connectors indicating which board each corresponds to.
#. Connect the SMA cables between the DAQ and the AFE board. Match the TIA
   outputs with the ADC inputs using the labeling on the SMA connectors so
   that they have the same letter (A, B, C, D). Ensure that P (positive) and N
   (negative) are matched between the boards.
#. Optionally connect one of the ADC channels to sample the laser drive signal
   by connecting the SMA outputs of the Laser board to an ADC channel.
#. Insert the lens into the 1.5" lens tube with the spherical surface pointing
   outwards. Position the lens such that the top of the spherical surface is
   aligned with the edge of the tube. Use the retaining ring to lock the lens
   in place. The 1" tube can be screwed on in front of the lens to limit the
   field of view.
#. Connect the external 12 V power supply to the Laser board.
#. Prepare the SD card: copy all files from
   ``BOOT/zynq-zc706-adv7511-fmclidar1`` onto the root of the SD card.
#. Plug the SD card into the FPGA carrier board and connect an HDMI monitor,
   USB keyboard, and mouse.
#. Power up the FPGA board. After booting, press the S1 switch on the Laser
   board to power the lasers.

.. tip::

   To prevent SD card corruption at system power down, run
   ``sudo shutdown -h now`` before removing power.
