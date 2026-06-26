.. _eval-adaq23875-fmcz prerequisites:

Prerequisites
===============================================================================

What you need depends on what you are trying to do. As a minimum, you need to
start out with:

Hardware prerequisites
-------------------------------------------------------------------------------

#. The ADAQ23875 evaluation board: :adi:`EVAL-ADAQ23875FMCZ <EVAL-ADAQ23875>`
#. An FPGA carrier platform:

   - :xilinx:`ZedBoard (AES-Z7EV-7Z020-G) <products/boards-and-kits/1-8dyf-11.html>`
     on FMC connector — the officially supported platform for this evaluation
     board.

#. Some way to interact with the ZedBoard:

   - LAN cable (Ethernet) — required for SSH access and IIO Oscilloscope
     communication
   - Host PC running Windows 10 or higher

#. A signal source for the analog input:

   - Audio Precision APX525 audio analyser (or equivalent low-noise source)
   - XLR-to-SMA adapter cable
   - SMA cable

#. A 12 V DC power supply for the ZedBoard.
#. An SD card with at least 16 GB of memory.

Software prerequisites
-------------------------------------------------------------------------------

#. :external+kuiper:doc:`Analog Devices Kuiper Linux <index>` image (flashed to
   SD card)
#. :ref:`IIO Oscilloscope <iio-oscilloscope>` application installed on the host
   PC

.. note::

   :adi:`Analog Devices <>` does not offer FPGA carrier platforms for sale or
   loan; obtaining one yourself is the normal part of development or evaluation.

Getting Started Checklist
-------------------------------------------------------------------------------

Before proceeding to the quickstart guide, ensure you have:

- [ ] EVAL-ADAQ23875FMCZ evaluation board
- [ ] ZedBoard FPGA development board (AES-Z7EV-7Z020-G)
- [ ] 12 V DC power supply for the ZedBoard
- [ ] SD card (16 GB or larger)
- [ ] LAN cable (Ethernet)
- [ ] SMA cable
- [ ] XLR-to-SMA adapter cable
- [ ] Low-noise signal source (e.g. Audio Precision APX525)
- [ ] Host PC running Windows 10 or higher
- [ ] IIO Oscilloscope installed on host PC
- [ ] Kuiper Linux image downloaded

Next Steps
-------------------------------------------------------------------------------

Once you have all the prerequisites ready, proceed to:

- :ref:`eval-adaq23875-fmcz quickstart` — for step-by-step setup instructions
