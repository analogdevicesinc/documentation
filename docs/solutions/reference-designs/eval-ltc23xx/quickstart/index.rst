.. _eval ltc23xx quickstart:

Quick start
===============================================================================

The quick start guides provide step-by-step instructions for setting up the
LTC23xx evaluation system. The primary path uses the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
running Kuiper Linux. The :adi:`DC2135A` + :adi:`MAX32666FTHR` path covers
the no-OS alternative.

.. important::

   This guide focuses on :adi:`LTC2378-20` with the `ZedBoard
   <https://digilent.com/reference/programmable-logic/zedboard/start>`__ for
   Linux (the primary and most supported path) and the :adi:`DC2135A` with the
   :adi:`MAX32666FTHR` for no-OS. The setup applies to all other supported
   devices as they share the same FMC connector and pin-compatible interface.

.. toctree::

   zed
   dc2135a

.. _eval ltc23xx carriers:

Supported carriers
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35

   * - Platform
     - LTC23xx board
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - FMC

Supported environments
-------------------------------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Platform
     - Linux software
     - no-OS software
   * - `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__
     - Yes
     - ---
   * - :adi:`DC2135A` + :adi:`MAX32666FTHR`
     - ---
     - Yes

Hardware setup
-------------------------------------------------------------------------------

ZedBoard + LTC2378-20 board
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../images/ltc2378-20_zed_setup.jpeg
   :alt: ZedBoard with LTC2378-20 FMC evaluation board connected via FMC slot
   :align: center
   :width: 800

   ZedBoard with LTC2378-20 FMC board hardware setup

DC2135A + MAX32666FTHR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to the :ref:`ZedBoard quick start <eval ltc23xx quickstart zed>` or the
:ref:`DC2135A + MAX32666FTHR quick start <eval ltc23xx quickstart dc2135a>`.
