Evaluating the ADF5902, 24 GHz, ISM Band, Multichannel FMCW Radar Transmitter
=============================================================================

The :adi:`EVAL-ADF5902` evaluation board allows the user to evaluate the performance of the :adi:`ADF5902` 24 GHz voltage controlled oscillator (VCO) programmable gain amplifier (PGA) with a 2-channel power amplifier (PA) output and ramping phase-locked loop (PLL).

Supported Carriers
==================

-  `ZedBoard <https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/zedboard/>`__

Required Hardware
-----------------

-  :adi:`EVAL-ADF5902` board & Power supply
-  :adi:`SDP-I-FMC` Interposer
-  ZedBoard

Required Software
-----------------

-  Xilinx SDK / Xilinx Vitis.
-  A UART terminal (Tera Term/PuTTY/Hyperterminal), Baud rate 115200.

Build Application
-----------------

In order to build the application and generate the .elf file, please follow the :doc:`NO-OS Build Guide </wiki-migration/resources/no-os/build>`.

Source files for the application can be found in the :doc:`Downloads </wiki-migration/resources/eval/user-guides/eval-adf5902/software/no-os-setup>` section.

Run Application
---------------

Start a UART terminal (set to 115200 baud rate), and program the device and run the elf file. An output example of the application is provided below:

::

   ADF5902 Successfully initialized!
   ADF5902 Locked Frequency: 24024999936 Hz
   ADF5902 Temperature value: 27.07 degC

Downloads
=========

.. admonition:: Download
   :class: download

   
   -  :git-no-OS:`ADF5902 Application <projects/adf5902_sdz>`
   

