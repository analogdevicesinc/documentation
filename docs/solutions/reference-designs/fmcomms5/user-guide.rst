.. _fmcomms5-user-guide:

User Guide
===============================================================================

The :adi:`AD-FMCOMMS5-EBZ` carries two :adi:`AD9361` transceivers, providing
four receive and four transmit channels on a single FMC card. This user guide
explains the board hardware, the IIO Oscilloscope plugin used to control the
dual transceiver pair, and the synchronization and calibration steps required to
operate the two devices as a coherent 4x4 MIMO system.

.. tip::

   If you have not set up your board yet, start with the
   :doc:`prerequisites` and :doc:`quickstart/index` pages first,
   then return here for in-depth configuration.

The pages below follow the typical workflow — from understanding the hardware,
through configuring the RF parameters, to synchronizing and phase-aligning the
two AD9361 devices:

- :doc:`hardware` — schematics, PCB layout, bill of materials, and
  configuration options for the AD-FMCOMMS5-EBZ board.
- :doc:`fmcomms5_plugin` — overview of the FMCOMMS5 plugin for the
  IIO Oscilloscope, including channel configuration rules and control
  of the dual :adi:`AD9361` transceiver pair.
- :doc:`multi-chip-sync` — explains how baseband sampling and data
  clocks are synchronized across the two AD9361 devices, and the RF
  synchronization limitations that motivate phase calibration.
- :doc:`phase-sync` — describes the phase synchronization calibration
  procedure and how it is implemented in IIO Oscilloscope and ``libad9361``.

.. toctree::
   :titlesonly:
   :hidden:

   hardware
   fmcomms5_plugin
   multi-chip-sync
   phase-sync
