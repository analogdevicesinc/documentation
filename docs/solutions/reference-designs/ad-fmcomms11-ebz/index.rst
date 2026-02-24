.. _ad-fmcomms11-ebz:

AD-FMCOMMS11-EBZ User Guide
============================

Introduction
------------

The AD-FMCOMMS11-EBZ board is a system platform board for communication
infrastructure applications that demonstrates the Direct to RF (DRF)
transmitter and observation receiver architecture. Using high sample rate
RFDAC(s) and RFADC(s), a number of components in previous generation
transmitters can be eliminated, such as mixers, modulators, IF amplifiers
and filters.

It is composed of the multi-GSPS RF ADC :adi:`AD9625` and DAC :adi:`AD9162`.
The transmit path contains a balun, low pass filter, gain block and variable
attenuation to produce an output appropriate for a power amplifier module.
Along the observation path, the PA output is coupled back into the board
through a variable attenuator, a balun and finally the ADC. Clock management
is taken care of on board; all the necessary clocks are generated from a
reference.

The platform supports the frequency range 70 MHz to 6 GHz.

.. image:: fmcomms11_image.png
   :align: center
   :width: 500

.. toctree::
   :hidden:

   hardware
   software

Quick Start
-----------

The AD-FMCOMMS11-EBZ connects to the HPC FMC connector on the ZC706 carrier.

Requirements
~~~~~~~~~~~~

- Host PC (Windows or Linux) with SD card writer
- USB keyboard/mouse for the Zynq (USB hub may be needed)
- HDMI display (Full HD only)
- Antenna or SMA cable for crossing Tx to Rx

Hardware Setup (ZC706)
~~~~~~~~~~~~~~~~~~~~~~

#. Insert the SD card into the ZC706 SD card interface connector (J30)
#. Plug the AD-FMCOMMS11-EBZ into the HPC connector (J37)
#. Connect HDMI display to the HDMI Video Connector (P1)
#. Connect USB mouse/keyboard to the USB 2.0 Micro-B connector (J49)
#. Connect 12 V power supply to power input connector (J22) - do not power
   on yet
#. Set boot mode switch SW11: position 1 down, 2 down, 3 up, 4 up, 5 down
#. Power on and wait ~30 seconds for the DONE LED to turn green
#. Wait another ~30 seconds for the HDMI display to become active

.. warning::

   This is a persistent file system. Please shut down properly using
   ``sudo shutdown -h now`` instead of just turning off the power switch.

More Information
----------------

- `ADI Reference Designs HDL User Guide <https://analogdevicesinc.github.io/hdl/user_guide/introduction.html>`__
- `JESD204B High-Speed Serial Interface Support <https://analogdevicesinc.github.io/hdl/library/jesd204/index.html>`__

Support
-------

If you have any questions regarding the AD-FMCOMMS11-EBZ feel free to ask on
the :ez:`FPGA Reference Designs Forum <fpga>`.
