.. _eval ltc23xx user-guide:

User guide
===============================================================================

.. important::

   This guide focuses on :adi:`LTC2378-20` with the `ZedBoard
   <https://digilent.com/reference/programmable-logic/zedboard/start>`__ for
   Linux (the primary and most supported path) and the :adi:`DC2135A` with the
   :adi:`MAX32666FTHR` for no-OS. The setup applies to all other supported
   devices as they share the same FMC connector and pin-compatible interface.

Hardware guide
-------------------------------------------------------------------------------

Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :adi:`LTC2378-20` FMC evaluation board connects to the `ZedBoard <https://digilent.com/reference/programmable-logic/zedboard/start>`__ via
the FMC connector.

.. figure:: ./images/ltc2378-20_zed_setup.jpeg
   :alt: ZedBoard with LTC2378-20 FMC evaluation board connected via FMC slot
   :align: center
   :width: 800

   ZedBoard with LTC2378-20 FMC Evaluation Board

Power supply
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FMC connector on the ZedBoard supplies all voltages required by the
evaluation board. No separate external supply is needed for the FMC board
itself. The ZedBoard is powered by its own 12V DC supply included in the
ZedBoard kit.

The VADJ level on the ZedBoard must be set to **2.5V** to match the I/O
voltage requirements of the :adi:`LTC2378-20`.

Software guide
-------------------------------------------------------------------------------

The :adi:`LTC2378-20` reference design runs the ADI Kuiper Linux distribution
on the ZedBoard. The ADC is exposed through the Linux IIO (Industrial I/O)
subsystem, which provides a standardized interface for data acquisition.

Once the board has booted, the following IIO-based tools can be used to
interact with and capture data from the device:

- :ref:`iio-oscilloscope`
- :external+scopy:doc:`Scopy <index>` v2.0 or later (must include IIO plugin)
